// composables/useWindowSize.ts
import {onMounted, onUnmounted, ref} from 'vue'

export function useWindowSize() {
    const windowWidth = ref<number>(window.innerWidth)
    const windowHeight = ref<number>(window.innerHeight)
    const onResize = () => {
        windowWidth.value = window.innerWidth
        windowHeight.value = window.innerHeight

    }
    onMounted(() => window.addEventListener('resize', onResize))
    onUnmounted(() => window.removeEventListener('resize', onResize))
    return {windowWidth, windowHeight}
}
