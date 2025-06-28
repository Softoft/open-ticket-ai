<script lang="ts" setup>
import {ref} from 'vue' // Import ref

// 'selectedPlan' is no longer a model. It's just a local state if needed.
// We can actually remove it if the component itself doesn't use the selected state.
// For this example, we'll assume it might be used for internal styling or logic later.
const selectedPlan = ref<string | null>(null)

// Props are defined as before
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

// The emit declaration remains the same
const emits = defineEmits<{
    (e: 'cta-click', productName: string): void
}>()

// --- Data Interfaces ---
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

// --- Methods ---
const handleCtaClick = (productName: string) => {
    // Set the local ref's value
    selectedPlan.value = productName
    // Emit the event to the parent
    emits('cta-click', productName)
}
</script>

<template>
    <div class="pricing-component container py-5">
        <h2 class="text-center display-4 fw-bold mb-5">{{ title }}</h2>
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 justify-content-center">
            <div
                v-for="(product, index) in products"
                :key="index"
                class="col"
            >
                <div
                    :class="{ 'border-primary border-2': product.featured }"
                    class="card h-100 shadow-sm"
                >
                    <div class="card-body p-4 d-flex flex-column">
                        <h3 class="card-title fw-bold">{{ product.name }}</h3>
                        <p class="text-body-secondary">{{ product.description }}</p>

                        <div class="my-3">
                            <span class="display-5 fw-bolder">${{ product.price }}</span>
                            <span v-if="product.pricePeriod" class="text-body-secondary">&nbsp;/ {{
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
.card {
    transition: all 0.3s ease-in-out;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
}

.featured-plan {
    transform: scale(1.05);
}
</style>
