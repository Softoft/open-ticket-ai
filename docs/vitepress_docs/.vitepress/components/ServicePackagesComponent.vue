<script lang="ts" setup>

const servicePackages = [
    {
        name: 'Essential Launch',
        price: 1000,
        description: 'Perfect for getting started with core AI capabilities.',
        features: [
            {text: 'Core Installation & System Setup', icon: 'fa-rocket'},
            {text: 'Deployment of Standard Prediction Model', icon: 'fa-brain'},
            {text: 'Ticket Prioritization Engine', icon: 'fa-sort-amount-up'},
            {text: 'Automated Queue Classification', icon: 'fa-sitemap'},
        ]
    },
    {
        name: 'Professional Acceleration',
        price: 4000,
        description: 'Tailor the AI to your specific business data and needs.',
        features: [
            {text: 'Core Installation & System Setup', icon: 'fa-rocket'},
            {text: 'Training of Queue Model', icon: 'fa-brain'},
            {text: 'Training of Prio Model', icon: 'fa-brain'},
            {text: 'Ticket Prioritization Engine', icon: 'fa-sort-amount-up'},
            {text: 'Automated Queue Classification', icon: 'fa-sitemap'},
        ]
    },
    {
        name: 'Enterprise Integration',
        price: 12000,
        description: 'Full integration and custom development for complex workflows.',
        features: [
            {text: 'Core Installation & System Setup', icon: 'fa-rocket'},
            {text: 'Training of Queue Model', icon: 'fa-brain'},
            {text: 'Training of Prio Model', icon: 'fa-brain'},
            {text: 'Ticket Prioritization Engine', icon: 'fa-sort-amount-up'},
            {text: 'Automated Queue Classification', icon: 'fa-sitemap'},
            {text: 'Custom Third-Party Ticket System Integration', icon: 'fa-project-diagram'},
            {text: 'Includes up to 3 Custom Attribute Predictions', icon: 'fa-magic'},
            {text: 'Each Additional Attribute Prediction: €3000', icon: 'fa-plus-circle'},
            {text: 'Bespoke Feature & Workflow Development', icon: 'fa-code-branch'},
        ]
    }
];

</script>

<template>
    <ProductCards :products="servicePackages" buttonText="Choose Plan"
                  ctaLink="mailto:sales@softoft.de"
                  title="Support"/>

</template>

<style scoped>

</style>
