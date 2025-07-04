<template>
  <Card class="mb-4">
    <div class="mb-2 flex items-center gap-2">
      <Badge :type="methodColor">{{ method.toUpperCase() }}</Badge>
      <code class="font-mono text-cloud-white">{{ endpoint }}</code>
    </div>
    <p class="mb-2 text-slate-400" v-if="description">{{ description }}</p>
    <slot />
  </Card>
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import Card from './Card.vue'
import Badge from './Badge.vue'

interface Props {
  method: string
  endpoint: string
  description?: string
}

const props = defineProps<Props>()

const methodColor = computed(() => {
  const m = props.method.toUpperCase()
  if (m === 'GET') return 'secondary'
  if (m === 'POST') return 'primary'
  if (m === 'PUT') return 'warning'
  if (m === 'DELETE') return 'danger'
  return 'secondary'
})
</script>
