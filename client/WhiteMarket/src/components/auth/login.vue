<template>
<div class="container h-100">
    <div class="row">
        <div class="my-5 col-md-6 offset-md-3">
            <div class="card card-outline-secondary">
                <div class="card-header">
                    <h3 class="mb-0">Login</h3>
                </div>
                <div class="card-body">
                    <form class="form" role="form" autocomplete="off" v-on:submit.prevent="Submit(email, password)">
                        <div class="form-group">
                            <label for="uname1">Username</label>
                            <input  type="text" 
                                    class="form-control" 
                                    name="uname1" 
                                    id="uname1" 
                                    v-model="email">
                            <div class="invalid-feedback">Please enter your username or email</div>
                        </div>
                        <div class="form-group">
                            <label>Password</label>
                            <input  type="password" 
                                    class="form-control" 
                                    id="pwd1" 
                                    v-model="password">
                            <div class="invalid-feedback">Please enter a password</div>
                        </div>
                        <div class="form-check small">
                            <label class="form-check-label">
                                <input type="checkbox" class="form-check-input"> <span>Remember me on this computer</span>
                            </label>
                        </div>
                        <button type="submit" class="btn btn-success btn-lg float-right" id="btnLogin">Login</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { API } from '@/utils/api'
import { LOGIN, LOGOUT } from '@/store/modules/auth'
import Axios from 'axios'
export default {
    data(){
        return{
            email:null,
            password:null
        }
    },
    methods: {
        Submit (email, password) {
            console.log(email)
            console.log(password)
            this.$store.dispatch(LOGIN, [email, password])
        },
        ClickMe () {
            API.get('/auth/me/').then(response => (console.log(response.data)))
        },
        ClickLogout () {
            this.$store.dispatch(LOGOUT);
        }
    }

}
</script>

<style>

</style>
