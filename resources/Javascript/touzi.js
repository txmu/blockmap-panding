var dianshu = prompt("请输入对方使用的点数:");
var cishu = prompt("请输入对方判定的次数");
var jizhi = prompt("请输入判定上限。传六填6，十点制填10");
var bod = prompt('被进攻地块是否有防御或被进攻方是否有防御的buff或己方是否有减进攻概率的debuff?写出减少的进攻概率，如果己方有增加进攻几率的buff或被进攻方有减防御的debuff，可以填负数。没有请填0:');
parseInt(dianshu);
parseInt(cishu);
parseInt(jizhi);
parseInt(bod);
function randomNum(minNum,maxNum){ 
    switch(arguments.length){ 
        case 1: 
            return parseInt(Math.random()*minNum+1,10); 
        break; 
        case 2: 
            return parseInt(Math.random()*(maxNum-minNum+1)+minNum,10); 
        break; 
            default: 
                return 0; 
            break; 
    } 
};
alert("判定了"+cishu+"次");
while (cishu>0) {
    var panding=randomNum(1,jizhi);
    var cishu=cishu-1;
    if (dianshu-bod>=panding) {
            alert(panding+'判定成功');
    }else{
            alert(panding+'判定失败');
    };
};   
   