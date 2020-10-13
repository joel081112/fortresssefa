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




