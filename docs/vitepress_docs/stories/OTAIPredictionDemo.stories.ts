import OTAIPredictionDemo from '../.vitepress/components/OTAIPredictionDemo.vue'
import type { Meta, StoryObj } from '@storybook/vue3'

const meta: Meta<typeof OTAIPredictionDemo> = {
  title: 'Components/OTAIPredictionDemo',
  component: OTAIPredictionDemo,
}
export default meta

type Story = StoryObj<typeof meta>

export const Default: Story = {
  render: () => ({
    components: { OTAIPredictionDemo },
    template: '<OTAIPredictionDemo />'
  })
}
