import login from './login';
import register from './register';
import store from '@/store/';

const isLogged = (to, from, next) => {
  if(store.getters.token)
      next('/')
   next()
}

export default 
  [
    {
      path: '/login',
      component: login,
      beforeEnter: isLogged,
    },
    {
      path: '/register',
      component: register,
      beforeEnter: isLogged,
    }
  ]
