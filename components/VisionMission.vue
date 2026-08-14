<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

useReveal()
</script>

<template>
  <section id="vision">
    <div class="container">
      <div class="vm-grid">
        <div class="vm-card">
          <div class="vm-icon" aria-hidden="true" v-html="icon('eye')"></div>
          <span class="eyebrow">{{ $t('vision.eyebrow') }}</span>
          <h3>{{ $t('vision.title') }}</h3>
          <p>{{ $t('vision.description') }}</p>
        </div>
        <div class="vm-card">
          <div class="vm-icon" aria-hidden="true" v-html="icon('target')"></div>
          <span class="eyebrow">{{ $t('mission.eyebrow') }}</span>
          <h3>{{ $t('mission.title') }}</h3>
          <p>{{ $t('mission.description') }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
