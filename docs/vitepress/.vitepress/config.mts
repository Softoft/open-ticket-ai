import {defineConfig} from 'vitepress'
import {generateNavbar} from './navbarUtil.js'

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
            ...generateNavbar('src')
        ],

        footer: {
            message: "<b>ATC</b> - AI Ticket Classification",
            copyright: "by <a href='https://www.softoft.de' target='_blank'>Softoft</a>",
        }
    }
})
