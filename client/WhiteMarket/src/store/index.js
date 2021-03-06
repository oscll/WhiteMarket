/* eslint-disable */ 
import Vuex from 'vuex';
import Vue from 'vue';
import actions from './actions';
import getters from './getters';
import mutations from './mutations';

import {authStore} from './modules/auth'
import {productsStore} from './modules/products'
import {cartStore} from './modules/cart'

Vue.use(Vuex);

const state = {
    errors: []
}

export default new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    state,
    mutations,
    actions,
    getters,
    modules: {
        authStore,
        productsStore,
        cartStore,
    },
})