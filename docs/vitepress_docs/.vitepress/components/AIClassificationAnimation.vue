<!-- TicketRouterTopDown.vue -->
<template>
    <ClientOnly>
        <div class="my-8">
            <div class="text-center mb-3">
                <button
                    :disabled="busy"
                    class="inline-flex items-center justify-center
             rounded-md bg-blue-600 px-8 py-3 font-semibold text-white
             transition-colors hover:bg-blue-700
             disabled:cursor-not-allowed disabled:opacity-40"
                    @click="handleClick">
                    <span v-if="busy">Processing</span>
                    <span v-else>Send Email</span>
                </button>
            </div>
            <svg ref="svgEl" :viewBox="`0 0 ${size.w} ${size.h}`" class="router-svg">
                <!-- ① Queue & AI boxes -->
                <g v-for="node in nodes" :key="node.id">
                    <rect
                        :id="node.id==='inbox' ? 'inbox-box'
               : node.id==='ai'    ? 'ai-box'
               : null"
                        :fill="node.fill"
                        :fill-opacity="node.alpha"
                        :height="nodeH"
                        :stroke="stroke"
                        :width="nodeW"
                        :x="node.x - nodeW / 2"
                        :y="node.y - nodeH / 2"
                        rx="6"
                    />
                    <text
                        :fill="text"
                        :x="node.x"
                        :y="node.y + 5"
                        font-size="13"
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
    </ClientOnly>
</template>

<script setup>
import {computed, onMounted, ref, watch, watchEffect} from 'vue'
import * as d3 from 'd3'
import {useWindowSize} from '../composables/useWindowSize'

const {windowHeight, windowWidth} = useWindowSize()
console.log(windowWidth, windowHeight)
const size = ref({w: 1000, h: 300})
const busy = ref(false)
/* ── canvas & layout ────────────────────────────── */
const defaultNodeWidth = 150;
const defaultNodeHeight = 44;

const widthBreakpoint = 1000

const nodeW = computed(() => {
    return defaultNodeWidth * (windowWidth.value < widthBreakpoint ? 1.5 : 1)
})
const nodeH = computed(() => {
    return defaultNodeHeight * (windowWidth.value < widthBreakpoint ? 1.5 : 1)
})
const svgEl = ref(null)

/* mail starts just above the canvas */
const mailPos = {x: size.value.w * 0.5, y: -size.value.h * 0.1}

const allQueues = [
    {id: 'billing', label: 'Billing', color: {light: '#ffb703', dark: '#ffd366'}},
    {id: 'it', label: 'IT', color: {light: '#36cfc9', dark: '#6be6e1'}},
    {id: 'hr', label: 'HR', color: {light: '#a259ff', dark: '#c599ff'}},
    {id: 'sales', label: 'Sales', color: {light: '#ff6b6b', dark: '#ff9292'}}
]
const queues = computed(() => {
    return windowWidth.value < widthBreakpoint ? allQueues.slice(0, 2) : allQueues
})
/* ── colour themes ──────────────────────────────── */
const light = {
    stroke: '#444',
    text: '#212121',
    alpha: 0.20,
    palette: {}
}
const dark = {
    stroke: '#9ca3af',
    text: '#e6e6e6',
    alpha: 0.35,
    palette: {}
}
allQueues.forEach(q => {
    light.palette[q.id] = q.color.light
    dark.palette[q.id] = q.color.dark
})
const theme = ref(light)

function detectTheme() {
    theme.value = document.documentElement.classList.contains('dark') ? dark : light
}


new MutationObserver(detectTheme)
    .observe(document.documentElement, {attributes: true, attributeFilter: ['class']})

/* ── node positions (top-down) ───────────────────── */
const topH = size.value.h * 0.30,
    bottomH = size.value.h * 0.90
const coreNodes = [
    {
        id: 'ai', label: 'Open Ticket AI',
        x: 0.5 * size.value.w, y: size.value.h * 0.30
    }
]

/* 2) alle Nodes als computed  – reagiert automatisch auf breakpoints */
const nodes = computed(() => {
    const between = 1 / (queues.value.length - 1 || 1)
    const queueNodes = queues.value.map((q, i) => ({
        id: q.id,
        label: q.label,
        x: size.value.w * (i * between),
        y: size.value.h * 0.90
    }))
    return [...coreNodes, ...queueNodes]
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
watch(queues, () => {
    queues.value.forEach((queue, index) => {
        const between = 1 / (queues.value.length - 1)

        const x = size.value.w * (index * between)
        nodes.push({
            id: queue.id,
            label: queue.label,
            x: x,
            y: bottomH,
        })
    });
})


/* Bézier helper */
function quad(a, b, lift = -60) {
    const mx = (a.x + b.x) / 2,
        my = (a.y + b.y) / 2 + lift
    return `M${a.x},${a.y} Q${mx},${my} ${b.x},${b.y}`
}


/* ── reactive colours ───────────────────────────── */
let stroke = '', text = ''
watchEffect(() => {
    stroke = theme.value.stroke
    text = theme.value.text
    nodes.value.forEach(n => {
        n.fill = theme.value.palette[n.id]
        n.alpha = theme.value.alpha
    })
})

/**
 * Returns an attrTween-compatible interpolator for a path.
 * @param {SVGPathElement} path   the rail to follow
 * @param {number} scale          optional uniform scale
 */
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
        .remove()
}

function handleClick() {
    if (busy.value) return
    busy.value = true
    launchEmail(queues[Math.random() * queues.length | 0].id)

    setTimeout(() => (busy.value = false), 1800)
}

onMounted(() => {
    detectTheme()
})
</script>

<style scoped>
svg.router-svg {
    width: 100%;
    height: auto;
    display: block;
}
</style>

