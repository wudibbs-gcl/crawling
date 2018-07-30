#coding:utf-8



# 1.将字符串转换为字节的方式称为编码 >>> encode
# 2.将字节转换为字符串的方式称为解码 >>> decode

s='林' #当程序执行时，无需加u，'林'也会被以unicode形式保存新的内存空间中,

#s可以直接encode成任意编码格式
s1=s.encode('utf-8')
s2=s.encode('gbk')



print(s) #林
print(s1) #b'\xe6\x9e\x97' 在python3中，是什么就打印什么
print(s2) #b'\xc1\xd6' 同上

print(type(s)) #<class 'str'>
print(type(s1)) #<class 'bytes'>
print(type(s2)) #<class 'bytes'>

 #      decode                 encode
# str ---------> str(Unicode) ---------> str

import requests
url = 'http://www.baidu.com'
r = requests.get(url)
text = r.content# r.text是字符串方式的响应体，r.content是字节方式的响应体
print(text.decode("utf-8"))# 解码：将十六进制Unicode编码，解码成中文字符串
