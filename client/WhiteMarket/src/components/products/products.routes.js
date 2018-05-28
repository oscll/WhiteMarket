import list from './list';
import edit from './edit';
import detail from './details';

export default 
[
  {
    path: '/products',
    name: 'products-list',
    component: list,
  },
  {
    path: '/myproducts',
    name: 'myproducts-list',
    component: list,
  },
  {
    path: '/myfavorited',
    name: 'favorited-list',
    component: list,
  },
  {
    path: '/product/add',
    component: edit,
  },
  {
    path: '/product/edit/:pk',
    component: edit,
  },
  {
    path: '/products/detail/:pk',
    component: detail,
  }
]