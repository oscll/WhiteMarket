/* eslint-disable */
import * as types from './mutation-types';
import { API } from '@/utils/api'
import { ERRORS } from '@/store/mutation-types';

export default {

  async [types.GET_PRODUCTS]({ commit },data) {
    API.get('/products/')
    .then(response => {
       commit(types.CHANGE_PRODUCTS, response.data)
       this.dispatch(types.GET_CATEGORIES);
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.GET_CATEGORIES]({ commit }) {
    API.get('/categories/')
    .then(response => {
      console.log(response)
       commit(types.CHANGE_CATEGORIES, response.data)
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.CHANGE_PRODUCTS]({ commit },data) {
       commit(types.CHANGE_PRODUCTS, data)
  },

  async [types.CREATE_PRODUCT]({ commit },data) {
    return API.post('/products/',data)
    .then(response => {
      return true
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },
  
  async [types.UPDATE_PRODUCT]({ commit },data) {
    return API.put(`/products/${data.pk}`,data)
    .then(response => {
      return true
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.REMOVE_PRODUCT]({ commit },data) {
    return API.delete(`/products/${data}`)
    .then(response => {
      this.dispatch(types.GET_MYPRODUCTS);
      return true
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },
  
  async [types.ADD_FAVORITED]({ commit },data) {
    return API.get(`/products/like/${data}`) .then(response => {
      console.log(response)
      commit(types.UPDATE_PRODUCT,response.data)
      return response.data
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.GET_PRODUCT]({ commit },data) {
    return API.get(`/products/${data}`)
    .then(response => {
      return response.data
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.GET_PRODUCTS_FAVORITED]({ commit },data) {
    API.get('/products/liked/')
    .then(response => {
       commit(types.CHANGE_PRODUCTS, response.data)
       this.dispatch(types.GET_CATEGORIES);
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.GET_PRODUCTS_FAVORITED]({ commit },data) {
    API.get('/products/liked/')
    .then(response => {
       commit(types.CHANGE_PRODUCTS, response.data)
       this.dispatch(types.GET_CATEGORIES);
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },

  async [types.GET_MYPRODUCTS]({ commit },data) {
    API.get(`/products/?owner=${JSON.parse(localStorage.getItem('user')).id}`)
    .then(response => {
       commit(types.CHANGE_PRODUCTS, response.data)
       this.dispatch(types.GET_CATEGORIES);
    }).catch(err => { 
      err.response ? this.dispatch(ERRORS, err.response.data) : ""
      reject(err)
    })
  },
/* 
  async [types.GET_PRODUCTS]({ commit },data) {
    API.get('/products')
    .then(response => (
       commit(types.CHANGE_PRODUCTS, response.data)
    )).catch(err => (this.dispatch(ERRORS, err.response.data)))
  },

  async [types.GET_PRODUCTS]({ commit },data) {
    API.get('/products')
    .then(response => (
       commit(types.CHANGE_PRODUCTS, response.data)
    )).catch(err => (this.dispatch(ERRORS, err.response.data)))
  }, */
};