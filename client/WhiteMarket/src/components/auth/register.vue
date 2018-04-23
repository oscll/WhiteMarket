<template>
    <div class="container">
        <form class="row my-5" v-on:submit.prevent="Submit()" role="form">
            <div class="col-sm-4 my-2 pb-3 col-xs-12">
                <div class="w-100 mb-5">
                    <label for="username">Username</label>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                        <input type="text" class="form-control" required id="username" placeholder="Username" v-model="username">
                    </div>
                </div>
                <div class="w-100 mb-5">
                    <label for="email">Email</label>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                        <input type="email" class="form-control" required id="email" placeholder="example@whitemarke.xyz" v-model="email">
                    </div>
                </div>
                <div class="w-100 mb-5">
                    <label for="password">Password</label>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                        <input type="password" class="form-control" required id="password" placeholder="Password" v-model="password">
                    </div>
                </div>

                <div class="w-100 mb-5">
            <button type="submit" class="btn btn-success btn-lg float-right" id="btnRegister">Register</button>
                </div>
            </div>
            <div class="col-sm-8 col-xs-12 my-2 pb-3" id="map">
                <input type="hidden" required id="latitude" v-model="latitude" > 
                <input type="hidden" required id="longitude" v-model="longitude" > 
            </div>
        </form>
    </div>
</template>

<script>
import { REGISTER } from '@/store/modules/auth'
export default {
    data(){
        return{
            email:null,
            password:null,
            username:null,
            latitude:null,
            longitude:null
        }
    },
    methods:{
        initMap: function() {
        // Create a map object and specify the DOM element for display.
            google.maps.visualRefresh = true;

            var infowindow = null;
            var map = new google.maps.Map(document.getElementById('map'), {
                center: new google.maps.LatLng(this.latitude, this.longitude),
                zoom: 10,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            });
            google.maps.event.addListener(map, 'click', (e) => {
                this.latitude = e.latLng.lat();
                this.longitude = e.latLng.lng();
                if (infowindow != null)
                    infowindow.close();

                infowindow = new google.maps.InfoWindow({
                    content: '<b>Mouse Coordinates : </b><br><b>Latitude : </b>' + e.latLng.lat() + '<br><b>Longitude: </b>' + e.latLng.lng(),
                    position: e.latLng
                });
                infowindow.open(map);
            });
        },
        createGoogleMaps: function() {
            return new Promise((resolve, reject) => {
                let gmap = document.createElement('script');
                gmap.src = `https://maps.googleapis.com/maps/api/js?key=`;
                gmap.type = 'text/javascript';
                gmap.onload = resolve;
                gmap.onerror = reject;
                document.body.appendChild(gmap);
            })
        },
        Submit () {
            this.$store.dispatch(REGISTER, [this.username, this.email, this.password, this.latitude, this.longitude])
            .then(this.$router.push('/'))
        },
    },

    mounted() {
        this.createGoogleMaps().then(this.initMap, this.googleMapsFailedToLoad);
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition((data)=>{
            console.log(data);
            console.log(this)
            this.latitude = data.coords.latitude;
            this.longitude = data.coords.longitude;
            this.createGoogleMaps().then(this.initMap, this.googleMapsFailedToLoad);
        });
        }else{
            console.log('No seas hipocrita')
        }
    },
}
</script>

<style lang="scss" scoped>
#map{
   min-height: 480px;
}
</style>
