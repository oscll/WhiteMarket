/* eslint-disable */
import * as types from './mutation-types';

export default {
  [types.ERRORS](state, errors) {
    console.log(errors)
    state.errors.push(errors);
  },
}