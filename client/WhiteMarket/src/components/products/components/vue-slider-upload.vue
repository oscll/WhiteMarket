<style lang="scss">
.main-slider{
  position: relative;

  .sliderButton{
    text-align: center;
  }
  .slider-back{
    &::before{
      content: "\f0a5";
      font-family: FontAwesome;
      font-size: 3vw;
    }
    position: absolute;
    top: 50%;
    z-index: 1;
    left: 0;
  }
  .slider-next{
    &::before{
      content: "\f0a4";
      font-family: FontAwesome;
      font-size: 3vw;
    }
    position: absolute;
    top: 50%;
    z-index: 1;
    right: 0;
  }
  .slider-append{
    &::before{
      content: "\f1c5";
      font-family: FontAwesome;
      font-size: 3vw;
    }
    display: flex;
    flex-direction: column;
    z-index: 1;
    bottom: 0;
    position: relative;
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
      <slider ref="slider" v-on="$listeners" :pages="someList" :sliderinit="sliderinit" @slide='slide' @tap='onTap' @init='onInit'>
        <div slot="loading">
          <div class="loadingDot">
          </div>
        </div>
      </slider>
    </div>
    <div class="sliderButton">
      <span class="slider-back" @click="slidePre"></span>
      <span class="slider-next" @click="slideNext"></span>
      <span class="slider-append" @click="appendslider">More images</span>
    </div>
  </div>
</template>
<script>
import slider from 'vue-concise-slider'
import uploader from '@/components/commons/vue-uploader-image'
export default {

  props:{
      images:{
        type:String,
        default: undefined
      },
  },
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
      if(that.images){
        that.someList = []
        let images = JSON.parse(that.images)
        images.forEach((image, index) => {
          if(index == 0){
            console.log('1')
            that.someList.push(
              {
                component:{
                  components:{
                    uploader
                  },
                  template: `<uploader v-on="$listeners" name="img${that.sliderinit.currentPage}" imgpk=${image.pk}> </uploader>`,
                }
              }
            )
          }else{
            console.log('2')
            that.sliderinit.currentPage++
            that.someList.push(
              {
                component:{
                  components:{
                    uploader
                  },
                  template: `<uploader v-on="$listeners" name="img${that.sliderinit.currentPage}" imgpk=${image.pk}> </uploader>`,
                }
              }
            )
          }
        });
        console.log('4')
        that.sliderinit.currentPage++
        that.someList.push(
          {
            component:{
              components:{
                uploader
              },
              template: `<uploader v-on="$listeners" name="img${that.sliderinit.currentPage}"> </uploader>`,
            }
          }
        )
      }else{
            console.log('3')
        that.someList = [
          {
            component:{
              components:{
                uploader
              },
              template: `<uploader v-on="$listeners" name="img${that.sliderinit.currentPage}"> </uploader>`,
            }
          },
        ]
      }
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
        this.sliderinit.currentPage++
        this.someList.push({
          component:{
            components:{
               uploader
            },
            template: `<uploader v-on="$listeners" name="img${this.sliderinit.currentPage}"> </uploader>`,
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
    }
  }
}
</script>