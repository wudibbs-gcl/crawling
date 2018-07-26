#coding:utf-8
import urllib
import urllib.request
import itertools
# import urllib.parse


'''
设置用户代理:
python2中使用的默认代理是Python-urllib/2.7下载网页内容。
容易遭到封IP
'''

def download(url,user_agent=None,numRetries=2):
	# print ("Downloading url:",url)
	headers = {"User_agent":user_agent}
	req = urllib.request.Request(url,headers)
	try:
	 	html = urllib.request.urlopen(url).read()
	except urllib.error.URLError as e:
	 	# print ("Downloading error:",e.reason)
	 	html = None
	 	if numRetries > 0:
	 		# 遇到500错误时，重试2次如果还是500则放弃
	 		if hasattr(e, 'code') and 500 <= e.code < 600:
	 			return download(url,user_agent,numRetries-1)
	return html

# urlAddress = "http://www.meetup.com"
# print ("Downloading url is:",download(urlAddress))
if __name__ == '__main__':
	# 连续中断5次下载，才会停止遍历
	maxErrors = 5# 最大下载错误次数
	numErrors = 0# 当前下载错误次数
	for page in itertools.count(start=0, step=1):
		url = 'http://example.webscraping.com/view/-%d' %(page)
		html = download(url)
		# print(html)
		break
		if html is None:
			numErrors += 1
			if numErrors == maxErrors:
				break
		else:
			numErrors = 0
