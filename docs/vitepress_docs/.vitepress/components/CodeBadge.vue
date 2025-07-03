<template>
  <span :class="badgeClass" class="badge me-2">
    <slot>{{ text }}</slot>
  </span>
</template>

<script lang="ts" setup>
import {computed} from 'vue';

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

const badgeClass = computed(() => `bg-${props.type}`);
</script>

<style scoped>
.badge {
    font-size: 0.8em;
    vertical-align: middle;
}
</style>
