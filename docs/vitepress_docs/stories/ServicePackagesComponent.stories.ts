import ServicePackagesComponent from '../.vitepress/components/ServicePackagesComponent.vue'
import type { Meta, StoryObj } from '@storybook/vue3'

const meta: Meta<typeof ServicePackagesComponent> = {
  title: 'Components/ServicePackagesComponent',
  component: ServicePackagesComponent,
}
export default meta

type Story = StoryObj<typeof meta>

export const Default: Story = {
  render: () => ({
    components: { ServicePackagesComponent },
    template: '<ServicePackagesComponent />'
  })
}
