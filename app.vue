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
    { property: 'og:image', content: `${siteUrl}/images/og-cover.svg` },
    { property: 'og:locale', content: locale.value === 'id' ? 'id_ID' : 'en_US' },
    { property: 'og:locale:alternate', content: locale.value === 'id' ? 'en_US' : 'id_ID' },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: seoTitle },
    { name: 'twitter:description', content: seoDesc },
    { name: 'twitter:image', content: `${siteUrl}/images/og-cover.svg` }
  ],
  link: [
    { rel: 'canonical', href: currentUrl },
    { rel: 'alternate', hreflang: 'id', href: siteUrl },
    { rel: 'alternate', hreflang: 'en', href: `${siteUrl}/en` },
    { rel: 'alternate', hreflang: 'x-default', href: siteUrl }
  ],
  script: [
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
            inLanguage: 'id-ID'
          }
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
  </div>
</template>
