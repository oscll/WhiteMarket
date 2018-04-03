import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ProductDetail from '@/components/ProductDetail'
import authRoutes from '@/components/auth/auth.routes'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: '/',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/product/:name',
      name: 'Product',
      component: ProductDetail,
      props: true
    },
    authRoutes
  ]
})
