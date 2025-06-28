<script lang="ts" setup>
const supportPlans = [
    {
        name: 'Basic Care',
        price: 100,
        description: 'Ensures your system remains stable, secure, and up-to-date.',
        features: [
            {text: 'Proactive System Updates & Patching', icon: 'fa-sync-alt'},
            {text: 'Uptime & Core Log Monitoring', icon: 'fa-chart-line'},
            {text: 'Monthly AI Performance Health Check', icon: 'fa-calendar-check'},
            {text: 'Support Response Time: Within 1 Business Day', icon: 'fa-clock'},
        ]
    },
    {
        name: 'Proactive Support',
        price: 300,
        description: 'Advanced monitoring and reporting for optimal performance.',
        features: [
            {text: 'All Basic Care Services', icon: 'fa-star'},
            {text: 'Weekly In-Depth Performance Monitoring', icon: 'fa-tachometer-alt'},
            {text: 'Comprehensive Monthly Performance Reports', icon: 'fa-file-alt'},
            {text: 'Priority Support Response: Within 1 Business Day', icon: 'fa-clock'},
        ]
    },
    {
        name: 'Enterprise Assurance',
        price: 1000,
        description: 'Complete operational oversight with strategic AI optimization.',
        features: [
            {text: 'All Proactive Support Services', icon: 'fa-star'},
            {text: 'Real-Time Monitoring & Anomaly Alerts', icon: 'fa-bell'},
            {text: 'Strategic AI Review & Optimization', icon: 'fa-chart-bar'},
            {text: 'Guaranteed Response Time: Within 1 Business Day', icon: 'fa-clock'},
        ]
    }
];

</script>

<template>
    <ProductCards :products="supportPlans" buttonText="Choose Plan"
                  ctaLink="mailto:sales@softoft.de" title="Services"/>
</template>

<style scoped>

</style>
