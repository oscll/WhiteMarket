import list from './list';
import edit from './vue-slider-upload';

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