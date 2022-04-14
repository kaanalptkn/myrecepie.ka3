$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
  });

  $('#password, #password_reconfirm').on('keyup', function () {
    if ($('#password').val() == $('#password_reconfirm').val()) {
      $('#message').html('Matching').css('color', 'green');
    } else 
      $('#message').html('Not Matching').css('color', 'red');
  });


var ingredients = document.getElementById('ingredients');
var add_btn_ing = document.getElementById('add-btn-ing');
var btn_remove = document.getElementById('btn-remove');

add_btn_ing.onclick = function(){
  var newField = document.createElement('input');
  newField.setAttribute('type','text');
  newField.setAttribute('name','ingredients');
  newField.setAttribute('class','ingredients');
  newField.setAttribute('placeholder','Add more ingredients and quantity');
  ingredients.appendChild(newField);
}

btn_remove.onclick = function(){
  var input_class = ingredients.getElementsByClassName('ingredients');
  if(input_class.length > 1) {
    ingredients.removeChild(input_class[(input_class.length) - 1]);
  }
}

var instructions = document.getElementById('instructions');
var add_btn_ins = document.getElementById('add-btn-ins');
var btn_remove_ins = document.getElementById('btn-remove-ins');

add_btn_ins.onclick = function(){
  var newField = document.createElement('input');
  newField.setAttribute('type','text');
  newField.setAttribute('name','instructions');
  newField.setAttribute('class','instructions');
  newField.setAttribute('placeholder','Add more instruction');
  instructions.appendChild(newField);
}

btn_remove_ins.onclick = function(){
  var input_class = instructions.getElementsByClassName('instructions');
  if(input_class.length > 1) {
    instructions.removeChild(input_class[(input_class.length) - 1]);
  }
}

    