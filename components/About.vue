<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { about, company: c } = company
useReveal()
</script>

<template>
  <section id="about">
    <div class="bg-grid" aria-hidden="true"></div>
    <div class="container">
      <div class="about-grid">
        <div class="about-text">
          <span class="eyebrow">{{ about.eyebrow }}</span>
          <h2>{{ about.title }}</h2>
          <p style="margin-top:18px">{{ about.heading }}</p>
          <p v-for="p in about.paragraphs" :key="p">{{ p }}</p>
          <div class="about-fields">
            <div v-for="f in about.fields" :key="f.title" class="field-card">
              <div class="field-icon" aria-hidden="true" v-html="icon(f.icon)"></div>
              <h4>{{ f.title }}</h4>
              <p>{{ f.description }}</p>
            </div>
          </div>
        </div>

        <div class="about-visual">
          <div class="about-card-stack">
            <div class="about-card">
              <div class="big">{{ c.foundedYear }}<small>+</small></div>
              <h4>Perusahaan Swasta Nasional</h4>
              <p>Berdiri sejak 2023, berkomitmen menghadirkan layanan prima di sektor pertambangan, eksplorasi hutan, dan konstruksi.</p>
              <div style="margin-top:20px;display:flex;gap:12px;flex-wrap:wrap">
                <span style="display:inline-flex;align-items:center;gap:8px;background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:8px 16px;font-size:13px;font-weight:700">
                  <span aria-hidden="true" v-html="icon('mountain')"></span> Mineral &amp; Batubara
                </span>
                <span style="display:inline-flex;align-items:center;gap:8px;background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:8px 16px;font-size:13px;font-weight:700">
                  <span aria-hidden="true" v-html="icon('tree')"></span> Eksplorasi Hutan
                </span>
              </div>
            </div>
            <div class="about-badge">Layanan Prima · Kepuasan Pelanggan</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
