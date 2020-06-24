$(".carousel-indicators").each(function () {
    if ($('ul > li').length > 9) {
        $('ul').hide();
    }


});

function myFunction() {
  document.getElementById("modal").src = $('.active').find('img').attr('src');
}


/*Test*/
$('#multiViewCarousel').carousel({
  interval: 10000
})

$('.carousel .carousel-item').each(function(){
    var minPerSlide = 4;
    var next = $(this).next();
    if (!next.length) {
    next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));

    for (var i=0;i<minPerSlide;i++) {
        next=next.next();
        if (!next.length) {
        	next = $(this).siblings(':first');
      	}

        next.children(':first-child').clone().appendTo($(this));
      }
});
