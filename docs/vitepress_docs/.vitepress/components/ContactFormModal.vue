<template>
    <div>
        <div
            :class="{ show: isVisible }"
            :style="{ display: isVisible ? 'block' : 'none' }"
            class="modal fade"
            tabindex="-1"
        >
            <div class="modal-dialog">
                <div class="modal-content">
                    <form @submit.prevent="handleSubmit">
                        <div class="modal-header">
                            <h5 id="contactFormLabel" class="modal-title">Contact Us</h5>
                            <button aria-label="Close" class="btn-close" type="button"
                                    @click="close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="mb-3">
                                <label class="form-label fw-bold">Plan of Interest</label>
                                <input
                                    v-model="form.plan"
                                    class="form-control"
                                    disabled
                                    readonly
                                    type="text"
                                />
                            </div>
                            <div class="mb-3">
                                <label class="form-label fw-bold">Your Name</label>
                                <input
                                    v-model="form.name"
                                    class="form-control"
                                    placeholder="e.g., Jane Doe"
                                    required
                                    type="text"
                                />
                            </div>
                            <div class="mb-3">
                                <label class="form-label fw-bold">Company Name</label>
                                <input
                                    v-model="form.company"
                                    class="form-control"
                                    placeholder="e.g., Example Corp"
                                    type="text"
                                />
                            </div>
                            <div class="mb-3">
                                <label class="form-label fw-bold">Work Email</label>
                                <input
                                    v-model="form.email"
                                    class="form-control"
                                    placeholder="jane.doe@example.com"
                                    required
                                    type="email"
                                />
                            </div>
                            <div class="mb-3">
                                <label class="form-label fw-bold">Please tell us a bit about your
                                    needs.</label>
                                <textarea
                                    v-model="form.requirements"
                                    class="form-control"
                                    placeholder=""
                                    rows="4"
                                ></textarea>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-secondary" type="button" @click="close">Close
                            </button>
                            <button class="btn btn-primary" type="submit">Request a Consultation
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div v-if="isVisible" class="modal-backdrop fade show"></div>
    </div>
</template>

<script lang="ts" setup>
import {defineExpose, ref} from 'vue'

interface ContactFormData {
    plan: string
    name: string
    company: string
    email: string
    requirements: string
}

const emit = defineEmits<{
    (e: 'submit', data: ContactFormData): void
}>()

const isVisible = ref(false)

const form = ref<ContactFormData>({
    plan: 'Professional Acceleration',
    name: '',
    company: '',
    email: '',
    requirements: ''
})

function open() {
    isVisible.value = true
}

function close() {
    isVisible.value = false
}

function handleSubmit() {
    emit('submit', {...form.value})
    close()
}

defineExpose({open, close})
</script>

<style scoped>
.modal-backdrop.show {
    opacity: 0.8;
}
</style>
