


var placing = function(){
    // if it is the first page then it will arrange the logo to the centre
    if($('#videoBg').length){
        // first the logo
        $('#videoBg').css('width',$(window).innerWidth()).css('height',$(window).innerHeight());
        if($(window).innerWidth() > 700){
            $('.scrollname').css('z-index','50');
            $('.scrollname').css('left', Math.max(0, ($(window).width() - $('.scrollname').innerWidth()) / 2) + "px");
            $('.scrollname').css('top', parseInt($(window).innerHeight(),10) - parseInt($('.scrollname').css('font-size'),10)*6);
            $('.modal-body').css('top',Math.max(0, parseInt($(window).innerHeight(),10)/3 - $('.modal-body').height()/2));
        }else{
            $('.scrollname').css('z-index','50');
            $('.scrollname').css('left', Math.max(0, ($(window).width() - $('.scrollname').innerWidth()) / 2)-10 + "px");
            $('.scrollname').css('top', parseInt($(window).innerHeight(),10) - parseInt($('.scrollname').css('font-size'),10)*3);
            $('.modal-body').css('top',Math.max(0, parseInt($(window).innerHeight(),10)/3 - $('.modal-body').height()/2));

        }

    }
};

$('.scrolldownlogo').click(function(){

    $('html,body').animate({
        scrollTop: $("#tvsection").offset().top
    });
});


var menuclose = function(){
    if($('.navmenu').hasClass('in')){
            $('#menunavicon').removeClass('tfg-close').addClass('tfg-menu');
    }
};

$('.navbar-toggle').click(function(){

    if(!$("#sitewrapper").hasClass("menuOpen")) {
        $("#sitewrapper").addClass("menuOpen");
        $("body, html").addClass("disable-scroll");
        $(".navmenu, .nav-trigger").addClass("opened");
        $('#menunavicon').removeClass('tfg-menu').addClass('tfg-close');

    } else {
        $("#sitewrapper").removeClass("menuOpen");
        $("body, html").removeClass("disable-scroll");
        $(".navmenu, .nav-trigger").removeClass("opened");
        $('#menunavicon').removeClass('tfg-close').addClass('tfg-menu');
    }


});


$('.navmenu').click(function(){
    $('.navmenu').removeClass('in');
    $('#menunavicon').removeClass('tfg-close').addClass('tfg-menu');
});


$('html, body').click(function(){
    if($('.navmenu').hasClass('in')){
        window.setTimeout(function() {
            menuclose();
        }, 300);
    }

});

$('#myModal, #playerModal').on('show.bs.modal', function () {
    $('.modal-content').css('height',$(window).height());
    $('html, body').animate({scrollTop:0},0);
    $("body, html").addClass("disable-scroll");
});

$('#myModal, #playerModal').on('hidden.bs.modal', function () {
    $("body, html").removeClass("disable-scroll");
});


$(document).ready(function(){
    placing();

});

$(window).resize(function() {
    placing();
});
