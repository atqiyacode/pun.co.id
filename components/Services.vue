<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { services } = company
useReveal()
</script>

<template>
  <section id="services">
    <div class="container">
      <div class="section-head reveal">
        <span class="index">Sect. 04 — Services</span>
        <h2>Our <span class="hl">Service</span></h2>
        <p>Lakukan sepenuh hati, atau lupakan sama sekali — itulah prinsip kerja kami di setiap penambangan &amp; kontrak.</p>
      </div>

      <div class="services-grid">
        <div v-for="(s, i) in services" :key="s.title" class="service-card reveal">
          <span class="num" aria-hidden="true">0{{ i + 1 }}</span>
          <div class="service-icon" aria-hidden="true" v-html="icon(s.icon)"></div>
          <h3>{{ s.title }}</h3>
          <p>{{ s.description }}</p>
          <span class="tag srv-tag">Layanan Utama</span>
        </div>
      </div>
    </div>
  </section>
</template>
