<template>
    <div v-if="queueResult && prioResult" class="mt-6">
        <h3 class="text-2xl font-semibold text-center text-vp-text mb-6">
            {{ t('otai_prediction_demo_component.resultTitle') }}
        </h3>

        <div class="grid gap-6 sm:grid-cols-2">
            <!-- Queue Card -->
            <div class="bg-white dark:bg-gray-800 p-5 rounded-2xl shadow-lg flex flex-col items-center">
                <h4 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-2">
                    {{ t('otai_prediction_demo_component.queueRowHeader') }}
                </h4>
                <p class="text-xl font-bold text-gray-900 dark:text-gray-100 mb-4">
                    {{ queueResult[0].label }}
                </p>
                <span
                    :class="[
            'inline-block px-4 py-1 rounded-full text-sm font-medium',
            badgeClass(queueResult[0].score)
          ]"
                >
          {{ asPercent(queueResult[0].score) }}
        </span>
            </div>

            <div class="bg-white dark:bg-gray-800 p-5 rounded-2xl shadow-lg flex flex-col items-center">
                <h4 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-2">
                    {{ t('otai_prediction_demo_component.priorityRowHeader') }}
                </h4>
                <p class="text-xl font-bold text-gray-900 dark:text-gray-100 mb-4">
                    {{ prioResult[0].label }}
                </p>
                <span
                    :class="[
            'inline-block px-4 py-1 rounded-full text-sm font-medium',
            badgeClass(prioResult[0].score)
          ]"
                >
          {{ asPercent(prioResult[0].score) }}
        </span>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import {useI18n} from 'vue-i18n'

const props = defineProps<{
    queueResult: { label: string; score: number }[] | null
    prioResult: { label: string; score: number }[] | null
}>()

const {t} = useI18n()

function asPercent(s: number) {
    return (s * 100).toFixed(1) + '%'
}

function badgeClass(s: number) {
    const p = s * 100
    if (p > 90) return 'bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100'
    if (p > 80) return 'bg-vp-brand text-white'
    if (p > 50) return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-800 dark:text-yellow-100'
    return 'bg-red-100 text-red-800 dark:bg-red-800 dark:text-red-100'
}
</script>
