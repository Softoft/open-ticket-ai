import {generateNavbar} from './navbarUtil.js'
import {defineConfig} from "vitepress";
var __VUE_PROD_DEVTOOLS__ = false
console.log(__VUE_PROD_DEVTOOLS__)
export default defineConfig({
    srcDir: `docs-src`,
    title: 'AI Ticket Classification',
    srcDir: './docs_src',
    head: [
        [
            'link',
            {
                rel: 'icon',
                href: 'https://softoft.sirv.com/Images/atc-logo-2024-blue.png?w=300&q=100&lightness=100&colorlevel.white=100'
            }
        ],
        [
            'link',
            {
                rel: 'stylesheet',
                href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css',
                integrity: 'sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==',
                crossorigin: 'anonymous'
            }
        ],
    ],
    description: '',
    sitemap: {
        hostname: 'https://ai-ticket-classification.softoft.de'
    },
    locales: {
        root: {
            label: 'English',
            lang: 'en',
            link: '/en/',
            themeConfig: {
                nav: [
                    ...generateNavbar('en'),
                ]
            }
        },
        de: {
            label: 'Deutsch',
            lang: 'de',
            link: '/de/',
            themeConfig: {
                nav: [
                    ...generateNavbar('de'),
                ]
            }
        }
    },
    themeConfig: {
        footer: {
            message: '<b>OTAI</b> - Open Ticket AI',
            copyright: "by <a href='https://www.softoft.de' target='_blank'>Softoft, Tobias Bück Einzelunternehmen</a>"
        }
    },
    vite: {
        define: {
            __VUE_PROD_DEVTOOLS__: false,
        },
    }
})
