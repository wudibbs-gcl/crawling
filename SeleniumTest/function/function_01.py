# function/function_01.py

from encapsulation.encapsulation import UIHandle
from constant.constant_1 import LOGIN_URL
from config.config_01 import browser_config
from time import sleep

def search(msg):
	# 打开浏览器
	driver = browser_config['chrome']
	# 传入driver对象
	uihandle = UIHandle(driver)
	# 输入URL地址
	uihandle.get(LOGIN_URL)
	# 调用二次封装后的方法，此处可见操作了哪个页面，
	# 哪个元素，msg是要插入的值，插入值得操作在另外一个用例文件中传入
	uihandle.Input('博客园首页','找找看输入框',msg)
	uihandle.Click('博客园首页','找找看按钮')
	uihandle.quit()