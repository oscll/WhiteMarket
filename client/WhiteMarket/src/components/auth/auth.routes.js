import login from './login';
import register from './register';

const isLogged = function(to,from,next) {
  if(localStorage.getItem('token')){
    next('/')
    return
  }
  next()
}
const notLogged = function(to,from,next) {
  if(!localStorage.getItem('token')){
    next('/')
    return
  }
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
    },
    {
      path: '/account',
      component: register,
      beforeEnter: notLogged,
    }
  ]
