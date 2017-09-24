/**
 * Created by Administrator on 2017/8/25.
 */

$(function () {
    var $h = $(window).height();
    $('.page').css({height: $h});
    var $pages = $('.page');

    var nowScreen = 0;
    var timer = null;

    $pages.eq(0).addClass('moving');

    $(window).mousewheel(function (event, dat) {
        clearTimeout(timer);
        timer = setTimeout(function () {

            if(dat==-1){
                nowScreen++;
            }
            else {
                nowScreen--;
            }
            if(nowScreen<0){
                nowScreen=0;
            }
            if(nowScreen>$pages.length-1){
                nowScreen = $pages.length-1;
            }
            $pages.eq(nowScreen).addClass('moving').siblings().removeClass('moving');
            $('ul li').eq(nowScreen).addClass('active').siblings().removeClass('active');
            $('.all').animate({top: -nowScreen*$h},300);

        },200);
    });

    $('ul li').click(function () {
        $(this).addClass('active').siblings().removeClass('active');
        $pages.eq($(this).index()).addClass('moving').siblings().removeClass('moving');
        $('.all').animate({top: -$(this).index()*$h});
    });
});