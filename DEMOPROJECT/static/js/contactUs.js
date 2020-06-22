$(function initMap() {
    var belfast = {lat: 54.679044, lng: -5.998068};
    var dundee = {lat: 56.481879, lng: -2.889296};
    var glasgow = {lat: 55.800615, lng: -4.399953};
    var london = {lat: 51.575048, lng: 0.402577};
    var manchester = {lat: 53.556474, lng: -2.526779};
    var warsaw = {lat: 54.400575, lng: 19.855841};
    var gothenburg = {lat: 57.659772, lng: 11.940422};
    var stockholm = {lat: 59.293698, lng: 18.030853};
    var malmo = {lat: 55.573130, lng: 13.040849};


    // Styles a map in night mode.
    var locations = [
        belfast,
        dundee,
        glasgow,
        london,
        manchester,
        warsaw,
        gothenburg,
        stockholm,
        malmo
    ];

    var map = new google.maps.Map(document.getElementById('map'), {
        center: belfast,
        zoom: 6,
        mapTypeId: 'hybrid'

    });
    var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var markers = locations.map(function (location, i) {
        return new google.maps.Marker({
            position: location,
            animation: google.maps.Animation.DROP,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

    function toggleBounce() {
        if (markers.getAnimation() !== null) {
            markers.setAnimation(null);
        } else {
            markers.setAnimation(google.maps.Animation.BOUNCE);
        }
    }
});

