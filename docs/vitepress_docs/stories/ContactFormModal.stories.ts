import ContactFormModal from '../.vitepress/components/ContactFormModal.vue'
import Button from '../.vitepress/components/core/Button.vue'
import { ref } from 'vue'
import type { Meta, StoryObj } from '@storybook/vue3'

const meta: Meta<typeof ContactFormModal> = {
  title: 'Components/ContactFormModal',
  component: ContactFormModal,
}
export default meta

type Story = StoryObj<typeof meta>

export const Default: Story = {
  render: (args) => ({
    components: { ContactFormModal, Button },
    setup() {
      const visible = ref(true)
      return { args, visible }
    },
    template: '<ContactFormModal v-if="visible" v-bind="args" />'
  }),
  args: { plan: 'Professional' }
}
