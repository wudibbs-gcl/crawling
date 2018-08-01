#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
#但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。



class A(object):
	bar = 1
	def fun1(self):
		print('foo')

	@classmethod
	def func2(cls):
		print('func2')
		print(cls.bar)
		cls().fun1()

A.func2()


# 如果我们有多个模块，每个模块下面都写了很多Python文件
# 每个Python文件里面都有测试用例，怎么把目录下所有用例都执行了呢？
# 答案是找到每个Python文件，逐个执行


import unittest,HTMLTestRunner

suit = unittest.TestSuite()#创建测试套件
all_cases = unittest.defaultTestLoader.discover('.','test_*.py')

for case in all_cases:
	suit.addTests(case)#添加所有测试用例

fp = open('res.html','wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='api_tests',
										description='所有测试用例执行情况')
runner.run(suit)