<script setup>
import { icon } from '~/utils/icons'

const company = await useCompanyData()
const wa = company.company.contact.whatsappHref
</script>

<template>
  <a
    class="wa-float"
    :href="wa"
    target="_blank"
    rel="noopener"
    :aria-label="'WhatsApp'"
  >
    <span class="wa-float-icon" aria-hidden="true" v-html="icon('wa')"></span>
    <span class="wa-float-label">Chat Kami</span>
  </a>
</template>
