import { computed } from 'vue'
import { useI18n } from '#imports'

// Iterate translated arrays safely.
// $tm() returns compiled message AST in production — unusable in v-for.
// This rebuilds a plain array via t(`${path}.${i}.${key}`).
// ponytail: `count` is hardcoded per call site; if item counts change,
// update the call sites (or move counts into company.json).
export const useLocaleItems = (path, count, keys) => {
  const { t } = useI18n()
  return computed(() =>
    Array.from({ length: count }, (_, i) => {
      const item = {}
      for (const k of keys) item[k] = t(`${path}.${i}.${k}`)
      return item
    })
  )
}
