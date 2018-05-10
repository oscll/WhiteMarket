import Vue from 'vue'
import Router from 'vue-router'
import authRoutes from '@/components/auth/auth.routes'
import productsRoutes from '@/components/products/products.routes'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: '/',
  routes: [
    {
      path: '/',
      redirect: '/products'
    },
    ...authRoutes,
    ...productsRoutes
  ]
})
