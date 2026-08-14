<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

useReveal()
</script>

<template>
  <section id="services">
    <div class="glow" style="top:-120px;right:-160px;width:480px;height:480px;background:rgba(212,175,55,0.14)" aria-hidden="true"></div>
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">{{ $t('services.eyebrow') }}</span>
        <h2>{{ $t('services.title') }}</h2>
        <p>{{ $t('services.subtitle') }}</p>
      </div>
      <div class="services-grid">
        <div v-for="(s, i) in $tm('services.items')" :key="s.title" class="service-card">
          <div class="num" aria-hidden="true">0{{ i + 1 }}</div>
          <div class="service-icon" aria-hidden="true" v-html="icon(s.icon)"></div>
          <h3>{{ s.title }}</h3>
          <p>{{ s.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
