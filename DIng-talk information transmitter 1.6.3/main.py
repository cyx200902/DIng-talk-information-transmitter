#by http://github.com/cyx200902
#   http://gitee.com/cyx/200902
#email        3603695237@qq.com
import urequests
import json
import time
from machine import Pin
import utime
p2 = Pin(2, Pin.OUT)
def get_accesstoken(appkey,appsecret):
	p2.value(0)
	time.sleep(1)
	p2.value(1)

	adata = {
		"appKey":appkey,
		"appSecret":appsecret
	}

	aheaders = {"Host":"api.dingtalk.com","Content-Type":"application/json"}

	url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"

	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	utime.sleep_ms(100)
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	utime.sleep_ms(100)
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	response = urequests.post(url, headers=aheaders, data=json.dumps(adata))
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	utime.sleep_ms(100)
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	utime.sleep_ms(100)
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)

	responsetext=json.loads(response.text)
	accesstoken=responsetext["accessToken"]
	return accesstoken
	#print(accesstoken)

def send_text(accesstoken,chatid,title,text):
	bdata = {
		"chatid":chatid,
		"msg":{
		"markdown":{
			"title":title,
			"text":text
		},
		"msgtype":"markdown"
		}
	}

	bheaders = {"Host":"api.dingtalk.com","Content-Type":"application/json"}

	burl = "https://oapi.dingtalk.com/chat/send?access_token="+accesstoken

	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	utime.sleep_ms(100)
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	utime.sleep_ms(100)
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	bresponse = urequests.post(burl, headers=bheaders, data=json.dumps(bdata))
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)
	utime.sleep_ms(100)
	p2.value(0)
	utime.sleep_ms(100)
	p2.value(1)

	bresponsetext=json.loads(bresponse.text)

	bcode=bresponsetext["errmsg"]
	p2.value(0)
	time.sleep(1)
	p2.value(1)
	return bcode


appkey="your-appkey"
appsecret="your-appsecret"
access=get_accesstoken(appkey,appsecret)
chatid="your-chatid"
title="Powered on  "
text="# Powered on in"+str(time.time())+"![alt a](https://images.gitee.com/uploads/images/2021/1005/182533_f7ac0b4a_7438896.png)"
mcode=send_text(access,chatid,title,text)
print(mcode)


while True:
	key = Pin(4, Pin.IN, Pin.PULL_UP)
	value1=key.value()
	value2=1
	if value1 != value2:
		print("buttun on")
		access = get_accesstoken(appkey, appsecret)
		title2 = "key on  "
		text2 = "# key on in" + str(time.time()) + "![alt a](https://images.gitee.com/uploads/images/2021/1006/132043_426613d1_7438896.png)"
		mcode2 = send_text(access, chatid, title2, text2)
		print(mcode)










