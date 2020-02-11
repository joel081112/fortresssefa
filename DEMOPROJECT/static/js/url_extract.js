

document.getElementById("demo").innerHTML =
"The full URL of this page is:<br>" + window.location.href;

var url_string = window.location.href; //window.location.href
var url = new URL(url_string);
var email = url.searchParams.get("email");
document.getElementById("demo2").innerHTML = email;

var password = url.searchParams.get("password");
document.getElementById("demo3").innerHTML = password;