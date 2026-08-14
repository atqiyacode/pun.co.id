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
      <div class="section-head reveal">
        <span class="index">Sect. 02 — Direction</span>
        <h2>Visi &amp; <span class="hl">Misi</span></h2>
      </div>

      <div class="vm-grid">
        <div class="vm-card reveal">
          <span class="vm-no">01</span>
          <div class="vm-icon" aria-hidden="true" v-html="icon('eye')"></div>
          <span class="eyebrow-lbl">Vision</span>
          <h3>{{ vision.title }}</h3>
          <p>{{ vision.description }}</p>
        </div>
        <div class="vm-card reveal">
          <span class="vm-no">02</span>
          <div class="vm-icon" aria-hidden="true" v-html="icon('target')"></div>
          <span class="eyebrow-lbl">Mission</span>
          <h3>{{ mission.title }}</h3>
          <p>{{ mission.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
