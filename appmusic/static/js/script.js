$(document).ready(function() {

  /*For Sticky Navigation*/
  $('.js--section-albums').waypoint(function(direction){
    if (direction == 'down') {
      $('nav').addClass('sticky');
    } else {
      $('nav').removeClass('sticky');
    }
  },{
    offset: '60px;'
  });

  /*Scroll on buttons*/
  $('.js-scroll-to-about').click(function(){
    $('html, body').animate({scrollTop: $('.section-about').offset().top-100},1000);
  });

  $('.js-scroll-to-songs').click(function(){
    $('html, body').animate({scrollTop: $('.js--section-songs').offset().top-100},700);
  });


  /*For Hamburger Icon Toggler*/
  $('.js--nav-icon').click(function() {
    var nav = $('.js--main-nav');
    var icon = $('.js--nav-icon i');


    nav.slideToggle(400);

    if(icon.hasClass('ion-navicon-round')){
      icon.addClass('ion-close-round');
      icon.removeClass('ion-navicon-round');
    } else{
      icon.addClass('ion-navicon-round');
      icon.removeClass('ion-close-round');
    }

  });

});
