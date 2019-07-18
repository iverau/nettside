

function test(){
    document.getElementById("denne").innerHTML = "Jaja";
}

var x = document.getElementById("denne");

function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        document.getElementById("denne").innerHTML = "Geolocation is not supported by this browser.";
    }
  }
  
  function showPosition(position) {
    document.getElementById("denne").innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
  }