<script setup>
import { icon } from '~/utils/icons'
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { contact } = company.company
useReveal()

const items = [
  { label: 'Telepon / WhatsApp', value: contact.phone, href: contact.phoneHref, icon: 'phone' },
  { label: 'Email', value: contact.email, href: `mailto:${contact.email}`, icon: 'mail' },
  { label: 'Website', value: 'www.pun.co.id', href: `https://${contact.website.replace(/^https?:\/\//, '')}`, icon: 'globe' },
  { label: 'Alamat', value: `${contact.address}, ${contact.addressDetail}`, href: null, icon: 'pin' }
]
</script>

<template>
  <section id="contact">
    <div class="container">
      <div class="section-head reveal">
        <span class="index">Sect. 06 — Contact</span>
        <h2>Hubungi <span class="hl">Kami</span></h2>
        <p>Mari wujudkan kebutuhan kontrak Anda bersama kami — layanan prima adalah dedikasi kami.</p>
      </div>

      <div class="contact-grid">
        <div class="contact-card reveal">
          <div class="contact-card-head">
            <span>Kontak <span class="hl">Resmi</span></span>
            <span>24/7</span>
          </div>
          <div class="contact-list">
            <div v-for="item in items" :key="item.label" class="contact-item">
              <div class="contact-icon" aria-hidden="true" v-html="icon(item.icon)"></div>
              <div>
                <h4>{{ item.label }}</h4>
                <a v-if="item.href" :href="item.href" target="_blank" rel="noopener">{{ item.value }}</a>
                <p v-else>{{ item.value }}</p>
              </div>
            </div>
          </div>
          <div class="contact-ctas">
            <a class="btn btn-orange" :href="contact.whatsappHref" target="_blank" rel="noopener">
              <span aria-hidden="true" v-html="icon('wa')"></span> WhatsApp
            </a>
            <a class="btn btn-paper" :href="contact.phoneHref">Telepon</a>
          </div>
        </div>

        <div class="contact-map reveal">
          <iframe
            :src="contact.mapsEmbed"
            title="Lokasi PT. Prima Utama Nasional"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen
          ></iframe>
        </div>
      </div>
    </div>
  </section>
</template>
