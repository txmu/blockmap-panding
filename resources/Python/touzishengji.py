import random

zuozhe=input('判定者:')
zongwanjia=[]
while 1==1:
    wanjia=input('玩家:')
    zongwanjia.append(wanjia)
    dianshu=int(input('请输入对方使用的点数:'))
    cishu=int(input('请输入对方判定的次数:'))
    jizhi=int(input('请输入判定上限，传六填6，十点制填10:'))
    bod=int(input('被进攻地块是否有防御或被进攻方是否有防御的buff或己方是否有减进攻概率的debuff?写出减少的进攻概率，如果己方有增加进攻几率的buff或被进攻方有减防御的debuff，可以填负数。没有请填0:'))
    print(wanjia,'判定了',cishu,'次')
    while cishu>0:
        panding=random.randint(1,jizhi)
        cishu=cishu-1
        if ( dianshu-bod>=panding ):
            print(panding,'判定成功')
        else:
            print(panding,'判定失败')
    xuqiu=input('您是否需要列出数据?输入其它数据将会退出程序。(yes/no)')
    if ( xuqiu=='yes'):
        print(zuozhe,'同志')
        print(zongwanjia)
    elif ( xuqiu=='no' ):
        print('ok')
    else:
        break
#我感觉那么简单的东西，就是初学者也能看懂，所以就不注释了。