$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

  $('#password, #password_reconfirm').on('keyup', function () {
    if ($('#password').val() == $('#password_reconfirm').val()) {
      $('#message').html('Matching').css('color', 'green');
    } else 
      $('#message').html('Not Matching').css('color', 'red');
  });