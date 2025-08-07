<!-- components/YoutubeVideo.vue -->
<template>
  <div class="relative w-full pb-[56.25%] overflow-hidden rounded-2xl shadow-lg">
    <!-- Vorschaubild als Hintergrund -->
    <button
      v-if="!loaded"
      @click="loaded = true"
      :style="{ backgroundImage: `url(https://i.ytimg.com/vi/${videoId}/maxresdefault.jpg)` }"
      class="absolute inset-0 bg-center bg-cover transform transition-transform duration-500 hover:scale-105"
    >
      <!-- dunkles Overlay -->
      <div class="absolute inset-0 bg-black bg-opacity-40"></div>
      <!-- Play-Icon -->
      <div class="relative z-10 flex items-center justify-center h-full">
        <svg xmlns="http://www.w3.org/2000/svg"
             class="w-16 h-16 text-white opacity-90"
             viewBox="0 0 24 24" fill="currentColor">
          <path d="M8 5v14l11-7z"/>
        </svg>
      </div>
    </button>

    <!-- echtes Video -->
    <iframe
      v-if="loaded"
      class="absolute inset-0 w-full h-full"
      :src="`https://www.youtube-nocookie.com/embed/${videoId}?rel=0&autoplay=1`"
      :title="title"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
      loading="lazy"
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const props = defineProps<{
  videoId: string
  title?: string
}>()
const loaded = ref(false)
</script>
