function initMap() {
    
    var location = {lat: 12.997173, lng: 77.584762};
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: location
    });
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}