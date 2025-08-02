import AIClassificationAnimation from "../components/AIClassificationAnimation.vue";

var __VUE_PROD_DEVTOOLS__ = false
console.log(__VUE_PROD_DEVTOOLS__)
import {h, nextTick, onMounted, watch} from 'vue'
import type {Theme} from 'vitepress'
import {useData} from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import ProductCards from '../components/ProductCards.vue'
import OTAIPredictionDemo from '../components/OTAIPredictionDemo.vue'
import ServicePackagesComponent from '../components/ServicePackagesComponent.vue'
import SupportPlansComponent from '../components/SupportPlansComponent.vue'
import CodeDocumentation from '../components/CodeDocumentation.vue'
import Button from '../components/core/Button.vue'
import Card from '../components/core/Card.vue'
import Badge from '../components/core/Badge.vue'
import Callout from '../components/core/Callout.vue'
import Tabs from '../components/core/Tabs.vue'
import FeatureGrid from '../components/core/FeatureGrid.vue'
import Accordion from '../components/core/Accordion.vue'
import './styles/index.scss'

import {createI18n, useI18n} from 'vue-i18n'
import deMessages from '../../docs_src/de/messages'
import enMessages from '../../docs_src/en/messages'

const i18n = createI18n({
    legacy: false,
    locale: 'en',
    fallbackLocale: 'en',
    messages: {
        de: deMessages,
        en: enMessages
    },
})

export default {
    extends: DefaultTheme, Layout: () => {
        return h(DefaultTheme.Layout, null, {})
    }, enhanceApp({app, router, siteData}) {
        app.use(i18n)
        app.component('ProductCards', ProductCards)
        app.component('OTAIPredictionDemo', OTAIPredictionDemo)
        app.component('ServicePackagesComponent', ServicePackagesComponent)
        app.component('SupportPlansComponent', SupportPlansComponent)
        app.component('CodeDocumentation', CodeDocumentation)
        app.component('AppButton', Button)
        app.component('AppCard', Card)
        app.component('AppBadge', Badge)
        app.component('AppCallout', Callout)
        app.component('AppTabs', Tabs)
        app.component('FeatureGrid', FeatureGrid)
        app.component('Accordion', Accordion)
        app.component('AIClassificationAnimation', AIClassificationAnimation)
    },
    setup() {
        const {isDark} = useData()

        const updateHtmlTheme = () => {
            if (isDark.value) {
                document.documentElement.setAttribute('data-bs-theme', 'dark')
            } else {
                document.documentElement.removeAttribute('data-bs-theme')
            }
        }
        const {lang} = useData()
        const {locale} = useI18n()

        watch(lang, (newLang) => {
            locale.value = newLang
        }, {immediate: true})


        onMounted(() => {
            updateHtmlTheme()
        })

        watch(isDark, () => {
            nextTick(() => {
                updateHtmlTheme()
            })
        })
    }

} satisfies Theme
