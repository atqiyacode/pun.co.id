<script setup>
import { ref, onMounted } from 'vue'
import { icon } from '~/utils/icons'

const company = await useCompanyData()
const links = [
  { label: 'Home', href: '#home' },
  { label: 'About', href: '#about' },
  { label: 'Visi & Misi', href: '#vision' },
  { label: 'Layanan', href: '#services' },
  { label: 'Proyek', href: '#projects' },
  { label: 'Kontak', href: '#contact' }
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
      <p>&copy; {{ new Date().getFullYear() }} {{ company.company.name }} — Rev. 1.0. All rights reserved.</p>
      <ul class="footer-links">
        <li v-for="l in links" :key="l.href"><a :href="l.href">{{ l.label }}</a></li>
      </ul>
    </div>
  </footer>

  <div class="footer-top">
    <button :class="{ show: showTop }" @click="scrollTop" aria-label="Kembali ke atas">
      <span aria-hidden="true" v-html="icon('up')"></span>
    </button>
  </div>
</template>
