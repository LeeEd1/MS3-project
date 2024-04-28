$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.modal').modal();

    setTimeout(function() {
      $('.flashes').fadeOut('slow');
    }, 3000);
  });