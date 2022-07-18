#异常处理 异常
#概念：
        # 程序在运行时，如果程序遇到一个错误，程序就会自动停止的行为，抛出错误信息的就叫异常

# 异常处理
# 保证程序的健壮性和稳定性
# 健壮性：健康    小问题 自己处理掉
# 稳定性：让程序稳定运行

'''
try:
    要执行的代码
except 错误类型:
    出现的错误
在执行程序时，会遇到不同类型的异常，针对不同的异常做出不同的处理

外面的代码依旧可执行

面试题：
                ioEerro 文件异常
                FileNotFoundError 找不到文件错误
                ValueError 值错误
                IndexError 索引错误
                TypeError 类型错误

想不到那么多异常 大概预测 碰到了别的问题 怎么办 报错？
（所有异常的祖宗 BaseError）
exception 异常的父类 exception继承BaseError
exception 拿到所有异常，都可以进行处理,能够接收所有异常并且处理
try:
   执行的代码
except Exception as e:
    异常处理
外面的代码依旧可执行
'''
import time

'''
try:
    要尝试的代码
except 错误类型：
    处理异常
except 错误类型：
    处理异常
except Exception as e：
    print("处理异常%s"%e)
else:
    没有异常才会执行的代码
finally:
    无论如何都会执行
'''

# 做自动化可以在函数内部捕获异常，也可以在调用函数的时候捕获异常
# 调用函数捕获异常，代码干净点

# raise自定义异常，特定的要求就会用自定义异常


# 时间和日期 打印日志    生成测试报告 订单
# 生成日历 年厉月厉日厉
import calendar

# 输出三月份的日历
cal = calendar.calendar(2022,3)
print(cal)

# 输出2022年的年历
nian = calendar.calendar(2022)
print(nian)

# 时间戳：从1970年1月1日0点0分0秒时间    -现在时间秒数
print('当前时间戳：',time.time())

#时间元组 元组（年月日时分秒 一周的第几日 一年的第几天 夏令时）
t = time.localtime(time.time()) #时间元组

# 时间元组转为日期 time.asctime()
print(time.asctime(time.localtime(time.time())))#默认为应为日期
time.strftime('%Y-%m-%d %H:%M:%S')#中文日期