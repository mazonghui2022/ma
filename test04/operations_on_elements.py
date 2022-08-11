'''
    元素的操作行为：
        例如输入、点击、获取相关内容、前进后退。。。
        将常见的所有在UI自动化测试领域下进行规整

    常用的方法：
        -添加注释
        -异常捕获
        -封装的问题，要封装就要思考清楚逻辑
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

#Chrome()浏览器配置
option = webdriver.ChromeOptions()
option.add_argument('start-maximized')#需要把这个传入到Chrome中

# 创建驱动
driver = webdriver.Chrome(options=option)
sleep(2)

#窗体最大化:不建议去使用，会改变页面大小；在selenium2开始就存在一个bug调用窗体最大化时会造成driver的超时异常
#可以通过Chrome浏览器进行配置，见上面,浏览器这么做就默认为最大化
# driver.maximize_window()

#设置窗体大小尺寸
# driver.set_window_size(200,1000)#设置当前窗口的宽度和高度

#打开访问的地址
driver.get('http://www.baidu.com')

#窗体最小化:不实用，不如不用
# driver.minimize_window()

#浏览器操作，前进 后退 刷新
# driver.forward()#前进
# driver.back()#后退
# driver.refresh()#刷新  最常见的是这个

#获取title,就是访问地址标签页的名称，用于在调试时可以判断一下，不代表可以用于做断言
print(driver.title) #ShopXO企业级B2C电商系统提供商 - 演示站点

#元素定位
# driver.find_element()#定位单个元素，如果同时有多个元素满足条件，定位第一个元素并返回
# driver.find_elements()#定位符合条件的所有元素，最终以list的格式返回

#获取到元素之后的操作行为
#输入操作
# driver.find_element().send_keys()

#文件上传:如果在系统操作汇总遇到文件上传的操作，如果是input标签则可以通过sendkeys直接操作，非input标签，弄死开发
# driver.find_element('id','').click()
# driver.find_element('id','').send_keys("可以传文件路径")

#点击:如果有点击的需求，统一通过click()来实现
# driver.find_element().click()

'''
    下拉框分为以下三种：
        1、基于input标签实现的下拉列表框
        2、基于Select标签实现的
        3、基于其他标签实现的
'''

#操作下拉列表框
# 1、悬停在设置元素上    ActionChains(参数未驱动对象)   .move_to_element("移动到那个元素定位")   .perform()执行
#悬停操作时，不要在driver的浏览器中进行移动
ActionChains(driver).move_to_element(driver.find_element('xpath','//span[text()="设置"]')).perform()
# 2、点击高级搜索
driver.find_element('link text','高级搜索').click()
#常见的下拉列表框操作一：其他标签
driver.find_element('xpath','//span[text()="全部时间"]').click()
#常见的下拉列表框操作二：input标签(一般input下拉框时具有只读属性，无法直接通过send_keys输入，输入前需要remove()掉只读属性)
driver.find_element('xpath','//input[text()="全部时间"]').send_keys("最近一月")
# Select标签下拉列表框：如果你测试的系统有这个标签，说明系统是老系统
select = Select(driver.find_element('id','citiId'))
#选择值
#通过下标选择
select.select_by_index(5)
#通过value选择
select.select_by_value('12')
#通过文本选择
select.select_by_visible_text('成都')

#退出浏览器
driver.close()#可以关闭掉一个标签页，后台还有这个进程，所有我们使用quit(),需要把后端进程一同关闭
driver.quit()