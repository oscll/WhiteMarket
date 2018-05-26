/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'
import { ERRORS } from '@/store/mutation-types';

export default {

  [types.ADD_ITEM_CART]({ commit },data) {
    console.log('action')
    commit(types.ADD_ITEM_CART,data)
  },

  [types.REMOVE_ITEM_CART]({ commit },data) {
    commit(types.REMOVE_ITEM_CART,data)
  },

};