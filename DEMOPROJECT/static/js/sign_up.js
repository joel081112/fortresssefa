function check(input) {
    if (input.value != document.getElementById('passNew').value) {
        input.setCustomValidity('Password Must be Matching.');
    } else {
        // input is valid -- reset the error message
        input.setCustomValidity('');
    }
}

function myFunction() {
    $("input:text").val("");
}

function showHidePassword() {
  var x = document.getElementById("pass");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}


function showHidePassword_id() {
  var x = document.getElementById("id_password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function showHidePasswordForm() {
  var x = document.getElementById("passNew");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function eyeEvent() {
    $("pass").removeClass('fa-eye-slash');
    $(this).toggleClass('fa-eye');
}


$('.passw').change(function(){
    if($(this).is(":checked")) {
        $('.im').toggleClass('fa-eye-slash');
    } else {
        $('.im').toggleClass('fa-eye');
    }
});