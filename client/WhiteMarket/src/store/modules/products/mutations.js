/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'

export default {
  [types.CHANGE_PRODUCTS](state, products) {
    console.log(products)
    state.products = products;
    localStorage.setItem('products',JSON.stringify(products));
  },
  [types.CHANGE_CATEGORIES](state, categories) {
    console.log(categories)
    categories.forEach(category => {
      state.categories.push(category.name)
    });
    localStorage.setItem('categories',JSON.stringify(state.categories));
  },
  [types.DELETE_PRODUCTS](state) {
    state.products = []; 
    localStorage.removeItem('products');
  },
};