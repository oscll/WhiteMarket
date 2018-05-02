<template>
  <div >
      <div v-if="imageUrl != undefined">
          <img :src="imageUrl" alt="Imagen subida !! ">
      </div>
      <div v-else :class="{ dragover: stateDragover , input: true}" @dragleave.prevent="stateDragover = false" @dragover.prevent="stateDragover = true" @dragenter.prevent @drop.prevent="uploadImage">
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
    data(){
        return{
            imageUrl: undefined,
            pk: undefined,
            error: undefined,
            stateDragover: false,
        }
    },
    methods:{
        uploadImage(e) {
            let files = e.target.files || e.dataTransfer.files;
            let file =new FormData()
            file.append('image', files[0])
            API.post('/images/', file, { headers: {'Content-Type': 'multipart/form-data'}})
            .then(response => {
                this.imageUrl = response.data.image;font-siz
                this.pk = response.data.pk;
            }).catch(err => { 
                if(err.response.status != 401)
                    this.error = 'No estas authenticated'
                else{
                    this.error = err.response.data.childNodes[0]
                    console.log(err.response.data)
                }
            })
        },
        
    },
}
</script>

<style lang="scss" scoped>
div{
    width: 100%;
    height: 100%;
}
.input{
    font-size: 1.25rem;
    background-color: #c8dadf;
    position: relative;
    padding: 100px 20px;
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
</style>