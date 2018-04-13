/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'
import { ERRORS } from '@/store/mutation-types';

export default {
  async [types.GET_PRODUCTS]({ commit },data) {
    console.log('get_products')
    API.get('/products')
    .then(response => (
        commit(types.CHANGE_PRODUCTS, response.data)
    )).catch(err => (this.dispatch(ERRORS, err.response.data)))
  },
/*   [types.LOGOUT]({ commit }) {
    console.log('logout')
    commit(types.LOGOUT);
  }, */
};