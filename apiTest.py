#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-01 18:39
# 
#  使用Excel测试用例实现简单接口测试
import requests,xlrd, json


class ApiTest:
    # 请求主方法
    def request(self, rqtype, rqurl, paramete, headers):
        self.rqurl = rqurl  # API地址
        self.rqtype = rqtype  # 请求类型get or post
        self.paramete = paramete  # 请求参数
        self.headers = headers  # 请求头

        if rqtype == "get":
            apirqhttp = requests.get(url=rqurl, params=paramete, headers=headers)  # 发送请求
            code = apirqhttp.status_code  # 保存返回状态
            pam = apirqhttp.text  # 保存返回数据并将json转为dict
            return code, pam
        if rqtype == "post":
            apirqhttp = requests.post(url=rqurl, data=paramete, headers=headers)
            code = apirqhttp.status_code
            pam = apirqhttp.text
            return code, pam
        else:
            print ("请求参数错误，请求类型只支持get+post，请求地址支持string，参数支持dict")

    # 获取B2B分销商token值方法
    def seltoken(self):
        rqtypes = "post"
        rqurls = "http://xxxxx.dddd.com//account/authorize"
        parametes = {"username": "Wbfxs001", "password": "111111Qq", "grant_type": "password"}
        headers = None
        cod, pam = ApiTest().request(rqtypes, rqurls, parametes, headers)  # 掉用request方法请求登录
        pam = json.loads(pam)  # 保存返回数据并将json转为dict
        access_token = pam["access_token"]  # 截取dic中access_token键的value
        access_token = "bearer " + str(access_token)  # 拼接access_token为最终需要的token值
        return access_token

    def xlsee(self, xlsFile):
        rqapi = xlrd.open_workbook(xlsFile)   # 获得文件对象
        sheet_name = rqapi.sheet_names()[0]  # 获取第一个sheet名称
        sheet = rqapi.sheet_by_name(sheet_name)  # 获取第一个sheet对象
        return sheet

if __name__ == "__main__":
    apitest = ApiTest()
    xlsFile = r"D:\RequestAPI.xlsx"  # 文件路径
    sheet1 = apitest.xlsee(xlsFile)
    nrow = sheet1.nrows   # 获取行总数
    ncols = sheet1.ncols  # 获取列总数
    col_data = sheet1.col_values(0)  # 获取第一列的数据

    for i in range(1, nrow):  # 循环每行，并获取每行每列的值
         row_data = sheet1.row_values(i)  # 获取第i行的数据
         nums = int(row_data[0])  # 获取第i行的某个数据
         rqtypes = str(row_data[2])
         rqurls = str(row_data[1])
         a = row_data[5:]
         parametes = dict(zip(a[0::2], a[1::2]))
         code = row_data[3]
         coderesult = row_data[4]

         access_token = apitest.seltoken()  # 获取token
         headers = {"Authorization": access_token}
         codetest, pamtest = apitest.request(rqtypes, rqurls, parametes, headers)
         print ("用例编号：", nums, "code码：", codetest)
         print (pamtest)