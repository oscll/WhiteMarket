/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'

export default {

  [types.LOGIN](state, token) {
    state.token = token;
    localStorage.setItem('token',token);
    API.defaults.headers.common['Authorization'] = `JWT ${token}`;
  },

  [types.USER](state, user) {
    state.user = user;
    localStorage.setItem('user',user);
  },

  [types.LOGOUT](state) {
    state.token = undefined;
    state.user = undefined;
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    API.defaults.headers.common['Authorization'] = undefined;
  },

  initialiseStore(state){
    if(localStorage.getItem('token')){
      API.post('/auth/jwt/verify/',{token: localStorage.getItem('token')})
      .then(response => (
          API.post('/auth/jwt/refresh/',{token: response.data.token})
          .then(response => {
            this.commit(types.LOGIN, response.data.token)
            this.dispatch(types.USER)
          })
          .catch(err => {
            console.log(err.response.data)
            this.commit(types.LOGOUT)
          })
      ))
      .catch(err => {
        console.log(err.response.data)
        this.commit(types.LOGOUT)
      })
    }
  }
};