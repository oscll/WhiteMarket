<template>
<div class="login">
<div class="container">
    <div class="row">
        <div @click="goHome" class="col-sm-12 login-head">
            <img src="@/assets/logo.svg" width="90" height="90" class="d-inline-block align-top" alt="">
            <h3 class="mb-0">Whitemarket</h3>
        </div>
        <div class="col-sm-12">
            <div class="card card-container mt20 card-login">
                <img id="profile-img" class="profile-img-card" ng-src="https://d3ginfw2u4xn7p.cloudfront.net/f7c4c82/images/avatar.png" src="https://d3ginfw2u4xn7p.cloudfront.net/f7c4c82/images/avatar.png">
                <p id="profile-name" class="profile-name-card"></p>
                <form class="form-login" autocomplete="off" @submit.prevent="Submit(email, password)">
                    <div class="form-group">
                        <input  type="email" 
                                :class="{'form-control': true, 'is-invalid': errors.has('email'), 'is-valid': !errors.has('email') && fields.email && fields.email.touched }"
                                name="email" 
                                placeholder="Email"
                                v-model="email"
                                v-validate="'required|email'" >
                            <span v-show="errors.has('email')" class="invalid-feedback">{{ errors.first('email')}}</span>
                    </div>
                    <div class="form-group">
                        <input  type="password" 
                                :class="{'form-control': true, 'is-invalid': errors.has('password'), 'is-valid': !errors.has('password') && fields.password && fields.password.touched }"
                                placeholder="Password"
                                name="password"
                                v-model="password"
                                v-validate="'required|alpha_num|min:8'" >
                            <span v-show="errors.has('password')" class="invalid-feedback">{{ errors.first('password') }}</span>
                    </div>
                    <button type="submit" class="btn btn-primary btn-lg button-login">Login</button>
                    <a href="#" class="forgot-password">
                        Forgotten your password?
                    </a>
                </form>
                <div>
                    <hr>
                    <div class="text-center">
                        <router-link to="/register">
                            Create account
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
</template>

<script>
import { LOGIN, LOGOUT } from '@/store/modules/auth'
export default {
    data(){
        return{
            email:null,
            password:null,
            validated:false,
        }
    },
    methods: {
        Submit(email, password) {
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.$store.dispatch(LOGIN, [email, password]).then(
                        () => {
                            this.$router.push('/')
                        },
                        (error) => {
                        }
                    )
                return;
                }
            });
            
        },
        goHome() {
            this.$router.push('/')
        }
    },

}
</script>

<style lang="scss" >
.form-login{
    max-width: 330px;
    padding: 0;
    margin: 0 auto;
}
.profile-img-card{
    width: 96px;
    height: 96px;
    margin: 0 auto 10px;
    display: block;
    border-radius: 50%;
    vertical-align: middle;
}
.card-login {
    max-width: 350px;
    padding: 40px;
    background-color: #f7f7f7;
    padding: 20px 25px 30px;
    margin: 0 auto 25px;
    margin-top: 50px;
    border-radius: 4px;
    box-shadow: 0 2px 2px rgba(0,0,0,.3);
}
.login-head{
    font-family: Gugi, cursive;
    font-size: 3rem;
    color: black;
    cursor: pointer;
    margin-top: 3rem;
}
.button-login{
    width: 100%;
    display: block;
    margin-bottom: 10px;
    z-index: 1;
    box-sizing: border-box;
}
.forgot-password{
    font-size: 12px;
    text-align: left;
    display: flex;
    justify-content: flex-start;
}
</style>

