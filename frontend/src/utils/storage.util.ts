export const storeAccessToken = (token: string) => {
  localStorage.setItem('ACCESS_TOKEN', token)
}

export const storeRefreshToken = (token: string) => {
  localStorage.setItem('REFRESH_TOKEN', token)
}

export const retrieveAccessToken = (): string | null => {
  return localStorage.getItem('ACCESS_TOKEN')
}

export const retrieveRefreshToken = (): string | null => {
  return localStorage.getItem('REFRESH_TOKEN')
}
