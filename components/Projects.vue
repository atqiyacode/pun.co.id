<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

useReveal()

const visualIcon = (title) => {
  const t = String(title || '').toLowerCase()
  if (t.includes('batubara') || t.includes('coal')) return icon('coal')
  if (t.includes('nikel') || t.includes('nickel')) return icon('nickel')
  return icon('mountain')
}
</script>

<template>
  <section id="projects">
    <div class="glow" style="bottom:-160px;left:-160px;width:480px;height:480px;background:rgba(52,211,153,0.1)" aria-hidden="true"></div>
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">{{ $t('projects.eyebrow') }}</span>
        <h2>{{ $t('projects.title') }}</h2>
        <p>{{ $t('projects.subtitle') }}</p>
      </div>
      <div class="projects-grid">
        <article v-for="p in $tm('projects.items')" :key="p.title" class="project-card">
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
