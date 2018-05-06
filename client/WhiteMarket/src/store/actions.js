/* eslint-disable */
import * as types from './mutation-types';

export default {
  [types.ERRORS]({ commit },errors) {
    this.commit((types.ERRORS),errors)
  },
}