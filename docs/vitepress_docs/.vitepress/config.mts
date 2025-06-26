import {defineConfig} from 'vitepress'
import {generateNavbar} from './navbarUtil.js'

// Map visible version labels to their directory names
export const versionMap = {
    next: 'v1_2_alpha',
    latest: 'v1_1',
    '1.1': 'v1_1',
    '1.0': 'v1_0',
    'v0_2': 'v0_2',
    'v0_1': 'v0_1',
} as const

// Resolve the directory of the currently selected version ("latest" by default)
const defaultVersion = versionMap.latest

// Helper to create the version dropdown based on the selected language
function versionDropdown(lang: 'en'|'de') {
  return {
    text: 'Version',
    items: Object.entries(versionMap).map(
      ([label, dir]) => ({ text: label, link: `/${lang}/${dir}/` })
    )
  }
}

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
        ]
    ],
    description: '',
    sitemap: {
        hostname: 'https://ai-ticket-classification.softoft.de'
    },
    // Change docs dir structure to be /{lang}/{version} instead of /{version}/{lang}
    locales: {
        root: {
            label: 'English',
            lang: 'en',
            link: '/en/',
            themeConfig: {
                nav: [
                    ...generateNavbar(``),
                    versionDropdown('en')
                ]
            }
        },
        de: {
            label: 'Deutsch',
            lang: 'de',
            link: '/de/',
            themeConfig: {
                nav: [
                    ...generateNavbar(``),
                    versionDropdown('de')
                ]
            }
        }
    },
    themeConfig: {
        footer: {
            message: '<b>ATC</b> - AI Ticket Classification',
            copyright: "by <a href='https://www.softoft.de' target='_blank'>Softoft</a>"
        }
    }
})
