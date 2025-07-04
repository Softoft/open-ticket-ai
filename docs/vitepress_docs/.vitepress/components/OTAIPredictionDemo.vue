<template>
    <h2 class="mb-4 w-full text-center text-gray-800 dark:text-gray-200">{{
        t('otai_prediction_demo_component.title')
        }}</h2>
    <div class="my-3 mx-auto max-w-4xl">
        <div class="flex justify-center">
            <div class="w-full max-w-3xl">

                <div class="mb-3">
                    <label class="block mb-1 font-bold" for="demo-example-select">
                        {{ t('otai_prediction_demo_component.pickExampleText') }}
                    </label>
                    <select
                        id="demo-example-select"
                        v-model="selected"
                        class="block w-full rounded border border-gray-300 p-2 dark:bg-gray-800 dark:border-gray-700"
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
                    <label class="block mb-1 font-bold" for="demo-subject">{{
                        t('otai_prediction_demo_component.subjectLabel')
                        }}</label>
                    <input
                        id="demo-subject"
                        v-model="subject"
                        :placeholder="t('otai_prediction_demo_component.subjectPlaceholder')"
                        class="block w-full rounded border border-gray-300 p-2 dark:bg-gray-800 dark:border-gray-700"
                        type="text"
                    />
                </div>

                <div class="mb-3">
                    <label class="block mb-1 font-bold" for="demo-body">{{
                        t('otai_prediction_demo_component.messageLabel')
                        }}</label>
                    <textarea
                        id="demo-body"
                        v-model="body"
                        :placeholder="t('otai_prediction_demo_component.messagePlaceholder')"
                        class="block w-full rounded border border-gray-300 p-2 dark:bg-gray-800 dark:border-gray-700"
                        rows="4"
                    ></textarea>
                </div>

                <button
                    :disabled="loading"
                    class="px-4 py-2 mt-1 mb-4 rounded bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50"
                    type="button"
                    @click="predict"
                >
                    <span v-if="loading" aria-hidden="true"
                          class="animate-spin h-4 w-4 mr-1 border-2 border-white border-t-transparent rounded-full"></span>
                    <span v-if="loading"
                          role="status">{{ t('otai_prediction_demo_component.loadingText') }}</span>
                    <span v-else
                          class="text-white">{{ t('otai_prediction_demo_component.submitButtonText') }}</span>
                </button>

                <div v-if="errorMessage" class="mt-4 rounded bg-red-100 p-3 text-red-700" role="alert">
                    {{ errorMessage }}
                </div>

                <div v-if="queueResult && prioResult" class="mt-4">
                    <h3 class="mb-3 font-bold text-gray-800 dark:text-gray-200">
                        {{ t('otai_prediction_demo_component.resultTitle') }}</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-300 dark:divide-gray-700">
                            <thead class="bg-gray-100 dark:bg-gray-700">
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
                                        :class="['inline-block px-2 py-1 rounded-full text-white text-sm', confidenceBadge(queueResult[0].score)]">
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
                                        :class="['inline-block px-2 py-1 rounded-full text-white text-sm', confidenceBadge(prioResult[0].score)]">
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
    const pct = score * 100;
    if (pct > 90) return 'bg-green-600';
    if (pct > 80) return 'bg-blue-600';
    if (pct > 50) return 'bg-yellow-400 text-black';
    return 'bg-red-600';
}

/**
 * Formats a 0–1 score as a percent string with one decimal
 */
function formatScore(score: number): string {
    // ... (function is unchanged)
    return (score * 100).toFixed(1) + '%';
}
</script>
