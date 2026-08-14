<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { icon } from '~/utils/icons'

const company = await useCompanyData()
const { company: c } = company
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
  onScroll()
})
onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))

const scrollTop = () => window.scrollTo({ top: 0, behavior: 'smooth' })
</script>

<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <!-- Brand -->
        <div class="footer-brand">
          <a href="#home" class="logo" aria-label="PT. Prima Utama Nasional — Home">
            <span class="logo-mark" aria-hidden="true">{{ c.shortName }}</span>
            <span>{{ c.name }}</span>
          </a>
          <p class="footer-tagline">{{ $t('footer.tagline') }}</p>
          <div class="footer-contact-lines">
            <p><span aria-hidden="true" v-html="icon('phone')"></span> {{ c.contact.phone }}</p>
            <p><span aria-hidden="true" v-html="icon('mail')"></span> {{ c.contact.email }}</p>
            <p><span aria-hidden="true" v-html="icon('pin')"></span> {{ $t('footer.address') }}</p>
          </div>
        </div>

        <!-- Menu -->
        <nav class="footer-col" :aria-label="$t('footer.quickLinks')">
          <h4 class="footer-title">{{ $t('footer.quickLinks') }}</h4>
          <ul class="footer-links">
            <li v-for="l in links" :key="l.href"><a :href="l.href">{{ $t(l.labelKey) }}</a></li>
          </ul>
        </nav>

        <!-- Kontak -->
        <div class="footer-col">
          <h4 class="footer-title">{{ $t('footer.contact') }}</h4>
          <ul class="footer-links">
            <li><a :href="c.contact.phoneHref">{{ c.contact.phone }}</a></li>
            <li><a :href="`mailto:${c.contact.email}`">{{ c.contact.email }}</a></li>
            <li><a :href="`https://${c.contact.website.replace(/^https?:\/\//, '')}`" target="_blank" rel="noopener">www.pun.co.id</a></li>
            <li><a :href="c.contact.whatsappHref" target="_blank" rel="noopener">WhatsApp</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; {{ new Date().getFullYear() }} {{ c.name }}. {{ $t('footer.rights') }}</p>
      </div>
    </div>
  </footer>

  <div class="footer-top">
    <button
      class="footer-top-btn"
      :class="{ show: showTop }"
      @click="scrollTop"
      :aria-label="$t('scrollTop')"
      :title="$t('scrollTop')"
    >
      <span aria-hidden="true" v-html="icon('up')"></span>
    </button>
  </div>
</template>

<style scoped>
.footer-grid {
  display: grid;
  grid-template-columns: 1.6fr 1fr 1fr;
  gap: 48px;
  padding: 64px 0 48px;
}
.footer-brand .logo { margin-bottom: 16px; }
.footer-tagline {
  color: var(--muted);
  font-size: 14.5px;
  max-width: 380px;
  margin-bottom: 22px;
}
.footer-contact-lines { display: flex; flex-direction: column; gap: 10px; }
.footer-contact-lines p {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  color: var(--muted);
  font-size: 13.5px;
  line-height: 1.5;
}
.footer-contact-lines svg { color: var(--accent); flex-shrink: 0; margin-top: 2px; }

.footer-title {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 20px;
}
.footer-links { display: flex; flex-direction: column; gap: 12px; list-style: none; }
.footer-links a { color: var(--muted); font-size: 14px; font-weight: 600; transition: color 0.25s; }
.footer-links a:hover { color: var(--accent); }

.footer-bottom {
  border-top: 1px solid var(--border);
  padding: 24px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}
.footer-bottom p { color: var(--muted); font-size: 13.5px; }

/* Scroll to top */
.footer-top { position: fixed; right: 22px; bottom: 22px; z-index: 50; }
.footer-top-btn {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  border: 1px solid var(--border);
  background: rgba(10, 17, 32, 0.85);
  backdrop-filter: blur(10px);
  color: var(--accent);
  font-size: 18px;
  cursor: pointer;
  transition: transform 0.3s ease, background 0.3s ease, opacity 0.3s ease;
  opacity: 0;
  pointer-events: none;
  transform: translateY(10px);
  display: grid;
  place-items: center;
}
.footer-top-btn.show {
  opacity: 1;
  pointer-events: auto;
  transform: translateY(0);
}
.footer-top-btn:hover {
  transform: translateY(-4px);
  background: var(--accent);
  color: #0a1120;
}

@media (max-width: 860px) {
  .footer-grid { grid-template-columns: 1fr; gap: 36px; padding: 48px 0 40px; }
}
</style>
