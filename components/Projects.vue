<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { projects } = company
useReveal()
</script>

<template>
  <section id="projects">
    <div class="bp-grid" aria-hidden="true"></div>
    <div class="container">
      <div class="section-head reveal">
        <span class="index">Sect. 05 — Portfolio</span>
        <h2>Our <span class="hl">Projects</span></h2>
        <p>Bukti nyata komitmen kami dalam memenuhi kebutuhan kontrak klien di berbagai lokasi Indonesia.</p>
      </div>

      <div class="projects-grid">
        <article v-for="p in projects" :key="p.title" class="project-card reveal">
          <div class="p-tab">FILE — {{ p.category.toUpperCase() }}</div>
          <div class="p-head">
            <span>{{ p.title }}</span>
            <span class="p-cat">CASE-0{{ projects.indexOf(p) + 1 }}</span>
          </div>
          <div class="p-body">
            <h3>{{ p.title }}</h3>
            <p>{{ p.description }}</p>
            <div class="p-meta">
              <span><span aria-hidden="true" v-html="icon('pin')"></span> {{ p.location }}</span>
              <span><span aria-hidden="true" v-html="icon('target')"></span> {{ p.client }}</span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
