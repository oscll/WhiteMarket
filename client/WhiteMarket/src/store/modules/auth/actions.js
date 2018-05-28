/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'
import { ERRORS } from '@/store/mutation-types';

export default {

  async [types.LOGIN]({ commit },data) {
    return API.post('/auth/jwt/create/',{ email: data[0], password: data[1]})
    .then(response => {
         commit(types.LOGIN, response.data.token)
         this.dispatch(types.USER)
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.REGISTER]({ commit },data) {
    return API.post('/auth/users/create/',{ username: data[0], email: data[1], password: data[2], latitude: data[3], longitude: data[4]})
    .then(() => {
        this.dispatch(types.LOGIN, [data[1], data[2]])
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.UPDATE_USER]({ commit },data) {
    return API.put('/auth/me/',{ username: data[0], email: data[1], latitude: data[2], longitude: data[3]})
    .then(() => {
        this.dispatch(types.USER)
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },
  
  async [types.USER]({ commit }) {
    return API.get('/auth/me/')
    .then(response => (
      commit(types.USER, response.data)
    )).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  [types.LOGOUT]({ commit }) {
    commit(types.LOGOUT);
  },
};