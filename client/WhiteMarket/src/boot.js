/* eslint-disable */ 
import Vue from 'vue';
Vue.config.debug = process.env.NODE_ENV !== 'production';

import Axios from 'axios';

Axios.defaults.baseURL = 'http://localhost:8000';
Axios.defaults.headers.common.Accept = 'application/json';


Vue.$http = Axios;
Object.defineProperty(Vue.prototype, '$http', {
  get() {
    return Axios;
  },
});
  