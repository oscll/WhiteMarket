<template>
<nav class="navbar navbar-dark navbar-expand-md bg-success justify-content-between bg-dark">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".dual-nav">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="navbar-collapse collapse dual-nav w-100">
        <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link pl-0" href="#">WhiteMarket <span class="sr-only">WhiteMarket</span></a>
            </li>
        </ul>
    </div>
    <form class="form-inline my-2 my-lg-0 align-items-center mx-auto d-block text-center w-100">
        <input class="form-control mr-sm-2" type="text" placeholder="Search">
    </form>
    <div class="navbar-collapse collapse dual-nav w-100">
        <ul class="nav navbar-nav ml-auto">
            <li class="nav-item text-white fas fa-sign-out-alt"><a v-on:click="ClickLogout" class="nav-link" href="#"></a></li>
            <li class="nav-item"><a class="nav-link" href="">{{token}}</a></li>
        </ul>
    </div>
</nav>
</template>
<script>
import { LOGOUT } from '@/store/modules/auth'
export default {
  computed: {
    token() {
      return this.$store.getters.token
    }
  },
  methods: {
      ClickLogout () {
          this.$store.dispatch(LOGOUT);
      }
  }
}
</script>
<style>

</style>

