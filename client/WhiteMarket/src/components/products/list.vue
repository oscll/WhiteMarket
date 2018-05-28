<template>
<div >
  <div class="row justify-content-center">
<!--     <div class="col-sm-2">
      <h4 class="mt-5">Categories</h4>
      <div v-for="category in categories" :key="category" class="custom-control custom-checkbox">
        <input @change="categories(category)" type="checkbox" :value="category" class="custom-control-input" :id="category">
        <label class="custom-control-label" :for="category">{{category}}</label>
      </div>
    </div> -->
    <div class="col-sm-10 flexy" v-if="!(products == 0)">
        <div class="card-deck justify-content-center">
            <div class="card mt-5" v-for="product in products" v-bind:key="product.pk">
              <div class="contain-img">
                <img class="card-img-top" :src="'http://localhost:8000'+product.images[0].thumbnail" width="250px" height="250px" alt="Card image cap">
                <span v-if="product.favorited" class="like" @click="like(product.pk)"></span>
                <span v-else class="unlike" @click="like(product.pk)">{{product.total_likes}}</span>
                <span class="views">{{product.total_views}}</span>
              </div>
              <div class="card-body">
              <h5 class="card-title">{{product.title}}</h5>
              <h5 class="card-title">{{product.price}}$</h5>
              <div v-if="edit" class="btn btn-danger delete-list" @click="remove(product.pk)">
              </div>
              <router-link v-if="edit" :to='"/product/edit/"+product.pk' tag="div" class="btn btn-primary" >
                Modificar 
              </router-link>

              <router-link v-else :to='"/products/detail/"+product.pk' tag="div" class="btn btn-primary" >
                Ver mas 
              </router-link>
              <p class="card-text"><small class="text-muted">{{date(product.created)}}</small></p>
              </div>
            </div>
        </div>
    </div>
    <div class="col-sm-10" v-if="products == 0">
      We couldn’t find any repositories matching
    </div>
  </div>
  <button v-if="next" class="btn btn-primary my-5" @click="nextProducts()"> NEXT_PAGE </button>
</div>
</template>

<script>
import { GET_PRODUCTS, ADD_FAVORITED, GET_PRODUCTS_FAVORITED, GET_MYPRODUCTS, REMOVE_PRODUCT, NEXT_PAGE } from '@/store/modules/products'
import {mapGetters} from 'vuex'
export default {
  data(){
    return{
      edit:false,
    }
  },
  computed: {
      ...mapGetters([
        'products',
        'token',
        'next',
        'categories',
      ])
  },
  methods: {
    date(date){
      let diference = new Date() - new Date(date)

      switch (true) {
        case (diference/1000) > 0 && (diference/1000) < 60  :
            return `Hace ${Math.round(diference/1000)} segundos.`
          break;
        case ((diference/1000)/60) > 0 && ((diference/1000)/60) < 60  :
            return `Hace ${Math.round((diference/1000)/60)} minutes.`
          break;
        case (((diference/1000)/60)/60) > 0 && (((diference/1000)/60)/60) < 60  :
            return `Hace ${Math.round(((diference/1000)/60)/60)} hours.`
          break;
        case ((((diference/1000)/60)/60)/24) > 0 && ((((diference/1000)/60)/60)/24) < 7  :
            return `Hace ${Math.round((((diference/1000)/60)/60)/24)} days.`
          break;
        case (((((diference/1000)/60)/60)/24)/7) > 0 && (((((diference/1000)/60)/60)/24)/7) < 13  :
            return `Hace ${Math.round(((((diference/1000)/60)/60)/24)/7)} weeks.`
          break;

        default:
            return `Hace mucho tiempo ${date.getFullYear}-${date.getMonth}-${date.getDate}`
          break;
      }

      return date; 
    },
    nextProducts(){
      this.$store.dispatch(NEXT_PAGE)
    },
    like(pk){
      this.$store.dispatch(ADD_FAVORITED, pk).then(
          () => {
          },
          (error) => {
          }
      )
    },
    remove(pk){
      this.$store.dispatch(REMOVE_PRODUCT, pk).then(
          () => {
            toastr.error("Product removed","Product")
          },
          (error) => {
          }
      )
    },
    getProducts(){
      switch (this.$route.name) {
        case 'products-list':
          this.$store.dispatch(GET_PRODUCTS)
          this.edit = false
          break;
        case 'myproducts-list':
          console.log('my products')
          this.$store.dispatch(GET_MYPRODUCTS)
          this.edit = true
          break;
        case 'favorited-list':
          console.log('my favorited list')
          this.$store.dispatch(GET_PRODUCTS_FAVORITED)
          this.edit = false
          break;
        default:
          this.$store.dispatch(GET_PRODUCTS)
          this.edit = false
          break;
      }
    }
  },
  beforeMount: function(){
    console.log(this.$route)
    this.getProducts()
  },
  watch:{
    token: function(){
      this.getProducts()
    },
    $route: function(){
      this.getProducts()
    },
    products: function(){
      console.log(this.products)
    }
  }
};
</script>

<style lang="scss" scoped>
.card{ 
  width: 250px !important;
}
.card-body{
  flex: initial;
}
@media (min-width:34em) {
    .card-deck > .card
    {
        width: 10%;
        flex-wrap: wrap;
        flex: initial; 
        justify-content: center
    }
}
.unlike{
    cursor: pointer;
    position: absolute;
    right: 5px;
    top: 5px;
    padding: 4px;
    font-size: 13px;
    background-color: white;
    -webkit-border-radius: 50px;
    -moz-border-radius: 50px;
    border-radius: 50px;
    &::before{
        content: '\f004';
        font-family: 'FontAwesome';
        -webkit-border-radius: 50px;
        -moz-border-radius: 50px;
        border-radius: 50px;
        padding: 4px;
        background-color: white;
    }
}
.like{
    cursor: pointer;
    position: absolute;
    right: 5px;
    top: 5px;
    &::before{
        content: '\f004';
        color: red;
        font-family: 'FontAwesome';
        -webkit-border-radius: 50px;
        -moz-border-radius: 50px;
        border-radius: 50px;
        padding: 4px;
        background-color: white;
    }
}
.views{
    position: absolute;
    left: 5px;
    top: 5px;
    padding: 4px;
    font-size: 13px;
    background-color: white;
    -webkit-border-radius: 50px;
    -moz-border-radius: 50px;
    border-radius: 50px;
    &::before{
        content: '\f06e';
        font-family: 'FontAwesome';
        padding-right:4px; 
    }
}
.delete-list{
  padding: 0 10px;
  &::before{
    content: "\f1f8";
    font-family: FontAwesome;
    color: black;
    font-size: 25px;
  }
}
</style>
