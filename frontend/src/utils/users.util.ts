import api from '../services/api'

interface User {
  email: string,
  // eslint-disable-next-line
  first_name: string, id: number, last_name: string,
}

export const saveUser = (userData: object) => {
  localStorage.setItem('USER', JSON.stringify(userData))
}

export const getUser = (): User => {
  // eslint-disable-next-line
  return JSON.parse(localStorage.getItem('USER') as any)
}

export const fetchUserProfile = (user: number) => {
  api.get(`userinfo/users/${user}/`)
    .then((data) => saveUser(data.data))
    .catch()
}
