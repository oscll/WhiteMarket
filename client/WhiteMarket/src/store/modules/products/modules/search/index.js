/* eslint-disable */
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

export const filterStore = {
  state: {
    search: undefined,
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
