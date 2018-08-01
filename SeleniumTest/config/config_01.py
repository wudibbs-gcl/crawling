# config/config_01.py

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import *

# config配置部分


# 浏览器种类维护在此

browser_config = {
			'ie':webdriver.Ie,
			'chrome':webdriver.Chrome,
			'firefox':webdriver.Firefox
}



# 元素抓取定位信息维护在此处，维护结构由外到内为：页面名称---页面下元素名称---元素的定位方式+参数
locat_config = {
	'博客园首页':{
		'找找看输入框':['id','zzk_q'],
		'找找看按钮':['xpath','//input[@value="找找看"]']
	}
}