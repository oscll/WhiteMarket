/* eslint-disable */
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

export const productsStore = {
  state: {
    count:0,
    next:undefined,
    products: [],
    latitude: undefined,
    longitude: undefined,
    categories: [],
    ordering: undefined,
    distance: 100,
    categories_selected: {},
  },
  actions,
  getters,
  mutations,
};

export * from './mutation-types';
