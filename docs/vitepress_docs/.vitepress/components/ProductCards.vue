<script lang="ts" setup>
var __VUE_PROD_DEVTOOLS__ = false

import {ref} from 'vue'
import Card from './core/Card.vue'
import Button from './core/Button.vue'

const selectedPlan = ref<string | null>(null)

const {
    products,
    title,
    buttonText = 'Choose Plan',
    buttonHref
} = defineProps<{
    products: Product[]
    title: string
    buttonText?: string
    buttonHref?: string
}>()

const emits = defineEmits<{
    (e: 'cta-click', productName: string): void
}>()

interface Feature {
    text: string
    icon: string
}

interface Product {
    name: string
    price: number
    pricePeriod?: string
    description: string
    features: Feature[]
    featured?: boolean
}

const handleCtaClick = (productName: string) => {
    selectedPlan.value = productName
    emits('cta-click', productName)
}
</script>

<template>
    <div class="my-5">
        <h2 class="mb-5 text-center text-4xl font-bold">{{ title }}</h2>
        <div class="grid gap-4 sm:grid-cols-1 lg:grid-cols-3 justify-center">
            <div
                v-for="(product, index) in products"
                :key="index"
                class="flex"
            >
                <Card
                    :class="['price-card h-full rounded-lg shadow-sm py-3',
                             { 'border-vp-brand border-2': product.featured }]">
                    <div class="flex flex-col px-2 xl:px-3 py-0">
                        <h3 class="font-bold">{{ product.name }}</h3>
                        <p class="text-vp-text-2 product-description">{{ product.description }}</p>

                        <div class="my-2">
                            <span class="text-3xl font-bold">${{ product.price }}</span>
                            <span v-if="product.pricePeriod" class="text-vp-text-2"> / {{
                                    product.pricePeriod
                                }}</span>
                        </div>

                        <hr>

                        <ul class="mb-4 list-none">
                            <li
                                v-for="(feature, fIndex) in product.features"
                                :key="fIndex"
                                class="flex items-center mb-3"
                            >
                                <i :class="['fas', feature.icon, 'mr-3', 'text-vp-brand']"></i>
                                <span>{{ feature.text }}</span>
                            </li>
                        </ul>

                        <div class="mt-auto">
                            <a v-if="buttonHref"
                               :class="['w-full text-center px-4 py-2 rounded text-sm font-medium',
                                        product.featured ? 'bg-vp-brand text-white hover:bg-vp-brand-light'
                                        : 'border border-vp-brand text-vp-brand hover:bg-vp-brand hover:text-white']"
                               :href="buttonHref"
                               @click.prevent="handleCtaClick(product.name)">
                                {{ buttonText }}
                            </a>
                            <Button v-else
                                    class="w-full text-sm font-medium"
                                    :class="product.featured ? 'bg-vp-brand text-white hover:bg-vp-brand-light'
                                           : 'border border-vp-brand text-vp-brand hover:bg-vp-brand hover:text-white'"
                                    @click="handleCtaClick(product.name)">
                                {{ buttonText }}
                            </Button>
                        </div>
                    </div>
                </Card>
            </div>
        </div>
    </div>
</template>

<style scoped>
.price-card {
    transition: all 0.3s ease-in-out;
}

.price-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
}

.product-description {
    min-height: 3rem;
}
</style>
