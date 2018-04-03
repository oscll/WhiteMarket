<template>
    <div>
       <h1 class="my-2">Ultimas unidades en tu Zona</h1> 
        <div class="card-columns my-2" >
            <product-view v-for="n in [1,2,3,4,5,6,7,8,9]" :key="n"></product-view>
        </div>
    </div>
</template>

<script>


import ProductView from '@/components/ProductView';
export default {

    components:{
        ProductView
    }
}
</script>

<style>

</style>
