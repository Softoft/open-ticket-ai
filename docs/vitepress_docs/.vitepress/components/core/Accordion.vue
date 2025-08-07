<template>
  <div class="divide-y divide-vp-border">
    <Disclosure
      v-for="(item, i) in items"
      :key="i"
      as="div"
      class="py-3"
    >
      <template #default="{ open }">
        <DisclosureButton
          class="flex w-full justify-between font-semibold text-left"
        >
          <span class="font-bold text-lg">{{ item.title }}</span>
          <span>{{ open ? '–' : '+' }}</span>
        </DisclosureButton>
        <DisclosurePanel class="pt-2 text-vp-text-2">
          <slot :name="`item-${i}`">{{ item.content }}</slot>
        </DisclosurePanel>
      </template>
    </Disclosure>
  </div>
</template>

<script setup lang="ts">
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue'

interface Item {
  title: string
  content?: string
}

const {items} = defineProps<{
  items: Item[]
}>()
</script>
