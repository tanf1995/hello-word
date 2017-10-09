$(function () {
   var block1 = $('.game_content div').eq(0);
   var block2 = $('.game_content div').eq(1);
   block1.css({top: 0, "left": 0});
   block2.css({"top": 0, "left": 300});

    $(window).keydown(function(event){
        switch(event.keyCode) {
            case 37:
                left();
                break;
        }
    });

    function left(){
        // for(var i=0;i<4;i++){
        //     for(var j=1;j<4;j++){
        //         str = i + j;
        //         if(block = $('.game_content #str')){
        //             alert(block);
        //         }
        //     }
        // }
        str2 = 10 + 1;
        alert(str);
    }
});
