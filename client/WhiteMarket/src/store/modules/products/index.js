/* eslint-disable */
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

export const productsStore = {
  state: {
    products: [],
  },
  actions,
  getters,
  mutations,
};

export * from './mutation-types';
