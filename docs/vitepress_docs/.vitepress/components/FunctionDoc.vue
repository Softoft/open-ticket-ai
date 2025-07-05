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
                    <Badge v-if="func.is_async" text="async" type=""/>
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
    background-color: var(--vp-c-bg);
    border: 1px solid var(--vp-c-divider);
}

.accordion-button {
    background-color: var(--vp-c-bg-soft);
    color: var(--vp-c-text-1);
    transition: background-color 0.15s ease-in-out;
}

.accordion-button:not(.collapsed) {
    background-color: var(--vp-c-bg-soft);
    color: var(--vp-c-text-1);
}

.accordion-button:focus {
    box-shadow: 0 0 0 0.25rem var(--vp-c-brand-soft);
    border-color: var(--vp-c-brand-1);
}

.accordion-button:hover {
    background-color: var(--vp-c-bg-soft);
}

.function-name {
    color: var(--vp-c-brand-1);
}

/* In dark mode, the default signature text can be too bright */
[data-bs-theme="dark"] .signature-text {
    color: var(--vp-c-text-2);
}

.font-monospace {
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
