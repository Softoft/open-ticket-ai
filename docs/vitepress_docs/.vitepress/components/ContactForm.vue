<!-- components/ContactForm.vue -->
<template>
  <div class="max-w-4xl mx-auto pt-4 pb-10 px-10 bg-gray-900 rounded-lg space-y-6">
      <h3 class="!text-2xl font-bold text-gray-100 mb-4">
        Contact Us
      </h3>
    <p class="text-sm text-gray-400">
      Or email us directly at
      <a href="mailto:sales@softoft.de" class="text-blue-400 hover:underline">
        sales@softoft.de
      </a>
    </p>

    <form
      action="https://formspree.io/f/movwyjqz"
      method="POST"
      class="space-y-4"
    >
      <!-- actual form fields (hidden) -->
      <input type="hidden" name="email" :value="email" />
      <input type="hidden" name="message" :value="message" />

      <div>
        <label for="email" class="block text-sm font-medium text-gray-200 mb-1">
          Your email
        </label>
        <TextField
          id="email"
          v-model="email"
          placeholder="you@domain.com"
          :disabled="isSubmitting"
        />
      </div>

      <div>
        <label for="message" class="block text-sm font-medium text-gray-200 mb-1">
          Your message
        </label>
        <TextArea
          id="message"
          v-model="message"
          placeholder="How can we help you?"
          rows="5"
        />
      </div>

      <Button
        type="submit"
        variant="primary"
        class="px-8 text-xl"
      >
        Send
      </Button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import TextField from './core/forms/TextField.vue'
import TextArea from './core/forms/TextArea.vue'
import Button from './core/Button.vue'

const email = ref('')
const message = ref('')

</script>
