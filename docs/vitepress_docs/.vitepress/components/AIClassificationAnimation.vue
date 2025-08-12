<!-- TicketRouterTopDown.vue -->
<template>
    <ClientOnly>
        <div class="my-8">
            <h3 class="text-2xl font-bold mb-5 border-none p-0">
                {{ t('otai_animation.title') }}
            </h3>
            <div class="border p-4 md:p-5 rounded-lg border-gray-700">
                <svg ref="svgEl" :viewBox="`0 0 ${size.w} ${size.h}`" class="router-svg">
                    <g v-for="node in nodes" :key="node.id">
                        <rect
                            :id="node.id==='inbox' ? 'inbox-box'
                                : node.id==='ai'    ? 'ai-box'
                                : null"
                            :fill="node.fill.value"
                            :fill-opacity="node.alpha.value"
                            :height="nodeH"
                            :stroke="theme.stroke"
                            :width="nodeW"
                            :x="node.x.value - nodeW / 2"
                            :y="node.y.value - nodeH / 2"
                            :class="node.class"
                            @click="node.onClick ? node.onClick() : null"
                            rx="6"
                        />
                        <text
                            :fill="theme.text"
                            :font-size="Math.round(Math.min(26, Math.max(12, nodeH * 0.25)))"
                            :x="node.x.value"
                            :y="node.y.value + 5"
                            style="user-select:none"
                            text-anchor="middle"
                        >
                            {{ node.label.value }}
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
import {computed, ComputedRef, ref, useTemplateRef, watch, Ref} from 'vue'
import * as d3 from 'd3'
import {useI18n} from 'vue-i18n'
import {breakpointsBootstrapV5, useBreakpoints, useElementVisibility, useWindowSize} from '@vueuse/core'

const target = useTemplateRef<HTMLDivElement>('el')
const targetIsVisible = useElementVisibility(target)
const {width: windowWidth, height: windowHeight} = useWindowSize()

const breakpoints = useBreakpoints(breakpointsBootstrapV5)

const {t} = useI18n()
const busy = ref(false)
/* ── canvas & layout ────────────────────────────── */
const smallNodeWidthFactor = 0.8; // for small screens
const largeNodeWidthFactor = 0.7; // for medium screens
const extraLargeNodeWidthFactor = 0.6; // for large screens

const standardSize = {
    w: 1200,
    h: 400
}
const numberQueues = computed(() => {
    if (breakpoints.smaller('sm').value) {
        return 2
    } else if (breakpoints.smaller('lg').value) {
        return 3
    }
    return 4
})


const size = computed(() => {
    return {
        w: Math.min(Math.max(windowWidth.value * 0.8, 0), standardSize.w * 2),
        h: Math.min(Math.max(windowWidth.value * 0.4, standardSize.h), standardSize.h * 2)
    }
})

const nodeW = computed(() => {
    const queueWidthFullWidth = size.value.w / numberQueues.value
    if (breakpoints.smaller('sm').value) {
        return queueWidthFullWidth * smallNodeWidthFactor
    } else if (breakpoints.smaller('md').value) {
        return queueWidthFullWidth * largeNodeWidthFactor
    }
    return queueWidthFullWidth * extraLargeNodeWidthFactor
})

const nodeH = computed(() => {
    return nodeW.value * 0.4
})
const svgEl = ref(null)
type Position = {
    x: Ref<number>,
    y: Ref<number>
}

/* mail starts just above the canvas */
const mailPos: Ref<Position> = computed(() => {
    return {
        x: ref(size.value.w * 0.5),
        y: ref(-size.value.h * 0.1)
    }
})
type Node = {
    id: string,
    label: Ref<string>,
    fill: Ref<string>,
    alpha?: Ref<number>,
    class?: string
    labelClass?: string,
    onClick?: () => void
} & Position

type Queue = {
    id: string,
    label: string,
    fill: string
}
const allQueues: Queue[] = [
    {id: 'billing', label: 'Billing', fill: '#ffd366'},
    {id: 'it', label: 'IT', fill: '#6be6e1'},
    {id: 'hr', label: 'HR', fill: '#c599ff'},
    {id: 'sales', label: 'Sales', fill: '#ff9292'}
]
const queues = computed(() => {
    return allQueues.slice(0, numberQueues.value)
})
/* ── colour themes ──────────────────────────────── */
const theme = {
    stroke: '#9ca3af',
    text: '#e6e6e6',
    defaultNodeAlpha: 0.35,
}

