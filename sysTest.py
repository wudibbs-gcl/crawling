# 提供Python运行环境的变量和函数
import sys

# sys.argv[0] #获取脚本名
# sys.argv[1] # 获取第一个参数
# 
# sys.argv命令行参数List，第一个元素是程序本身路径
# print('脚本名称：{}'.format(sys.argv[0]))
# for x in sys.argv:
# 	if x == sys.argv[0]:
# 		continue
# 	print('参数为：',x)
# print('总参数个数:{}'.format(len(sys.argv)-1))

# print(sys.getdefaultencoding())# 系统当前编码
# sys.setdefaultencoding('utf-8')#Python3中已经没有这个方法
# reload(sys)
# print(sys.getfilesystemencoding())
#sys.setfilesystemencoding()#python3中已经没有这个方法

# sys.modules.keys()
# sys.modules.keys() 返回所有已经导入的模块列表
# print(sys.modules)# 返回所有已经导入的模块，key是模块名，value是模块
# print(sys.modules.keys())
# print(sys.modules.values())


# sys.exc_info()获取当前正在处理的异常类，exc_type,exc_value,exc_traceback当前处理的异常的详细信息
# print(sys.exc_info())

# sys.exit([arg])# 退出解释器程序，arg=0为正常退出
# print(sys.exit())# 下面的代码将不会被执行
# print(sys.maxunicode)# 最大unicode值
# print(sys.maxsize)# 最大int值
# print(sys.path)# sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
#sys.path.append("自定义模块路径")#可以直接导入
# print(sys.platform)# 返回操作系统平台名称


# sys.stdout 
# 使用sys.stdout 重定向输出


# f = open('log.txt','a')#以追加模式打开一个文件
# __console__ = sys.stdout#总在重定向前保存stdout,这样的话之后还可以将其恢复正常
# sys.stdout = f#将后续的标准输出都写入刚才打开的文件
# print('hello python3')
# sys.stdout.write("nice body\n")
# print('hello python4')
# sys.stdout = __console__# 将标准输出改为console命令行模式
# print("hello world")# 输出到命令行下
# f.close()


# sys.stderr #重定向错误信息
ferror = open('error.txt','a')#存储错误日志的文件，追加模式写入
# __console__ = sys.stderr
sys.stderr = ferror#错误输出到日志文件
# raise Exception('this error will be logged')


# 使用print() 打印error到std
print (sys.stderr,"wrong log")

# print(sys.stdout.write('stdout.write 默认不换行'))# 输出到console
#接受标准输入，等价于raw_input()
# name = sys.stdin.readlines(2)
# print('输出：{}'.format(name))
