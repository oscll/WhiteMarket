<template>
    <div>
        <div v-if="token != ''" class="btn btn-primary sing-in">
            <router-link to="/login" tag="span">
                Sing in
            </router-link>
        </div>
        <div v-else class="btn sing-in">
            {{username}}
        </div>
    </div> 
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.sing-in{
    &:before{
        content: '\f2bd';
        font-family: 'FontAwesome';
        
    }
}
</style>
