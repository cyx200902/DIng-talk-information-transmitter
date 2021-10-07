#by http://github.com/cyx200902
#   http://gitee.com/cyx/200902
#email        3603695237@qq.com

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
######################################################################


import sys

from machine import Pin
import time
p2 = Pin(2, Pin.OUT)
print("on")
time.sleep(2)
p2.value(1)


def dingtalk_help():
    dingtalk_help_en=\
    """
    
Using translation software, there may be syntax errors!!!    
Instructions for intelligent Internet information terminal
1) The project is open source, please specify the use of adaptation
2) The project needs to be used with esp8266 ch340g serial WiFi development board
3) Using micro Python firmware (esp8266-20210902-v1.17. Bin)
4) Specific instructions
a) Download firmware
b) Install firmware burning Library
pip install esptool
c) Install the drive
d) Execute command
esptool.py --port COM10 --baud 460800 write_ flash --flash_ size=detect -fm dio 0 esp8266-20210902-v1.17.bin
e) Burn boot.py
F) change appkey, appsecret, chatid and other configuration information in main.py
g) Burn main.py
h) Open micro Python repl
I) rest motherboard
J) enter the WiFi name and password as prompted
k) Waiting for WiFi connection
L) success
5) Appkey, appsecret, chatid and other information need to be obtained by registering the enterprise internal application in the nailing developer background https://open-dev.dingtalk.com/
    """
    print(dingtalk_help_en)



#sys.path.append('examples')


def is_legal_wifi(essid, password):
    if len(essid) == 0 or len(password) == 0:
        return False
    return True


def do_connect():
    import json
    import network


    try:
        with open('wifi_config.json', 'r') as f:
            config = json.loads(f.read())
    except:
        essid = ''
        password = ''

        while True:

            print()
            print("Intelligent Internet information terminal")
            print("by http://github.com/cyx200902")
            print("The document is at https://gitee.com/cyx200902/ding-talk-information-transmitter")
            essid = input('wifi name:')
            password = input('wifi passwrod:')

            if is_legal_wifi(essid, password):
                config = dict(essid=essid, password=password)
                with open('wifi_config.json', 'w') as f:
                    f.write(json.dumps(config))
                break
            else:
                print('ERROR, Please Input Right WIFI')

    wifi = network.WLAN(network.STA_IF)
    if not wifi.isconnected():
        print('connecting to network...')
        wifi.active(True)
        wifi.connect(config['essid'], config['password'])
        import utime

        for i in range(200):
            print('Connect WiFi for {} times'.format(i))
            if wifi.isconnected():
                p2.value(0)
                time.sleep(3)
                p2.value(1)
                break
            p2.value(0)
            utime.sleep_ms(50)
            p2.value(1)
            utime.sleep_ms(50)

        if not wifi.isconnected():
            wifi.active(False)
            print('wifi connection error, please reconnect')
            import os
            try:
                os.remove('wifi_config.json')
            except:
                pass
            do_connect()
        else:
            print('network config:', wifi.ifconfig())

def re_do_connect():
    import os
    print("Are you sure to delete WiFi information?(Y/N)")
    delete=input("")
    if delete=="Y":
        os.remove("wifi_config.json")
        print("WiFi information deleted successfully,Please reconfigure WiFi information")
        do_connect()
    elif delete=="y":
        os.remove("wifi_config.json")
        print("WiFi information deleted successfully,Please reconfigure WiFi information")
        do_connect()
    else:
        exit()


do_connect()