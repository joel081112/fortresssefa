$(".carousel-indicators").each(function () {
    if ($('ul > li').length > 4) {
        $('ul').hide();
    }

    if ($('.modal01').css('display') == 'block') {
        $('ul').hide();
    }

});

