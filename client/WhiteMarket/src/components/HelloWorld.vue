<template>
  <div>
    <ul>
      <li v-for="n in products" :key="n.pk">{{n.title}} --- {{n.price}}$ </li>
    </ul>
  </div>
</template>

<script>
/* eslint-disable */ 
export default {
  name: 'HelloWorld',
  data () {
    return{
      products: []
    }
  },
  created () {
    console.log(this);
    this.$http.get('http://localhost:8000/api/products/')
    .then(response => {
         this.products = response.data
    })
    .catch(error => {
      console.log(error);
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
