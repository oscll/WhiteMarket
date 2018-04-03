<template>
  <div id="app">
    <main-header> </main-header>
    <router-view/>
    <main-footer></main-footer>
  </div>
</template>

<script>
import MainHeader from '@/components/Header'
import MainFooter from '@/components/Footer'
export default {
  name: 'App',
  components: {
    MainHeader,
    MainFooter
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
