/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'

export default {
  [types.SET_CATEGORIES](state, categories) {
    state.categories = categories;
    localStorage.setItem('filter/categories',categories);
  },
  [types.SET_ORDERING](state, ordering) {
    state.ordering = ordering;
    localStorage.setItem('filter/ordering',products);
  },
  [types.CHANGE_PRODUCTS](state, products) {
    console.log(products)
    state.products = products;
    localStorage.setItem('products',products);
  },
  [types.CHANGE_PRODUCTS](state, products) {
    console.log(products)
    state.products = products;
    localStorage.setItem('products',products);
  },
  [types.CHANGE_PRODUCTS](state, products) {
    console.log(products)
    state.products = products;
    localStorage.setItem('products',products);
  },
  [types.CHANGE_PRODUCTS](state, products) {
    console.log(products)
    state.products = products;
    localStorage.setItem('products',products);
  },
};