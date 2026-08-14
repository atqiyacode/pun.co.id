// Loads company data from static JSON at build time
import companyData from '~/content/company.json'

export const useCompanyData = () => {
  return JSON.parse(JSON.stringify(companyData))
}
