<script lang="ts" setup>
// Define TypeScript interfaces for better type safety and reusability
interface Feature {
    text: string;
    icon: string; // e.g., 'fa-check', 'fa-star'
}

interface Product {
    name: string;
    price: number;
    features: Feature[];
}

// Use the new Vue 3.5 defineProps syntax with the Product interface
const {products, title} = defineProps<{
    products: Product[],
    title: string,
    buttonText?: string
    ctaLink?: string
}>();

const emits = defineEmits<{
    (e: 'cta-click', productName: string): void;
}>();

const handleCtaClick = (productName: string) => {
    console.log(`CTA clicked for ${productName}`);
    emits('cta-click', productName);
}
</script>

<template>
    <h2 class="text-center mb-4">{{ title }}</h2>
    <div class="product-grid">
        <div
            v-for="(product, index) in products"
            :key="index"
            class="product-card"
        >
            <div class="product-card-header">
                <h5 class="product-name">{{ product.name }}</h5>
            </div>
            <div class="product-card-body">
                <h6 class="product-price">{{ product.price }}</h6>
                <p class="features-title">Features included:</p>
                <ul class="features-list">
                    <li
                        v-for="(feature, fIndex) in product.features"
                        :key="fIndex"
                        class="feature-item"
                    >
                        <i :class="['fas', feature.icon, 'feature-icon']"></i>
                        <span>{{ feature.text }}</span>
                    </li>
                </ul>
                <a class="cta-button" :href="ctaLink">
                    {{ buttonText || 'Get Started'}}
                </a>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Main grid container for the product cards */
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
}

/* Individual product card styling for dark theme */
.product-card {
    border: 1px solid #444;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    background-color: #2c2c2e;
    color: #e0e0e0;
    display: flex;
    flex-direction: column;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
}

/* Card header section */
.product-card-header {
    padding: 1.25rem 1.25rem 0 1.25rem;
}

/* Product name title */
.product-name {
    margin: 0;
    font-size: 1.25rem;
    font-weight: 600;
    color: #f5f5f5;
}

/* Card body section */
.product-card-body {
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}

/* Product price subtitle */
.product-price {
    color: #ffffff;
    font-size: 1.5rem;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 1.5rem;
}

/* "Features included" text */
.features-title {
    font-weight: 500;
    margin-bottom: 0.5rem;
    color: #a0a0a0;
}

/* Unordered list for features */
.features-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

/* Individual feature list item */
.feature-item {
    padding: 0.75rem 0;
    display: flex;
    align-items: center;
    font-size: 1rem;
}

/* Font Awesome icon styling */
.feature-icon {
    margin-right: 0.75rem;
    width: 1.25em;
    text-align: center;
    color: #3b82f6;
}

/* Call to Action button */
.cta-button {
    background-color: #3b82f6;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    text-align: center;
    margin-top: auto; /* Pushes the button to the bottom */
    transition: background-color 0.2s ease-in-out;
}

.cta-button:hover {
    background-color: #2563eb;
}
</style>
