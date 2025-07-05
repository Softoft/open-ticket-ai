import Button from '../.vitepress/components/core/Button.vue'
import type { Meta, StoryObj } from '@storybook/vue3'

const meta: Meta<typeof Button> = {
  title: 'Core/Button',
  component: Button,
  argTypes: {
    variant: { control: { type: 'select' }, options: ['primary', 'secondary'] },
    disabled: { control: 'boolean' }
  },
}
export default meta

type Story = StoryObj<typeof meta>

export const Primary: Story = {
  render: (args) => ({
    components: { Button },
    setup() { return { args } },
    template: '<Button v-bind="args">Primary Button</Button>'
  }),
  args: { variant: 'primary', disabled: false }
}

export const Secondary: Story = {
  render: (args) => ({
    components: { Button },
    setup() { return { args } },
    template: '<Button v-bind="args">Secondary Button</Button>'
  }),
  args: { variant: 'secondary', disabled: false }
}
