/* eslint-disable */ 
import Vue from 'vue';
Vue.config.debug = process.env.NODE_ENV !== 'production';

import Axios from 'axios';
import BootstrapVue from 'bootstrap-vue';
import VeeValidate from 'vee-validate';

import './../node_modules/bootstrap/dist/css/bootstrap.css';

/* Vue.use(VeeValidate)

Axios.defaults.baseURL = 'http://localhost:8000';
Axios.defaults.headers.common.Accept = 'application/json';
 */
/* Vue.$http = Axios;
Object.defineProperty(Vue.prototype, '$http', {
  get() {
    return Axios;
  },
}); */

/* import { LOGIN } from '@/store/modules/auth'
if(localStorage.getItem('token')){
  this.$store.dispatch(LOGIN, localStorage.getItem('token'))
}
   */