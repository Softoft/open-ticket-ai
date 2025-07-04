<template>
  <button
    :class="[
      'inline-flex items-center font-semibold rounded transition focus:outline-none',
      variantClasses,
      disabled ? 'opacity-50 cursor-not-allowed' : ''
    ]"
    :disabled="disabled"
  >
    <slot />
  </button>
</template>

<script lang="ts" setup>
import { computed } from 'vue'

interface Props {
  variant?: 'primary' | 'secondary'
  disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  disabled: false
})

const variantClasses = computed(() => {
  return props.variant === 'secondary'
    ? 'border border-slate-700 text-slate-300 hover:bg-slate-900 px-4 py-2'
    : 'bg-electric-teal text-black hover:brightness-110 px-4 py-2'
})
</script>
