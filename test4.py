#coding:utf-8

# 3种抓取网页数据的方法: re, BeautifulSoup,lxml


# 链接爬虫添加缓存支持

class Downloader(object):
	"""docstring for Downloader"""
	def __init__(self, delay=5,
		user_agent="wswp",proxies=None,
		numRetries=1,cache=None):

		super(Downloader, self).__init__()
		self.throttle = Throttle(delay)
		self.user_agent = user_agent
		self.proxies = proxies
		self.numRetries = numRetries
		self.cache = cache

	def __call__(self):
		result = None
		if self.cache:
			try:
				result = self.cache[url]
			except KeyError as e:
				pass
			else:
				if self.numRetries >0 and 500<= result['code'] <600:
					result = None

		if result is None:
			self.throttle.wait(url)


		