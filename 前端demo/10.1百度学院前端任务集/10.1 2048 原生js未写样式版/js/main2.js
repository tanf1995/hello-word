window.onload = function () {
    var main_box = document.getElementsByClassName('main')[0];
    var li_block = [];
    var usable_coor = [];
    var win = false;

    restart();

    //重启游戏
    function restart() {
        main_box.innerHTML = '';
        li_block = [];
        new_block();
        new_block();
    }

    //生成一个新元素块
    function new_block() {
        if(li_block.length<16){
            //产生一个元素块
            renew_coor();
            var coor = get_coor();
            var x = coor[0];
            var y = coor[1];
            produce_block(x, y, -1);
            renew_coor();
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
            if(li_block.length==16){
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
            if(li_block.length==16){
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
            if(li_block.length==16){
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
            if(li_block.length==16){
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

    //随机生成坐标
    function get_coor() {
        var coor_index =  Math.floor(Math.random()*usable_coor.length);
        x = usable_coor[coor_index][0];
        y = usable_coor[coor_index][1];
        return [x, y]
    }

    //更新未使用的坐标
    function renew_coor() {
        usable_coor = [];
        for(var i=0;i<4;i++){
            for(var j=0;j<4;j++){
                usable_coor.push([i, j]);
            }
        }

        var num = [];
        for(var k=0;k<li_block.length;k++){
            num.push(parseInt(li_block[k][0])*4 + parseInt(li_block[k][1]));
        }
        num = drop_sort(num);
        for(var l=0;l<num.length;l++){
            usable_coor.splice(num[l], 1);
        }
    }

    // 生成块
    function produce_block(i, j, value) {
        var newblock = document.createElement('div');
        var block_value = 0;
        newblock.classList.add('block');
        newblock.style.top = j*100 + 'px';
        newblock.style.left = i*100 + 'px';

        if (value==-1){
            num = Math.random()*10;
            if (num >0.3){
                newblock.innerHTML = '2';
                block_value = 2;
            }
            else{
                newblock.innerHTML = '4';
                block_value = 4;
            }
        }
        else {
            newblock.innerHTML = value;
            block_value = value;
        }
        main_box.appendChild(newblock);

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

    //移动元素块__上
    function move_up() {
        //根据先行后列来排序，  列升序
        var res = [];
        var rows = [[],[],[],[]];
        for(var k=0;k<li_block.length;k++){
            if (li_block[k][0]==0) {
                rows[0].push(li_block[k]);
            }
            else if(li_block[k][0]==1){
                rows[1].push(li_block[k]);
            }
            else if(li_block[k][0]==2){
                rows[2].push(li_block[k]);
            }
            else{
                rows[3].push(li_block[k]);
            }
        }
        for(var o=0;o<4;o++){
            for(var l=0;l<rows[o].length-1;l++){
                var is_sort = true;
                for(var p=0;p<rows[o].length-l-1;p++){
                    if(rows[o][p][1]>rows[o][p+1][1]){
                        var mid = rows[o][p];
                        rows[o][p] = rows[o][p+1];
                        rows[o][p+1] = mid;
                        is_sort = false;
                    }
                }
                if(is_sort==true){
                    break;
                }
            }
            //合并相同值的块
            for (var i=0;i<rows[o].length-1;i++){
                if(rows[o][i][2]==rows[o][i+1][2]){
                    rows[o][i][2] = parseInt(rows[o][i][2])*2;
                    rows[o].splice(i+1,1);
                }
            }

            //改变块位置，全部上移
            for (var m=0;m<rows[o].length;m++){
                rows[o][m] = [rows[o][m][0], m, rows[o][m][2]];
                res.push(rows[o][m]);
            }
        }
        // li_block = res;
        return res;
    }

    //移动元素块__下
    function move_down() {
        //根据先行后列来排序， 列降序
        var res = [];
        var rows = [[],[],[],[]];
        for(var k=0;k<li_block.length;k++){
            if (li_block[k][0]==0) {
                rows[0].push(li_block[k]);
            }
            else if(li_block[k][0]==1){
                rows[1].push(li_block[k]);
            }
            else if(li_block[k][0]==2){
                rows[2].push(li_block[k]);
            }
            else{
                rows[3].push(li_block[k]);
            }
        }
        for(var o=0;o<4;o++){
            for(var l=0;l<rows[o].length-1;l++){
                var is_sort = true;
                for(var p=0;p<rows[o].length-l-1;p++){
                    if(rows[o][p][1]<rows[o][p+1][1]){
                        var mid = rows[o][p];
                        rows[o][p] = rows[o][p+1];
                        rows[o][p+1] = mid;
                        is_sort = false;
                    }
                }
                if(is_sort==true){
                    break;
                }
            }
            //合并相同值的块
            for (var i=0;i<rows[o].length-1;i++){
                if(rows[o][i][2]==rows[o][i+1][2]){
                    rows[o][i][2] = parseInt(rows[o][i][2])*2;
                    rows[o].splice(i+1,1);
                }
            }

            //改变块位置，全部下移
            for (var m=0;m<rows[o].length;m++){
                rows[o][m] = [rows[o][m][0], 3-m, rows[o][m][2]];
                res.push(rows[o][m]);
            }
        }
        // li_block = res;
        return res;
    }

    //移动元素块__左
    function move_left() {
        //根据先列后行来排序，  行升序
        var res = [];
        var cols = [[],[],[],[]];
        for(var k=0;k<li_block.length;k++){
            if (li_block[k][1]==0) {
                cols[0].push(li_block[k]);
            }
            else if(li_block[k][1]==1){
                cols[1].push(li_block[k]);
            }
            else if(li_block[k][1]==2){
                cols[2].push(li_block[k]);
            }
            else{
                cols[3].push(li_block[k]);
            }
        }
        for(var o=0;o<4;o++){
            for(var l=0;l<cols[o].length-1;l++){
                var is_sort = true;
                for(var p=0;p<cols[o].length-l-1;p++){
                    if(cols[o][p][0]>cols[o][p+1][0]){
                        var mid = cols[o][p];
                        cols[o][p] = cols[o][p+1];
                        cols[o][p+1] = mid;
                        is_sort = false;
                    }
                }
                if(is_sort==true){
                    break;
                }
            }
            //合并相同值的块
            for (var i=0;i<cols[o].length-1;i++){
                if(cols[o][i][2]==cols[o][i+1][2]){
                    cols[o][i][2] = parseInt(cols[o][i][2])*2;
                    cols[o].splice(i+1,1);
                }
            }

            //改变块位置，全部左移
            for (var m=0;m<cols[o].length;m++){
                cols[o][m] = [m, cols[o][m][1], cols[o][m][2]];
                res.push(cols[o][m]);
            }
        }
        // li_block = res;
        return res;
    }

    //移动元素块__右
    function move_right() {
        //根据先列后行来排序，  行升序
        var res = [];
        var cols = [[],[],[],[]];
        for(var k=0;k<li_block.length;k++){
            if (li_block[k][1]==0) {
                cols[0].push(li_block[k]);
            }
            else if(li_block[k][1]==1){
                cols[1].push(li_block[k]);
            }
            else if(li_block[k][1]==2){
                cols[2].push(li_block[k]);
            }
            else{
                cols[3].push(li_block[k]);
            }
        }
        for(var o=0;o<4;o++){
            for(var l=0;l<cols[o].length-1;l++){
                var is_sort = true;
                for(var p=0;p<cols[o].length-l-1;p++){
                    if(cols[o][p][0]<cols[o][p+1][0]){
                        var mid = cols[o][p];
                        cols[o][p] = cols[o][p+1];
                        cols[o][p+1] = mid;
                        is_sort = false;
                    }
                }
                if(is_sort==true){
                    break;
                }
            }
            //合并相同值的块
            for (var i=0;i<cols[o].length-1;i++){
                if(cols[o][i][2]==cols[o][i+1][2]){
                    cols[o][i][2] = parseInt(cols[o][i][2])*2;
                    cols[o].splice(i+1,1);
                }
            }

            //改变块位置，全部左移
            for (var m=0;m<cols[o].length;m++){
                cols[o][m] = [3-m, cols[o][m][1], cols[o][m][2]];
                res.push(cols[o][m]);
            }
        }
        // li_block = res;
        return res;
    }

    //重设块坐标
    function reset_coor() {
        main_box.innerHTML = '';
        var mid_li = li_block;
        li_block = [];
        for(var n=0;n<mid_li.length;n++){
            var x = mid_li[n][0];
            var y = mid_li[n][1];
            var value = mid_li[n][2];
            // alert(x + '--' + y);
            produce_block(x, y, value);
        }
    }

    //判断游戏是否结束
    function is_failed() {
        var rows = move_up();
        var cols = move_left();
        if(rows.length==16 && cols.length==16){
            return true;
        }
        return false;
    }

    //判断是否完成2048
    function is_win() {
        for(var i=0;i<li_block.length;i++){
            if(li_block[i][2]==2048){
                return true;
            }
        }
        return false;
    }
};
