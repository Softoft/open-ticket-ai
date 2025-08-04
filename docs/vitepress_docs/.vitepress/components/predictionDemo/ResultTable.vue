<template>
    <div v-if="queueResult && prioResult" class="mt-6">
        <span class="text-2xl font-semibold text-center text-vp-text my-6">
            {{ t('otai_prediction_demo_component.resultTitle') }}
        </span>

        <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <!-- Queue Card -->
            <div class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg flex flex-col items-center text-center">
                <span
                    class="text-lg font-medium text-gray-500 dark:text-gray-400 mb-4 min-h-[3rem] flex items-center justify-center"
                >
                    {{ t('otai_prediction_demo_component.queueRowHeader') }}
                </span>
                <span class="flex-1 text-xl font-bold text-gray-900 dark:text-gray-100 mb-1">
                    {{ mainQueue }}
                </span>
                <span class="flex-1 text-md font-bold text-gray-900 dark:text-gray-100 mb-4">
                    > {{ subQueue }}
                </span>
                Confidence:
                <span
                    :class="[
            'inline-block px-4 py-1 rounded-full text-sm font-medium',
            badgeClass(queueResult[0].score)
          ]"
                >
          {{ asPercent(queueResult[0].score) }}
        </span>
            </div>

            <!-- Priority Card -->
            <div class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg flex flex-col items-center text-center">
                <span
                    class="text-lg font-medium text-gray-500 dark:text-gray-400 mb-4 min-h-[3rem] flex items-center justify-center"
                >
                    {{ t('otai_prediction_demo_component.priorityRowHeader') }}
                </span>
                <p class="flex-1 text-xl font-bold text-gray-900 dark:text-gray-100 mb-4">
                    {{ prioResult[0].label }}
                </p>
                <div class="flex-1 text-md text-gray-900 dark:text-gray-100">
                    Confidence:

                    <span
                        :class="[
            'px-4 py-1 rounded-full text-sm font-medium',
            badgeClass(prioResult[0].score)
          ]"
                    >
          {{ asPercent(prioResult[0].score) }}
        </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import {computed} from 'vue'
import {useI18n} from 'vue-i18n'

const {queueResult, prioResult} = defineProps<{
    queueResult: { label: string; score: number }[] | null
    prioResult: { label: string; score: number }[] | null
}>()

const {t} = useI18n()

function asPercent(s: number) {
    return `${(s * 100).toFixed(1)}%`
}

// Split at /
const mainQueue = computed(() => {
    if (!queueResult || queueResult.length === 0) return null
    return queueResult[0].label.split('/')[0]
})

const subQueue = computed(() => {
    if (!queueResult || queueResult.length === 0) return null
    const parts = queueResult[0].label.split('/')
    return parts.length > 1 ? parts.slice(1).join('/') : null
})

function badgeClass(s: number) {
    const p = s * 100
    if (p > 90) return 'bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100'
    if (p > 80) return 'bg-vp-brand text-white'
    if (p > 50) return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-800 dark:text-yellow-100'
    return 'bg-red-100 text-red-800 dark:bg-red-800 dark:text-red-100'
}
</script>
