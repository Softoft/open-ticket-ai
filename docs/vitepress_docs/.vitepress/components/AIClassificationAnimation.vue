<!-- TicketRouterTopDown.vue -->
<template>
    <ClientOnly>
        <div class="my-8">
            <h3 class="text-2xl font-bold mb-5 border-none p-0">
                {{ t('otai_animation.title') }}
            </h3>
            <div class="border p-4 md:p-5 rounded-lg border-gray-700">
                <div class="text-center mb-3">
                    <button

                        :disabled="busy"
                        class="inline-flex items-center justify-center
             rounded-md bg-blue-600 px-8 py-3 font-semibold text-white
             transition-colors hover:bg-blue-700
             disabled:cursor-not-allowed disabled:opacity-40"
                        @click="handleClick">
                        <span v-if="busy">{{ t('otai_animation.processingText') }}</span>
                        <span v-else>{{ t('otai_animation.startAnimationText') }}</span>
                    </button>
                </div>
                <svg ref="svgEl" :viewBox="`0 0 ${size.w} ${size.h}`" class="router-svg">
                    <g v-for="node in nodes" :key="node.id">
                        <rect
                            :id="node.id==='inbox' ? 'inbox-box'
                                : node.id==='ai'    ? 'ai-box'
                                : null"
                            :fill="node.fill"
                            :fill-opacity="node.alpha"
                            :height="nodeH"
                            :stroke="strokeColor"
                            :width="nodeW"
                            :x="node.x - nodeW / 2"
                            :y="node.y - nodeH / 2"
                            rx="6"
                        />
                        <text
                            :fill="textColor"
                            :font-size="Math.round(nodeH * 0.25)"
                            :x="node.x"
                            :y="node.y + 5"
                            style="user-select:none"
                            text-anchor="middle"
                        >
                            {{ node.label }}
                        </text>
                    </g>

                    <path
                        id="inbox-ai"
                        :d="quad(mailPos, nodesMap.ai, -40)"
                        fill="none"
                        stroke="transparent"
                    />
                    <path
                        v-for="e in outEdges"
                        :id="e.id"
                        :key="e.id"
                        :d="e.d"
                        fill="none"
                        stroke="transparent"
                    />

                    <!-- ③ Dynamic layers -->
                    <g id="envelopes"/> <!-- flying mail icon -->
                    <g id="tickets"/> <!-- coloured ticket dots -->
                </svg>
            </div>
        </div>
    </ClientOnly>
    <div ref="el" class="w-100 h-2"></div>
</template>

<script lang="ts" setup>
import {computed, ref, useTemplateRef, watch, watchEffect} from 'vue'
import * as d3 from 'd3'
import {useWindowSize} from '../composables/useWindowSize'
import {useI18n} from 'vue-i18n'
import {useElementVisibility} from '@vueuse/core'

const target = useTemplateRef<HTMLDivElement>('el')
const targetIsVisible = useElementVisibility(target)

const {windowHeight, windowWidth} = useWindowSize()
const {t} = useI18n()
const busy = ref(false)
/* ── canvas & layout ────────────────────────────── */
const defaultNodeHeight = 40;
const widthBreakpointMd = 1000;
const widthBreakpointSm = 700;


const numberQueues = computed(() => {
    if (windowWidth.value < widthBreakpointSm) {
        return 2
    } else if (windowWidth.value < widthBreakpointMd) {
        return 3
    }
    return 4
})


const size = computed(() => {
    return {
        w: Math.min(windowWidth.value * 0.8, widthBreakpointMd),
        h: Math.min(windowHeight.value * 0.4, 600)
    }
})

const nodeW = computed(() => {
    const queueWidthFullWidth = size.value.w / numberQueues.value
    if (windowWidth.value < widthBreakpointSm) {
        return queueWidthFullWidth * 0.8
    } else if (windowWidth.value < widthBreakpointMd) {
        return queueWidthFullWidth * 0.7
    }
    return queueWidthFullWidth * 0.6
})

const nodeH = computed(() => {
    return defaultNodeHeight * (800 / size.value.h)
})
const svgEl = ref(null)


/* mail starts just above the canvas */
const mailPos = computed(() => {
    return {
        x: size.value.w * 0.5,
        y: -size.value.h * 0.1
    }
})

const allQueues = [
    {id: 'billing', label: 'Billing', color: {light: '#ffb703', dark: '#ffd366'}},
    {id: 'it', label: 'IT', color: {light: '#36cfc9', dark: '#6be6e1'}},
    {id: 'hr', label: 'HR', color: {light: '#a259ff', dark: '#c599ff'}},
    {id: 'sales', label: 'Sales', color: {light: '#ff6b6b', dark: '#ff9292'}}
]
const queues = computed(() => {
    return windowWidth.value < widthBreakpointMd ? allQueues.slice(0, numberQueues.value) : allQueues
})
/* ── colour themes ──────────────────────────────── */
const dark = {
    stroke: '#9ca3af',
    text: '#e6e6e6',
    alpha: 0.35,
    palette: {}
}
allQueues.forEach(q => {
    dark.palette[q.id] = q.color.dark
})
const theme = ref(dark)

