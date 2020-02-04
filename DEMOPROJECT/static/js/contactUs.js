// Initialize and add the map
function initMap() {
  // The location of fortress
  var fortress = {lat: 54.679329, lng: -5.998501};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at fortress
  var marker = new google.maps.Marker({position: fortress, map: map});
}