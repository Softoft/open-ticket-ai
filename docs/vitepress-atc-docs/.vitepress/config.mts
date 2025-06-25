import {defineConfig} from 'vitepress'

export default defineConfig({
    title: "AI Ticket Classification",
    head: [
        ['link', {
            rel: 'icon',
            href: 'https://softoft.sirv.com/Images/atc-logo-2024-blue.png?w=300&q=100&lightness=100&colorlevel.white=100'
        }]
    ],
    description: "",
    sitemap: {
        hostname: "https://ai-ticket-classification.softoft.de"
    },
    themeConfig: {
        nav: [
            {text: 'Home', link: '/'},
            {text: 'Features', link: '/concepts/key-features'},
            {text: 'Get Started', link: '/get-started'},
            {text: 'Dev Info', link: '/developer-information'},
            {
                text: 'Concepts', items: [
                    {text: 'Community Edition', link: '/concepts/community-edition-overview'},
                    {text: 'Key Features', link: '/concepts/key-features'},
                    {text: 'MVP Technical Overview', link: '/concepts/mvp-technical-overview'},
                    {text: 'Pipeline Architecture', link: '/concepts/pipeline-architecture'},
                ]
            },
            {
                text: "Guides", items: [
                    {text: 'Hardware Requirements', link: '/guide/hardware-requirements'},
                    {text: 'Installation', link: '/guide/installation-guide'},
                    {text: 'Quickstart', link: '/guide/quickstart-guide'},
                    {text: 'Running Application', link: '/guide/running-classifier'},
                    {text: 'Training Own Model', link: '/guide/training-models'},
                ]
            },
            {
                text: 'Blog', items: [
                    {
                        text: "AI in Open Source Ticketsystems",
                        link: "/blog/ai-in-open-source-ticketsystems"
                    },
                    {
                        text: "AI Trend in Ticketsystems",
                        link: "/blog/ai-in-ticketsystems"
                    }
                ]
            },
            {text: 'API', link: '/reference/api'},
        ],

        footer: {
            message: "<b>ATC</b> - AI Ticket Classification",
            copyright: "by <a href='https://www.softoft.de' target='_blank'>Softoft</a>",
        }
    }
})
