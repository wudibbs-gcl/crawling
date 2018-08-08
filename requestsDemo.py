import requests
import xlwt


'''requests模块抓取网页源码并保存到文件示例'''
html = requests.get("http://www.baidu.com")
with open('test.txt', 'w',encoding="utf-8") as f:
    f.write(html.text)


# 读取test.txt
with open('test.txt','r') as f:
	strs = f.read()
	strs = strs.strip(';').strip('\n').strip('\t').strip('\r')
	strs = strs.split(' ')


# 将test.txt内容写到execl中
# print(len(strs))
book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')
row = 0
for index,values in enumerate(strs):
	if index+1 % 5 != 0:
		
		sheet.write(row,col,values)
		col += 1
	else:
		row += 1
		col = 0
		sheet.write(row,col,values)
		col += 1
	

book.save('txtWriteExcel.xls')
