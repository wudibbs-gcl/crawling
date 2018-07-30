# 遍历文档树
# 通过这段例子来演示怎样从文档的一段内容找到另一段内容


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

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.head)# <head><title>The Dormouse's story</title></head>
# print(soup.body.b)

# 通过点取属性的方式只能获得当前名字的第一个tag
# print(soup.a) #<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# 如果想要得到所有的<a>标签,或是通过名字得到比一个tag更多的内容的时候,就需要用到 Searching the tree 中描述的方法,比如: find_all()
# print(soup.find_all())
# print(type(soup.find_all()))
# for x in soup.find_all('a'):# 遍历所有a节点
# 	print(x)

# tag的 .contents 属性可以将tag的子节点以列表的方式输出
head_tag = soup.head
# print(head_tag.contents)# [<title>The Dormouse's story</title>]
title_tag = head_tag.contents[0]
# print(title_tag)# tag的.contents属性可以将tag的子节点以列表的方式输出

# BeautifulSoup对象本身一定会包含子节点，也就是说<html>标签也是BeautifulSoup对象子节点
# 字符串没有.contents属性，因为字符串没有子节点
# print(len(soup.contents[0]))
# print(len(soup.contents[1]))
# for child in title_tag.children:# 通过tag的.children生成器，可以对tag子节点进行循环
# 	print(child)


# 如果tag只有一个NavigableString类型子节点，那么这个tag可以使用.string得到子节点
# print(title_tag.string)

# 输出的字符串可能包含很多空格或空行，使用.stripped_strings可以去除多余空白
# 全部是空格的行会被忽略掉,段首和段末的空白会被删除
for string in soup.stripped_strings:
	# print(string.replace('\t','').replace('\n','').replace('\r',''))
	print(string)
	# print(''.join(string.split("\t|\n|\r")))


