<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-4 my-2 pb-3">
                <div class="w-100 my-5">
                    <label for="username">Username</label>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                        <input type="text" class="form-control" required id="username" placeholder="Username" v-model="username">
                    </div>
                </div>
                <div class="w-100 my-5">
                    <label for="email">Email</label>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                        <input type="email" class="form-control" required id="email" placeholder="example@whitemarke.xyz" v-model="email">
                    </div>
                </div>
                <div class="w-100 my-5">
                    <label for="password">Password</label>
                    <div class="input-group">
                        <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                        <input type="password" class="form-control" required id="password" placeholder="Password" v-model="password">
                    </div>
                </div>
            </div>
            <div class="col-sm-8 my-2 pb-3" id="map">
                
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            email:null,
            password:null,
            username:null,
            lat:null,
            long:null
        }
    },
    methods:{
        initMap: function() {
        // Create a map object and specify the DOM element for display.
        google.maps.visualRefresh = true;

        var infowindow = null;
        var map = new google.maps.Map(document.getElementById('map'), {
            center: new google.maps.LatLng(39.9078, 32.8252),
            zoom: 10,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
            google.maps.event.addListener(map, 'click', (e) => {
                        this.lat = e.latLng.lat();
                        this.long = e.latLng.lng();
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
        initGoogleMaps: function() {
            // We would set up our options object beforehand or grab it from Redux in my case
            this.vueGMap = new google.maps.Map(document.getElementById('map')); 
        }
    },

    mounted() {
        this.createGoogleMaps().then(this.initMap, this.googleMapsFailedToLoad);
    }

}
</script>

<style>

</style>
