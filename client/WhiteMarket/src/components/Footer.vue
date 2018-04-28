<template>
  <footer>
      <div>
            <ul class="list-unstyled list-inline font-small">
                <li class="list-inline-item pr-2 white-text" @click="modal('Bitcoin','LTdsVS8VDw6syvfQADdhf2PHAm3rMGJvPX')"><i class="icon-bitcoin"></i></li>
                <li class="list-inline-item pr-2 white-text" @click="modal('Ethereum','0x0074709077B8AE5a245E4ED161C971Dc4c3C8E2B')"><i class="icon-ethereum"></i></li>
                <li class="list-inline-item pr-2 white-text" @click="modal('Monero','3CMCRgEm8HVz3DrWaCCid3vAANE42jcEv9')"><i class="icon-monero"></i></li>
            </ul>
      </div>
          <!-- Modal -->
            <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Donation {{coin}}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="row wallet">
                    <h2 class="modal-title" >{{wallet}}</h2>
                    </div>
                    <qrcode v-if="wallet" :val="wallet"></qrcode>
                </div>
                <div class="modal-footer">
                    <h5 class="modal-footer">Thanks for your MONEY</h5>
                    <button type="button" class="btn btn-secondary" data-dismiss="modal" aria-label="Close">Close</button>
                </div>
                </div>
            </div>
            </div>
  </footer>
</template>

<script>
import vueQrcode from '@/components/commons/vue-qrcode'
export default {
    data(){
        return{
            coin:undefined,
            wallet:undefined,
            val:"https://github.com/",
        }
    },
    components:{
        qrcode: vueQrcode
    },
    methods:{
        modal: function(coin, wallet) {
            console.log(coin)
            console.log(wallet)
            this.coin = coin;
            this.wallet = wallet
            $('#myModal').modal('show')
        }
    }
    

}
</script>

<style lang="scss" scoped>
div ul{
        li {
            [class^="icon-"], [class*=" icon-"]{
                font-size: 25px;
            }
            display: flex;
            justify-content: center;
            align-items: center;
        }
        display: flex;
        justify-content: center;
        margin: 0;
    }
.wallet{
    display: flex;
    justify-content: center;
}
</style>
