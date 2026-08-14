<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'
import { useLocaleItems } from '~/composables/useLocaleItems'

const company = await useCompanyData()
const { company: c } = company
useReveal()
const fields = useLocaleItems('about.fields', company.counts.aboutFields, ['title', 'description', 'icon'])
</script>

<template>
  <section id="about">
    <div class="bg-grid" aria-hidden="true"></div>
    <div class="container">
      <div class="about-grid">
        <div class="about-text">
          <span class="eyebrow">{{ $t('about.eyebrow') }}</span>
          <h2>{{ $t('about.title') }}</h2>
          <p style="margin-top:18px">{{ $t('about.heading') }}</p>
          <p>{{ $t('about.paragraph1') }}</p>
          <p>{{ $t('about.paragraph2') }}</p>
          <div class="about-fields">
            <div v-for="f in fields" :key="f.title" class="field-card">
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
              <h4>{{ $t('about.cardTitle') }}</h4>
              <p>{{ $t('about.cardText') }}</p>
              <div style="margin-top:20px;display:flex;gap:12px;flex-wrap:wrap">
                <span style="display:inline-flex;align-items:center;gap:8px;background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:8px 16px;font-size:13px;font-weight:700">
                  <span aria-hidden="true" v-html="icon('mountain')"></span> {{ $t('about.fields.3.title') }}
                </span>
                <span style="display:inline-flex;align-items:center;gap:8px;background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:8px 16px;font-size:13px;font-weight:700">
                  <span aria-hidden="true" v-html="icon('tree')"></span> {{ $t('about.fields.2.title') }}
                </span>
              </div>
            </div>
            <div class="about-badge">{{ $t('about.badge') }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
