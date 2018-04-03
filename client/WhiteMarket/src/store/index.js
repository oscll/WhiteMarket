/* eslint-disable */ 
import Vuex from 'vuex';
import Vue from 'vue';
import {authStore} from './modules/auth'

Vue.use(Vuex);

const state = {
    products: []
}

export default new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    state,
    modules: {
        authStore,
    },
})