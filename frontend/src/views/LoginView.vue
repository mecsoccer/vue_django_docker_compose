<template>
    <div id="login-page">
        <div class="fm-container">
            <div class="logo-container">
                <img width="100px" alt="SmartEnergy logo" src="https://www.smartenergylab.pt/wp-content/uploads/2021/03/SmartEnergyLab_00_Home_imagens-01.png">
            </div>
            <form id="login-form" @submit="login">
                <div class="form-fields">
                    <div class="custom-input">
                      <font-awesome-icon icon="fa-solid fa-user" />
                      <input class="input-field" id="email" type="email" placeholder="Email" name="email" @input="handleInput" />
                    </div>
                    <div class="custom-input">
                      <font-awesome-icon icon="fa-solid fa-lock" />
                      <input class="input-field" id="password" type="password" placeholder="Password" name="password" @input="handleInput" />
                    </div>
                    <span></span>
                </div>
                <div class="submit-btn-container">
                    <button type="submit" :disabled="checkValidity()">login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script lang="ts">
import { fetchUserProfile } from '@/utils/users.util'
import { Component, Vue } from 'vue-property-decorator'
import api from '../services/api'
interface FormValues {
  email: string;
  password: string;
}

  @Component
export default class Login extends Vue {
  formValues: FormValues = {
    email: '',
    password: ''
  }

  loading = false

  checkValidity (): boolean {
    return !(this.formValues.email && this.formValues.password) || this.loading
  }

  handleInput (event: Event): void {
    const { name, value } = event.target as HTMLInputElement
    this.formValues = { ...this.formValues, [name]: value }
  }

  login (e: Event): void {
    e.preventDefault()
    const payload = {
      email: this.formValues.email,
      password: this.formValues.password
    }
    this.loading = true
    api().post('token/', payload)
      .then((data) => {
        this.loading = false
        localStorage.setItem('ACCESS_TOKEN', data.data.access)
        localStorage.setItem('REFRESH_TOKEN', data.data.refresh)
        const tokenPayload = window.atob(data.data.access?.split('.')[1] || '')
        const { user_id: user } = JSON.parse(tokenPayload)
        fetchUserProfile(user)
      })
      .then(() => {
        this.$router.push('/dashboard')
      })
      .catch(({ response, message }) => {
        this.loading = false
        if (!response) return alert(message)
        this.formValues.password = ''
        alert('invalid email or password')
      })
  }

  mounted (): void {
    const token = localStorage.getItem('ACCESS_TOKEN')
    if (token) this.$router.push('/dashboard')
  }
}
</script>

<style scoped lang="scss">
#login-page {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  width: 100%;
  height: 100%;
  min-height: 100vh;
  .fm-container{
    width: 80%;
    max-width: 450px;
    height: auto;
    background-color: #F8F8F8;
    border-radius: 20px;
    padding: 5%;
  }
  .logo-container{
    margin-bottom: 20px;
    img{
      width: 60%;
      max-width: 200px;
    }
  }
  #login-form{
    div{
      width: 100%;
    }
    .form-fields{
      margin-bottom: 50px;
    }
    .custom-input{
      position: relative;
      display: flex;
      align-items: center;
      height: 35px;
      margin-bottom: 20px;
      overflow: hidden;
      svg{
        position: absolute;
        left: 0;
        font-size: 20px;
        opacity: 0.7;
      }
      input{
        font-size: 18px;
        height: inherit;
        width: 100%;
        background-color: transparent;
        padding: 0 10px 0 30px;
        border-bottom: 2px solid #EAEAEA;
        border-top: 0;
        border-left: 0;
        border-right: 0;
        outline: none;
        opacity: 0.7;
      }
      .input-field:focus{
        border-bottom: 3px solid #3BBBC8;
        outline: none;
      }
    }
    .submit-btn-container{
      button{
        width: 100%;
        height: 50px;
        text-transform: uppercase;
        background-color: #3BBBC8;
        border-radius: 25px;
        border: none;
        color: #F8F8F8;
        font-size: 18px;
        font-weight: bold;
      }
      button:hover{
        background-color: #206b74;
        cursor: pointer;
      }
      button:disabled{
        background-color: #c7c7c7;
      }
    }
  }
}

</style>
