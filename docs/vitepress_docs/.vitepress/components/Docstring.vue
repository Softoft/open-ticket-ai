<template>
  <div v-if="doc" class="docstring-container mt-3">
    <p v-if="doc.short_description" class="lead">{{ doc.short_description }}</p>
    <div v-if="doc.long_description" v-html="doc.long_description" class="long-description"></div>

    <!-- Parameters Section -->
    <div v-if="doc.params && doc.params.length > 0" class="mt-4">
      <h6 class="text-muted">Parameters</h6>
      <ul class="list-group list-group-flush">
        <li v-for="param in doc.params" :key="param.name" class="list-group-item px-0">
          <code>{{ param.name }}</code>
          <span v-if="param.type" class="text-info ms-2">({{ param.type }})</span>
          <span v-if="param.is_optional" class="text-muted ms-2">(optional)</span>
          <p v-if="param.description" class="mb-0 ms-2" v-html="param.description"></p>
          <small v-if="param.default" class="text-muted d-block ms-2">
            Default: <code>{{ param.default }}</code>
          </small>
        </li>
      </ul>
    </div>

    <!-- Returns Section -->
    <div v-if="doc.returns" class="mt-4">
      <h6 class="text-muted">Returns</h6>
      <p>
        <span v-if="doc.returns.type" class="text-info">({{ doc.returns.type }})</span>
        <span v-if="doc.returns.description" class="ms-2" v-html="doc.returns.description"></span>
      </p>
    </div>

    <!-- Raises Section -->
    <div v-if="doc.raises && doc.raises.length > 0" class="mt-4">
      <h6 class="text-muted">Raises</h6>
      <ul class="list-group list-group-flush">
        <li v-for="err in doc.raises" :key="err.name" class="list-group-item px-0">
          <code class="text-danger">{{ err.type }}</code>
          <p v-if="err.description" class="mb-0 ms-2" v-html="err.description"></p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
// Import the specific type for a docstring
import type { DocstringData } from '../composables/useApiDocs';

interface Props {
  doc?: DocstringData;
}

defineProps<Props>();
</script>

<style scoped>
.docstring-container {
  font-size: 0.95rem;
}
.list-group-item {
  background-color: transparent;
  border: none;
}
.long-description {
  color: #454d54;
}
</style>
