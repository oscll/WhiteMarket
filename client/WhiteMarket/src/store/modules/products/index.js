/* eslint-disable */
import actions from './actions';
import getters from './getters';
import mutations from './mutations';
import {filterStore} from './modules/search'

export const productsStore = {
  state: {
    products: [],
  },
  actions,
  getters,
  mutations,
  modules:{
    filterStore,
  }
};

export * from './mutation-types';
