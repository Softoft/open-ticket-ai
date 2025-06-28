<template>
  <div>
    <div
      class="modal fade"
      :class="{ show: isVisible }"
      tabindex="-1"
      :style="{ display: isVisible ? 'block' : 'none' }"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <form @submit.prevent="handleSubmit">
            <div class="modal-header">
              <h5 class="modal-title" id="contactFormLabel">Contact Us</h5>
              <button type="button" class="btn-close" aria-label="Close" @click="close"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label class="form-label fw-bold">Plan of Interest</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="form.plan"
                  readonly
                  disabled
                />
              </div>
              <div class="mb-3">
                <label class="form-label fw-bold">Your Name</label>
                <input
                  v-model="form.name"
                  type="text"
                  class="form-control"
                  placeholder="e.g., Jane Doe"
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label fw-bold">Company Name</label>
                <input
                  v-model="form.company"
                  type="text"
                  class="form-control"
                  placeholder="e.g., Example Corp"
                />
              </div>
              <div class="mb-3">
                <label class="form-label fw-bold">Work Email</label>
                <input
                  v-model="form.email"
                  type="email"
                  class="form-control"
                  placeholder="e.g., jane.doe@example.com"
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label fw-bold">Please tell us a bit about your needs.</label>
                <textarea
                  v-model="form.requirements"
                  class="form-control"
                  rows="4"
                  placeholder="For example: What ticket system are you currently using? What is your approximate monthly ticket volume? What are your main goals with AI automation (e.g., faster response times, reducing manual work)?"
                ></textarea>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="close">Close</button>
              <button type="submit" class="btn btn-primary">Request a Consultation</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div v-if="isVisible" class="modal-backdrop fade show"></div>
  </div>
</template>

<script lang="ts" setup>
import { ref, defineExpose } from 'vue'

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
  emit('submit', { ...form.value })
  close()
}

defineExpose({ open, close })
</script>

<style scoped>
.modal-backdrop.show {
  opacity: 0.8;
}
</style>
