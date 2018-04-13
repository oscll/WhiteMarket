<template>
<div class="container h-100">
    <div class="row">
        <div class="card-deck">
            <div class="card my-5" v-for="product in products" v-bind:key="product.pk">
                <img class="card-img-top" :src="product.img" alt="Card image cap">
                <div class="card-body">
                <h5 class="card-title">{{product.title}}</h5>
                <p class="card-text">{{product.description}}</p>
                <p class="card-text"><small class="text-muted">{{product.created}}<!-- Last updated 3 mins ago --></small></p>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import Axios from "axios";
import { GET_PRODUCTS, } from '@/store/modules/products'
export default {
/*   data() {
    return {
      email: null,
      password: null
    };
  },
  methods: {
    Submit(email, password) {
      console.log(email);
      console.log(password);
      this.$store.dispatch(LOGIN, [email, password]);
    },
    ClickMe() {
      API.get("/auth/me/").then(response => console.log(response.data));
    },
    ClickLogout() {
      this.$store.dispatch(LOGOUT);
    }
  } */
  computed: {
    products() {
      return this.$store.getters.products
    }
  },
  beforeCreate: function(){
    this.$store.dispatch(GET_PRODUCTS)
  }
};
</script>

<style>

</style>
