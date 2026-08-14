import { ref } from 'vue'

// Theme state: 'dark' (default) | 'light'. Persisted in localStorage, honors prefers-color-scheme.
const THEME_KEY = 'pun-theme'

export const theme = ref('dark')

export function initTheme() {
  if (import.meta.client) {
    theme.value = localStorage.getItem(THEME_KEY) || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark')
  }
}

export function setTheme(t) {
  theme.value = t
  if (import.meta.client) {
    localStorage.setItem(THEME_KEY, t)
    document.documentElement.setAttribute('data-theme', t)
  }
}

export function toggleTheme() {
  setTheme(theme.value === 'dark' ? 'light' : 'dark')
}
