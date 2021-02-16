$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });

    $('.scrollup').click(function () {
        $("html, body").animate({
            scrollTop: 0
        }, 1200);
        return false;
    });
});

$(function initMap() {
    var belfast = {lat: 54.677164, lng: -5.989427};
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




/*
→	iPhone / iPad	→	fb://page/?id=367639123362658	→
→	Android	→	fb://page/367639123362658	→
→	desktop	→	facebook.com/367639123362658	*/

var ua = navigator.userAgent;
var plat = navigator.platform;
var a = document.getElementsByClassName('facebook');

if (ua.match(/iPhone/i)) {
    $(".facebook").href = "https://facebook.com/367639123362658";
} else if (ua.match(/iPad/i)) {
      $(".facebook").href = "https://facebook.com/367639123362658";
}
else{
      $(".facebook").attr("href", "https://facebook.com/367639123362658");
}

if (plat.indexOf("Win") > -1) {
    $(".facebook").attr("href", "https://facebook.com/367639123362658");
} else if (plat.indexOf("Mac") > -1) {
    $(".facebook").attr("href", "https://facebook.com/367639123362658");
}
else {
     $(".facebook").href = "https://facebook.com/367639123362658";
}

$("p#limiter").each(function() {
    var text = $(this).text();
    text = text.replace(/_/g, " ");
    $(this).text(text);
});



/*products .js*/
$(".carousel-indicators").each(function () {
    if ($('ul > li').length > 9) {
        $('ul').hide();
    }
});

function myFunction() {
  document.getElementById("modal").src = $('.active').find('img').attr('src');
}


/*Test*/
$('#carouselExampleIndicators2').carousel({
    interval: 25000
});

$('#carouselExampleIndicators').carousel({
    interval: 25000
});


$('.mini .carousel .carousel-item').each(function(){
    var next = $(this).next();

    if (!next.length) {
        next = $(this).siblings(':first');
    }

    next.children(':first-child').clone().appendTo($(this));

    if (next.next().length>0) {
        for (var i=0;i<2;i++) {
        next=next.next();
        if (!next.length) {
        	next = $(this).siblings(':first');
      	}

        next.children(':first-child').clone().appendTo($(this));
      }
    }
    else {
        $(this).siblings(':first').children(':first-child').clone().appendTo($(this));
    }


});


/*signup .js*/
function check(input) {
    if (input.value != document.getElementById('passNew').value) {
        input.setCustomValidity('Password Must be Matching.');
    } else {
        // input is valid -- reset the error message
        input.setCustomValidity('');
    }
}

function myFunction() {
    $("input:text").val("");
}

function showHidePassword() {
  var x = document.getElementById("pass");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}



function showHidePassword_id() {
  var x = document.getElementById("id_password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
function showHidePassword_id1() {
  var x = document.getElementById("id_password1");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
function showHidePassword_id2() {
  var x = document.getElementById("id_password2");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
function showHidePassword_idold() {
  var x = document.getElementById("id_oldpassword");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}


function showHidePasswordForm() {
  var x = document.getElementById("passNew");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function eyeEvent() {
    $("pass").removeClass('fa-eye-slash');
    $(this).toggleClass('fa-eye');
}









