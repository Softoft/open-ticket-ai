<!-- pages/SyntheticDataSection.vue -->
<template>
    <section class="my-12 px-4">
        <h2 class="mb-6 text-3xl font-bold text-center text-white">

        </h2>
        <ProductCards
            :products="syntheticPackages"
            title="Synthetic Data Packages"/>
    </section>
</template>

<script lang="ts" setup>
import ProductCards from './ProductCards.vue'
import type {Product} from './product.types'

// define your three tiers, matching the Service Packages style
const syntheticPackages: Product[] = [
    {
        name: 'Starter Data Kit',
        price: 2000,
        description: '25k synthetic tickets with queue labels only',
        features: [
            {text: '25k synthetic tickets', icon: 'fa-database'},
            {text: 'Queue labels only', icon: 'fa-tags'},
        ],
    },
    {
        name: 'Growth Data Kit',
        price: 4000,
        description: '50k tickets with queue & priority labels',
        features: [
            {text: '50k synthetic tickets', icon: 'fa-cubes'},
            {text: 'Queue & priority labels', icon: 'fa-layer-group'},
            {text: 'Basic schema validation', icon: 'fa-check-circle'},
        ],
    },
    {
        name: 'Enterprise Data Kit',
        price: 8000,
        description: 'Unlimited tickets & custom schema support',
        features: [
            {text: '200k synthetic tickets', icon: 'fa-infinity'},
            {text: 'Custom schema & attributes', icon: 'fa-project-diagram'},
            {text: 'Dedicated integration support', icon: 'fa-headset'},
            {text: 'Data quality & audit report', icon: 'fa-file-alt'},
        ],
    },
]
</script>
