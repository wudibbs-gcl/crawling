#coding:utf-8

'''
MongoDB 数据库操作
'''


from pymongo import MongoClient

client = MongoClient("localhost",27017)# 通过pymongo模块连接MongoDB
url