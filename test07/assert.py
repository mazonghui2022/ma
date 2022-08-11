'''
    所有的自动化测试都需要有成功的结果，所以需要在流程自动化执行的末尾，有一个校验的功能。
    就像是需要有一个预期结果与实际结果对比的行为。
    Ui自动化下断言的行为，只需要在流程的末尾来执行即可
    一般就只有一次断言就足够解决流程的自动化了
    UI自动化中断言所选择的点，一定是具备有代表性的内容，要关键核心的点才可以作为断言的依据。
    在自动化体系中，断言是一种相对比较固定的形态，流程就是获取指定的内容，对内容进行判断，是否与预期相符合
    1、
        #定义预期结果，并获取实际结果
        expected = '预期结果'
        driver.find_element().text/.get_attribute
        #关键的断言 关键字
        assert expected == reality,'断言失败'
'''
from time import sleep

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
webdriver = webdriver.Chrome(options=options)
webdriver.implicitly_wait(5)
webdriver.get('http://39.98.138.157/shopxo/index.php')
webdriver.find_element('link text','登录').click()
webdriver.find_element('name','accounts').send_keys('xuzhu666')
webdriver.find_element('name','pwd').send_keys('123465')
webdriver.find_element('xpath','//button[text()="登录"]').click()
#断言部分
#定义预期结果并获取实际结果
expected = '退出'
#建议这么写捕获
try:
    reality = webdriver.find_element('link text','退出').text
except Exception as e:
    print(e)
    reality = None
#关键的断言关键字
assert expected == reality,'断言失败:{0}不等于{1}'.format(expected,reality)
#断言的本质就是if。。。else结构
# webdriver.quit()
