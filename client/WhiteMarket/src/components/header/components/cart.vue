<template>
    <div>
        <div v-if="token != undefined" class="flexy dropdown">
            <div  class="btn cart-header dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                {{cart.length}}
            </div>
            <div class="dropdown-menu " aria-labelledby="dropdownMenuLink">
                <div id="cart-dropdown">
                    <ul class="list-group mb-3">
                        <li v-for="entry in cart" :key="entry[0]" class="list-group-item d-flex justify-content-between lh-condensed">
                            <div>
                                <h6 class="my-0">{{entry[1].item.title}}</h6>
                                <small class="text-muted">Cant: {{entry[1].cant}}</small>
                            </div>
                            <span class="text-muted">${{entry[1].price_total}}</span>
                            <div class="btn btn-danger delete-cart" @click="removeToCart(entry[0])">
                            </div>
                        </li>

                        <li class="list-group-item d-flex justify-content-between">
                            <span>Total (USD)</span>
                            <strong>${{total_Price}}</strong>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div> 
</template>

<script>
import { LOGOUT } from '@/store/modules/auth'
import { REMOVE_ITEM_CART } from '@/store/modules/cart'
import {mapState, mapGetters} from 'vuex'
export default {
    computed: {
        ...mapState({
/*             cartArray: state => [...state.cartStore.cart], */
            token: state => state.authStore.token
        }),
        ...mapGetters([
            'cart'
        ]),
        total_Price(){
            let total_Price = 0
            this.cart.forEach(item => {
                total_Price += item[1].price_total
            });
            return total_Price
        }
    },
    methods: {
        logout () {
            this.$store.dispatch(LOGOUT).then(this.$router.push('/'));
        },
        removeToCart(pk){
            this.$store.dispatch(REMOVE_ITEM_CART, pk)
        }
    },

}
</script>

<style lang="scss" scoped>
.cart-header{
    cursor: pointer;
    &::before{
        content: '\f07a';
        font-family: 'FontAwesome';
    }
}
.flexy{
    color: white;
}
.dropdown-menu #cart-dropdown{
    width: 270px
}
.delete-cart{
  padding: 0 10px;
  background: #fff;
  &::before{
    content: "\f1f8";
    font-family: FontAwesome;
    color: black;
    font-size: 20px;
  }
}
</style>
