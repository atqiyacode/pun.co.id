<script setup>
import { icon } from '~/utils/icons'

const company = await useCompanyData()
const { hero } = company
</script>

<template>
  <section id="home" class="hero">
    <div class="hero-bg" aria-hidden="true">
      <svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMax slice" style="position:absolute;inset:0;width:100%;height:100%">
        <defs>
          <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#0a1120"/>
            <stop offset="55%" stop-color="#0d1730"/>
            <stop offset="100%" stop-color="#14213d"/>
          </linearGradient>
          <radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
            <stop offset="0%" stop-color="#f5d97a"/>
            <stop offset="55%" stop-color="#d4af37" stop-opacity="0.55"/>
            <stop offset="100%" stop-color="#d4af37" stop-opacity="0"/>
          </radialGradient>
          <linearGradient id="m1" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#14213d"/>
            <stop offset="100%" stop-color="#0d1730"/>
          </linearGradient>
        </defs>
        <rect width="1440" height="900" fill="url(#sky)"/>
        <circle cx="1050" cy="330" r="190" fill="url(#sun)"/>
        <circle cx="1050" cy="330" r="62" fill="#f5d97a" opacity="0.95"/>
        <path d="M0 560 L220 430 L420 540 L640 400 L860 540 L1060 420 L1240 530 L1440 440 L1440 900 L0 900 Z" fill="#14213d" opacity="0.75"/>
        <path d="M0 660 L260 520 L500 640 L760 500 L1000 640 L1220 540 L1440 630 L1440 900 L0 900 Z" fill="url(#m1)"/>
        <path d="M0 780 L180 660 L380 760 L620 640 L860 770 L1100 660 L1300 760 L1440 700 L1440 900 L0 900 Z" fill="#0a1120"/>
        <g fill="#f5d97a" opacity="0.14">
          <circle cx="180" cy="240" r="2"/><circle cx="320" cy="180" r="1.6"/><circle cx="520" cy="300" r="1.4"/>
          <circle cx="700" cy="200" r="2"/><circle cx="880" cy="260" r="1.5"/><circle cx="1250" cy="210" r="1.8"/>
        </g>
      </svg>
    </div>

    <div class="container">
      <div class="hero-content">
        <span class="hero-eyebrow"><span class="dot" aria-hidden="true"></span>{{ hero.eyebrow }}</span>
        <h1>
          {{ hero.titleLine1 }}
          <span class="grad">{{ hero.titleLine2 }}</span>
        </h1>
        <p class="hero-sub">{{ hero.subtitle }}</p>
        <div class="hero-ctas">
          <a href="#services" class="btn btn-gold">Lihat Layanan <span aria-hidden="true" v-html="icon('arrow')"></span></a>
          <a href="#contact" class="btn btn-ghost">Hubungi Kami</a>
        </div>
      </div>

      <div class="hero-stats">
        <div v-for="s in hero.stats" :key="s.label" class="stat">
          <div class="stat-value">{{ s.value }}</div>
          <div class="stat-label">{{ s.label }}</div>
        </div>
      </div>
    </div>
  </section>
</template>
