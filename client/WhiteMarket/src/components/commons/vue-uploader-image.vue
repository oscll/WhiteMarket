<template>
  <div class="vue-uploader">
      <div v-if="imageUrl != undefined" class="reviewThumb">
          <img :src="imageUrl" alt="Imagen subida !! ">
          <div @click="newImage()" class="newImage">
          </div>
      </div>
      <div v-else :class="{ dragover: stateDragover , dragzone : true}" @dragleave.prevent="stateDragover = false" @dragover.prevent="stateDragover = true" @dragenter.prevent @drop.prevent="uploadImage">
          <h3>Drag and Drop <br> or Click</h3>
          <input type="file" name="image" @change.prevent="uploadImage">
      </div>
      <div>
          {{error}}
      </div>
  </div>
</template>

<script>
import { API } from '@/utils/api'
export default {
    props:{
        name:{
            type:String,
            default:'urlImageUpload'
        }
    },
    data(){
        return{
            imageUrl: 'https://dz13w8afd47il.cloudfront.net/sites/default/files/3%20for%2025%20-%20Home%20-%20Front%20V3%20-%20Approved.png',
            pk: undefined,
            error: undefined,
            stateDragover: false,
        }
    },
    methods:{
        uploadImage(e) {
            let files = e.target.files || e.dataTransfer.files;
            let file =new FormData()
            file.append('image', files[0]);
            API.post('/images/', file, { headers: {'Content-Type': 'multipart/form-data'}})
            .then(response => {
                this.imageUrl = response.data.image;font-siz;
                this.pk = response.data.pk;
                this.$emit(this.name, this.imageUrl);


            }).catch(err => { 
                if(err.response.status == 401)
                    toastr.error('No estas authenticated','Error upload image');
                else{
                    for(let key in err.response.data) {
                        if(err.response.data.hasOwnProperty(key)) {
                           toastr.error(err.response.data[key],'Error upload image'+key);
                        }
                    }
                }
            })
        },
        newImage(){
            this.imageUrl = undefined;
        }
        
    },
}
</script>

<style lang="scss" scoped>
.dragzone{
    
    &::before{
        content: "\f03e";
        font-family: FontAwesome;
        font-size: 110px;
    }

    height: 100%;
    width: 100%;
    font-size: 1.25rem;
    background-color: #c8dadf;
    outline: 2px dashed #92b0b3;
    outline-offset: -10px;
    -webkit-transition: outline-offset .15s ease-in-out, background-color .15s linear;
    transition: outline-offset .15s ease-in-out, background-color .15s linear;
}
.dragover{
    outline-offset: -20px;
    outline-color: #c8dadf;
    background-color: #fff;
}
input[type=file]{
    opacity: 0;
    width: 100%;
    height: 100%;
    cursor: pointer;
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
}
.reviewThumb{
    img{
        width: auto;
        height: auto;
    }
    width: auto;
    position: relative;
}
.vue-uploader{
    width: 100%;
    height: 100%;
}
.newImage{
    &::before{
        content:"\f057";
        font-family: FontAwesome;
        font-size:20px;
        position: absolute;
        top: 10px; 
        right: 10px; 
        width: 30px;
        color: black;
        height: 30px;
    }
        position: absolute;
        top: 10px; 
        right: 10px; 
}
</style>