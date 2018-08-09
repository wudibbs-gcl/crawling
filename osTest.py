import os


# os.access()
# 查看文件是否有指定权限，有则返回True否则返回flase
# print(os.access('test.txt',os.F_OK))# 文件是否存在
# print(os.access('test.txt',os.R_OK))# 是否可读
# print(os.access('test.txt',os.W_OK))# 是否可写
# print(os.access('test.txt',os.X_OK))#  是否可执行


# os.chdir()
# 改变当前工作目录到指定路径
# print(os.getcwd())
# print(os.chdir('D:\\'))#切换目录
# print(os.getcwd())

# os.chmod()
# 更改文件或目录权限
import stat,os
os.chmod('test.txt',stat.S_IXOTH)# 其他用
'''
权限指定：

stat.S_IXOTH: 其他用户有执行权0o001
stat.S_IWOTH: 其他用户有写权限0o002
stat.S_IROTH: 其他用户有读权限0o004
stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
stat.S_IXGRP: 组用户有执行权限0o010
stat.S_IWGRP: 组用户有写权限0o020
stat.S_IRGRP: 组用户有读权限0o040
stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
stat.S_IXUSR: 拥有者具有执行权限0o100
stat.S_IWUSR: 拥有者具有写权限0o200
stat.S_IRUSR: 拥有者具有读权限0o400
stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
stat.S_IREAD: windows下设为只读
stat.S_IWRITE: windows下取消只读
'''

# os.chown()
# 只支持Linux下
#os.chown('test.txt',0,0)# Windows下没有此方法

# os.chroot()
# 方法用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。

# os.close()
# 用于关闭指定文件描述符fd
# print(os.name)# 'nt' Windows 'posix' linux
# print(os.listdir('E:\\testfile'))# 返回指定目录下所有文件和目录名，return list
# os.remove('新建文本文档.txt')#删除指定文件
# os.rmdir('aaa')#删除指定目录
# os.mkdir('directory')#新建指定目录
# print(os.path.isfile('D:\\testfile'))# 判断指定对象是否为文件，是返回True，否返回False
# print(os.path.isdir('D:\\testfile'))# 判断指定对象是否为文件夹，是返回True，否返回False
# print(os.path.exists("D:\\testfile\\aa.txt"))#判断指定对象是否存在，存在返回True，不存在返回False
# print(os.path.split('D:\\testfile\\crawing\\test.txt'))#--->('D:\\testfile\\crawing', 'test.txt')
# print(os.system('pwd'))#打开命令行窗口
# os.system('echo "hello world"')# 控制台打印
# print(os.path.getsize('D:\\testfile\\crawling\\apiTest.py'))# 返回指定目录大小，如果指定文件，则返回文件大小
# print(sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)]))# 查看当前目录所有文件大小之和
# print(os.path.abspath('.'))# 获取绝对路径
# print(os.path.join('D:\\testfile\\crawling','test.txt'))#type: <class 'str'> return :D:\testfile\crawling\test.txt
# print(os.path.basename('test.txt'))# return；test.txt 返回文件名
# print(os.path.basename('D:\\testfile\\crawling'))# 返回当前所在文件夹名 return: crawling
# print(os.path.dirname('D:\\testfile\\crawling'))#返回文件或文件夹所在路径 	return: D:\testfile
# print(os.path.getmtime('.'))# 返回此路径下最后一次修改的时间戳1533792538.672805










# 获取当前目录下，文件的最后一次修改自然时间
# import time
# 时间戳转换为自然时间
# timeStamp = os.path.getmtime('.')
# timeArrry = time.localtime(timeStamp)
# timeStr = time.strftime("%Y-%m-%d %H:%M:%S",timeArrry)# 将tuple时间转换为str
# print(timeStr)

# 当前时间转换为时间戳
# timeCur = time.time()#时间戳
# print(timeCur)

# # 时间str转换为时间戳
# a = "2013-10-10 23:40:00"# str
# timeArrry = time.strptime(a,'%Y-%m-%d %H:%M:%S')# str format>>>>struct_time
# print(int(time.mktime(timeArrry)))# tuple(struct_time) >>>>float point number时间戳

# # 获取当前时间并按照指定格式输出
# timeStamp = time.time()# 时间戳
# timeTuple = time.localtime(timeStamp)# 时间戳>>>>>struct_time
# print(time.strftime('%Y-%m-%d %H:%M:%S',timeTuple))# format[,tuple]>>>>> str
