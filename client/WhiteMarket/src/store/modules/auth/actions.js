/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'
import { ERRORS } from '@/store/mutation-types';

export default {
  async [types.LOGIN]({ commit },data) {
    console.log('login')
    API.post('/auth/jwt/create/',{ email: data[0], password: data[1]})
    .then(response => (
        commit(types.LOGIN, response.data.token)
    )).catch(err => (this.dispatch(ERRORS, err.response.data)))
  },
  [types.LOGOUT]({ commit }) {
    console.log('logout')
    commit(types.LOGOUT);
  },
};