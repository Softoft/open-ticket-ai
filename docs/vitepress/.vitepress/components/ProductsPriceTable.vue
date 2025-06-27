/**
 * ProductsPriceTable renders a responsive table of projects with their prices
 * and feature lists.
 *
 * @prop projects Array of objects containing `name`, `price` and `features`.
 *
 * @example
 * ```vue
 * <script setup lang="ts">
 * import ProductsPriceTable from '.vitepress/components/ProductsPriceTable.vue'
 *
 * const projects = [
 *   { name: 'Basic', price: 1000, features: ['Setup'] }
 * ]
 * </script>
 *
 * <div class="table-responsive">
 *   <ProductsPriceTable :projects="projects" />
 * </div>
 * ```
 */
<template>
  <table class="table table-striped table-hover">
    <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Price</th>
        <th scope="col">Features</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(project, index) in projects" :key="index">
        <td>{{ project.name }}</td>
        <td>{{ formatPrice(project.price) }}</td>
        <td>
          <ul class="mb-0">
            <li v-for="(f, idx) in project.features" :key="idx">{{ f }}</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
const props = defineProps<{
  projects: { name: string; price: number; features: string[] }[]
}>()

const formatPrice = (value: number): string =>
  new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(value)
</script>
