/* eslint-disable */
import * as types from './mutation-types';

export default {
  [types.LOGIN]({ commit }, token) {
    console.log('login')
    commit(types.LOGIN, token);
  },
  [types.LOGOUT]({ commit }) {
    console.log('logout')
    commit(types.LOGOUT);
  },
};