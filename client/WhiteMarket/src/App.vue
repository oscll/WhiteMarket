<template>
  <div id="app">
    <main-header> </main-header>
    <router-view/>
    <main-footer></main-footer>
  </div>
</template>

<script>
/* eslint-disable */
import MainHeader from '@/components/header/Header'
import MainFooter from '@/components/Footer'
export default {
  name: 'App',
  components: {
    MainHeader,
    MainFooter
  }
}
</script>

<style lang="scss">
  @import url(https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css);  
  @import url("./assets/scss/style.scss");
  @import url('https://fonts.googleapis.com/css?family=Gugi');
</style>

