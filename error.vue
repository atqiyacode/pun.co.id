<script setup>
const props = defineProps({ error: Object })

const is404 = computed(() => props.error?.statusCode === 404)
const code = computed(() => props.error?.statusCode || 404)
const message = computed(() => (is404.value ? $t('notfound.subtitle') : (props.error?.message || $t('notfound.subtitle'))))
</script>

<template>
  <section class="notfound">
    <div class="bg-grid" aria-hidden="true"></div>
    <div class="container notfound-inner">
      <div class="notfound-code">{{ code }}</div>
      <span class="eyebrow">Error</span>
      <h1>{{ $t('notfound.title') }}</h1>
      <p>{{ message }}</p>
      <div class="notfound-cta">
        <a href="/" class="btn btn-gold">{{ $t('notfound.home') }}</a>
      </div>
    </div>
  </section>
</template>