/* ── node positions (top-down) ───────────────────── */
const coreNodes = computed(() => [
    {
        id: 'ai', label: 'Open Ticket AI',
        x: 0.5 * size.value.w, y: size.value.h * 0.30
    }
])

/* 2) alle Nodes als computed  – reagiert automatisch auf breakpoints */
const nodes = computed(() => {
    const between = 1 / (queues.value.length - 1 || 1)
    const maxWidth = size.value.w - nodeW.value
    const queueNodes = queues.value.map((q, i) => ({
        id: q.id,
        label: q.label,
        x: maxWidth * i * between + (nodeW.value * 0.5),
        y: size.value.h * 0.8
    }))
    return [...coreNodes.value, ...queueNodes]
})

/* 3) Map + Edges bauen ebenfalls als computed */
const nodesMap = computed(() =>
    Object.fromEntries(nodes.value.map(n => [n.id, n]))
)

const outEdges = computed(() =>
    queues.value.map(q => ({
        id: `ai-${q.id}`,
        d: quad(nodesMap.value.ai, nodesMap.value[q.id], -80)
    }))
)


/* Bézier helper */
function quad(a, b, lift = -60) {
    const mx = (a.x + b.x) / 2,
        my = (a.y + b.y) / 2 + lift
    return `M${a.x},${a.y} Q${mx},${my} ${b.x},${b.y}`
}


/* ── reactive colours ───────────────────────────── */
let strokeColor = ''
let textColor = ''
watchEffect(() => {
    strokeColor = theme.value.stroke
    textColor = theme.value.text
    nodes.value.forEach(n => {
        n.fill = theme.value.palette[n.id]
        n.alpha = theme.value.alpha
    })
})


function alongPath(path, scale = 1) {
    const L = path.getTotalLength()
    const suffix = scale !== 1 ? ` scale(${scale})` : ''
    return t => {
        const pt = path.getPointAtLength(t * L)
        return `translate(${pt.x},${pt.y})${suffix}`
    }
}


function createEnvelope() {
    const envelopeLayer = d3.select(svgEl.value).select('#envelopes')

    /* g wrapper so rect & flap move together */
    const envelope = envelopeLayer.append('g')
        .attr('transform', `translate(${mailPos.x},${mailPos.y}) scale(1.2)`)

    /* envelope body */
    envelope.append('rect')
        .attr('x', -14).attr('y', -10)
        .attr('width', 28).attr('height', 20)
        .attr('rx', 3)
        .attr('fill', theme.value.text)
        .attr('stroke', theme.value.text)
        .attr('stroke-width', 2)

    /* envelope flap line */
    envelope.append('polyline')
        .attr('points', '-14,-10 0,2 14,-10')
        .attr('fill', 'none')
        .attr('stroke', theme.value.stroke)
        .attr('stroke-width', 2)
    return envelope
}

/* ── envelope + ticket animation ────────────────── */
function launchEmail(dest) {
    if (busy.value) return
    busy.value = true
    const envelope = createEnvelope()
    const mailInPath = d3.select('#inbox-ai').node()

    envelope.transition()
        .duration(1000)
        .ease(d3.easeCubicOut)
        .attrTween('transform', () => alongPath(mailInPath, 1.2))
        .on('end', () => {
            d3.select('#ai-box')
                .transition().duration(160).attr('stroke-width', 6)
                .transition().duration(160).attr('stroke-width', 1)
            envelope.remove()
            launchTicket(dest)
        })
}

function launchTicket(dest) {
    const g = d3.select(svgEl.value).select('#tickets')
    const aiToQueue = d3.select(`#ai-${dest}`).node()
    const dot = g.append('circle')
        .attr('r', 7)
        .attr('fill', '#9ca3af')


    d3.select('#ai-box')
        .transition().duration(160).attr('stroke-width', 6)
        .transition().duration(160).attr('stroke-width', 1)
    dot.attr('fill', theme.value.palette[dest])
    dot.transition()
        .duration(1200)
        .ease(d3.easeCubicInOut)
        .attrTween('transform', () => alongPath(aiToQueue))
        .on('end', () => {
            busy.value = false
        })
        .remove()


}

function handleClick() {
    launchEmail(queues.value[Math.random() * queues.value.length | 0].id)
}


watch(targetIsVisible, (isVisible) => {
    if (isVisible) {
        launchEmail(queues.value[Math.random() * queues.value.length | 0].id)
    }
})
</script>

<style scoped>
svg.router-svg {
    width: 100%;
    height: auto;
    display: block;
}
</style>

