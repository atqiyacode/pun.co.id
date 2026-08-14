<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { vision, mission } = company
useReveal()
</script>

<template>
  <section id="vision">
    <div class="container">
      <div class="vm-grid">
        <div class="vm-card">
          <div class="vm-icon" aria-hidden="true" v-html="icon('eye')"></div>
          <span class="eyebrow">{{ vision.eyebrow }}</span>
          <h3>{{ vision.title }}</h3>
          <p>{{ vision.description }}</p>
        </div>
        <div class="vm-card">
          <div class="vm-icon" aria-hidden="true" v-html="icon('target')"></div>
          <span class="eyebrow">{{ mission.eyebrow }}</span>
          <h3>{{ mission.title }}</h3>
          <p>{{ mission.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
