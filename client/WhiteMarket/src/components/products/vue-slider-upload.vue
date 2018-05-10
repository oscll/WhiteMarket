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
        currentPage: 1,
        tracking: true,
        thresholdDistance: 100, // 滑动距离阈值判定
        thresholdTime: 300, // 滑动时间阈值判定
        direction: 'horizontal', // 垂直滚动
        loop: false, // 无限循环
        finite: 7
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
          html: '<uploader></uploader>',
          component: uploader
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
      this.someList.push({
        html: '<uploader></uploader>',
        component: uploader
      }); 
      setTimeout(()=>{
        this.$refs.slider.$emit('slideNext');
      },250)
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