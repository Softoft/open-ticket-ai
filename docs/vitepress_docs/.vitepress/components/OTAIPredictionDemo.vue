<template>
    <h2 class="mb-4 w-100 text-center text-body-emphasis">{{
            t('otai_prediction_demo_component.title')
        }}</h2>
    <div class="container my-3">
        <div class="row justify-content-center">
            <div class="col-md-12 col-lg-8">

                <div class="mb-3">
                    <label class="form-label fw-bold" for="demo-example-select">
                        {{ t('otai_prediction_demo_component.pickExampleText') }}
                    </label>
                    <select
                        id="demo-example-select"
                        v-model="selected"
                        class="form-select"
                        @change="applyExample"
                    >
                        <option :value="-1" disabled>
                            {{ t('otai_prediction_demo_component.exampleSelectDefault') }}
                        </option>
                        <option v-for="(ex, i) in examples" :key="i" :value="i">
                            {{ ex.name }}
                        </option>
                    </select>
                </div>

                <div class="mb-3">
                    <label class="form-label fw-bold" for="demo-subject">{{
                            t('otai_prediction_demo_component.subjectLabel')
                        }}</label>
                    <input
                        id="demo-subject"
                        v-model="subject"
                        :placeholder="t('otai_prediction_demo_component.subjectPlaceholder')"
                        class="form-control"
                        type="text"
                    />
                </div>

                <div class="mb-3">
                    <label class="form-label fw-bold" for="demo-body">{{
                            t('otai_prediction_demo_component.messageLabel')
                        }}</label>
                    <textarea
                        id="demo-body"
                        v-model="body"
                        :placeholder="t('otai_prediction_demo_component.messagePlaceholder')"
                        class="form-control"
                        rows="4"
                    ></textarea>
                </div>

                <button
                    :disabled="loading"
                    class="btn btn-lg btn-primary mb-4 mt-1"
                    type="button"
                    @click="predict"
                >
                    <span v-if="loading" aria-hidden="true"
                          class="spinner-border spinner-border-sm me-1"></span>
                    <span v-if="loading"
                          role="status">{{ t('otai_prediction_demo_component.loadingText') }}</span>
                    <span v-else
                          class="text-white">{{ t('otai_prediction_demo_component.submitButtonText') }}</span>
                </button>

                <div v-if="errorMessage" class="alert alert-danger" role="alert">
                    {{ errorMessage }}
                </div>

                <div v-if="queueResult && prioResult" class="mt-4">
                    <h3 class="fw-bold text-body-emphasis mb-3">
                        {{ t('otai_prediction_demo_component.resultTitle') }}</h3>
                    <div class="table-responsive">
                        <table class="table table-dark table-hover align-middle">
                            <thead class="table-light">
                            <tr>
                                <th scope="col">
                                    {{ t('otai_prediction_demo_component.typeColumnHeader') }}
                                </th>
                                <th scope="col">
                                    {{ t('otai_prediction_demo_component.predictionColumnHeader') }}
                                </th>
                                <th class="text-center" scope="col">
                                    {{ t('otai_prediction_demo_component.confidenceColumnHeader') }}
                                </th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <th scope="row">
                                    {{ t('otai_prediction_demo_component.queueRowHeader') }}
                                </th>
                                <td>{{ queueResult[0].label }}</td>
                                <td class="text-center">
                                    <span
                                        :class="['badge', 'fs-6', confidenceBadge(queueResult[0].score)]">
                                        {{ formatScore(queueResult[0].score) }}
                                    </span>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    {{ t('otai_prediction_demo_component.priorityRowHeader') }}
                                </th>
                                <td>{{ prioResult[0].label }}</td>
                                <td class="text-center">
                                    <span
                                        :class="['badge', 'fs-6', confidenceBadge(prioResult[0].score)]">
                                        {{ formatScore(prioResult[0].score) }}
                                    </span>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>

import {ref} from 'vue'
import {examples} from "./demoExamples";
import {useI18n} from 'vue-i18n'

const {t} = useI18n()

async function query(endpoint: string, payload: any) {
    // ... (rest of the function is unchanged)
    const res = await fetch(endpoint, {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    if (!res.ok) throw new Error(`Error ${res.status}: ${res.statusText}`)
    return res.json()
}

// your real endpoints here
const QUEUE_EP = 'https://uwlzdugezcmrk5vk.eu-west-1.aws.endpoints.huggingface.cloud'
const PRIORITY_EP = 'https://rxnypflnfgdbgoxr.us-east-1.aws.endpoints.huggingface.cloud'

// form state
const subject = ref('')
const body = ref('')
const loading = ref(false)
const errorMessage = ref<string | null>(null)

// API results
const queueResult = ref<any>(null)
const prioResult = ref<any>(null)

// select logic
const selected = ref(-1)

function applyExample() {
    const ex = examples[selected.value]
    subject.value = ex.subject
    body.value = ex.body
    queueResult.value = null
    prioResult.value = null
    errorMessage.value = null
}

// retry+backoff prediction
async function predict() {
    loading.value = true
    errorMessage.value = null
    queueResult.value = null
    prioResult.value = null

    const text = (subject.value + ' ').repeat(2) + body.value
    const maxAttempts = 4

    for (let attempt = 1; attempt <= maxAttempts; attempt++) {
        try {
            const [q, p] = await Promise.all([
                query(QUEUE_EP, {inputs: text, parameters: {}}),
                query(PRIORITY_EP, {inputs: text, parameters: {}})
            ])
            queueResult.value = q
            prioResult.value = p
            break
        } catch (e) {
            console.error(`Attempt ${attempt} failed`, e)
            if (attempt === maxAttempts) {
                // Use the t() function for the error message
                errorMessage.value = t('otai_prediction_demo_component.predictionError')
            } else {
                const delay = 1000 * Math.pow(2, attempt - 1)
                await new Promise(res => setTimeout(res, delay))
            }
        }
    }

    loading.value = false
}

function confidenceBadge(score: number): string {
    // ... (function is unchanged)
    const pct = score * 100;
    if (pct > 90) return 'bg-success';
    if (pct > 80) return 'bg-info';
    if (pct > 50) return 'bg-warning text-dark';
    return 'bg-danger';
}

/**
 * Formats a 0–1 score as a percent string with one decimal
 */
function formatScore(score: number): string {
    // ... (function is unchanged)
    return (score * 100).toFixed(1) + '%';
}
</script>
