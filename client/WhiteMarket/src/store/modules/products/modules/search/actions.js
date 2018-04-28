/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'
import { ERRORS } from '@/store/mutation-types';

export default {
  async [types.GET_SEARCH]({ commit }) {
    debugger
    API.get('/products')
    .then(response => (
       this.commit(types.PRODUCTS.CHANGE_PRODUCTS, ))
    .catch(err => {
      console.log(err)
      this.dispatch(ERRORS, err.response.data)
      err.response ? this.dispatch(ERRORS, err.response.data) : ""

    }))
  },
};