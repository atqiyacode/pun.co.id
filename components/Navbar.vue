<script setup>
import { ref, onMounted } from 'vue'

const links = [
  { label: 'Home', href: '#home' },
  { label: 'About', href: '#about' },
  { label: 'Services', href: '#services' },
  { label: 'Projects', href: '#projects' },
  { label: 'Contact', href: '#contact' }
]
const scrolled = ref(false)
const open = ref(false)

const onScroll = () => { scrolled.value = window.scrollY > 40 }
onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
})

function toggle() { open.value = !open.value }
function go() { open.value = false }
</script>

<template>
  <header class="nav" :class="{ scrolled }">
    <div class="container nav-inner">
      <a href="#home" class="logo" aria-label="PT. Prima Utama Nasional — Home">
        <span class="logo-mark">PUN</span>
        <span class="logo-text">Prima Utama Nasional<small>EST. 2023 — CONTRACTOR</small></span>
      </a>

      <nav :aria-label="'Navigasi utama'">
        <ul class="nav-links" :class="{ open }">
          <li v-for="l in links" :key="l.href">
            <a :href="l.href" @click="go">{{ l.label }}</a>
          </li>
          <li>
            <a href="#contact" class="btn btn-orange nav-cta" @click="go">Hubungi Kami</a>
          </li>
        </ul>
      </nav>

      <button class="hamburger" :class="{ open }" @click="toggle" :aria-label="open ? 'Tutup menu' : 'Buka menu'" :aria-expanded="open">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
</template>
