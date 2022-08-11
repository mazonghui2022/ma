'''
    相对定位器进行元素定位，在selenium4 中所新增的内容
    基于人的方向来对元素进行定位，只需要定位一个元素，就可以吧这个元素周围的所有元素都定位到
    实际使用中，会出现定位不准确

'''

#相对定位器 locate_with(BY对象-->BY.id，'元素属性')        .above(核心元素)上 .below(核心元素)下 .to_left_of(核心元素)左 .to_right_of(核心元素)右 .near(核心元素)附近

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
driver.maximize_window()

#核心元素
elements = driver.find_element('id','kw')

#上下左右及附近
el =driver.find_elements(locate_with(By.ID,'id').above(elements))
el2 =driver.find_elements(locate_with(By.ID,'id').below(elements))
el3 =driver.find_elements(locate_with(By.ID,'id').to_left_of(elements))
el4 =driver.find_elements(locate_with(By.ID,'id').to_right_of(elements))
el5 =driver.find_elements(locate_with(By.ID,'id').near(elements))

print(el)
print(el2)
print(el3)
print(el4)
print(el5)