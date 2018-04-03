<template>
    <h1>{{name}}</h1>
</template>

<script>
export default {

    props: {
        name: {
            type: String,
            default: "Fancy Button!",
            required: true,
        }
    }

}
</script>

<style>

</style>
