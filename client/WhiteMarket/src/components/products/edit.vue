<template>
<div class="container h-100">
    <div class="row">
         <div class="col-md-10 offset-md-1">
            <hr class="my-5">
            <h3>Create Product</h3>
            
            <!-- form complex input -->
            <form class="form-row mt-4" @submit.prevent="Submit()">
                <div class="col-sm-12 pb-3">
                    <label for="productTitle">Title</label>
                    <input type="text" 
                        name="title" 
                        id="productTitle" 
                        :class="{'form-control': true, 'is-invalid': errors.has('title'), 'is-valid': !errors.has('title') && fields.title && fields.title.touched }"
                        placeholder="WhiteMarket Product !!!" 
                        v-model="title"
                        v-validate="'required|alpha_num|max:50|min:3'" >
                    <span v-show="errors.has('title')" class="invalid-feedback">{{ errors.first('title')}}</span>
                </div>
                <div class="col-sm-12 pb-3">
                    <label for="productAmount">Amount</label>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                        <input type="decimal" 
                            id="productAmount" 
                            placeholder="616.11" 
                            name="amount"
                            :class="{'form-control': true, 'is-invalid': errors.has('amount'), 'is-valid': !errors.has('amount') && fields.amount && fields.amount.touched }"
                            v-validate="'required|numeric|min_value:3'" 
                            v-model="amount">
                    <span v-show="errors.has('amount')" class="invalid-feedback">{{ errors.first('amount')}}</span>
                    </div>
                </div>
                <div class="col-sm-12 pb-3">
                    <label for="inputZip">Stock</label>
                    <input type="number" 
                        class="form-control" 
                        id="inputStock" 
                        name="stock"
                        :class="{'form-control': true, 'is-invalid': errors.has('stock'), 'is-valid': !errors.has('stock') && fields.stock && fields.stock.touched }"
                        v-validate="'required|numeric|min_value:1'" 
                        v-model="stock">
                    <span v-show="errors.has('stock')" class="invalid-feedback">{{ errors.first('stock')}}</span>
                </div>
                <div class="col-sm-12 pb-3">
                    <label for="inputSt">State</label>
                    <select name="state"
                        :class="{'form-control': true, 'is-invalid': errors.has('state'), 'is-valid': !errors.has('state') && fields.state && fields.state.touched }"
                        v-validate="'required|in:0,1,2,3'" 
                        id="inputState" v-model="state">
                        <option selected value="616000">Choose a state</option>
                        <option value="0">New</option>
                        <option value="1">Reconditioned</option>
                        <option value="2">Used</option>
                        <option value="3">Broken</option>
                    </select>
                    <span v-show="errors.has('state')" class="invalid-feedback">{{ errors.first('state')}}</span>
                </div>
                <div class="col-sm-12 pb-3">
                    <label for="inputSt">Category</label>
                    <select name="category" 
                        :class="{'form-control': true, 'is-invalid': errors.has('category'), 'is-valid': !errors.has('category') && fields.category && fields.category.touched }"
                        v-validate="'required|not_in:616000'" 
                        id="inputCategory" 
                        v-model="category">
                        <option selected value="616000">Choose a category</option>
                        <option v-for="(category, index) in categories()" :key="index" :value=category >{{category}}</option>
                    </select>
                    <span v-show="errors.has('category')" class="invalid-feedback">{{ errors.first('category')}}</span>
                </div>
                <div class="col-sm-12 pb-3">
                    <vueUploaderImage v-on="$listeners" 
                    @img0="img.img0=$event"
                    @img1="img.img1=$event"
                    @img2="img.img2=$event"
                    @img3="img.img3=$event"
                    @img4="img.img4=$event"
                    @img5="img.img5=$event"
                    @img6="img.img6=$event"
                    ></vueUploaderImage>
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
                            <textarea name="description" 
                                class="form-control" 
                                id="inputDescription" 
                                :class="{'form-control': true, 'is-invalid': errors.has('description'), 'is-valid': !errors.has('description') && fields.description && fields.description.touched }"
                                v-validate="'required|min:10|max:10000'" 
                                v-model="description"></textarea>
                            <span v-show="errors.has('description')" class="invalid-feedback">{{ errors.first('description')}}</span>
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
            state:616000,
            category:616000,
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
        Submit(){
            console.log(this.img)
            console.log(this.title)
            console.log(this.description)
            console.log(this.img)
            console.log(this.img)
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
