import login from './login';
import register from './register';

export default 
  [
    {
      path: '/login',
      component: login,
    },
    {
      path: '/register',
      component: register,
    }
  ]
