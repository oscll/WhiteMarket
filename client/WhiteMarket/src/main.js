// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
/* eslint-disable */ 
import App from './App'
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
require('./boot');
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
