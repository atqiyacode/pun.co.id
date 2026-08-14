<script setup>
import { useReveal } from '~/composables/useReveal'
import { useLocaleItems } from '~/composables/useLocaleItems'

useReveal()
const items = useLocaleItems('journey.items', 4, ['year', 'title', 'description'])
</script>

<template>
  <section id="journey">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">{{ $t('journey.eyebrow') }}</span>
        <h2>{{ $t('journey.title') }}</h2>
        <p>{{ $t('journey.subtitle') }}</p>
      </div>
      <div class="timeline">
        <div v-for="j in items" :key="j.year" class="tl-item">
          <span class="tl-dot" aria-hidden="true"></span>
          <div class="tl-year">{{ j.year }}</div>
          <h3>{{ j.title }}</h3>
          <p>{{ j.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
