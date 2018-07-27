#coding:utf-8


'''
爬取100万个网页

'''

import csv
from zipfile import ZipFile
from io import StringIO
from downloader import Downloader

d = Downloader()
print(type(d))