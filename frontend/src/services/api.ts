import axios from 'axios'

const instance = () => {
  const token = localStorage.getItem('ACCESS_TOKEN')
  return axios.create({
    baseURL: 'http://localhost:8000/api/v1/',
    headers: {
      'Content-Type': 'application/json',
      Authorization: 'Bearer ' + token
    }
  })
}

export default instance
