/* eslint-disable */
import * as types from './mutation-types';

export default {
  [types.ERRORS](state, errors) {
    state.errors.push(errors);
    switch (typeof errors) {
      case 'string':
        toastr.error(errors,'Error upload image');
        break;
      case 'object':
        for(let key in errors) {
            if(errors.hasOwnProperty(key)) {
                toastr.error(errors[key],key);
            }
        }
        break;
    
      default:
        break;
    }
  },
}