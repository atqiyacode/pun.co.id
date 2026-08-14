<script setup>
import { ref, onMounted } from 'vue'
import { icon } from '~/utils/icons'
import { theme, initTheme, toggleTheme } from '~/composables/useTheme'

const company = await useCompanyData()
const links = [
  { labelKey: 'nav.home', href: '#home' },
  { labelKey: 'nav.about', href: '#about' },
  { labelKey: 'nav.services', href: '#services' },
  { labelKey: 'nav.projects', href: '#projects' },
  { labelKey: 'nav.contact', href: '#contact' }
]
const scrolled = ref(false)
const open = ref(false)

const onScroll = () => { scrolled.value = window.scrollY > 40 }
onMounted(() => {
  initTheme()
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
        <span class="logo-mark" aria-hidden="true">{{ company.company.shortName }}</span>
        <span>{{ company.company.name }}</span>
      </a>

      <nav :aria-label="$t('nav.home')">
        <ul class="nav-links" :class="{ open }">
          <li v-for="l in links" :key="l.href">
            <a :href="l.href" @click="go">{{ $t(l.labelKey) }}</a>
          </li>
          <li>
            <a href="#contact" class="btn btn-gold nav-cta" @click="go">{{ $t('nav.cta') }}</a>
          </li>
        </ul>
      </nav>

      <div class="nav-right">
        <button
          class="theme-toggle"
          @click="toggleTheme"
          :aria-label="theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'"
          :title="theme === 'dark' ? 'Light mode' : 'Dark mode'"
        >
          <span aria-hidden="true" v-html="icon(theme === 'dark' ? 'sun' : 'moon')"></span>
        </button>
        <button class="lang-switch" @click="$i18n.setLocale($i18n.locale === 'id' ? 'en' : 'id')" :aria-label="'Switch language'">
          {{ $i18n.locale === 'id' ? 'EN' : 'ID' }}
        </button>
        <button class="hamburger" :class="{ open }" @click="toggle" :aria-label="open ? $t('scrollTop') : $t('nav.home')" :aria-expanded="open">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>
</template>
