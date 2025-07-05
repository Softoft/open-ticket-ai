<template>
    <div>
        <div
            v-if="isVisible"
            class="fixed inset-0 z-50 flex items-center justify-center"
        >
            <div class="bg-vp-bg rounded-lg shadow-lg max-w-lg w-full">
                <form @submit.prevent="handleSubmit">
                    <div class="flex items-center justify-between p-4 border-b border-vp-border">
                        <h5 id="contactFormLabel" class="text-lg font-semibold">Contact Us</h5>
                                <Button aria-label="Close" type="button"
                                class="px-2 text-vp-text hover:text-vp-brand"
                                variant="secondary" @click="close">&times;</Button>
                    </div>
                    <div class="p-4">
                            <div class="mb-3">
                                <label class="mb-1 font-bold">Plan of Interest</label>
                                <input
                                    v-model="form.plan"
                                    class="block w-full rounded border border-vp-border p-2 mb-2 bg-vp-bg"
                                    disabled
                                    readonly
                                    type="text"
                                />
                            </div>
                            <div class="mb-3">
                                <label class="mb-1 font-bold">Your Name</label>
                                <input
                                    v-model="form.name"
                                    class="block w-full rounded border border-vp-border p-2 bg-vp-bg"
                                    placeholder="e.g., Jane Doe"
                                    required
                                    type="text"
                                />
                            </div>
                            <div class="mb-3">
                                <label class="mb-1 font-bold">Company Name</label>
                                <input
                                    v-model="form.company"
                                    class="block w-full rounded border border-vp-border p-2 bg-vp-bg"
                                    placeholder="e.g., Example Corp"
                                    type="text"
                                />
                            </div>
                            <div class="mb-3">
                                <label class="mb-1 font-bold">Work Email</label>
                                <input
                                    v-model="form.email"
                                    class="block w-full rounded border border-vp-border p-2 bg-vp-bg"
                                    placeholder="jane.doe@example.com"
                                    required
                                    type="email"
                                />
                            </div>
                            <div class="mb-3">
                                <label class="mb-1 font-bold">Please tell us a bit about your
                                    needs.</label>
                                <textarea
                                    v-model="form.requirements"
                                    class="block w-full rounded border border-vp-border p-2 bg-vp-bg"
                                    placeholder=""
                                    rows="4"
                                ></textarea>
                            </div>
                        </div>
                        <div class="flex justify-end gap-2 border-t border-vp-border p-4">
                            <Button variant="secondary" type="button" @click="close">Close
                            </Button>
                            <Button class="bg-vp-brand text-white hover:bg-vp-brand-light" type="submit">Request a Consultation
                            </Button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div v-if="isVisible" class="fixed inset-0 z-40 bg-black/50" @click="close"></div>
    </div>
</template>

<script lang="ts" setup>

import {defineExpose, ref} from 'vue'
import Button from './core/Button.vue'

interface ContactFormData {
    plan: string
    name: string
    company: string
    email: string
    requirements: string
}

const {plan} = defineProps<{
    plan: string
}>()




const form = ref<ContactFormData>({
    plan: plan,
    name: '',
    company: '',
    email: '',
    requirements: ''
})
</script>


