import SupportPlansComponent from '../.vitepress/components/SupportPlansComponent.vue'
import type { Meta, StoryObj } from '@storybook/vue3'

const meta: Meta<typeof SupportPlansComponent> = {
  title: 'Components/SupportPlansComponent',
  component: SupportPlansComponent,
}
export default meta

type Story = StoryObj<typeof meta>

export const Default: Story = {
  render: () => ({
    components: { SupportPlansComponent },
    template: '<SupportPlansComponent />'
  })
}
