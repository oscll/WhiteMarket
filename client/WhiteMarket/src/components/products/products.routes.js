import list from './list';
import edit from './edit';
import detail from './details';

export default 
[
  {
    path: '/products',
    component: list,
  },
  {
    path: '/product/add',
    component: edit,
  },
  {
    path: '/products/detail/:pk',
    component: detail,
  }
]