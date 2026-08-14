<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { contact } = company.company
useReveal()

const items = computed(() => [
  { label: $t('contact.phoneLabel'), value: contact.phone, href: contact.phoneHref, icon: 'phone' },
  { label: $t('contact.emailLabel'), value: contact.email, href: `mailto:${contact.email}`, icon: 'mail' },
  { label: $t('contact.websiteLabel'), value: 'www.pun.co.id', href: `https://${contact.website.replace(/^https?:\/\//, '')}`, icon: 'globe' },
  { label: $t('contact.addressLabel'), value: `${contact.address}, ${contact.addressDetail}`, href: null, icon: 'pin' }
])
</script>

<template>
  <section id="contact">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">{{ $t('contact.eyebrow') }}</span>
        <h2>{{ $t('contact.title') }}</h2>
        <p>{{ $t('contact.subtitle') }}</p>
      </div>

      <div class="contact-grid">
        <div class="contact-card">
          <div v-for="item in items" :key="item.label" class="contact-item">
            <div class="contact-icon" aria-hidden="true" v-html="icon(item.icon)"></div>
            <div>
              <h4>{{ item.label }}</h4>
              <a v-if="item.href" :href="item.href" target="_blank" rel="noopener">{{ item.value }}</a>
              <p v-else>{{ item.value }}</p>
            </div>
          </div>
          <div class="contact-ctas">
            <a class="btn btn-gold" :href="contact.whatsappHref" target="_blank" rel="noopener">
              <span aria-hidden="true" v-html="icon('wa')"></span> {{ $t('contact.whatsapp') }}
            </a>
            <a class="btn btn-ghost" :href="contact.phoneHref">{{ $t('contact.call') }}</a>
          </div>
        </div>

        <div class="contact-map">
          <iframe
            :src="contact.mapsEmbed"
            :title="$t('contact.mapTitle')"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen
          ></iframe>
        </div>
      </div>
    </div>
  </section>
</template>
