<template>
  <div class="my-8">
    <h2 class="!mb-6 !text-4xl font-bold text-center">{{ title }}</h2>
    <div class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
      <ProductCard
        v-for="product in products"
        :key="product.name"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import ProductCard from './ProductCard.vue'
import {Product} from "./product.types";

const props = defineProps<{
  products: Product[]
  title: string
}>()
</script>
