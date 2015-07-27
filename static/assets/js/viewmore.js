/**
 * Created by martinvowles on 21/10/2014.
 */

var sellect = '';

$('#tv_button').click(function(){

   $('.btn_drop').css('visibility', 'visible');
   $('.btn_drop_ul').css('visibility', 'visible');

   setTimeout(function () {
      if($('.btn_drop').css('visibility') == 'visible'){
          $('.btn_drop').css('visibility', 'hidden');
          $('.btn_drop_ul').css('visibility', 'hidden');
      }
    }, 3000);

});


$('.viewmore_btn').click(function(){
    var numbertv = $('.img_tv').length;
    var tvsec = $('.tvloader');
    var videourl = "tv/request/"+ numbertv +"/";

    $.getJSON( videourl, {})
        .done(function( data ){
            if(data.length === 0){
                $('.viewmore_btn').hide();
            }
            for(var d = 0; d < data.length; d++){
                if (data[d].fields.episode){
                    var output ="<div class='col-md-4 small-tv-item' data-lab='{0}'><div data-lab='{0}'><div class='img_tv load_img_tv'><i class='fa fa-play-circle'></i><img class='outputimg' src='/media/{1}' alt=''></div><div class='col-md-12 border'><h1 class='tv_title'>{2}</h1><h2 class='tv_ep tv_text'>Episode {3}: Part {4}</h2></div></div></div>".f(data[d].fields.vimeourl, data[d].fields.staticimage, data[d].fields.title, data[d].fields.episode, data[d].fields.part);
                }else{
                    var output ="<div class='col-md-4 small-tv-item' data-lab='{0}'><div data-lab='{0}'><div class='img_tv load_img_tv'><i class='fa fa-play-circle'></i><img class='outputimg' src='/media/{1}' alt=''></div><div class='col-md-12 border'><h1 class='tv_title'>{2}</h1></div></div></div>".f(data[d].fields.vimeourl, data[d].fields.staticimage, data[d].fields.title);
                }
                tvsec.append(output);
            }
            var newlength= $('.img_tv').length;

            if(newlength % 6 === 0){

            }else{
                $('.viewmore_btn').hide();
            }
        });

});
/*
$('.btn_drop_ul').click(function(){
   var tvsec = $('.tvloader');
   var sellect = $(this).html();
   var videourl = "tv/request/0/"+sellect+"/";
   sellect = sellect.replace(" ","_");
    if (sellect == 'ALL'){
      videourl = "tv/request/0/";
    }
   tvsec.empty();
   $.getJSON( videourl, {})
        .done(function( data ){
            for(var d = 0; d < data.length; d++){
                if (data[d].fields.episode){
                    var output ="<div class='col-md-4 small-tv-item' data-lab='{0}'><div data-lab='{0}'><div class='img_tv load_img_tv'><i class='fa fa-play-circle'></i><img class='outputimg' src='/media/{1}' alt=''></div><div class='col-md-12 border'><h1 class='tv_title'>{2}</h1><h2 class='tv_ep tv_text'>Episode {3}: Part {4}</h2></div></div></div>".f(data[d].fields.vimeourl, data[d].fields.staticimage, data[d].fields.title, data[d].fields.episode, data[d].fields.part);
                }else{
                    var output ="<div class='col-md-4 small-tv-item' data-lab='{0}'><div data-lab='{0}'><div class='img_tv load_img_tv'><i class='fa fa-play-circle'></i><img class='outputimg' src='/media/{1}' alt=''></div><div class='col-md-12 border'><h1 class='tv_title'>{2}</h1></div></div></div>".f(+data[d].fields.vimeourl, data[d].fields.staticimage, data[d].fields.title);
                }
                tvsec.append(output);
            }
        });

   $('.btn_drop').css('visibility', 'hidden');
   $('.btn_drop_ul').css('visibility', 'hidden');

});
*/
$(document).on('click', '.small-tv-item', function () {
    $('#playerModal').modal('show');$('.vimeovideo').attr('src',$(this).attr('data-lab')).attr('height',$(window).innerHeight());
});


String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

$('.carousel-control').click(function(){

});

