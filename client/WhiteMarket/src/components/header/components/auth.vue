<template>
    <div>
        <router-link v-if="token == undefined" to="/login" tag="div">
            <div class="btn btn-primary sing-in">
                Sing in
        </div>
        </router-link>
        <div v-else class="flexy">
            <div class="btn sing-in">
                {{username}}
            </div>
            <div class="logout" @click="logout()">
                
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
          this.$store.dispatch(LOGOUT);
      }
  }

}
</script>

<style lang="scss" scoped>
.sing-in{
    &::before{
        content: '\f2bd';
        font-family: 'FontAwesome';
        
    }
/*     text-transform: capitalize; */
}
.logout{
    &::before{
        content: '\f08b';
        font-family: 'FontAwesome';
        
    }
}
.flexy{
    color: white;
}
</style>
