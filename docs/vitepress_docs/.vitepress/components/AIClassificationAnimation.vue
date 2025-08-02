<template>
    <ClientOnly>
        <svg ref="svgEl" :height="H" :viewBox="`0 0 ${W} ${H}`" :width="W">
            <!-- queues & AI -->
            <g v-for="n in nodes" :key="n.id">
                <rect :id="n.id==='ai' ? 'ai-box' : null"
                      :fill="n.fill" :fill-opacity="n.alpha"
                      :height="nodeH" :stroke="stroke"
                      :width="nodeW" :x="n.x-nodeW/2"
                      :y="n.y-nodeH/2"
                      rx="6"/>
                <text :fill="text" :x="n.x"
                      :y="n.y+5"
                      font-size="13" style="user-select:none"
                      text-anchor="middle">{{ n.label }}
                </text>
            </g>

            <!-- invisible routes -->
            <path id="inbox-ai" :d="quad(nodesMap.inbox,nodesMap.ai,60)"
                  fill="none" stroke="transparent"/>
            <path v-for="e in outEdges"
                  :id="e.id" :key="e.id" :d="e.d"
                  fill="none" stroke="transparent"/>

            <g id="tickets"/>
        </svg>
    </ClientOnly>
</template>

<script setup>
import {onMounted, reactive, ref, watchEffect} from 'vue'
import * as d3 from 'd3'

/* ── layout ─────────────────────────────────────── */
const W = 1100, H = 450, nodeW = 150, nodeH = 44
const svgEl = ref(null)

/* ── colour palettes ────────────────────────────── */
const light = {
    stroke: '#444',
    text: '#212121',
    alpha: .20,
    palette: {billing: '#ffb703', it: '#36cfc9', hr: '#a259ff', sales: '#ff6b6b', manual: '#9e9e9e'}
}
const dark = {
    stroke: '#9ca3af',
    text: '#e6e6e6',
    alpha: .35,
    palette: {billing: '#ffd366', it: '#6be6e1', hr: '#c599ff', sales: '#ff9292', manual: '#b3b3b3'}
}
const theme = ref(null)     // will hold either light or dark object

/* detect current mode & listen for changes */
function detectTheme() {
    const htmlDark = document.documentElement.classList.contains('dark')
    theme.value = htmlDark ? dark : light
}

detectTheme()
/* OS toggle */
/* Tailwind / custom toggle */
new MutationObserver(detectTheme).observe(document.documentElement, {attributes: true, attributeFilter: ['class']})

const topH = H * 0.1
const midH = H * 0.5
const downH = H * 0.6
const bottomH = H * 0.9
const nodes = reactive([
    {id: 'inbox', label: 'New Ticket', x: W / 2, y: topH},
    {id: 'ai', label: 'Open Ticket AI', x: W / 2, y: midH},
    {id: 'billing', label: 'Billing', x: W * 0.15, y: bottomH},
    {id: 'it', label: 'IT', x: W * 0.38, y: bottomH},
    {id: 'hr', label: 'HR', x: W * 0.62, y: bottomH},
    {id: 'sales', label: 'Sales', x: W * 0.85, y: bottomH},
    {id: 'manual', label: 'Manual', x: W * 0.9, y: downH}
])
const nodesMap = Object.fromEntries(nodes.map(n => [n.id, n]))

function quad(a, b, lift = 80) {
    const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2 - lift
    return `M${a.x},${a.y} Q${mx},${my} ${b.x},${b.y}`
}

const outEdges = ['billing', 'it', 'hr', 'sales', 'manual'].map(to => ({
    id: `ai-${to}`, to, d: quad(nodesMap.ai, nodesMap[to], 120)
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

/* ── animation (unchanged) ──────────────────────── */
function launchTicket(dest) {
    const g = d3.select(svgEl.value).select('#tickets')
    const p1 = d3.select('#inbox-ai').node(), p2 = d3.select(`#ai-${dest}`).node()
    const dot = g.append('circle').attr('r', 7).attr('fill', theme.value.palette[dest]).attr('opacity', 0)
    const along = p => t => {
        const L = p.getTotalLength(), pt = p.getPointAtLength(t * L);
        return `translate(${pt.x},${pt.y})`
    }
    dot.transition().duration(800).ease(d3.easeCubicOut)
        .attr('opacity', 1).attrTween('transform', () => along(p1))
        .on('end', () => {
            d3.select('#ai-box').transition().duration(160)
                .attr('stroke-width', 6).transition().duration(160).attr('stroke-width', 1)
            dot.transition().duration(1200).ease(d3.easeCubicInOut)
                .attrTween('transform', () => along(p2))
                .attr('opacity', 0).remove()
        })
}

/* demo driver */
onMounted(() => {
    const choices = ['billing', 'it', 'hr', 'sales', 'manual']
    setInterval(() => launchTicket(choices[Math.random() * choices.length | 0]), 3000)
})
</script>

<style scoped>
svg {
    font-family: Inter, system-ui, sans-serif
}
</style>
