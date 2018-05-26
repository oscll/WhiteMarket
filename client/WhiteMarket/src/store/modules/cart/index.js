/* eslint-disable */
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

export const cartStore = {
  state: {
    cart: JSON.parse(localStorage.getItem('cart')) || [],
  },
  actions,
  getters,
  mutations,
};

export * from './mutation-types';
