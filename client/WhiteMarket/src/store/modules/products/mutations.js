/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'

export default {
  [types.CHANGE_PRODUCTS](state, response) {
    console.log(response)
    state.products = response.results;
    state.next = response.next;
    state.count = response.count;
  },
  [types.CHANGE_CATEGORIES](state, categories) {
    console.log(categories)
    categories.results.forEach(category => {
      state.categories.push(category.name)
    });
  },
  [types.DELETE_PRODUCTS](state) {
    state.products = []; 
  },
};