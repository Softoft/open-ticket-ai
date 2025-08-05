<template>
    <h2 class="mb-4 w-full text-center text-vp-text">{{
            t('otai_prediction_demo_component.title')
        }}</h2>
    <div class="my-3 mx-auto max-w-4xl">
        <div class="flex justify-center">
            <div class="w-full max-w-3xl">

                <div class="mb-3">
                    <SelectComponent
                        v-model="selected"
                        @update:modelValue="applyExample"
                        :label="t('otai_prediction_demo_component.pickExampleText')"
                        :placeholder="t('otai_prediction_demo_component.exampleSelectDefault')"
                        :options="exampleOptions"
                    >
                    </SelectComponent>
                </div>

                <div class="mb-3">
                    <label class="block mb-1 font-bold" for="demo-subject">{{
                        t('otai_prediction_demo_component.subjectLabel')
                        }}</label>
                    <input
                        id="demo-subject"
                        v-model="subject"
                        :placeholder="t('otai_prediction_demo_component.subjectPlaceholder')"
                        class="block w-full rounded border border-vp-border p-3 bg-vp-bg-soft"
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
                        class="block w-full rounded border border-vp-border p-3 bg-vp-bg-soft"
                        rows="6"
                    ></textarea>
                </div>

                <Button
                    :disabled="loading"
                    class="px-4 py-2 mt-1 mb-4 bg-vp-brand-1 text-white hover:bg-vp-brand-light disabled:opacity-50"
                    @click="predict"
                >
                    <span v-if="loading" aria-hidden="true"
                          class="animate-spin h-4 w-4 mr-1 border-2 border-white border-t-transparent rounded-full">

                    </span>
                    <span v-if="loading"
                          role="status">{{ t('otai_prediction_demo_component.loadingText') }}</span>
                    <span v-else
                          class="text-white">{{ t('otai_prediction_demo_component.submitButtonText') }}</span>
                </Button>

                <div v-if="errorMessage" class="mt-4 rounded bg-red-100 p-3 text-red-700" role="alert">
                    {{ errorMessage }}
                </div>

                <ResultTable v-if="queueResult && prioResult" :prio-result="prioResult" :queue-result="queueResult"/>

            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>

import {ref} from 'vue'
import Button from '../core/Button.vue'
import {examples} from "../demoExamples";
import {useI18n} from 'vue-i18n'
import ResultTable from "./ResultTable.vue";
import SelectComponent from "../core/SelectComponent.vue";

const {t} = useI18n()

const exampleOptions = examples.map(ex => ({
    value: ex.name,
    label: ex.name,
    subject: ex.subject,
    body: ex.body
}))

async function query(endpoint: string, payload: any) {
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
const selected = ref(exampleOptions[0].value)

function applyExample() {
    const selectedOption = exampleOptions.find(opt => opt.value === selected.value)
    subject.value = selectedOption.subject
    body.value = selectedOption.body
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
    const maxAttempts = 8

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
                const delay = 500 * Math.pow(2, attempt - 1)
                await new Promise(res => setTimeout(res, delay))
            }
        }
    }

    loading.value = false
}

</script>
