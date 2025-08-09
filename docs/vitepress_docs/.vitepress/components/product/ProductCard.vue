<!-- components/ProductCard.vue -->
<template>
    <Card
        class="group flex flex-col h-full bg-gray-900 border border-gray-700 rounded-xl overflow-hidden transition duration-200 hover:shadow-xl hover:scale-[1.02]">
        <template #header>
            <div class="text-center px-4 min-h-32">
                <h3 class="!text-3xl font-semibold text-white">{{ product.name }}</h3>
                <div class="mt-2">
                    <span class="text-2xl font-bold text-white">{{ formattedPrice }}€</span>
                    <span v-if="product.pricePeriod" class="text-sm text-gray-400">/ {{ product.pricePeriod }}</span>
                </div>
            </div>
        </template>

        <template #default>
            <div class="px-5 flex-1 flex flex-col">
                <p class="text-gray-400 mb-2 leading-relaxed">
                    {{ product.description }}
                </p>

                <ul class="space-y-2 !m-0 !p-0">
                    <li
                        v-for="(feature, i) in coreFeatures"
                        :key="i"
                        class="flex items-start !m-0 !px-0 py-2"
                    >
                        <i :class="['fas', feature.icon, 'mt-1 mr-2 text-indigo-500']" aria-hidden="true"></i>
                        <span class="text-gray-200">{{ feature.text }}</span>
                    </li>
                </ul>

                <Accordion
                    v-if="extraFeatures.length"
                    :items="accordionItems"
                    class="mt-auto"
                >
                    <template #item-0>
                        <ul class="space-y-2 !m-0 !p-0">
                            <li
                                v-for="(feature, i) in extraFeatures"
                                :key="i"
                                class="flex items-start !m-0 !px-0 py-2"
                            >
                                <i :class="['fas', feature.icon, 'mt-1 mr-2 text-indigo-500']" aria-hidden="true"></i>
                                <span class="text-gray-200">{{ feature.text }}</span>
                            </li>
                        </ul>
                    </template>
                </Accordion>
            </div>
        </template>
    </Card>
</template>

<script lang="ts" setup>
import {computed} from 'vue'
import Card from '../core/Card.vue'
import Accordion from '../core/Accordion.vue'
import type {Feature, Product} from './product.types'

const props = defineProps<{ product: Product }>()

const MAX_CORE = 5

const coreFeatures = computed<Feature[]>(() =>
    props.product.features.slice(0, MAX_CORE)
)
const extraFeatures = computed<Feature[]>(() =>
    props.product.features.slice(MAX_CORE)
)
const accordionItems = computed(() =>
    extraFeatures.value.length
        ? [{title: `+${extraFeatures.value.length} more`}]
        : []
)

const formattedPrice = computed(() =>
    new Intl.NumberFormat('de-DE', {maximumFractionDigits: 0}).format(
        props.product.price
    )
)
</script>
