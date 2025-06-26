<template>
  <div class="container my-4">
    <h2 class="mb-4 text-white">ATC Ticket Demo</h2>

    <!-- Examples dropdown -->
    <div class="mb-3">
      <label class="form-label fw-bold text-white">Beispiel wählen</label>
      <select
          v-model="selected"
          class="form-select mb-2"
          @change="applyExample"
      >
        <option :key=-1 disabled selected value="-1">Wähle ein Beispiel</option>
        <option v-for="(ex, i) in examples" :key="i" :value="i">
          {{ ex.name }}
        </option>
      </select>
    </div>

    <!-- Subject input -->
    <div class="mb-3">
      <label class="form-label fw-bold text-white">Betreff</label>
      <input
          v-model="subject"
          class="form-control"
          placeholder="Betreff eingeben"
          type="text"
      />
    </div>

    <!-- Body textarea -->
    <div class="mb-3">
      <label class="form-label fw-bold text-white">Nachricht</label>
      <textarea
          v-model="body"
          class="form-control"
          placeholder="Nachricht eingeben"
          rows="4"
      ></textarea>
    </div>

    <VPButton
        :disabled="loading"
        :text="loading ? 'Lädt…' : 'Vorhersage starten'"
        class="mb-4"
        theme="brand"
        @click="predict"
    >
    </VPButton>
    <div v-if="errorMessage" class="text-danger mb-3">
      {{ errorMessage }}
    </div>

    <!-- Clean results -->
    <div v-if="queueResult && prioResult" class="container mt-4">
      <h3 class="fw-bold text-white mb-4">Ergebnis</h3>
      <table class="atc-results-table text-white">
        <thead>
        <tr>
          <th scope="col">Typ</th>
          <th scope="col">Prediction</th>
          <th scope="col">Confidence</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <th scope="row">Queue</th>
          <td>{{ queueResult[0].label }}</td>
          <td>
            <VPBadge
                :type="confidenceBadge(queueResult[0].score)"
                :text="formatScore(queueResult[0].score)"
            />
          </td>
        </tr>
        <tr>
          <th scope="row">Priorität</th>
          <td>{{ prioResult[0].label }}</td>
          <td>
            <VPBadge
                :type="confidenceBadge(prioResult[0].score)"
                :text="formatScore(prioResult[0].score)"
            />
          </td>
        </tr>
        </tbody>
      </table>
    </div>

  </div>
</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {VPButton, VPBadge} from 'vitepress/theme'
import {examples} from "./demoExamples";

// helper to POST to your HF endpoints
async function query(endpoint: string, payload: any) {
  const res = await fetch(endpoint, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  })
  if (!res.ok) throw new Error(`Error ${res.status}: ${res.statusText}`)
  return res.json()
}

// your real endpoints here
const QUEUE_EP = 'https://uwlzdugezcmrk5vk.eu-west-1.aws.endpoints.huggingface.cloud'
const PRIORITY_EP = 'https://rxnypflnfgdbgoxr.us-east-1.aws.endpoints.huggingface.cloud'

// form state
const subject = ref('')
const body = ref('')
const loading = ref(false)
const errorMessage = ref<string|null>(null)

// API results
const queueResult = ref<any>(null)
const prioResult = ref<any>(null)
// select logic
const selected = ref(-1)

function applyExample() {
  const ex = examples[selected.value]
  subject.value = ex.subject
  body.value    = ex.body
  queueResult.value = null
  prioResult.value  = null
  errorMessage.value = null
}

// retry+backoff prediction
async function predict() {
  loading.value = true
  errorMessage.value = null
  queueResult.value = null
  prioResult.value  = null

  const text = (subject.value + ' ').repeat(2) + body.value
  const maxAttempts = 4

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      const [q, p] = await Promise.all([
        query(QUEUE_EP,    { inputs: text, parameters: {} }),
        query(PRIORITY_EP, { inputs: text, parameters: {} })
      ])
      queueResult.value = q
      prioResult.value  = p
      break
    } catch (e) {
      console.error(`Attempt ${attempt} failed`, e)
      if (attempt === maxAttempts) {
        errorMessage.value = 'Vorhersage fehlgeschlagen. Bitte später erneut versuchen.'
      } else {
        // exponential backoff: 1s, then 2s
        const delay = 1000 * Math.pow(2, attempt - 1)
        await new Promise(res => setTimeout(res, delay))
      }
    }
  }

  loading.value = false
}

// format score as percent with one decimal
function confidenceBadge(score: number): string {
  const pct = score * 100;
  if (pct > 90) return 'tip';
  if (pct > 80) return 'info';
  if (pct > 50) return 'warning';
  return 'danger';
}

/**
 * Formats a 0–1 score as a percent string with one decimal
 */
function formatScore(score: number): string {
  return (score * 100).toFixed(1) + '%';
}
</script>

<style lang="scss" scoped>
@import "./styles/custom-bootstrap";

.atc-results-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 1rem 0;

  thead {
    background-color: var(--vp-c-default-3);
  }

  th, td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--vp-c-divider);
    vertical-align: middle;
  }

  th {
    color: var(--vp-c-text-2);
    font-weight: 600;
    text-align: left;
  }

  tbody tr:hover {
    background-color: var(--vp-c-bg-soft);
  }

  VPBadge {
    display: inline-block;
    min-width: 3.5rem;
    text-align: center;
  }
}

/* On medium+ screens, constrain the table to 80% width and center it */
@media (min-width: 768px) {
  .atc-results-table {
    max-width: 80%;
    margin-left: auto;
    margin-right: auto;
  }
  .atc-results-table th,
  .atc-results-table td {
    padding: 1rem 1.5rem;
  }
}

/* On very large screens, go up to 90% width */
@media (min-width: 1200px) {
  .atc-results-table {
    max-width: 90%;
  }
}

.form-control {
  background-color: var(--vp-input-bg-color) !important;
  color: var(--vp-c-text-1) !important;
  border: 1px solid var(--vp-input-border-color) !important;
  transition: border-color 0.2s ease-in-out;
}

/* Change border color on focus */
.form-control:focus {
  outline: none !important;
  border-color: var(--vp-c-brand-1) !important; /* your primary accent */
  box-shadow: 0 0 0 0.2rem var(--vp-c-brand-soft) !important;
}

/* dropdown arrow a bit brighter */
.form-select {
  background-color: var(--vp-input-bg-color) !important;
  color: var(--vp-c-text-1) !important;
  border: 1px solid var(--vp-input-border-color) !important;
  transition: border-color 0.2s ease-in-out;
}

.form-select:focus {
  outline: none !important;
  border-color: var(--vp-c-brand-1) !important;
  box-shadow: 0 0 0 0.2rem var(--vp-c-brand-soft) !important;
}

.form-control,
.form-select {
  border-radius: 0.5rem !important;
}
</style>
