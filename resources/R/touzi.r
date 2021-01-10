#不一定能用
while (1==1){
    dianshu <- exit(dianshu)
    cishu <- exit(cishu)
    jizhi <- exit(jizhi)
      bod <- exit(bod)
     while (cishu>0)
    {
        panding <- sample(1:jizhi,cishu)
            if(dianshu-bod>=panding){
                print(panding)
                print("判定成功")
            }else{
                print(panding)
          print("判定失败")
    }
}


