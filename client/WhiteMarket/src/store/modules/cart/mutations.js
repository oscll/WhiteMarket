/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'

export default {
  [types.ADD_ITEM_CART](state, response) {
    console.log('mutation')
    let cart = new Map(state.cart)
    cart.set(response.pk,response)
    state.cart = [...cart]
    localStorage.setItem('cart',JSON.stringify(state.cart))
  },
  [types.REMOVE_ITEM_CART](state, pk) {
    let cart = new Map(state.cart)
    cart.delete(pk) 
    state.cart = [...cart]
    localStorage.setItem('cart',JSON.stringify(state.cart))
  },
};