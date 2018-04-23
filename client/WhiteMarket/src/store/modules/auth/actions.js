/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'
import { ERRORS } from '@/store/mutation-types';

export default {

  async [types.LOGIN]({ commit },data) {
    API.post('/auth/jwt/create/',{ email: data[0], password: data[1]})
    .then(response => {
         commit(types.LOGIN, response.data.token)
         this.dispatch(types.USER)
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
    })
  },

  async [types.REGISTER]({ commit },data) {
    API.post('/auth/users/create/',{ username: data[0], email: data[1], password: data[2], latitude: data[3], longitude: data[4]})
    .then(() => {
        this.dispatch(types.LOGIN, [data[1], data[2]])
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
    })
  },

  async [types.USER]({ commit }) {
    API.get('/auth/me')
    .then(response => (
      commit(types.USER, response.data)
    )).catch(err => (this.dispatch(ERRORS, err.response.data)))
  },

  [types.LOGOUT]({ commit }) {
    commit(types.LOGOUT);
  },
};