<script setup>
import { ref, onMounted } from 'vue'
import { icon } from '~/utils/icons'

const company = await useCompanyData()
const links = [
  { labelKey: 'nav.home', href: '#home' },
  { labelKey: 'nav.about', href: '#about' },
  { labelKey: 'vision.eyebrow', href: '#vision' },
  { labelKey: 'nav.services', href: '#services' },
  { labelKey: 'nav.projects', href: '#projects' },
  { labelKey: 'nav.contact', href: '#contact' }
]
const showTop = ref(false)
const onScroll = () => { showTop.value = window.scrollY > 600 }
onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
})

const scrollTop = () => window.scrollTo({ top: 0, behavior: 'smooth' })
</script>

<template>
  <footer class="footer">
    <div class="container footer-inner">
      <p>&copy; {{ new Date().getFullYear() }} {{ company.company.name }}. {{ $t('footer.rights') }}</p>
      <ul class="footer-links">
        <li v-for="l in links" :key="l.href"><a :href="l.href">{{ $t(l.labelKey) }}</a></li>
      </ul>
    </div>
  </footer>

  <div class="footer-top">
    <button :class="{ show: showTop }" @click="scrollTop" :aria-label="$t('scrollTop')">
      <span aria-hidden="true" v-html="icon('up')"></span>
    </button>
  </div>
</template>
