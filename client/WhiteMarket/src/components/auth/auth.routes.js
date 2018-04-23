import login from './login';
import register from './register';
import store from '@/store';


export default 
  [
    {
      path: '/login',
      component: login,
      beforeEnter: (to, from, next) => {
        if(store.getters.token)
          next('/')
        next()
      },
    },
    {
      path: '/register',
      component: register,
      beforeEnter: (to, from, next) => {
        if(store.getters.token)
          next('/')
        next()
      },
    }
  ]
