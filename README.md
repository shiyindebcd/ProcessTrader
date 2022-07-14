# 进程交易者


#### 介绍
一个用python实现的，基于pyside6和天勤SDK的，多用户，多进程期货程序化交易框架，可实现完全无人职守的自动化国内期货交易，或者半程序化交易


#### 软件架构
软件基于pyside6实现各种界面，天勤sdk的包用于实际的期货交易过程


#### 安装教程

1
先安装python， 建议python版本在3.9以上

2
在cmd里输入以下命令，安装必要的python包


pip install pyside6 -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install tqsdk2 -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install tqsdk -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install ping3 -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple/




3
运行main.py



#### 使用说明

将  自启动脚本.bat  这个文件里的第6行  cd E:\进程交易者
这个地址改成你自己的本软件文件夹地址
双击 自启动脚本.bat 即可运行软件

然后对这个bat文件创建个快捷方式，放到C:\Users\你的电脑用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 文件夹下，即可实现开机自启动软件

其他详细用法请参考B站的视频解说
