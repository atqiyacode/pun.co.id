<script setup>
import { icon } from '~/utils/icons'

const company = await useCompanyData()
const { hero, company: c } = company
</script>

<template>
  <section id="home" class="hero">
    <div class="bp-grid" aria-hidden="true"></div>

    <div class="container hero-inner">
      <!-- cover sheet meta -->
      <div class="hero-top-row">
        <span class="tag orange">Contractor · Mining · Trading</span>
        <div class="hero-docno">
          DOC. NO. <b>PUN/CP/2026-01</b><br>
          REV. 1.0 — INDONESIA
        </div>
      </div>

      <h1>
        Prima Utama<br>
        <span class="stroke">Nasional</span>
      </h1>

      <p class="hero-sub">{{ hero.subtitle }}</p>

      <div class="hero-ctas">
        <a href="#services" class="btn btn-orange">Lihat Layanan <span aria-hidden="true" v-html="icon('arrow')"></span></a>
        <a href="#contact" class="btn btn-paper">Hubungi Kami</a>
      </div>

      <!-- stamped stat strip -->
      <div class="hero-meta-row">
        <div v-for="s in hero.stats" :key="s.label" class="stat">
          <div class="stat-value"><em>{{ s.value }}</em></div>
          <div class="stat-label">{{ s.label }}</div>
        </div>
      </div>

      <div class="hero-sticker">
        <div class="sticker">
          Kepuasan Pelanggan<small>Kebanggaan Kami</small>
        </div>
      </div>
    </div>
  </section>
</template>