/* ── node positions (top-down) ───────────────────── */
const coreNodes: ComputedRef<Node[]> = computed(() => [
        {
        id: 'button',
        label: computed(() => busy.value ? t('otai_animation.processingText') : t('otai_animation.startAnimationText')),
        x: ref(0.5 * size.value.w),
        y: ref(size.value.h * 0.1),
        fill: ref('#535bf2'),
        alpha: ref(theme.defaultNodeAlpha),
        class: 'fill-blue-600 cursor-pointer hover:opacity-80',
        labelClass: 'cursor-pointer text-white',
        onClick: handleClick
    },
    {
        id: 'ai',
        label: ref('Open Ticket AI'),
        x: ref(0.5 * size.value.w),
        y: ref(size.value.h * 0.30),
        fill: ref('#535bf2'),
        alpha: ref(theme.defaultNodeAlpha),
        class: '',
        labelClass: '',
        onClick: null
    }
])

/* 2) alle Nodes als computed  – reagiert automatisch auf breakpoints */
const nodes = computed(() => {
    const between = 1 / (queues.value.length - 1 || 1)
    const maxWidth = size.value.w - nodeW.value
    const queueNodes = queues.value.map((q, i) => ({
        id: q.id,
        label: ref(q.label),
        fill: ref(q.fill),
        alpha: ref(theme.defaultNodeAlpha),
        x: ref(maxWidth * i * between + (nodeW.value * 0.5)),
        y: ref(size.value.h - nodeH.value * 0.5 - 20),
        class: 'hover:opacity-80 queue-node',
        labelClass: '',
        onClick: null
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
function quad(a: Position, b: Position, lift = -60) {
    if (!a || !b) {
        console.warn('Invalid nodes for quad:', a, b)
        return ''
    }
    const mx = (a.x.value + b.x.value) / 2,
        my = (a.y.value + b.y.value) / 2 + lift
    return `M${a.x.value},${a.y.value} Q${mx},${my} ${b.x.value},${b.y.value}`
}


function alongPath(path, scale = 1) {
    console.log('alongPath', path, scale)
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
        .attr('transform', `translate(${mailPos.value.x},${mailPos.value.y}) scale(1.2)`)

    /* envelope body */
    envelope.append('rect')
        .attr('x', -14).attr('y', -10)
        .attr('width', 28).attr('height', 20)
        .attr('rx', 3)
        .attr('fill', theme.text)
        .attr('stroke', theme.text)
        .attr('stroke-width', 2)

    /* envelope flap line */
    envelope.append('polyline')
        .attr('points', '-14,-10 0,2 14,-10')
        .attr('fill', 'none')
        .attr('stroke', theme.stroke)
        .attr('stroke-width', 2)
    return envelope
}

/* ── envelope + ticket animation ────────────────── */
function launchEmail(dest: Node) {
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

function launchTicket(dest: Node) {
    const g = d3.select(svgEl.value).select('#tickets')
    const aiToQueue = d3.select(`#ai-${dest.id}`).node()
    const dot = g.append('circle')
        .attr('r', 7)
        .attr('fill', '#9ca3af')


    d3.select('#ai-box')
        .transition().duration(160).attr('stroke-width', 6)
        .transition().duration(160).attr('stroke-width', 1)
    dot.attr('fill', dest.fill.value)
    dot.transition()
        .duration(1200)
        .ease(d3.easeCubicInOut)
        .attrTween('transform', () => alongPath(aiToQueue))
        .on('end', () => {
            busy.value = false
        })
        .remove()


}

function getRandomQueueNode(){
    const queueNodes = nodes.value.filter(n => n.class.includes('queue-node'))
    return queueNodes[Math.random() * queueNodes.length | 0]
}

function handleClick() {
    launchEmail(getRandomQueueNode())
}


watch(targetIsVisible, (isVisible) => {
    if (isVisible) {
        launchEmail(getRandomQueueNode())
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

