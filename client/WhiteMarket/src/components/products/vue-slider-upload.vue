<style lang="scss">
.main-slider{
  position: relative;

  .sliderButton{
    text-align: center;
  }
  .sliderButton button{
    display: inline-block;
    background: #fff;
    border-radius: 3px;
    /*width: 100px;*/
    height: 30px;
    border: 1px solid #333;
    line-height: 30px;
    margin-left: 10px;
    padding: 0 15px;
    margin-top: 10px;
  }
  .slider-back{
    position: absolute;
    top: 50%;
    z-index: 1;
    left: 0;
  }
  .slider-next{
    position: absolute;
    top: 50%;
    z-index: 1;
    right: 0;
  }
  .slider-append{
    z-index: 1;
    bottom: 0;
  }
}
.slider-pagination-bullet-active {
    background: #e00606 none repeat scroll 0 0;
    opacity: 1;
}
</style>
<template>
  <div class="main-slider">
    <div style="margin:20px">
      <slider ref="slider" :pages="someList" :sliderinit="sliderinit" @slide='slide' @tap='onTap' @init='onInit'>
        <div slot="loading">
          <div class="loadingDot">
          </div>
        </div>
      </slider>
    </div>
    <div class="sliderButton">
      <button class="slider-back" @click="slidePre">back</button>
      <button class="slider-next" @click="slideNext">next</button>
      <button class="slider-append" @click="appendslider">append</button>
    </div>
  </div>
</template>
<script>
import slider from 'vue-concise-slider'
import uploader from '@/components/commons/vue-uploader-image'
export default {
  data () {
    return {
      someList: [],
      sliderinit: {
        currentPage: 0,
        tracking: true,
        direction: 'horizontal', // 垂直滚动
        loop: false, // 无限循环
        // autoplay:1000 // 自动播放:时间[ms]
      }
    }
  },
  components: {
    slider,
    uploader,
  },
  mounted () {
    let that = this
    setTimeout(function () {
      that.someList = [
        {
          component:{
            components:{
               uploader
            },
            template: `<uploader name="img${that.sliderinit.currentPage}"> </uploader>`,
          }
        },
      ]
    }, 2000)
  },
  methods: {
    slideNext () {
      this.$refs.slider.$emit('slideNext')
      // slider.$emit('slideNext')
    },
    slidePre () {
      this.$refs.slider.$emit('slidePre')
      // slider.$emit('slidePre')
    },
    appendslider () {
      if(this.sliderinit.currentPage < 7){
        this.someList.push({
          component:{
            components:{
               uploader
            },
            template: `<uploader name="img${this.sliderinit.currentPage++}"> </uploader>`,
          }
        }); 
        setTimeout(()=>{
          this.$refs.slider.$emit('slideNext');
        },250)
      }else{
        toastr.warning("Solo puedes tener 7 imagenes !!")
      }
      console.log(this.sliderinit.currentPage)
    },
    // 监听事件发生了变化,需要指向一个子组件实例
    slide (data) {
    },
    onTap (data) {
    },
    onInit (data) {
      console.log(data)
    }
  }
}
</script>