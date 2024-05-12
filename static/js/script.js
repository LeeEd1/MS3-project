$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('select').formSelect();

    setTimeout(function() {
      $('.flashes').fadeOut('slow');
    }, 3000);
  });