import {defineConfig} from "vitepress";
import {NavGenerator, NavGeneratorOptions} from "./util/navgen.ts";
import {withMermaid} from "vitepress-plugin-mermaid";

var __VUE_PROD_DEVTOOLS__ = false
console.log(__VUE_PROD_DEVTOOLS__)

const navGeneratorOptions: NavGeneratorOptions = {
    rootPath: './docs_src',
    allowedExtensions: ['.md'],
    excludePatterns: [/^_/, /\/_/, /\/\./],
    hideHiddenEntries: true,
    includeIndexAsFolderLink: false,
    includeEmptyDirectories: false,
    stripExtensionsInLinks: true,
    sidebarCollapsible: true,
    sidebarCollapsed: true,
    sortComparator: (a: string, b: string) => a.localeCompare(b, undefined, {numeric: true, sensitivity: 'base'})
}

const navGenerator = new NavGenerator(navGeneratorOptions);
export default withMermaid(defineConfig({

    title: 'AI Ticket Classification',
    srcDir: './docs_src',
    appearance: 'force-dark',
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
    lastUpdated: true,
    cleanUrls: true,
    sitemap: {
        hostname: 'https://open-ticket-ai.com',
    },
    mermaid: {
        securityLevel: 'loose', // needed for `click` links to work
    },
    locales: {
        root: {
            label: 'English',
            lang: 'en',
            link: '/en/',
            themeConfig: {
                nav: [
                    ...navGenerator.generateNavbar('en'),
                ],
                sidebar: navGenerator.generateSidebar("en")
            }
        },
        de: {
            label: 'Deutsch',
            lang: 'de',
            link: '/de/',
            themeConfig: {
                nav: [
                    ...navGenerator.generateNavbar('de'),
                ],
                sidebar: navGenerator.generateSidebar("de")
            }
        },
        fr: {
            label: 'French',
            lang: 'fr',
            link: '/fr/',
            themeConfig: {
                nav: [
                    ...navGenerator.generateNavbar('fr'),
                ],
                sidebar: navGenerator.generateSidebar("fr")
            }
        },
        es: {
            label: 'Spanish',
            lang: 'es',
            link: '/es/',
            themeConfig: {
                nav: [
                    ...navGenerator.generateNavbar('es'),
                ],
                sidebar: navGenerator.generateSidebar("es")
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
            __VUE_PROD_DEVTOOLS__: 'false',
        },
        ssr: {
            noExternal: [
                'vue-i18n',
                '@intlify/message-compiler',
                '@intlify/shared'
            ]
        },
    }
}))
