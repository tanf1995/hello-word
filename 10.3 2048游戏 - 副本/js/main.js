$(function () {
    var main_box = $('.game_window .game_content');
    var score = $('.score span');
    //li_block存放[x坐标，y坐标， 值]
    var li_block = [];
    var usable_coor = [];
    var win = false;
    var max_score = 0;

    restart();

    $('.newgame').click(function () {
        restart();
    });

    //重启游戏
    function restart() {
        main_box.empty();
        li_block = [];
        win = false;
        new_block();
        new_block();
    }

    function new_block() {
        //产生一个元素块
        var num = [];
        var x = -1;
        var y = -1;
        var coor_index = -1;
        if(li_block.length<16){
            //更新可用坐标
            usable_coor = [];
            for(var i=0;i<4;i++){
                for(var j=0;j<4;j++){
                    usable_coor.push([i, j]);
                }
            }
            for(var k=0;k<li_block.length;k++){
                num.push(parseInt(li_block[k][0])*4 + parseInt(li_block[k][1]));
            }
            num = drop_sort(num);
            for(var l=0;l<num.length;l++){
                usable_coor.splice(num[l], 1);
            }

            //获取新块坐标
            coor_index =  Math.floor(Math.random()*usable_coor.length);
            x = usable_coor[coor_index][0];
            y = usable_coor[coor_index][1];

            //生成快
            produce_block(x, y, -1);
            return true;
        }
        return false;
    }

    //键盘控制游戏
    document.onkeydown=function(event){
        var e = event || window.event || arguments.callee.caller.arguments[0];
        if(e && e.keyCode==38){ // 上
            li_block = move_up();
            reset_coor();
            new_block();
            if(is_win() && !win){
                alert('恭喜，完成2048目标，可继续游戏打到更高分数！');
                win = true;
            }
            score.text(max_score);
            is_failed();
            console.log('li:'+li_block.length);
            if(li_block.length>=16){
                if (is_failed()){
                    if(win==true){
                        alert('游戏结束，YOU WIN!');
                        return;
                    }
                    alert('游戏失败！');
                    return;
                }
            }
            return;
        }
        if(e && e.keyCode==40){ // 下
            li_block = move_down();
            reset_coor();
            new_block();
            if(is_win() && !win){
                alert('恭喜，完成2048目标，可继续游戏打到更高分数！');
                win = true;
            }
            score.text(max_score);
            if(li_block.length>=16){
                if (is_failed()){
                    if(win==true){
                        alert('游戏结束，YOU WIN!');
                        return;
                    }
                    alert('游戏失败！');
                    return;
                }
            }
            return;

        }
        if(e && e.keyCode==37){ // 左
            li_block = move_left();
            reset_coor();
            new_block();
            if(is_win() && !win){
                alert('恭喜，完成2048目标，可继续游戏打到更高分数！');
                win = true;
            }
            score.text(max_score);
            if(li_block.length>=16){
                if (is_failed()){
                    if(win==true){
                        alert('游戏结束，YOU WIN!');
                        return;
                    }
                    alert('游戏失败！');
                    return;
                }
            }
            return;
        }
        if(e && e.keyCode==39){ // 右
            li_block = move_right();
            reset_coor();
            new_block();
            if(is_win() && !win){
                alert('恭喜，完成2048目标，可继续游戏打到更高分数！');
                win = true;
            }
            score.text(max_score);
            if(li_block.length>=16){
                if (is_failed()){
                    if(win==true){
                        alert('游戏结束，YOU WIN!');
                        return;
                    }
                    alert('游戏失败！');
                }
            }
        }
    };





    //重设块坐标
    function reset_coor() {
        main_box.empty();
        var mid_li = li_block;
        li_block = [];
        for(var n=0;n<mid_li.length;n++){
            var x = mid_li[n][0];
            var y = mid_li[n][1];
            var value = mid_li[n][2];
            produce_block(x, y, value);
        }
    }

    //判断游戏是否结束
    function is_failed() {
        var cols_ju = move_left();
        var te2 = move_right();
        var rows_ju = move_up();
        var te1 = move_down();
        console.log(cols_ju.length);
        console.log(te2.length);
        console.log(rows_ju.length);
        console.log(te1.length);
        return (rows_ju.length==16 && cols_ju.length==16);
    }

    //判断是否完成2048
    function is_win() {
        for(var i=0;i<li_block.length;i++){
            if(li_block[i][2]>max_score){
                max_score = li_block[i][2];
            }

            if(li_block[i][2]==2048){
                return true;
            }
        }
        return false;
    }

    // 生成块
    function produce_block(i, j, value) {
        // var newblock = document.createElement('div');
        var newblock = $("<div></div>");
        var block_value = 0;
        newblock.addClass('block');
        newblock.css({top:j*100, left: i*100});
        // newblock.style.top = j*100 + 'px';
        // newblock.style.left = i*100 + 'px';

        if (value==-1){
            num = Math.random()*10;
            if (num >0.3){
                newblock.text(2);
                block_value = 2;
            }
            else{
                newblock.text(4);
                block_value = 4;
            }
        }
        else {
            newblock.text(value);
            block_value = value;
        }
        //块配色
        if(block_value==2){
            newblock.css({backgroundColor: '#ffba4e'});
        }
        else if(block_value==4){
            newblock.css({backgroundColor: '#ffa353'});
        }
        else if(block_value==8){
            newblock.css({backgroundColor: '#f07855'});
        }
        else if(block_value==16){
            newblock.css({backgroundColor: '#ce7f85'});
        }
        else if(block_value==32){
            newblock.css({backgroundColor: '#db5e5a'});
        }
        else if(block_value==64){
            newblock.css({backgroundColor: '#cb8182'});
        }
        else if(block_value==128){
            newblock.css({backgroundColor: '#ab3d6a'});
        }
        else if(block_value==256){
            newblock.css({backgroundColor: '#8b658e'});
        }
        else if(block_value==512){
            newblock.css({backgroundColor: '#d5cb9a'});
        }
        else if(block_value==1024){
            newblock.css({backgroundColor: '#f6ea86'});
        }
        else {
            newblock.css({backgroundColor: '#6385a0'});
        }
        main_box.append(newblock);
        newblock.fadeIn();
        li_block.push([i, j, block_value]);
    }


    //数组降序排序
    function drop_sort(li) {
        var is_sort = true;
        for(var i=0;i<li.length-1;i++){
            is_sort = true;
            for(var j=0;j<li.length-i-1;j++){
                if (li[j] <li[j+1]){
                    var mid = li[j];
                    li[j] = li[j+1];
                    li[j+1] = mid;
                    is_sort = false;
                }
            }
            if(is_sort==true){
                break;
            }
        }
        return li;
    }

});
