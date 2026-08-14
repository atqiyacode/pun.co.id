<script setup>
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { journey } = company
useReveal()
</script>

<template>
  <section id="journey">
    <div class="bp-grid" aria-hidden="true"></div>
    <div class="container">
      <div class="section-head reveal">
        <span class="index">Sect. 03 — Timeline</span>
        <h2>Our <span class="hl">Journey</span></h2>
        <p>Kisah perusahaan kami dari tahun ke tahun — setiap langkah adalah komitmen menuju layanan prima.</p>
      </div>

      <div class="timeline">
        <div v-for="(j, i) in journey" :key="j.year" class="tl-item reveal">
          <span class="tl-dot" aria-hidden="true">{{ i + 1 }}</span>
          <div class="tl-year"><em>{{ j.year }}</em></div>
          <h3>{{ j.title }}</h3>
          <p>{{ j.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
