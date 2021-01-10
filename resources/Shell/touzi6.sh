#!/bin/bash

#此脚本使用方法:请先运行dianshu6=(对方输入的点数)这个命令（可以通过查看echo $dianshu6来查看输入的数值），然后再chmod 777 touzi6.sh，然后再用./touzi6.sh运行此脚本。

#此脚本用于传六。

panding=$[RANDOM%6+1]
if ["$dianshu" -ge "$panding"]
then
        echo $panding
        echo 判定成功
 else
        echo $panding
        echo 判定失败
fi
