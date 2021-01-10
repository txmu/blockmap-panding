#!/bin/bash

#此脚本使用方法:请先运行dianshu10=(对方输入的点数)这个命令（可以通过查看echo $dianshu10来查看输入的数值），然后再chmod 777 touzi10.sh，然后再用./touzi10.sh运行此脚本。

#此脚本用于十点制。

panding=$[RANDOM%10+1]
if ["$dianshu10" -ge "$panding"]
then
        echo $panding
        echo 判定成功
 else
        echo $panding
        echo 判定失败
fi
