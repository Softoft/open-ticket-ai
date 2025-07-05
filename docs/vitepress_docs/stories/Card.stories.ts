import Card from '../.vitepress/components/core/Card.vue'
import type { Meta, StoryObj } from '@storybook/vue3'

const meta: Meta<typeof Card> = {
  title: 'Core/Card',
  component: Card,
}
export default meta

type Story = StoryObj<typeof meta>

export const Default: Story = {
  render: (args) => ({
    components: { Card },
    setup() { return { args } },
    template: '<Card>Simple card content</Card>'
  }),
}
