$(".account").click(function() {
    var X = $(this).attr('id');
    if (X == 1) {
        $(".accountsub").hide();
        $(this).attr('id', '0');
    }
    else {
        $(".accountsub").show();
        $(this).attr('id', '1');
    }
});

//Mouse click on sub menu
$(".accountsub").mouseup(function() {
    return false
});

//Mouse click on my account link
$(".account").mouseup(function() {
    return false
});

//Document Click
$(document).mouseup(function() {
    $(".accountsub").hide();
    $(".account").attr('id', '');
});