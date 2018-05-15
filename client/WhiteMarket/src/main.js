// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
/* eslint-disable */ 
import App from './App'
import router from './router'
import store from './store'
import VueMarkdown from 'vue-markdown'
/* import { sync } from 'vuex-router-sync' */
require('es6-promise').polyfill()


Vue.config.productionTip = false
Vue.config.devtools = true
Vue.config.silent = false
Vue.config.debug = process.env.NODE_ENV !== 'production';
Vue.use(VueMarkdown)
/* const unsync = sync(store, router) */

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  beforeCreate(){
    this.$store.commit('initialiseStore')
  },
  components: { App },
  template: '<App/>',
  router,
})
