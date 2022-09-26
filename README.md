# 进程交易者
<br/>

## 介绍
<br/>
一个用python实现的，基于pyside6和天勤SDK的，多用户，多进程期货程序化交易框架，可实现完全无人职守的自动化国内期货交易，或者半程序化交易  
<br/><br/>


## 软件架构
<br/>
软件基于pyside6实现各种界面，天勤sdk的包用于实际的期货交易过程  
<br/><br/> 


## 安装教程
<br/>

1. 先安装python， 建议python版本在3.9以上
<br/>

2. 在cmd里输入以下命令，安装必要的python包
~~~
pip install pyside6 -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install tqsdk2 -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install tqsdk -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install ping3 -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple/

pip install pyqtgraph -i https://pypi.tuna.tsinghua.edu.cn/simple/

~~~

3. 运行*main.py*  即可启动程序
   
---


<br/><br/>
## 使用说明
<br/>

将*自启动脚本.bat*  这个文件里的第6行  

~~~
cd E:\进程交易者
~~~

这个地址改成你自己的本软件文件夹地址

双击 自启动脚本.bat 即可运行软件

<br/>

要想让软件开机自启支, 就对这个bat文件创建个快捷方式，放到
~~~
C:\Users\你的电脑用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 
~~~
文件夹下，即可实现开机自启动软件
<br/><br/><br/><br/>
## 主题切换
<br/>
在  main.py  中,把 THEME 改成 dark 或 light ,即可切换到两种主题
<br/><br/><br/><br/>
## 详解视频
<br/>
软件的详细用法请参考B站的视频解说

[点此跳转到B站视频链接](https://www.bilibili.com/video/BV1tY4y177sv?share_source=copy_web&vd_source=0f0ae5e8365c85cd112830a14d80cef6)
