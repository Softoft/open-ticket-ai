import SupportPlansComponent from '../.vitepress/components/SupportPlansComponent.vue'
import type { Meta, StoryObj } from '@storybook/vue3'
import { i18n } from './i18nSetup'

const meta: Meta<typeof SupportPlansComponent> = {
  title: 'Components/SupportPlansComponent',
  component: SupportPlansComponent,
}
export default meta

type Story = StoryObj<typeof meta>

export const Default: Story = {
  render: (args, { app }) => ({
    components: { SupportPlansComponent },
    setup() {
      app.use(i18n)
      return { args }
    },
    template: '<SupportPlansComponent />'
  })
}
