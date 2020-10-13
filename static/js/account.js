$(".account").click(function () {
    var X = $(this).attr('id');
    var iconClose = document.getElementById('close');
    var iconOpen = document.getElementById('open');
    var accountSub = document.getElementsByClassName('accountsub');

    if (X == 1) {
        $(".accountsub").hide();

        $("#close").hide();
        $("#open").show();

        $(this).attr('id', '0');

    } else {
        $(".accountsub").show();

        $("#open").hide();
        $("#close").show().css("display", "inline"); ;

        $(this).attr('id', '1');

    }
});

//Mouse click on sub menu
$(".accountsub").mouseup(function () {
    return false
});

//Mouse click on my account link
$(".account").mouseup(function () {
    return false
});

//Document Click
$(document).mouseup(function () {
    $(".accountsub").hide();
    $(".account").attr('id', '');
    $("#open").hide();
    $("#close").show().css("display", "inline-block"); ;
});

function clicked(e)
{
    if(!confirm('Are you sure?'))e.preventDefault();
}

