<template>
<div class="container h-100">
    <div class="row">
         <div class="col-md-10 offset-md-1">
            <hr class="my-5">
            <h3>Create Product</h3>
            
            <!-- form complex input -->
            <form class="form-row mt-4">
                <div class="col-sm-12 pb-3">
                    <label for="productTitle">Title</label>
                    <input type="text" class="form-control" id="productTitle" placeholder="WhiteMarket Product !!!" v-model="title">
                </div>
                <div class="col-sm-12 pb-3">
                    <label for="productAmount">Amount</label>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                        <input type="decimal" class="form-control" id="productAmount" placeholder="616.11" v-model="amount">
                    </div>
                </div>
                <div class="col-sm-12 pb-3">
                    <label for="inputZip">Stock</label>
                    <input type="number" class="form-control" id="inputStock" v-model="stock">
                </div>
                <div class="col-sm-12 pb-3">
                    <label for="inputSt">State</label>
                    <select class="form-control" id="inputState" v-model="state">
                        <option selected value="none">Choose a state</option>
                        <option value="new">New</option>
                        <option value="reconditioned">Reconditioned</option>
                        <option value="used">Used</option>
                        <option value="broken">Broken</option>
                    </select>
                </div>
                <div class="col-sm-12 pb-3">
                    <label for="inputSt">Category</label>
                    <select class="form-control" id="inputCategory" v-model="category">
                        <option selected value="none">Choose a category</option>
                        <option v-for="(category, index) in categories()" :key="index" :value=category >{{category}}</option>
                    </select>
                </div>
                <div class="col-sm-12 pb-3">
                    <vueUploaderImage @img0="active($event)"></vueUploaderImage>
                </div>
                <div class="col-md-12 pb-3">
                    <ul class="nav nav-tabs" id="myTab" role="tablist">
                        <li class="nav-item">
                            <a class="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Text</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile" aria-selected="false">Markdown</a>
                        </li>
                    </ul>
                    <div class="tab-content" id="myTabContent">
                        <div class="tab-pane fade show active tabs-border" id="home" role="tabpanel" aria-labelledby="home-tab">
                            <textarea class="form-control" id="inputDescription" v-model="description"></textarea>
                        </div>
                        <div class="tab-pane fade tabs-border" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                            <vue-markdown :source=description>
                            </vue-markdown>
                        </div>
                    </div>
                </div>
                <button type="submit" class="btn btn-primary btn-lg col-sm-12 mb-3">Create</button>
            </form>
        </div>
    </div>
</div>
</template>

<script>
import vueUploaderImage from '@/components/products/components/vue-slider-upload'
import VueMarkdown from 'vue-markdown'
export default {
    data(){
        return{
            title:null,
            amount:null,
            stock:1,
            description:"# Description",
            state:"none",
            category:"none",
            img:{},
        }
    },
    components:{
        vueUploaderImage,
        VueMarkdown,
    },
    methods:{
        categories(){
            return this.$store.getters.categories
        },
        active($event){
            console.log($event)
        }
    },
} 
</script>

<style lang="scss" scoped>
.tabs-border, #inputDescription {
    border: 1px solid #ddd;
    min-height: 350px;
}
.nav-tabs{
    border: initial;
}
textarea.form-control{
    border: initial !important;
    height: 100%;
}

</style>
