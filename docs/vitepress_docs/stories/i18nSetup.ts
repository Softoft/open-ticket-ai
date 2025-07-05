import { createI18n } from 'vue-i18n'
import en from '../docs_src/en/messages.ts'
import de from '../docs_src/de/messages.ts'

export const i18n = createI18n({
  legacy: false,
  locale: 'en',
  fallbackLocale: 'en',
  messages: {
    en,
    de,
  },
})
