import requests
import json


r = requests.get('http://www.baidu.com/')#不带参数的get请求
r1 = requests.get('http://www.baidu.com/',params={'wd':'123'})#带参数的get请求

requests.post('http://www.baidu.com/',data=None,json=None)#post请求
requests.put('http://www.baidu.com/')#put请求
requests.delete('http://www.baidu.com/')#delete
requests.head('http://www.baidu.com/')
requests.options('http://www.baidu.com/')

# 为url传递参数
urlParams = {"key":'value'}
r = requests.get('http://www.baidu.com/',params=urlParams)
# print(type(r))
# print(r.url)# 打印url字符串 http://www.baidu.com/?key=value


# response
# print(r.encoding)#获取当前编码
# r.encoding = 'utf-8'#设置编码为utf-8
# print(r.text)#将encoding解析后的内容，字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# print(r.content)#以字节形式返回，字节方式的响应体，会自动为你解码gzip和deflate压缩
# print(r.headers)#字典对象存储响应头，字典键不区分大小写，若键不存在则返回None
# print(r.status_code)
# print(r.raw)#返回原始响应体，也就是urllib的response对象，使用r.raw.read()
# print(r.ok)# 查看r.ok的布尔值，可以知道是否登录成功

# # 特殊方法
# # print(r.json())#Requests中内置的JSON解析器，以JSON形式返回，提前返回的内容确保是JSON格式的，不然解析出错，会抛出异常
# r.raise_for_status()#如果不是200，可以使用 r.raise_for_status() 抛出异常

# post发送json请求
# r = requests.post('https://api.github.com/some/endpoint',data=json.dumps({'some':'data'}))
# # print(r.json())

# # 定制头和Cookie信息
# header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
# 						AppleWebKit/537.36 (KHTML, like Gecko)\
#  						Chrome/66.0.3359.181 Safari/537.36'}
# cookie = {'key':'value'}# 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
# data = {'some':'data'}
# # 带header,cookie
# r = requests.get('https://api.github.com/some/endpoint',headers=header,cookies=cookie)
# # 带参数，header，cookie
# r = requests.get('https://www.baidu.com/some/endpoint',data=data,headers=header,cookies=cookie)
# # print(r.cookies)# 返回cookies信息
# # print(r.history)#返回重定向信息,当然可以在请求是加上allow_redirects = false 阻止重定向

# # timeout
# r = requests.get('https://www.baidu.com/some/endpoint',timeout=10)


# # 会话对象
# s = requests.Session()
# s.auth=('auth','pwd')
# s.headers = {'key':'value'}
# s.get('https://www.baidu.com/')

# # Proxies 代理
# proxies = {"http":'ip1','http':'ip2'}
# # 如果代理需要用户名和密码，则需要这样
# proxies1 = {
# 	"http":"http://user:passwd@xxx.xxxx.xxx.xxx:port/"
# }
# requests.get('https://www.baidu.com/',proxies=proxies)



# xml请求
#! /usr/bin/python3

# class url_request():
#     def __init__(self):
#         """init"""

# if __name__ == '__main__':
#     heards = {'Content-type': 'text/xml'}
#     XML = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><Request xmlns="http://tempuri.org/"><jme><JobClassFullName>WeChatJSTicket.JobWS.Job.JobRefreshTicket,WeChatJSTicket.JobWS</JobClassFullName><Action>RUN</Action><Param>1</Param><HostIP>127.0.0.1</HostIP><JobInfo>1</JobInfo><NeedParallel>false</NeedParallel></jme></Request></soap:Body></soap:Envelope>'
#     url = 'http://jobws.push.mobile.xxxxxxxx.com/RefreshWeiXInTokenJob/RefreshService.asmx'
#     r = requests.post(url=url, heards=heards, data=XML)
#     data = r.text
#     print(data)


# 异常处理

# URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
# try:
#     r = requests.get(URL, params={'ip': '8.8.8.8'}, timeout=1)
#     r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
# except requests.RequestException as e:
#     print(e)
# else:
#     result = r.json()
#     print(type(result), result,sep='\n')



#  会话对象，同一个实例对象发出的所有请求之间保持cookies，
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 
s = requests.Session()
s.headers.update(headers)
# s.auth = ('superuser', '123')
s.get('https://www.kuaipan.cn/account_login.htm')
 
_URL = 'http://www.kuaipan.cn/index.php'
s.post(_URL, params={'ac':'account', 'op':'login'},
       data={'username':'****@foxmail.com', 'userpwd':'********', 'isajax':'yes'})
r = s.get(_URL, params={'ac':'zone', 'op':'taskdetail'})
print(r.json())
s.get(_URL, params={'ac':'common', 'op':'usersign'})