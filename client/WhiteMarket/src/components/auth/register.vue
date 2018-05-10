<template>
    <div class="container">
        <form class="row my-5" @submit.prevent="Submit()" role="form">
            <div class="col-sm-4 my-2 col-xs-12">
                <router-link tag="div" role="button" class="mb-5 w-100" to="/">
                    <img src="@/assets/logo.svg" width="90" height="90" class="d-inline-block align-top" alt="">
                    <h3 class="mb-0">{{title}} Account</h3>
                </router-link>
                <div class="w-100 mb-5">
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text input-user"></span></div>
                        <input type="text" class="form-control" required id="username" placeholder="Username" v-model="username">
                    </div>
                </div>
                <div class="w-100 mb-5">
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text input-email"></span></div>
                        <input type="email" class="form-control" required id="email" :disabled="this.edit" placeholder="Email" v-model="email">
                    </div>
                </div>
                <div class="w-100 mb-5">
                    <div class="input-group" v-if="!this.edit">
                        <div class="input-group-prepend"><span class="input-group-text input-lock"></span></div>
                        <input type="password" class="form-control" required id="password" placeholder="Password" v-model="password" >
                    </div>
                    <div v-else>
                        <changepassword></changepassword>
                    </div>
                </div>

                <div class="w-100">
            <button type="submit" class="btn btn-primary btn-lg mb-0 form-button">{{title}}</button>
                </div>
            </div>
            <div class="col-sm-8 col-xs-12 my-2 pb-3" >
                <mapleaflet clickLatLong="true" 
                    @location="latitude = $event.lat; longitude = $event.lng"
                    :latitude="latitude"
                    :longitude="longitude"></mapleaflet>
                <input type="hidden" required id="latitude" v-model="latitude" > 
                <input type="hidden" required id="longitude" v-model="longitude" > 
            </div>
        </form>
    </div>
</template>
<script>
import { REGISTER, UPDATE_USER } from '@/store/modules/auth'
import mapleaflet from '@/components/commons/vue-mapleaflet'
import changepassword from '@/components/auth/components/vue-change-password'
import {mapGetters} from 'vuex'
export default {
    components:{
        mapleaflet,
        changepassword,
    },
    computed: {
      ...mapGetters([
        'user',
      ])
    },
    data(){
        return{
            map: null,
            email:null,
            password:'undefined',
            username:null,
            latitude:38,
            longitude:-0.2,
            edit: false,
            title: "Create",
        }
    },
    methods:{
        Submit() {
            if(this.edit){
                this.$store.dispatch(UPDATE_USER, [this.username, this.email, this.latitude, this.longitude])
                .then(
                    () => {
                        this.$router.push('/')
                    },
                    (error) => {
                    }
                )
            }else{
                this.$store.dispatch(REGISTER, [this.username, this.email, this.password, this.latitude, this.longitude])
                .then(
                    () => {
                        this.$router.push('/')
                    },
                    (error) => {
                    }
                )
            }
        },
        loadUser(){
            if(this.user){
                this.email = this.user.email
                this.username = this.user.username
                this.latitude = this.user.latitude
                this.longitude = this.user.longitude
                this.title = "Update"
                this.edit = true
            }
        },
    },
    created(){
        this.loadUser()
    },
    watch:{
        user:function(){
            this.loadUser()
        } 
    }

}
</script>

<style lang="scss" scoped>
#map{
   min-height: 505px;
}
form{
    & > div{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .input-user{
        &::before{
            content: '\f007';
            font-family: 'FontAwesome';
        }
    }
    .input-email{
        &::before{
            content: '\f0e0';
            font-family: 'FontAwesome';
        }
    }
    .input-lock{
        &::before{
            content: '\f13e';
            font-family: 'FontAwesome';
        }
    }
}
</style>
