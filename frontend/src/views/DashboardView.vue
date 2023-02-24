<template>
    <div id="dashboard-page">
        <div class="fm-container">
            <nav class="topbar-nav max-content">
              <img width="80px" alt="SmartEnergy logo" src="https://www.smartenergylab.pt/wp-content/uploads/2021/03/SmartEnergyLab_00_Home_imagens-03.png">
              <div class="nav-div-83wjdu32">
                  <div class="img-avatar-div-323jhd" @mouseover="showLogout = true">
                      <div class="img-div-23j3ds">
                          <img src="https://via.placeholder.com/50x50.png/8B8B8B/FFFFFF" />
                      </div>
                      <span>Your Name</span>
                  </div>
                  <div v-if="showLogout" class="logout-div-3jwe42" @click="logout()" @mouseleave="showLogout = false">
                    <font-awesome-icon icon="fa-solid fa-right-from-bracket" /> Logout</div>
              </div>
            </nav>
            <div class="body-da23jd" @click="showLogout = false">
                <div class="table-container-323u3238 max-content">
                    <div class="title-div-j434lss">
                        <h2>Log Table</h2>
                    </div>
                    <table>
                        <tr>
                            <th>S/N</th>
                            <th>Location</th>
                            <th>Energy (kWh)</th>
                            <th>Date</th>
                            <th>Cost (&#x20AC;/kWh)</th>
                        </tr>
                        <tr v-for="item in chargeSessionCost" :key="item.id">
                            <td>{{ item.id }}</td>
                            <td>{{ item.location }}</td>
                            <td>{{ new Intl.NumberFormat("de-DE").format(item.energy_kWh) }}</td>
                            <td>{{ (new Date(item.charge_datetime)).toLocaleDateString().replace(/\//g, '-') }} {{ (new Date(item.charge_datetime)).toLocaleTimeString() }}</td>
                            <td>{{ new Intl.NumberFormat("de-DE").format(item.cost) }}</td>
                        </tr>
                    </table>
                </div>
                <pagination v-model="page" :records="200" @paginate="handlePaginate"/>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import api from '../services/api'
import Pagination from 'vue-pagination-2'
import { getUser } from '@/utils/users.util'
import { retrieveAccessToken } from '@/utils/storage.util'

interface ChargeSessionData {
  id: number,
  // eslint-disable-next-line
  user_info: number, location: string, energy_kWh: number, cost: number, charge_datetime: number
}
@Component({
  components: {
    Pagination
  }
})
export default class Login extends Vue {
  showLogout = false
  page = 1
  user = getUser()
  chargeSessionCost: Array<ChargeSessionData> = []

  logout (): void {
    localStorage.clear()
    this.$router.push('/login')
  }

  handlePaginate (page: number): void {
    this.page = page
    this.getDashboardData(getUser().id, page)
  }

  getDashboardData (user: number, page: number): void {
    api.get('/chargesessioncost/', { params: { user_info: user, page } })
      .then((data) => {
        this.chargeSessionCost = data.data
      })
      .catch((error) => console.log(error))
  }

  mounted (): void {
    const accessToken = retrieveAccessToken()
    const tokenPayload = window.atob(accessToken?.split('.')[1] || '')
    if (!tokenPayload) {
      this.$router.push('/login')
    }
    const { user_id: user } = JSON.parse(tokenPayload)
    this.getDashboardData(user, 1)
  }
}
</script>

<style scoped lang="scss">
.VuePagination{
  overflow: scroll;
    @media screen and (min-width: 600px) {
      display: flex;
      justify-content: center;
    }
}
#dashboard-page {
  width: 100%;
  height: 100%;
  min-height: 100vh;
  .topbar-nav{
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 70px;
    width: 90%;
    margin: auto;
    @media screen and (min-width: 600px) {}
    .nav-div-83wjdu32{
        display: flex;
        align-items: center;
        position: relative;
        .img-avatar-div-323jhd{
            display: flex;
            align-items: center;
        }
        .logout-div-3jwe42{
            position: absolute;
            top: 50px;
            width: 100%;
            height: 30px;
            background-color: #EFEFEF;
            border-radius: 5px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-evenly;
        }
        .img-div-23j3ds{
            width: 50px;
            height: 50px;
            border-radius: 25px;
            background-color: #EAEAEA;
            overflow: hidden;
            margin-right: 5px;
        }
        span{
            color: #F8F8F8;
        }
    }
  }
  .body-da23jd{
    background-color: #EAEAEA;
    padding: 40px 5%;
    @media screen and (min-width: 600px) {
      padding: 5%;
    }
    .table-container-323u3238{
        width: 100%;
        background-color: #EFEFEF;
        box-shadow: 2px 2px 2px gainsboro;
        border-radius: 30px;
        overflow: hidden;
        min-height: 80vh;
        overflow-x: scroll;
        margin: 0 auto 25px;
        .title-div-j434lss{
            color: #000000;
            text-align: left;
            padding: 20px 30px;
        }
        table {
            color: #000000;
            border-collapse: collapse;
            border-spacing: 0;
            width: 100%;
            border: 1px solid #ddd;
        }
        th{
            color: #8B8B8B;
            background-color: #c7c7c7;
        }
        th:first-child, td:first-child{
          text-align: center;
        }
        th, td {
        text-align: left;
        padding: 16px;
        }
        tr{
            background-color: #EAEAEA;
        }
        tr:nth-child(even) {
        background-color: #F8F8F8;
        }
    }
  }
}

</style>
