<template>
<div>
    <button type="button" class="btn btn-primary btn-lg mb-0 form-button" @click="modal">Change Password</button>
    <!-- Modal -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true" @keyup.enter="Submit">
        <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Change Password</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="form-group">
                        <label for="recipient-name" class="col-form-label">Current Password :</label>
                        <input type="password" class="form-control" id="recipient-name" v-model="oldpassword">
                    </div>
                    <div class="form-group">
                        <label for="message-text" class="col-form-label">New Password :</label>
                        <input type="password" class="form-control" id="password-name" v-model="newpassword">
                    </div>
                </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" @click="Submit" >Save changes</button>
            </div>
            </div>
        </div>
    </div>
</div>
  
</template>

<script>
import { API } from '@/utils/api'
import { ERRORS } from '@/store/mutation-types.js'
export default {

    data(){
        return{
            newpassword:null,
            oldpassword:null,
        }
    },
    methods:{
        Submit() {
            if(this.newpassword && this.oldpassword){
                API.post('/auth/password/',{"current_password":this.oldpassword,"new_password":this.newpassword})
                .then(() => {
                    toastr.success("Password Changed","Password")
                    $('#myModal').modal('hide')

                }).catch(err => { 
                    err.response ? this.$store.dispatch(ERRORS, err.response.data) : ""
                })
            }
        },
        modal(){
            $('#myModal').modal('show')
        }
    },
}
</script>

<style>

</style>
