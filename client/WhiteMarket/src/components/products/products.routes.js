import list from './list';
import edit from './edit';

export default 
[
  {
    path: '/products',
    component: list,
  },
  {
    path: '/product/add',
    component: edit,
  }
]