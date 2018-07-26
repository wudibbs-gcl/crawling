#coding:utf-8

#使用爬虫爬取数据前，我们需要解析网站robots.txt文件
 
import urllib.request
import urllib.error 
import re #正则表达式
import urllib.parse #将url链接从相对路径（浏览器可懂但python不懂）转为绝对路径（python也懂了）
import urllib.robotparser #爬取数据前解析网站robots.txt文件，避免爬取网站所禁止或限制的


def download(url, user_agent = "brain", num_retries = 2):  #下载url网页
    print("downloading：",url)
    header = {"user-agent": user_agent} #设置用户代理，而不使用python默认的用户代理Python-urllib/3.6
    req = urllib.request.Request(url, headers = header)
    try:
        html = urllib.request.urlopen(req).read()
    except urllib.error.URLError as e:    #下载过程中出现问题
        print("download error：",e.reason)
        html = None
 
        if num_retries > 0:     #错误4XX发生在请求存在问题，而5XX错误则发生在服务端存在问题，所以在发生5XX错误时重试下载
            if hasattr(e, "code") and 500<= e.code <600:
                return  download(url, user_agent, num_retries-1)  # recursively retry 5XX HTTP errors
    return html
#download("http://example.webscraping.com") #访问正常
#download("http://httpstat.us/500") #这个网页测试用，一直是5XXerror
 
#跟踪链接的爬虫：link_crawler()函数传入两个参数：要爬取的网站URL、用于跟踪链接的正则表达式。
def link_crawler(seed_url, link_regex):
    """先下载 seed_url 网页的源代码，然后提取出里面所有的链接URL，接着对所有匹配到的链接URL与link_regex 进行匹配，
	如果链接URL里面有link_regex内容，就将这个链接URL放入到队列中，
	下一次 执行 while crawl_queue: 就对这个链接URL 进行同样的操作。
	反反复复，直到 crawl_queue 队列为空，才退出函数。"""
    crawl_queue = [seed_url]
    seen = set(crawl_queue) #有可能链接中互相重复指向，为避免爬取相同的链接，所以我们需要记录哪些链接已经被爬取过(放在集合seen中)，若已被爬取过，不再爬取
    while crawl_queue:
        url = crawl_queue.pop()
        
        rp = urllib.robotparser.RobotFileParser()   #爬取前解析网站robots.txt，检查是否可以爬取网站，避免爬取网站禁止或限制的
        rp.set_url("http://www.sina.com/robots.txt")
        rp.read()
        user_agent = "brain" #这里就是你爬取网站所使用的的代理
        if rp.can_fetch(user_agent, url):
            html = download(url)
            html = str(html)
            #filter for links matching our regular expression
            if html == None:
                continue
            for link in get_links(html):
                if re.match(link_regex, link):
                    link = urllib.parse.urljoin(seed_url, link) #把提取的相对url路径link(view/178)转化成绝对路径(/view/Poland-178)link
                    if link not in seen:  #判断是否之前已经爬取
                        seen.add(link) #之前没有的话加在集合中以便后续继续判断
                        crawl_queue.append(link) #之前没有的话这个链接可用，放在列表中继续进行爬取
        else:
            print("Blocked by %s robots,txt" % url)
            continue
        
def get_links(html):
    """用来获取一个html网页中所有的链接URL"""
    #做了一个匹配模板 webpage_regex，匹配 <a href="xxx"> or <a href='xxx'>这样的字符串，并提取出里面xxx的URL，请注意这里的xxxURL很可能是源码中相对路径，eg view/1 正常访问肯定是打不开的
    webpage_regex = re.compile('<a href=["\'](.*?)["\']', re.IGNORECASE)
    return re.findall(webpage_regex,html)
    #return re.findall('<a[^>]+href=["\'](.*?)["\']', html)也可以这样实现，但没有上面的先编译模板再匹配好                                                    
 
#只想找http://www.sina.com
#只想找http://www.sina.com
#只想找http://example.webscraping.com/index... or http://example.webscraping.com/view...
link_crawler("http://www.sina.com", "/(index|view)")
