<script setup>
const company = await useCompanyData()
const { seo, company: c, services } = company
const siteUrl = 'https://www.pun.co.id'

useHead({
  title: seo.title,
  titleTemplate: '%s',
  meta: [
    { name: 'description', content: seo.description },
    { name: 'keywords', content: seo.keywords },
    { name: 'author', content: c.name },
    { name: 'robots', content: 'index, follow' },
    { name: 'theme-color', content: '#08140e' },
    // OpenGraph
    { property: 'og:type', content: 'website' },
    { property: 'og:site_name', content: c.name },
    { property: 'og:title', content: seo.title },
    { property: 'og:description', content: seo.description },
    { property: 'og:url', content: siteUrl },
    { property: 'og:image', content: `${siteUrl}${seo.ogImage}` },
    { property: 'og:locale', content: 'id_ID' },
    // Twitter
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: seo.title },
    { name: 'twitter:description', content: seo.description },
    { name: 'twitter:image', content: `${siteUrl}${seo.ogImage}` }
  ],
  link: [
    { rel: 'canonical', href: siteUrl }
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
            description: seo.description,
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
            image: `${siteUrl}${seo.ogImage}`,
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
          },
          ...services.map((s, i) => ({
            '@type': 'Service',
            '@id': `${siteUrl}/#service-${i + 1}`,
            name: s.title,
            description: s.description,
            provider: { '@id': `${siteUrl}/#organization` },
            areaServed: 'Indonesia'
          }))
        ]
      })
    }
  ]
})
</script>

<template>
  <div>
    <Navbar />
    <NuxtPage />
    <Footer />
  </div>
</template>
