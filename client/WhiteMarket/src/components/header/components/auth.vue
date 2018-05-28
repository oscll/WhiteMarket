<template>
    <div>
        <router-link v-if="token == undefined" to="/login" tag="div">
            <div class="btn btn-primary sing-in">
                Sing in
        </div>
        </router-link>
        <div v-else class="flexy dropdown">
            <div  class="btn sing-in dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                {{username}}
            </div>
            
            <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                <router-link to="/account" tag="div" class="btn sing-in dropdown-item" >
                    Mis datos 
                </router-link>
                <router-link to="/myfavorited" tag="div" class="link-favorited dropdown-item" >
                    Mis favoritos 
                </router-link>
                <router-link to="/myproducts" tag="div" class="link-myproducts dropdown-item" >
                    Mis productos 
                </router-link>
                <router-link to="/product/add" tag="div" class="link-addproduct dropdown-item" >
                    Crear producto
                </router-link>
                <div class="dropdown-item logout" @click="logout()"> Logout</div>
            </div>

        </div>
    </div> 
</template>

<script>
import { LOGOUT } from '@/store/modules/auth'
export default {
  computed: {
    token() {
        return this.$store.getters.token
    },
    username(){
        if(this.$store.getters.user)
            return this.$store.getters.user.username
    }
  },
  methods: {
      logout () {
          this.$store.dispatch(LOGOUT).then(this.$router.push('/'));
      }
  }

}
</script>

<style lang="scss" scoped>
.sing-in{
    cursor: pointer;
    &::before{
        content: '\f2bd';
        font-family: 'FontAwesome';
        
    }
}
.logout{
    cursor: pointer;
    &::before{
        content: '\f08b';
        font-family: 'FontAwesome';
        
    }
}
.link-favorited{
    cursor: pointer;
    &::before{
        content: '\f004';
        font-family: 'FontAwesome';
        
    }
}
.link-myproducts{
    cursor: pointer;
    &::before{
        content: '\f044';
        font-family: 'FontAwesome';
        
    }
}
.link-addproduct{
    cursor: pointer;
    &::before{
        content: '\f067';
        font-family: 'FontAwesome';
        
    }
}
.flexy{
    color: white;
}
</style>
