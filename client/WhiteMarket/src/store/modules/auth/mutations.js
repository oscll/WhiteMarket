/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'

export default {
  [types.LOGIN](state, token) {
    state.token = token;
    localStorage.setItem('token',token);
    API.defaults.headers.common['Authorization'] = `JWT ${token}`;
  },
  [types.LOGOUT](state) {
    state.token = undefined;
    localStorage.removeItem('token');
    API.defaults.headers.common['Authorization'] = undefined;
  },
  initialiseStore(state){
    if(localStorage.getItem('token')){
       // types.LOGIN(localStorage.getItem('token'))
      API.post('/auth/jwt/verify/',{token: localStorage.getItem('token')})
      .then(response => (
          API.post('/auth/jwt/refresh/',{token: response.data.token})
          .then(response => (
            this.commit('authStore/LOGIN', response.data.token)
          ))
          .catch(err => (console.log(err.response.data)))
      ))
      .catch(err => (console.log(err.response.data)))
    }
  }
};