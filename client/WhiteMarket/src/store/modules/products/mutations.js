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
    state.categories = [] 
    categories.results.forEach(category => {
      state.categories.push(category.name)
    });
  },
/*   [types.DELETE_PRODUCTS](state) {
    state.products = []; 
  }, */
  [types.UPDATE_PRODUCT](state, response) {
    for (var i = 0, len = state.products.length; i < len; i++) {
      if(state.products[i].pk == response.pk){
        state.products[i].favorited = !state.products[i].favorited
        state.products[i].total_likes = response.total_likes
        break
      } 
    }
  },
};