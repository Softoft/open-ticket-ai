---
layout: home

hero:
    name: "Open Ticket AI"
    text: ""
    tagline: Save time and money by automating
    image:
        light: https://softoft.sirv.com/Images/atc-logo-2024-blue.png?w=300&q=100
        dark: https://softoft.sirv.com/Images/atc-logo-2024-blue.png?w=300&q=100
        alt: VitePress
    actions:
        -   theme: brand
            text: Get Started
            link: /get-started
        -   theme: alt
            text: Feature Overview
            link: /concepts/community-edition-overview

features:
    -   title: Einfache Installation
        details: Installieren Sie ATC einfach mit Docker auf Ihrem Server.
        icon:
            light: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/server-solid.png?h=48&q=100"
            dark: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/server-solid.png?h=48&q=100&colorlevel.white=0"
            height: 48
            width: "auto"
            alt: "OTOBO ATC AI Icon"
    -   title: Leistungsstarke API
        details: Nutzen Sie die HTTP REST API für die Datenübertragung und Modellverwaltung.
        icon:
            light: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/code-solid.png?h=48&q=100"
            dark: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/code-solid.png?h=48&q=100&colorlevel.white=0"
            height: 48
            width: "auto"
            alt: "OTOBO ATC AI Icon"
    -   title: OTOBO Integration
        details: Verwenden Sie das ATC Add-On für nahtlose Integration in OTOBO.
        icon:
            light: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/plug-solid.png?h=48&q=100"
            dark: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/plug-solid.png?h=48&q=100&colorlevel.white=0"
            height: 48
            width: "auto"
            alt: "OTOBO ATC AI Icon"
    -   title: Automatisierte Klassifizierung
        details: Automatisieren Sie die Klassifizierung von Support-Tickets.
        icon:
            light: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/robot-solid.png?h=48&q=100"
            dark: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/robot-solid.png?h=48&q=100&colorlevel.white=0"
            height: 48
            width: "auto"
            alt: "OTOBO ATC AI Icon"
    -   title: Hohe Sicherheit
        details: Alle Daten werden lokal verarbeitet, um Datenschutz zu gewährleisten.
        icon:
            light: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/lock-solid.png?h=48&q=100"
            dark: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/lock-solid.png?h=48&q=100&colorlevel.white=0"
            height: 48
            width: "auto"
            alt: "OTOBO ATC AI Icon"
    -   title: Flexibilität
        details: Passen Sie die Konfiguration nach Ihren Bedürfnissen an.
        icon:
            light: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/gear-solid.png?h=48&q=100"
            dark: "https://softoft.sirv.com/Images/otobo/docs/custom/icons/gear-solid.png?h=48&q=100&colorlevel.white=0"
            height: 48
            width: "auto"
            alt: "OTOBO ATC AI Icon"
---


<script setup>import {useRouter} from 'vitepress';

const myProducts = [
  {
    name: 'Basic',
    price: 1000,
    features: [
      { text: 'Installation & Basic Setup', icon: 'fa-play-circle' },
      { text: 'Prediction with Standard Model', icon: 'fa-brain' },
      { text: 'Prioritization', icon: 'fa-tasks' },
      { text: 'Queue Classification', icon: 'fa-stream' },
    ]
  },
  {
    name: 'Pro',
    price: 9000,
    features: [
      { text: 'Installation & Basic Setup', icon: 'fa-play-circle' },
      { text: 'Fine-Tuning on Customer Data', icon: 'fa-cogs' },
      { text: 'Prioritization', icon: 'fa-tasks' },
      { text: 'Queue Classification', icon: 'fa-stream' },
    ]
  },
  {
    name: 'Enterprise',
    price: 12000,
    features: [
      { text: 'All Pro Features', icon: 'fa-check-circle' },
      { text: 'Installation & Basic Setup', icon: 'fa-play-circle' },
      { text: 'Fine-Tuning on Customer Data', icon: 'fa-cogs' },
      { text: 'Prioritization', icon: 'fa-tasks' },
      { text: 'Queue Classification', icon: 'fa-stream' },
      { text: 'New Attribute Prediction', icon: 'fa-star' },
      { text: 'New Ticket System Integration', icon: 'fa-project-diagram' },
    ]
  }
];

const mySupportProducts = [
  {
    name: 'Basic',
    price: 150,
    features: [
      { text: 'Apply updates', icon: 'fa-sync-alt' },
      { text: 'Basic monitoring (uptime, logs)', icon: 'fa-chart-line' },
      { text: 'Monthly AI performance review', icon: 'fa-calendar-alt' },
      { text: 'Response time ≤ 1 day', icon: 'fa-clock' },
    ]
  },
  {
    name: 'Pro',
    price: 400,
    features: [
      { text: 'Basic services', icon: 'fa-tools' },
      { text: 'Performance monitoring (weekly)', icon: 'fa-chart-line' },
      { text: 'Monthly reporting', icon: 'fa-file-alt' },
      { text: 'Response time ≤ 1 day', icon: 'fa-clock' },
    ]
  },
  {
    name: 'Enterprise',
    price: 1000,
    features: [
      { text: 'Pro services', icon: 'fa-briefcase' },
      { text: 'Real-time monitoring & alerts', icon: 'fa-bell' },
      { text: 'Quarterly AI review & optimization', icon: 'fa-chart-bar' },
      { text: 'Response time ≤ 1 day', icon: 'fa-clock' },
    ]
  }
];
const router = useRouter();

function navigateToGetStarted() {
  router.push('/get-started');
}

</script>



<OTAIPredictionDemo/>

## Products

<ProductCards :products="myProducts" title="Services" buttonText="Choose Plan" ctaLink="mailto:sales@softoft.de" />

## Support

<ProductCards :products="mySupportProducts" title="Support" buttonText="Choose Plan" ctaLink="mailto:sales@softoft.de" />

## Contact

<div class="text-center mt-8">
  <p class="text-lg font-semibold">Interested in our services?</p>
  <p class="text-gray-600">Contact us for a personalized offer.</p>
  <a href="mailto:sales@softoft.de" class="mt-4 inline-block bg-blue-600 text-white px-6 py-3 rounded hover:bg-blue-700 transition-colors">
    Email us at sales@softoft.de
  </a>
</div>
