#coding:utf-8

import builtwith#查看网站使用的技术，安装：pip install builtwith
import whois# 查看网站所有者信息 ，安装：pip install python-whois
import urllib

# builtTechology = builtwith.parse(urlAddress)
# print(builtTechology)
# print(whois.whois("www.baidu.com"))

'''
请求网页地址，读取响应数据，并作出异常判断
'''
def download(url,numRetries=2):
	print ("Downloading url:",url)
	try:
	 	html = urllib.request.urlopen(url).read()
	except urllib.error.URLError as e:
	 	print ("Downloading error:",e.reason)
	 	html = None
	 	if numRetries > 0:
	 		# 遇到500错误时，重试2次如果还是500则放弃
	 		if hasattr(e, 'code') and 500 <= e.code < 600:
	 			return download(url,numRetries-1)
	return html

# 请求http://httpstat.us/500 返回500
# urlAddress = "http://httpstat.us/500"
urlAddress = "http://www.meetup.com"

print ("Downloading url is:",download(urlAddress))