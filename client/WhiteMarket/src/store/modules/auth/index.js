/* eslint-disable */
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

export const authStore = {
  state: {
    token: undefined,
    user: undefined,
  },
  actions,
  getters,
  mutations,
};

export * from './mutation-types';
