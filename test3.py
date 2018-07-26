#coding:utf-8

import re
from test2 import download

# 链接爬虫

def linkCrawler(seedUrl,linkRegex):
	crawlQueue = [seedUrl]
	while crawlQueue:
		url = crawlQueue.pop()
		html = download(url)
		for link in getLinks(html):
			if re.match(linkRegex, link):
				crawlQueue.append(link)
	return crawlQueue

	
def getLinks(html):
	webpageRegex = re.compile('<a[^>]href=["\'](.*?)["\']',re.IGNORECASE)
	return webpageRegex.findall(html.decode('utf-8'))

print(linkCrawler("http://example.webscraping.com/index/1", "/(index|view)"))