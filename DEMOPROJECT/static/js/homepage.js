$(function () {
    var text = $(".text");
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        var homeIm2Class = $('.homeIm2');

        if (scroll >= 200) {
            text.removeClass("hidden");
        } else {
            text.addClass("hidden");
        }
        if (scroll + 250 > homeIm2Class.offset().top) { // when the div with homeIm2 class scrolls into view
            text.hide();
        }
        if (scroll + 250 < homeIm2Class.offset().top) { // when the div with homeIm2 class scrolls into view
            text.show();
        }


    });
});


$(function () {
  $(window).scroll(function () {

      var fadeClass = $('.fadeInBlock');

    for(var i=0; i<fadeClass.length; i++){

      var bottom_of_object = $(fadeClass[i]).position().top + $(fadeClass[i]).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();

      /* Adjust the "200" to either have a delay or that the content starts fading a bit before you reach it  */
      bottom_of_window = bottom_of_window + 200;

      if (bottom_of_window > bottom_of_object) {

        $(fadeClass[i]).animate({
          'opacity': '1'
        }, 2500);

      }

    }
  });
});

$(function () {
    var fadeOnL = $('.fadeonload');
    for(var i=0; i<fadeOnL.length; i++) {
        $(fadeOnL[i]).animate({'opacity': '1', 'margin-left': '100px'}, 1000);
    }
});





