<template>
  <div class="w-full">
    <Listbox v-model="selected" :disabled="disabled">
      <ListboxLabel v-if="label" class="block text-sm font-medium text-gray-300 mb-1">
        {{ label }}
      </ListboxLabel>

      <div class="relative">
        <ListboxButton
          class="w-full rounded-md border border-gray-600 bg-gray-800 py-2 pl-3 pr-10 text-left shadow-sm focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white/75 focus-visible:ring-offset-2 focus-visible:ring-offset-indigo-500 text-white"
        >
          <span class="block truncate">{{ selectedLabel }}</span>
          <span class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
            <ChevronUpDownIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
          </span>
        </ListboxButton>

        <transition
          leave-active-class="transition duration-100 ease-in"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <ListboxOptions
            class="absolute mt-0 w-full overflow-auto rounded-md bg-gray-700 text-base shadow-lg ring-1 ring-black/20 focus:outline-none list-none p-0"
          >
            <ListboxOption
              v-for="option in options"
              :key="option.value"
              :value="option.value"
              :disabled="option.disabled"
              as="template"
              v-slot="{ active, selected: isSelected, disabled: isDisabled }"
            >
              <li
                :class="[
                  'relative cursor-default select-none py-2 pl-10 mx-0 pr-4 rounded-md transition-colors',
                  // UPDATED: Added styles for active and disabled states for better hierarchy
                  {
                    'bg-indigo-500 text-white': active && !isDisabled,
                    'text-gray-300': !active,
                    'opacity-50 cursor-not-allowed': isDisabled,
                  }
                ]"
              >
                <span :class="[isSelected ? 'font-semibold' : 'font-normal', 'block truncate']">
                  {{ option.label }}
                </span>
                <span
                  v-if="isSelected"
                  class="absolute inset-y-0 left-0 flex items-center pl-3"
                  :class="{ 'text-white': active, 'text-indigo-400': !active }"
                >
                  <CheckIcon class="h-5 w-5" aria-hidden="true" />
                </span>
              </li>
            </ListboxOption>
          </ListboxOptions>
        </transition>
      </div>
    </Listbox>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import {
  Listbox,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
  ListboxLabel,
} from '@headlessui/vue'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'

// UPDATED: Option can now be disabled
interface Option {
  value: string | number
  label: string
  disabled?: boolean
}

const props = withDefaults(
  defineProps<{
    options: Option[]
    modelValue?: string | number | null
    placeholder?: string
    disabled?: boolean
    label?: string
  }>(),
  {
    modelValue: null,
    placeholder: 'Select an option',
    disabled: false,
    label: '',
  }
)

const emit = defineEmits<{
  (e: 'update:modelValue', value: string | number | null): void
}>()

const selected = ref(props.modelValue)

watch(
  () => props.modelValue,
  (newValue) => {
    selected.value = newValue
  }
)

watch(selected, (newValue) => {
  emit('update:modelValue', newValue)
})

const selectedLabel = computed(() => {
  const foundOption = props.options.find(opt => opt.value === selected.value)
  return foundOption ? foundOption.label : props.placeholder
})
</script>
