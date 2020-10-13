$("p#limiter").each(function() {
    var text = $(this).text();
    text = text.replace(/_/g, " ");
    $(this).text(text);
});
