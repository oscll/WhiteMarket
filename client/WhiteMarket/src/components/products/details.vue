<template>
    <div class="container py-5">
    <div class="row">
        <div class="col-md-6">
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                    <li :class="{'active': index==0}" v-for="(image,index) in product.images" v-bind:key="index" data-target="#carouselExampleIndicators" :data-slide-to="index"></li>
                </ol>
                <div class="carousel-inner">
                    <div :class="{'carousel-item': true, 'active': index==0}" v-for="(image,index) in product.images" v-bind:key="index">
                        <img class="d-block " :src="'http://localhost:8000'+image.image" alt="First slide">
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
        </div>
        <div class="col-md-6 text-left">
            <h4 class="title-product">{{product.title}}</h4>
            <h4 class="d-inline price-product">${{product.price}}</h4><small class="text-muted"><sup>&nbsp;USD</sup></small>
            <br>
            <hr>
            <small>Seller: <span class="text-primary">{{product.owner.email}}</span></small>
            <br>
            <small>Total views: <span class="text-primary">{{product.total_views}}</span></small>
            <br>
            <small>Total likes: <span class="text-primary">{{product.total_likes}}</span></small>
            <br>
            <small>Availability: <span class="text-primary">{{product.stock}} In Stock</span></small>
            <br>
                <div class="">
                    <label for="inputQuantity" class="col-form-label-sm">Quantity: </label>
                    <div class="form-quantity">
                        <div class="minus" role="button" @click=" quantity > 1 ? quantity-- : quantity"></div>
                        <input 
                            type="text" 
                            id="inputQuantity" 
                            style="text-align: center;" 
                            name="quantity" 
                            v-model="quantity" 
                            :class="{'form-control': true, 'form-control-sm': true, 'is-invalid': errors.has('quantity'), 'is-valid': !errors.has('quantity') && fields.quantity && fields.quantity.touched }"
                            v-validate="{ required: true, numeric: true, min_value:1, max_value:product.stock}">
                        <div class="plus" role="button" @click="quantity < product.stock ? quantity++ : quantity "></div>
                    <span v-show="errors.has('quantity')" class="invalid-feedback">{{ errors.first('quantity')}}</span>
                    </div>
                </div>
            <hr>
            <br>
            <form>
                <div
                :class="{'like-product':product.favorited, 'unlike-product':!product.favorited}"
                @click="like()"
                >
                    
                </div>
                <div class="buy-cart">
                    <button class="btn btn-success btn-lg mr-2" type="submit"><i class="fas fa-cart-arrow-down"></i>&nbsp; Add to Cart</button>
                    <button class="btn btn-success btn-lg" type="submit"><i class="far fa-money-bill-alt"></i>&nbsp; Comprar</button>
                </div>
            </form>
        </div>
    </div>
    <div class="row my-4">
        <div class="tab-content" id="productTabContent">
                    <vue-markdown :source=product.description>
                    </vue-markdown>
        </div>
    </div>
    <div class="row map-product">
        <mapleaflet 
            :latitude="product.owner.latitude"
            :longitude="product.owner.longitude">
        </mapleaflet>
    </div>
</div>
</template>

<script>
import { GET_PRODUCT, ADD_FAVORITED } from '@/store/modules/products'
import VueMarkdown from 'vue-markdown' 
import mapleaflet from '@/components/commons/vue-mapleaflet'
export default {
     data(){ 
         return{ 
                product:{},
                quantity:1,
        }
    },
    components:{
        VueMarkdown,
        mapleaflet,
    },
    beforeMount(){
        console.log(this.$route.params.pk)
        this.$store.dispatch(GET_PRODUCT, this.$route.params.pk).then(
            (data) => {
                this.product = data 
            } 
        )
    },
    methods:{
        like(){
            this.$store.dispatch(ADD_FAVORITED, this.product.pk).then(
                (response) => {
                    console.log(response)
                    this.product = response
                },
                (error) => {
                }
            )
        }
    }

}
</script>

<style lang="scss">
.carrousel.slider {
    height: 550px;
    img {
        height: 100%;
        width: auto;
        margin: 0 auto;
    }
}
img.d-block {
    margin: 0 auto;
}
.title-product{
    font-weight: 700;
}
.price-product{
    color: #343a34;
    font-size: 35px;
    font-weight: 700;
    line-height: 20px;
    margin-top: 15px;
}
.form-quantity{
    display: inline-flex;
    width: auto;
    .minus, .plus{
        background: white;
        border: 1px solid #9a9696;
        width: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0 15px;
    }
   .minus::before{
       content: '\f068';
       font-family: FontAwesome;
   } 
   .plus::before{
       content: '\f067';
       font-family: FontAwesome;
   } 
   input{
        max-width: 50px;
        background: #d3d3d3;
        max-height: 26px;
        border: none;
        border-radius: initial;
   }
}
.unlike-product{
    cursor: pointer;
    width: 60px;
    height: 60px;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #d3d3d3;
    margin-right: 5px;
    border-radius: 0.3rem;
    &::before{
        content: '\f004';
        font-family: 'FontAwesome';
        font-size: 30px;
    }
}
.like-product{
    cursor: pointer;
    width: 60px;
    height: 60px;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #d3d3d3;
    margin-right: 5px;
    border-radius: 0.3rem;
    &::before{
        content: '\f004';
        color: red;
        font-family: 'FontAwesome';
        font-size: 30px;
    }
}
.buy-cart{
    width: calc(100% - 65px);
    float: right;
    height: 60px;

    button{
        width: 48%;
        height: 100%;
    }
}
.map-product{
    height: 300px;
}
</style>