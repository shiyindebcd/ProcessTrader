@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~0"" h",0)(window.close)&&exit
:begin
C:
cd C:\Users\shiyinde\Desktop\进程交易者
python main.py
