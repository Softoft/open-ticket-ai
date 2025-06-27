import {h, onMounted} from 'vue'
import type {Theme} from 'vitepress'
// .vitepress/theme/index.ts
import DefaultTheme from 'vitepress/theme'
import './style.scss'
import ProductCards from '../components/ProductCards.vue'
import OTAIPredictionDemo from '../components/OTAIPredictionDemo.vue'


export default {
    extends: DefaultTheme, Layout: () => {
        return h(DefaultTheme.Layout, null, {})
    }, enhanceApp({app, router, siteData}) {
        app.component('ProductCards', ProductCards)
        app.component('OTAIPredictionDemo', OTAIPredictionDemo)
    }

} satisfies Theme
