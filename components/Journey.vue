<script setup>
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { journey } = company
useReveal()
</script>

<template>
  <section id="journey">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Our Journey</span>
        <h2>Perjalanan Kami</h2>
        <p>Kisah perusahaan kami dari tahun ke tahun — setiap langkah adalah komitmen menuju layanan prima.</p>
      </div>
      <div class="timeline">
        <div v-for="j in journey" :key="j.year" class="tl-item">
          <span class="tl-dot" aria-hidden="true"></span>
          <div class="tl-year">{{ j.year }}</div>
          <h3>{{ j.title }}</h3>
          <p>{{ j.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
