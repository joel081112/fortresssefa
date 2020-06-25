$(".carousel-indicators").each(function () {
    if ($('ul > li').length > 8) {
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


$(".mini .carousel").swipe({
        swipe: function (event, direction, distance, duration, fingerCount, fingerData) {
            if (direction == 'left') $(this).carousel('next');
            if (direction == 'right') $(this).carousel('prev');
        },
        allowPageScroll: "vertical"
    });




