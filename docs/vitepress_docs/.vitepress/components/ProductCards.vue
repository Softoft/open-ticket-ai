<script lang="ts" setup>
var __VUE_PROD_DEVTOOLS__ = false

import {ref} from 'vue'

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
    <div class="pricing-component my-5">
        <h2 class="text-center display-3 fw-bold mb-5">{{ title }}</h2>
        <div class="row row-cols-1 row-cols-lg-3 g-4 justify-content-center">
            <div
                v-for="(product, index) in products"
                :key="index"
                class="col"
            >
                <div
                    :class="{ 'border-primary border-2': product.featured }"
                    class="card price-card h-100 shadow-sm py-3"
                >
                    <div class="card-body px-2 px-xl-3 py-0 d-flex flex-column">
                        <h3 class="card-title fw-bold">{{ product.name }}</h3>
                        <p class="text-body-secondary product-description">{{ product.description }}</p>

                        <div class="my-2">
                            <span class="display-5 fw-bolder">${{ product.price }}</span>
                            <span v-if="product.pricePeriod" class="text-body-secondary"> / {{
                                    product.pricePeriod
                                }}</span>
                        </div>

                        <hr>

                        <ul class="list-unstyled mb-4">
                            <li
                                v-for="(feature, fIndex) in product.features"
                                :key="fIndex"
                                class="d-flex align-items-center mb-3"
                            >
                                <i :class="['fas', feature.icon, 'me-3', 'text-primary']"></i>
                                <span>{{ feature.text }}</span>
                            </li>
                        </ul>

                        <div class="mt-auto">
                            <a v-if="buttonHref"
                               :class="['btn', 'w-100', 'btn-lg', product.featured ? 'btn-primary' : 'btn-outline-primary']"
                               :href="buttonHref"
                               @click.prevent="handleCtaClick(product.name)"
                            >
                                {{ buttonText }}
                            </a>
                            <button v-else
                                    :class="['btn', 'w-100', 'btn-lg', product.featured ? 'btn-primary' : 'btn-outline-primary']"
                                    @click="handleCtaClick(product.name)"
                            >
                                {{ buttonText }}
                            </button>
                        </div>
                    </div>
                </div>
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

.product-description{
    min-height: 3rem;
}
</style>
