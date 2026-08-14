<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { about, company: c } = company
useReveal()
</script>

<template>
  <section id="about">
    <div class="bp-grid" aria-hidden="true"></div>
    <div class="container">
      <div class="section-head reveal">
        <span class="index">Sect. 01 — About</span>
        <h2>Who We <span class="hl">Are</span></h2>
      </div>

      <div class="about-grid">
        <div class="about-text reveal">
          <p v-html="about.heading"></p>
          <p v-for="p in about.paragraphs" :key="p"><strong>{{ p }}</strong></p>

          <div class="about-fields">
            <div v-for="(f, i) in about.fields" :key="f.title" class="field-card reveal">
              <span class="fno">FLD-0{{ i + 1 }}</span>
              <div class="field-icon" aria-hidden="true" v-html="icon(f.icon)"></div>
              <h4>{{ f.title }}</h4>
              <p>{{ f.description }}</p>
            </div>
          </div>
        </div>

        <div class="about-spec reveal">
          <div class="about-spec-head">
            <span>Company <span class="hl">Spec</span></span>
            <span>CP-2026</span>
          </div>
          <div class="about-spec-body">
            <div class="spec-row"><span class="k">Legal Name</span><span class="v">{{ c.legalName }}</span></div>
            <div class="spec-row"><span class="k">Established</span><span class="v">{{ c.foundedYear }}</span></div>
            <div class="spec-row"><span class="k">Sector</span><span class="v">Mining · Forestry · Construction</span></div>
            <div class="spec-row"><span class="k">Coverage</span><span class="v">Seluruh Indonesia</span></div>
            <div class="spec-row"><span class="k">Motto</span><span class="v">Layanan Prima, Kebanggaan Kami</span></div>
            <div class="spec-badge">✔ Siap menerima kontrak penambangan, eksplorasi &amp; konstruksi baru</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
