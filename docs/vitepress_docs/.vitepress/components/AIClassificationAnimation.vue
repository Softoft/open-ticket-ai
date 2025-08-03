<!-- TicketRouterTopDown.vue -->
<template>
    <ClientOnly>
        <svg ref="svgEl" :viewBox="`0 0 1000 500`" class="router-svg">
            <!-- ① Queue & AI boxes -->
            <g v-for="n in nodes" :key="n.id">
                <rect
                    :id="n.id==='inbox' ? 'inbox-box'
               : n.id==='ai'    ? 'ai-box'
               : null"
                    :fill="n.fill"
                    :fill-opacity="n.alpha"
                    :height="nodeH"
                    :stroke="stroke"
                    :width="nodeW"
                    :x="n.x - nodeW / 2"
                    :y="n.y - nodeH / 2"
                    rx="6"
                />
                <text
                    :fill="text"
                    :x="n.x"
                    :y="n.y + 5"
                    font-size="13"
                    style="user-select:none"
                    text-anchor="middle"
                >
                    {{ n.label }}
                </text>
            </g>

            <path
                id="mail-in"
                :d="quad(mailPos, nodesMap.inbox, -40)"
                fill="none"
                stroke="transparent"
            />
            <path
                id="inbox-ai"
                :d="quad(nodesMap.inbox, nodesMap.ai, -60)"
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
    </ClientOnly>
</template>

<script setup>
import {onBeforeUnmount, onMounted, reactive, ref, watchEffect} from 'vue'
import * as d3 from 'd3'

const size = ref({w: 1000, h: 500})

/* ── canvas & layout ────────────────────────────── */
const nodeW = 150, nodeH = 44
const svgEl = ref(null)

/* mail starts just above the canvas */
const mailPos = {x: size.value.w * 0.5, y: -size.value.h * 0.1}

/* ── colour themes ──────────────────────────────── */
const light = {
    stroke: '#444',
    text: '#212121',
    alpha: 0.20,
    palette: {
        billing: '#ffb703', it: '#36cfc9', hr: '#a259ff',
        sales: '#ff6b6b', manual: '#9e9e9e'
    }
}
const dark = {
    stroke: '#9ca3af',
    text: '#e6e6e6',
    alpha: 0.35,
    palette: {
        billing: '#ffd366', it: '#6be6e1', hr: '#c599ff',
        sales: '#ff9292', manual: '#b3b3b3'
    }
}
const theme = ref(light)

/* Tailwind / VitePress dark-mode toggle support */
function detectTheme() {
    theme.value = document.documentElement.classList.contains('dark') ? dark : light
}

detectTheme()
new MutationObserver(detectTheme)
    .observe(document.documentElement, {attributes: true, attributeFilter: ['class']})

/* ── node positions (top-down) ───────────────────── */
const topH = size.value.h * 0.10,
    midH = size.value.h * 0.50,
    downH = size.value.h * 0.60,
    bottomH = size.value.h * 0.90

const nodes = reactive([
    {id: 'inbox', label: 'New Ticket', x: size.value.w * 0.5, y: topH},
    {id: 'ai', label: 'Open Ticket AI', x: size.value.w * 0.5, y: midH},
    {id: 'billing', label: 'Billing', x: size.value.w * 0.10, y: bottomH},
    {id: 'it', label: 'IT', x: size.value.w * 0.30, y: bottomH},
    {id: 'hr', label: 'HR', x: size.value.w * 0.50, y: bottomH},
    {id: 'sales', label: 'Sales', x: size.value.w * 0.70, y: bottomH},
    {id: 'manual', label: 'Manual', x: size.value.w * 0.90, y: downH}
])
const nodesMap = Object.fromEntries(nodes.map(n => [n.id, n]))

/* Bézier helper */
function quad(a, b, lift = -60) {
    const mx = (a.x + b.x) / 2,
        my = (a.y + b.y) / 2 + lift
    return `M${a.x},${a.y} Q${mx},${my} ${b.x},${b.y}`
}

/* AI → queue curves */
const outEdges = ['billing', 'it', 'hr', 'sales', 'manual'].map(to => ({
    id: `ai-${to}`,
    to,
    d: quad(nodesMap.ai, nodesMap[to], -80)
}))

/* ── reactive colours ───────────────────────────── */
let stroke = '', text = ''
watchEffect(() => {
    stroke = theme.value.stroke
    text = theme.value.text
    nodes.forEach(n => {
        n.fill = theme.value.palette[n.id] ?? theme.value.palette.manual
        n.alpha = theme.value.alpha
    })
})

/* ── envelope + ticket animation ────────────────── */
function launchEmail(dest) {
    const envLayer = d3.select(svgEl.value).select('#envelopes')

    /* g wrapper so rect & flap move together */
    const env = envLayer.append('g')
        .attr('transform', `translate(${mailPos.x},${mailPos.y}) scale(1.2)`)

    /* envelope body */
    env.append('rect')
        .attr('x', -14).attr('y', -10)
        .attr('width', 28).attr('height', 20)
        .attr('rx', 3)
        .attr('fill', theme.value.text)
        .attr('stroke', theme.value.text)
        .attr('stroke-width', 2)

    /* envelope flap line */
    env.append('polyline')
        .attr('points', '-14,-10 0,2 14,-10')
        .attr('fill', 'none')
        .attr('stroke', theme.value.stroke)
        .attr('stroke-width', 2)

    const pMail = d3.select('#mail-in').node()
    const along = p => t => {
        const len = p.getTotalLength(), pt = p.getPointAtLength(t * len)
        return `translate(${pt.x},${pt.y}) scale(1.2)`
    }

    /* envelope → inbox */
    env.transition()
        .duration(1000)
        .ease(d3.easeCubicOut)
        .attrTween('transform', () => along(pMail))
        .on('end', () => {
            /* flash inbox */
            d3.select('#inbox-box')
                .transition().duration(160).attr('stroke-width', 6)
                .transition().duration(160).attr('stroke-width', 1)
            env.remove()
            launchTicket(dest)
        })
}

function launchTicket(dest) {
    const g = d3.select(svgEl.value).select('#tickets')
    const p1 = d3.select('#inbox-ai').node()
    const p2 = d3.select(`#ai-${dest}`).node()
    const dot = g.append('circle')
        .attr('r', 7)
        .attr('fill', theme.value.palette[dest])
        .attr('opacity', 0)

    const along = p => t => {
        const len = p.getTotalLength(), pt = p.getPointAtLength(t * len)
        return `translate(${pt.x},${pt.y})`
    }

    dot.transition()                       /* inbox → AI */
        .duration(800)
        .ease(d3.easeCubicOut)
        .attr('opacity', 1)
        .attrTween('transform', () => along(p1))
        .on('end', () => {
            /* flash AI box */
            d3.select('#ai-box')
                .transition().duration(160).attr('stroke-width', 6)
                .transition().duration(160).attr('stroke-width', 1)

            dot.transition()                  /* AI → queue */
                .duration(1200)
                .ease(d3.easeCubicInOut)
                .attrTween('transform', () => along(p2))
                .attr('opacity', 0)
                .remove()
        })
}

/* ── demo driver: launch an email every 3 s ─────── */
onMounted(() => {
    const queues = ['billing', 'it', 'hr', 'sales', 'manual']
    setInterval(() => {
        launchEmail(queues[Math.random() * queues.length | 0])
    }, 3000)
})
</script>

<style scoped>
svg.router-svg {
    width: 100%;
    height: auto;
    max-width: 1100px;
    display: block;
}
</style>
