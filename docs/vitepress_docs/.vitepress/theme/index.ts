import {h, onMounted} from 'vue'
import type {Theme} from 'vitepress'
// .vitepress/theme/index.ts
import DefaultTheme from 'vitepress/theme'
import './style.scss'
import Redocs from '../components/Redocs.vue'

export default {
    extends: DefaultTheme, Layout: () => {
        return h(DefaultTheme.Layout, null, {})
    }, enhanceApp({app, router, siteData}) {

        app.component('Redocs', Redocs)
    }
} satisfies Theme
