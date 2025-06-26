import { defineConfig } from 'vitepress'
import { generateNavbar } from './navbarUtil.js'

// Map visible version labels to their directory names
export const versionMap = {
  next: 'v1_2_alpha',
  latest: 'v1_1',
  '1.1': 'v1_1',
  '1.0': 'v1_0'
} as const

// Resolve the directory of the currently selected version ("latest" by default)
const defaultVersion = versionMap.latest

// Helper to create the version dropdown based on the selected language
function createVersionDropdown(lang: string) {
  const items = Object.entries(versionMap).map(([label, dir]) => ({
    text: label,
    link: `/${dir}/${lang}/`
  }))
  return {
    text: 'Version',
    items
  }
}

export default defineConfig({
  srcDir: `docs-src`,
  title: 'AI Ticket Classification',
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
  locales: {
    root: {
      label: 'English',
      lang: 'en',
      themeConfig: {
        nav: [
          ...generateNavbar(`docs-src/en`),
          createVersionDropdown('en')
        ]
      }
    },
    de: {
      label: 'Deutsch',
      lang: 'de',
      link: '/de/',
      themeConfig: {
        nav: [
          ...generateNavbar(`docs-src/de`),
          createVersionDropdown('de')
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
