<template>
  <div id="app">
    <router-view/>
    <footer>&#169; 2021 Smart Energy Lab. All rights reserved.</footer>
  </div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400&display=swap');
html, body{
  width: 100%;
  margin: 0;
  background-color: #273043 !important;
}
*{
  box-sizing: border-box;
}

#app {
  font-family: Jost, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  footer{
    color: #F8F8F8;
    padding: 15px 0;
  }
}

nav {
  // padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.max-content{
  @media screen and (min-width: 1500px) {
    max-width: 1800px;
  }
}
</style>
