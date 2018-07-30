from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')# 解析器：Python标准库 	BeautifulSoup(markup, "html.parser")
tag = soup.a
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.p)
tag.name = 'block'
# print(tag)
# # print(soup.li)
# print(soup.body)
# print(soup.get_text())# 文档中文字内容
# for link in soup.find_all('a'):
#     print(link.get('href'))

# attributes属性
# print(tag['class'])#['sister']
# print(tag.attrs)#{'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}

# css_soup = BeautifulSoup('<p class="body strikeout"></p>','html.parser')
# print(css_soup.p['class'])# ['body', 'strikeout']

print(tag.string)
# print(type(tag.string))

unicode_string = tag.string # Python3 取消unicode()函数，默认是utf-8编码
unicode_string
print(type(unicode_string))

# 处理注释
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,'html5lib') # 解析HTML或xml文档：内置html.parser,lxml,html5lib
comment = soup.b.string
print(type(comment))
# <class 'bs4.element.Comment'>