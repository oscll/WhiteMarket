<template>
<div >
  <div class="row">
    <div class="col-sm-2">
      <div class="custom-control custom-checkbox">
        <input type="checkbox" class="custom-control-input" id="customCheck1">
        <label class="custom-control-label" for="customCheck1">Boots</label>
      </div>
    </div>
    <div class="col-sm-10 flexy" v-if="!(products == 0)">
        <div class="card-deck">
            <div class="card mt-5" v-for="product in products" v-bind:key="product.pk">
                <img class="card-img-top" :src="product.img" alt="Card image cap">
                <div class="card-body">
                <h5 class="card-title">{{product.title}}</h5>
                <p class="card-text"><small class="text-muted">{{date(product.created)}}</small></p>
                </div>
            </div>
        </div>
    </div>
    <div class="col-sm-10" v-if="products == 0">
      We couldn’t find any repositories matching
    </div>
  </div>
</div>
</template>

<script>
import { GET_PRODUCTS, } from '@/store/modules/products'
export default {

  computed: {
    products() {
      return this.$store.getters.products
    }
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
    }
  },
  beforeCreate: function(){
    this.$store.dispatch(GET_PRODUCTS)
  }
};
</script>

<style lang="scss" scoped>
.card{ 
  width: 250px !important;
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
</style>
