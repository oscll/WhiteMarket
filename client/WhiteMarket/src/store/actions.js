/* eslint-disable */
import * as types from './mutation-types';

export default {
  [types.ERRORS]({ commit },errors) {
    this.commit((types.ERRORS),errors)
    toastr.info("error")
    this.getters.errors.forEach(error => {
      toastr.info(error)
    })
  },
}