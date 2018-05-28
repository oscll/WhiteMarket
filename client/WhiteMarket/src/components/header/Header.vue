<template>
    <nav class="navbar navbar-dark navbar-expand-md justify-content-between bg-dark" @click="show">
        <div class="container">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".dual-nav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <a class="navbar-brand" href="#">
                <router-link to="/products" tag="div"> 
                    <img src="@/assets/logo-white.svg" width="25" height="25" class="d-inline-block align-top" alt="Logo white Whitemarket">
                    Whitemarket
                </router-link>
            </a>
            <div class="navbar-collapse collapse dual-nav w-100">
            <form @submit.prevent="SubmitSearch()" class="form-inline my-2 my-lg-0 align-items-center mx-auto d-block text-center">
                <input class="form-control mr-sm-2" v-model="search" name="search" type="text" placeholder="Search">
            </form>
                <ul class="nav navbar-nav ml-auto  navbar-right">
                    <li class="nav-item"> <cart></cart> </li>
                    <li class="nav-item"> <auth></auth> </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
<script>
import auth from './components/auth.vue'
import cart from './components/cart.vue'
import { GET_PRODUCTS_SEARCH } from '@/store/modules/products'
export default {
    data(){
        return{
            search:''
        }
    },
    components:{
        auth,
        cart,
    },
    methods:{
        show(){
            console.log(this)
        },
        SubmitSearch(){
            this.$store.dispatch(GET_PRODUCTS_SEARCH, this.search)
        }
    }
}
</script>
<style lang="scss" scoped>
.navbar-brand{
    font-family: Gugi, cursive;
}
nav{
    display: block;
}
</style>
