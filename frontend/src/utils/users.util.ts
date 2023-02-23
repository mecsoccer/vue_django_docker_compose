import api from '../services/api'

export const saveUser = (userData: object) => {
  localStorage.setItem('USER', JSON.stringify(userData))
}

export const getUser = (): object | null => {
  return JSON.parse(localStorage.getItem('USER') as any)
}

export const fetchUserProfile = (user: number) => {
  api().get(`userinfo/users/${user}/`)
    .then((data) => saveUser(data.data))
    .catch()
}
