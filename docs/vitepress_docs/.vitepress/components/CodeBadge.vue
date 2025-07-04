<template>
  <Badge :type="type" class="me-2">
    <slot>{{ text }}</slot>
  </Badge>
</template>

<script lang="ts" setup>
import Badge from './core/Badge.vue'

// Define typed props using the <script setup> syntax
interface Props {
    text?: string;
    // Use a union type for better type safety on the 'type' prop
    type?: 'primary' | 'secondary' | 'success' | 'danger' | 'warning' | 'info';
}

// Use withDefaults to provide default values for the typed props
const props = withDefaults(defineProps<Props>(), {
    type: 'secondary',
    text: '',
});

</script>

<style scoped>
.me-2 {
  margin-right: 0.5rem;
}
</style>
