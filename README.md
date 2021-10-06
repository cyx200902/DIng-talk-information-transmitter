# DIng-talk information transmitter

#### 介绍
一款开源的esp8266开发的钉钉消息发送器，可以自定义事件发送信息提醒

#### 硬件说明
1.esp8266开发板（推荐）


#### 安装教程

1.下载固件

2.安装固件烧录库

    pip install esptool

3.安装驱动

4.执行命令

    esptool.py --port COM10 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20210902-v1.17.bin

5.烧录boot.py

6.更改main.py中appkey，appsecret，chatid等配置信息

7.烧录main.py

8.打开micropython REPL

9.REST主板

10.根据提示输入WiFi名和密码

11.等待wifi连接

12.成功


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

