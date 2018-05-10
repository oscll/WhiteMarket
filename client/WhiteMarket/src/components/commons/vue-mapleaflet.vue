<template>
  <div id="map">
  </div>
</template>

<script>
export default {
    props: {
        latitude: {
        type: Number,
        default: 38.821103
        },
        longitude: {
        type: Number,
        default: -0.609543
        },
        clickLatLong: {
        type: String,
        default: false
        },
        items: {
        type: Object,
        },
    },
    watch:{
        latitude(){
            this.markerLatLong({latlng: {lat:this.latitude,lng:this.longitude},located: true})
        },
        longitude(){
            this.markerLatLong({latlng: {lat:this.latitude,lng:this.longitude},located: true})
        },
    },
    methods:{
        markerLatLong(e) {
            if(this.marker){
                if(this.clickLatLong) {
                    if(!e.located)
                        this.$emit('location', e.latlng)
                    this.marker.setLatLng(e.latlng)
                    this.map.setView(e.latlng)
                }
            }
        },
        
        mountmap(){
            this.map = L.map('map').setView([this.latitude, this.longitude], 13); 
            L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>',
                id: 'mapbox.streets'
            }).addTo(this.map);
            // Icon options
            let iconOptions = {
                iconUrl: '/static/logo.png',
                iconSize: [25, 25]
            }
            let customIcon = L.icon(iconOptions);
            this.marker = new L.marker({lat: this.latitude, lng: this.longitude}, {title:'located', clickable: true, icon: customIcon, draggable:true});

            this.marker.addTo(this.map)
            this.map.on('click', this.markerLatLong);
        }
    },

    mounted() {
        this.mountmap()
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition((data)=>{
                this.$emit('location', {lat: data.coords.latitude, lng: data.coords.longitude})
            });
        }else{
            console.log('No seas hipocrita')
        }
    },
}
</script>

<style lang="scss" scoped>
div#map{
    width: 100%;
    height: 100%;
}
</style>
