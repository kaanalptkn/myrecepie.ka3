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


var ingredients_input = document.getElementById('ingredients-input');
var add_btn_ing = document.getElementById('add-btn-ing');
var btn_remove = document.getElementById('btn-remove');

add_btn_ing.onclick = function(){
  var newField = document.createElement('input');
  newField.setAttribute('type','text');
  newField.setAttribute('name','ingredients-input');
  newField.setAttribute('class','ingredients-input');
  newField.setAttribute('siz',50);
  newField.setAttribute('placeholder','Add more ingredients and quantity');
  ingredients_input.appendChild(newField);
}

btn_remove.onclick = function(){
  var input_class = ingredients_input.getElementsByClassName('ingredients-input');
  if(input_class.length > 1) {
    ingredients_input.removeChild(input_class[(input_class.length) - 1]);
  }
}

var instruction_input = document.getElementById('instruction-input');
var add_btn_ins = document.getElementById('add-btn-ins');
var btn_remove_ins = document.getElementById('btn-remove-ins');

add_btn_ins.onclick = function(){
  var newField = document.createElement('input');
  newField.setAttribute('type','text');
  newField.setAttribute('name','instruction-input');
  newField.setAttribute('class','instruction-input');
  newField.setAttribute('siz',50);
  newField.setAttribute('placeholder','Add more instruction');
  instruction_input.appendChild(newField);
}

btn_remove_ins.onclick = function(){
  var input_class = instruction_input.getElementsByClassName('instruction-input');
  if(input_class.length > 1) {
    instruction_input.removeChild(input_class[(input_class.length) - 1]);
  }
}

    