// composables/useWindowSize.ts
import {onMounted, onUnmounted, ref} from 'vue'

export function useWindowSize() {
    const windowWidth = ref<number>(0)
    const windowHeight = ref<number>(0)
    const onResize = () => {
        windowWidth.value = window.innerWidth
        windowHeight.value = window.innerHeight

    }
    onMounted(() => {
            onResize()
            window.addEventListener('resize', onResize)
        }
    )
    onUnmounted(() => window.removeEventListener('resize', onResize))
    return {windowWidth, windowHeight}
}
