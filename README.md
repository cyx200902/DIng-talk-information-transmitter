 **Github/[Gitee](http://gitee.com/cyx200902/ding-talk-information-transmitter)**
# DIng-talk information transmitter

#### 介绍
一款开源的esp8266开发的钉钉消息发送器，可以自定义事件发送信息提醒

#### 硬件说明
1.esp8266开发板（推荐）


#### 安装教程

1.下载固件[esp8266-20210902-v1.17.bin](http://github.com/cyx200902/ding-talk-information-transmitter/blob/master/tools/esp8266-20210902-v1.17.bin)

2.安装固件烧录库

    pip install esptool

3.安装驱动[CP210x_Universal_Windows_Driver.zip](https://github.com/cyx200902/ding-talk-information-transmitter/blob/master/tools/CP210x_Universal_Windows_Driver.zip)

4.执行命令

    esptool.py --port COM10 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20210902-v1.17.bin

5.使用micropython REPL连接开发板[MicroPython File Uploader.exe](http://github.com/cyx200902/ding-talk-information-transmitter/blob/master/tools/MicroPython%20File%20Uploader.exe)

6.烧录boot.py

7.更改main.py中appkey，appsecret，chatid等配置信息

8.烧录main.py

9.打开micropython REPL

10.REST主板

11.根据提示输入WiFi名和密码

12.等待wifi连接

13.成功


#### 使用说明

1.  开机发送开机提示
2.  自带参考自定义信息发送
3.  可根据需求二次开发

#### 参与贡献

1.  开发:[轩轩](http://gitee.com/cyx200902)
2.  开发板赞助:龙龙


#### 其他说明

1.  需要连接wifi
2.  appkey，appsecret，chatid等信息需要在钉钉开发者后台注册企业内部应用获取[钉钉开放平台](http://open-dev.dingtalk.com/)
3.  重置wifi信息在micropython REPL中输入`re_do_connect()`，按照步骤提示重置wifi信息
4.  英语帮助在micropython REPL中输入`dingtalk_help()`

