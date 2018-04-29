// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
/* eslint-disable */ 
import App from './App'
import router from './router'
import store from './store'
import { sync } from 'vuex-router-sync'
require('es6-promise').polyfill()


Vue.config.productionTip = false
const unsync = sync(store, router)

/* eslint-disable no-new */
require('./boot');
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  beforeCreate(){
    this.$store.commit('initialiseStore')
  }
})
