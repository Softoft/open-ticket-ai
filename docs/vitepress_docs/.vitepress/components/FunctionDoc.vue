<template>
    <!-- Render only header and body; no nested Accordion -->
    <div class="space-y-2 p-4 border border-gray-200 dark:border-gray-700 rounded">
        <div class="flex items-center space-x-2 cursor-pointer">
            <Badge v-if="func.is_async" type="warning">async</Badge>
            <span class="font-mono font-bold text-lg">
        {{ func.name }}
        <span class="text-gray-800 dark:text-gray-200">{{ func.signature }}</span>
      </span>
        </div>
        <div class="mt-2">
            <Docstring :doc="func.docstring"/>
        </div>
    </div>
</template>

<script lang="ts" setup>
import type {FunctionData} from '../composables/useApiDocs'
import Badge from './core/Badge.vue'
import Docstring from './Docstring.vue'

defineProps<{ func: FunctionData }>()
</script>
