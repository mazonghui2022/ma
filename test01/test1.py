'''
    养成一个正常的思维逻辑：
        电脑很蠢，代码也很蠢，他们不知道你心里所想的任何事情，只知道代码写了什么就执行什么。
'''
from time import sleep

from selenium import webdriver

#创建一个浏览器驱动，基于驱动启动浏览器
driver = webdriver.Chrome()

#get() 填写需要访问的地址
driver.get('http://www.jd.com')

#找到输入框，不要使用find_element_by_*()去定位元素
el = driver.find_element()
#输入值
el.send_keys('测试')
#找到搜索按钮进行点击
driver.find_element().click()

# 等待三秒
sleep(3)

#关闭
driver.quit()