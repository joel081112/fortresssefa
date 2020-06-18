$(function initMap(){
    var location = {lat: -34.397, lng: 150.644};
    var map;
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: location

    })
});