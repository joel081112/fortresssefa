var count = $(".brand .slider__inner >div").length;
$('.brand .slider__inner').width('calc( ' + count + ' * 100%)');


/*.slider__nav:checked:nth-of-type(9) ~ .slider__inner {
    left: -800%;


    $('.timeline .slider__nav:checked:nth-of-type(9) ~ .slider__inner').left('calc( (-' + count+ '-1) * 100%)');


}*/


var countT = $(".timeline .slider__inner >div").length;
$('.timeline .slider__inner').width('calc( ' + countT + ' * 100%)');

$(".timeline .slider__inner >div").forEach(function(countT) {
        $('.timeline .slider__nav:checked:nth-of-type(countT) ~ .slider__inner ').left('calc( (' + countT + '-1) * -100%)');

    });