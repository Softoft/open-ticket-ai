import FunctionDoc from '../.vitepress/components/FunctionDoc.vue'
import type { Meta, StoryObj } from '@storybook/vue3'

const meta: Meta<typeof FunctionDoc> = {
  title: 'Components/FunctionDoc',
  component: FunctionDoc,
}
export default meta

type Story = StoryObj<typeof meta>

const sampleFunc = {
  name: 'add',
  signature: '(a: number, b: number) => number',
  docstring: {
    short_description: 'Adds two numbers',
    long_description: 'Returns the sum of a and b.'
  },
  is_async: false
}

export const Default: Story = {
  render: (args) => ({
    components: { FunctionDoc },
    setup() { return { args } },
    template: '<FunctionDoc v-bind="args" />'
  }),
  args: { func: sampleFunc }
}
