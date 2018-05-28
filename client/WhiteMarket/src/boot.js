/* eslint-disable */ 
import Vue from 'vue';
import { API } from '@/utils/api'
Vue.config.debug = process.env.NODE_ENV !== 'production';
if(localStorage.getItem('token')){
  API.defaults.headers.common['Authorization'] = `JWT ${localStorage.getItem('token')}`;
}