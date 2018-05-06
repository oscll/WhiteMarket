/* eslint-disable */
import actions from './actions';
import getters from './getters';
import mutations from './mutations';
import {filterStore} from './modules/search'

export const productsStore = {
  state: {
    products: [],
    latitude: undefined,
    longitude: undefined,
    categories: [],
    ordering: undefined,
  },
  actions,
  getters,
  mutations,
  modules:{
    filterStore,
  }
};

export * from './mutation-types';
