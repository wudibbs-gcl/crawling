#coding:utf-8


import itchat
import jieba
import matplotlib.pyplot as plt
import snownlp
from PIL import Image
import numpy
import wordcloud
import TencentYoutuyun

# 获得好友信息
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)
# print(friends)


def analyseSex(firends):
	sexs = list(map(lambda x:x['Sex'],friends[1:]))
	counts = list(map(lambda x:x[1],Counter(sexs).items()))
	labels = ['Unknow','Male','Female']
	colors = ['red','yellowgreen','lightskyblue']
	plt.figure(figsize=(8,5), dpi=80)
	plt.axes(aspect=1)
	plt.pie(counts, #性别统计结果
				labels=labels, #性别展示标签
				colors=colors, #饼图区域配色
				labeldistance = 1.1, #标签距离圆点距离
				autopct = '%3.1f%%', #饼图区域文本格式
				shadow = False, #饼图是否显示阴影
				startangle = 90, #饼图起始角度
				pctdistance = 0.6 #饼图区域文本距离圆点距离
	)
plt.legend(loc='upper right',)
plt.title(u'%s的微信好友性别组成' % friends[0]['NickName'])
plt.show()
plt.legend()