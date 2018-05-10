<template>
    <nav class="navbar navbar-dark navbar-expand-md justify-content-between bg-dark" @click="show">
        <div class="container">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".dual-nav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="navbar-collapse collapse dual-nav w-100">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="navbar-brand" href="#">
                            <img src="@/assets/logo-white.svg" width="30" height="30" class="d-inline-block align-top" alt="Logo white Whitemarket">
                            Whitemarket
                        </a>
                    </li>
                </ul>
            </div>
            <form class="form-inline my-2 my-lg-0 align-items-center mx-auto d-block text-center w-100">
                <input class="form-control mr-sm-2" type="text" placeholder="Search">
            </form>
            <div class="navbar-collapse collapse dual-nav w-100">
                <ul class="nav navbar-nav ml-auto">
                    <li class="nav-item"> <auth></auth> </li>
                </ul>
            </div>
        </div>
    </nav>
</template>
<script>
import auth from './components/auth.vue'
export default {
    components:{
        auth
    },
    methods:{
        show(){
            console.log(this)
        }
    }
}
</script>
<style lang="scss" scoped>
.navbar-brand{
    font-family: Gugi, cursive;
}
nav{
    display: block;
}
</style>
