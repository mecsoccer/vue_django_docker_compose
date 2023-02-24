import { retrieveAccessToken, retrieveRefreshToken, storeAccessToken } from '@/utils/storage.util'
import axios from 'axios'

const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000/api/v1/',
  headers: {
    'Content-type': 'application/json',
    Authorization: 'Bearer ' + retrieveAccessToken()
  }
})

const refreshToken = async () => {
  try {
    const refresh = retrieveRefreshToken()
    const resp = await instance.post('token/refresh/', { refresh })
    return resp
  } catch (e) {
    console.log('Error', e)
  }
}

instance.interceptors.request.use(
  async (config) => {
    const token = retrieveAccessToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

instance.interceptors.response.use(
  (response) => {
    return response
  },
  async function (error) {
    const originalRequest = error.config
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true

      const resp = await refreshToken()

      const accessToken = resp?.data.access

      storeAccessToken(accessToken)
      instance.defaults.headers.common.Authorization = `Bearer ${accessToken}`
      return instance(originalRequest)
    }
    return Promise.reject(error)
  }
)

export default instance
