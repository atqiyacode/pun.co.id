import { onMounted, onBeforeUnmount } from 'vue'

// Reveal-on-scroll: observe every .reveal element inside the component
export const useReveal = () => {
  let observer = null

  onMounted(() => {
    observer = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
          observer.unobserve(entry.target)
        }
      }
    }, { threshold: 0.12 })

    for (const el of document.querySelectorAll('.reveal')) {
      observer.observe(el)
    }
  })

  onBeforeUnmount(() => {
    if (observer) observer.disconnect()
  })
}
