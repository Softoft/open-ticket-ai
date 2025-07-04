<template>
  <div class="divide-y divide-slate-700">
    <div v-for="(item, i) in items" :key="i">
      <button
        class="flex w-full justify-between py-3 font-semibold text-left"
        @click="toggle(i)"
      >
        <span>{{ item.title }}</span>
        <span>{{ openIndex === i ? '-' : '+' }}</span>
      </button>
      <div v-show="openIndex === i" class="pb-3 text-slate-400">
        <slot :name="`item-${i}`">{{ item.content }}</slot>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

interface Item {
  title: string
  content?: string
}

const props = defineProps<{ items: Item[] }>()
const openIndex = ref<number | null>(null)

function toggle(i: number) {
  openIndex.value = openIndex.value === i ? null : i
}
</script>
