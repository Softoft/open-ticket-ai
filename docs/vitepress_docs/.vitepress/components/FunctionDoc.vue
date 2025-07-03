<template>
    <div class="accordion-item">
        <span :id="`heading-${uniqueId}`" class="accordion-header">
            <button
                :aria-controls="`#collapse-${uniqueId}`"
                :data-bs-target="`#collapse-${uniqueId}`"
                aria-expanded="false"
                class="accordion-button collapsed"
                data-bs-toggle="collapse"
                type="button"
            >
                <span class="d-flex align-items-center w-100">
                    <CodeBadge v-if="func.is_async" text="async" type="info"/>
                    <span class="font-monospace text-nowrap">
                        <span class="function-name fw-bold me-1">{{ func.name }}</span>
                        <span class="signature-text">{{ func.signature }}</span>
                    </span>
                </span>
            </button>
        </span>
        <div :id="`collapse-${uniqueId}`" :aria-labelledby="`heading-${uniqueId}`" class="accordion-collapse collapse">
            <div class="accordion-body">
                <Docstring :doc="func.docstring"/>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import {computed} from 'vue';
import type {FunctionData} from '../composables/useApiDocs';
import Docstring from './Docstring.vue';
import CodeBadge from './CodeBadge.vue';

interface Props {
    func: FunctionData;
    parentId?: string;
}

const props = defineProps<Props>();

// Create a unique ID for accordion controls to prevent collisions
const uniqueId = computed(() => {
    const parent = props.parentId ? props.parentId.replace(/\W/g, '_') : 'global';
    return `${parent}-${props.func.name}`;
});
</script>

<style scoped>
.accordion-item {
    /* Use Bootstrap variables for automatic dark/light theme support */
    background-color: var(--bs-body-bg);
    border: 1px solid var(--bs-border-color-translucent);
}

.accordion-button {
    background-color: var(--bs-tertiary-bg);
    color: var(--bs-body-color);
    transition: background-color 0.15s ease-in-out;
}

.accordion-button:not(.collapsed) {
    background-color: var(--bs-secondary-bg);
    color: var(--bs-emphasis-color);
}

.accordion-button:focus {
    box-shadow: 0 0 0 0.25rem rgba(var(--bs-primary-rgb), 0.25);
    border-color: var(--bs-primary);
}

.accordion-button:hover {
    background-color: var(--bs-secondary-bg);
}

.function-name {
    color: var(--bs-primary);
}

/* In dark mode, the default signature text can be too bright */
[data-bs-theme="dark"] .signature-text {
    color: var(--bs-gray-400);
}

.font-monospace {
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
