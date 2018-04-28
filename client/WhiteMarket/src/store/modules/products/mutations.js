/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'

export default {
  [types.CHANGE_PRODUCTS](state, products) {
    console.log(products)
    state.products = products;
    localStorage.setItem('products',products);
  },
  [types.DELETE_PRODUCTS](state) {
    state.products = []; 
    localStorage.removeItem('products');
  },
};