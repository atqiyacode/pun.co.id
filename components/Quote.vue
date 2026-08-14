<script setup>
import { useReveal } from '~/composables/useReveal'

const company = await useCompanyData()
const { quote } = company
useReveal()
</script>

<template>
  <section class="quote-section">
    <div class="bg-grid" aria-hidden="true"></div>
    <div class="container">
      <div class="quote-mark" aria-hidden="true">&ldquo;</div>
      <p class="quote-text">{{ quote.text }}</p>
      <div class="quote-author">@{{ quote.author }}</div>
    </div>
  </section>
</template>
