import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  ssr: true,
  devtools: { enabled: false },
  css: [
    '@fontsource-variable/plus-jakarta-sans',
    '~/assets/css/main.css',
    '~/assets/css/tailwind.css'
  ],
  vite: {
    plugins: [tailwindcss()]
  },
  modules: ['@nuxtjs/i18n'],
  i18n: {
    locales: [
      { code: 'id', name: 'Indonesia', file: 'id.json', iso: 'id-ID' },
      { code: 'en', name: 'English', file: 'en.json', iso: 'en-US' }
    ],
    defaultLocale: 'en',
    lazy: true,
    langDir: '.',
    strategy: 'prefix_except_default',
    detectBrowserLanguage: false
  },
  app: {
    head: {
      htmlAttrs: { lang: 'en' },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'theme-color', content: '#0a1120' }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }
      ]
    }
  },
  nitro: {
    prerender: {
      routes: ['/', '/id']
    }
  }
})
