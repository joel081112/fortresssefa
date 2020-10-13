var count = $(".brand .slider__inner >div").length;
var width = count * 100;
$('.brand .slider__inner').width(width + '%');


var countT = $(".timeline .slider__inner >div").length;
var widthT = countT * 100;
$('.timeline .slider__inner').width(widthT + '%');


$('.slider').each(function() {
  const $slider = $(this);
  $(this).find('form input').each(function(i) {
    $(this).on('change', function() {
      $slider.find('.slider__inner').css('left', (-100 * i) + "%");
    });
  });
});

/*.slider__nav:checked:nth-of-type(9) ~ .slider__inner {
    left: -800%;


    $('.timeline .slider__nav:checked:nth-of-type(9) ~ .slider__inner').left('calc( (-' + count+ '-1) * 100%)');
}*/

