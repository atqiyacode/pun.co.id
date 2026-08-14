<script setup>
const { t, locale } = useI18n()
const company = await useCompanyData()
const c = company.company
const siteUrl = 'https://www.pun.co.id'

const seoTitle = computed(() => t('seo.title'))
const seoDesc = computed(() => t('seo.description'))
const seoKeywords = computed(() => t('seo.keywords'))
const currentUrl = computed(() => locale.value === 'id' ? siteUrl : `${siteUrl}/en`)

useHead({
  title: seoTitle,
  titleTemplate: '%s',
  htmlAttrs: { lang: locale },
  meta: [
    { name: 'description', content: seoDesc },
    { name: 'keywords', content: seoKeywords },
    { name: 'author', content: c.name },
    { name: 'robots', content: 'index, follow' },
    { name: 'theme-color', content: '#0a1120' },
    { property: 'og:type', content: 'website' },
    { property: 'og:site_name', content: c.name },
    { property: 'og:title', content: seoTitle },
    { property: 'og:description', content: seoDesc },
    { property: 'og:url', content: currentUrl },
    { property: 'og:image', content: `${siteUrl}/images/og-cover.png` },
    { property: 'og:locale', content: locale.value === 'id' ? 'id_ID' : 'en_US' },
    { property: 'og:locale:alternate', content: locale.value === 'id' ? 'en_US' : 'id_ID' },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: seoTitle },
    { name: 'twitter:description', content: seoDesc },
    { name: 'twitter:image', content: `${siteUrl}/images/og-cover.png` }
  ],
  link: [
    { rel: 'canonical', href: currentUrl },
    { rel: 'alternate', hreflang: 'id', href: siteUrl },
    { rel: 'alternate', hreflang: 'en', href: `${siteUrl}/en` },
    { rel: 'alternate', hreflang: 'x-default', href: siteUrl },
    { rel: 'icon', type: 'image/png', href: '/images/favicon.png' },
    { rel: 'apple-touch-icon', sizes: '180x180', href: '/images/apple-touch-icon.png' }
  ],
  script: [
    {
      innerHTML: `(function(){try{var t=localStorage.getItem('pun-theme');if(!t)t=window.matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';document.documentElement.setAttribute('data-theme',t)}catch(e){}})()`
    },
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'Organization',
            '@id': `${siteUrl}/#organization`,
            name: c.name,
            url: siteUrl,
            logo: `${siteUrl}/favicon.svg`,
            description: t('seo.description'),
            foundingDate: '2023',
            telephone: c.contact.phone,
            email: c.contact.email,
            address: {
              '@type': 'PostalAddress',
              streetAddress: `${c.contact.address}, ${c.contact.addressDetail}`,
              addressLocality: 'Jakarta Selatan',
              addressRegion: 'DKI Jakarta',
              postalCode: '12930',
              addressCountry: 'ID'
            },
            sameAs: []
          },
          {
            '@type': 'ProfessionalService',
            '@id': `${siteUrl}/#business`,
            name: c.name,
            url: siteUrl,
            image: `${siteUrl}/images/og-cover.svg`,
            telephone: c.contact.phone,
            priceRange: '$$',
            address: {
              '@type': 'PostalAddress',
              streetAddress: `${c.contact.address}, ${c.contact.addressDetail}`,
              addressLocality: 'Jakarta Selatan',
              addressRegion: 'DKI Jakarta',
              postalCode: '12930',
              addressCountry: 'ID'
            }
          },
          {
            '@type': 'WebSite',
            '@id': `${siteUrl}/#website`,
            url: siteUrl,
            name: c.name,
            publisher: { '@id': `${siteUrl}/#organization` },
            inLanguage: locale.value === 'id' ? 'id-ID' : 'en-US'
          },
          ...[0, 1, 2].map((i) => ({
            '@type': 'Service',
            '@id': `${siteUrl}/#service-${i + 1}`,
            name: t(`services.items.${i}.title`),
            description: t(`services.items.${i}.description`),
            provider: { '@id': `${siteUrl}/#organization` },
            areaServed: 'Indonesia'
          }))
        ]
      })
    }
  ]
})

watch(locale, () => {
  const head = useHead()
  head.refresh?.()
})
</script>

<template>
  <div>
    <Navbar />
    <NuxtPage />
    <Footer />
    <WhatsAppFloat />
  </div>
</template>
