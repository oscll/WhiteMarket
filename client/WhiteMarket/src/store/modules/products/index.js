/* eslint-disable */
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

export const productsStore = {
  state: {
    products: [],
    categories: [],
    latitude: undefined,
    longitude: undefined,
    categories: [],
    ordering: undefined,
  },
  actions,
  getters,
  mutations,
};

export * from './mutation-types';
