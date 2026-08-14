<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { projects } = company
useReveal()

const visualIcon = (title) => {
  const t = title.toLowerCase()
  if (t.includes('batubara') || t.includes('coal')) return icon('coal')
  if (t.includes('nikel')) return icon('nickel')
  return icon('mountain')
}
</script>

<template>
  <section id="projects">
    <div class="glow" style="bottom:-160px;left:-160px;width:480px;height:480px;background:rgba(52,211,153,0.1)" aria-hidden="true"></div>
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Our Project</span>
        <h2>Yang Telah Kami Kerjakan</h2>
        <p>Bukti nyata komitmen kami dalam memenuhi kebutuhan kontrak klien di berbagai lokasi Indonesia.</p>
      </div>
      <div class="projects-grid">
        <article v-for="p in projects" :key="p.title" class="project-card">
          <div class="project-visual">
            <span class="project-cat">{{ p.category }}</span>
            <span class="pv-icon" aria-hidden="true" v-html="visualIcon(p.title)"></span>
          </div>
          <div class="project-body">
            <h3>{{ p.title }}</h3>
            <p>{{ p.description }}</p>
            <div class="project-meta">
              <span><span class="ico" aria-hidden="true" v-html="icon('pin')"></span> {{ p.location }}</span>
              <span><span class="ico" aria-hidden="true" v-html="icon('target')"></span> {{ p.client }}</span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
