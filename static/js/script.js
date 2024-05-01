$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.modal').modal();
    $('.collapsible').collapsible();

    setTimeout(function() {
      $('.flashes').fadeOut('slow');
    }, 3000);
  });