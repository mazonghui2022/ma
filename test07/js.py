'''
    JS执行器
        能够提供Selenium以外的操作，来更好的满足我们自动化测试的需求
        因为selenium本身操作的是页面的前端内容，在特殊的场景下
        selenium很可能在使用上被限制，这个时候就可以通过js执行器来完成需要的操作行为
        所有的js执行器大体都是关联到document对象的
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

'''
    document对象执行的常见函数：
        1、removeAttribute(attribute_name)   移除指定对象的指定属性
        2、setAttribute(attribute_name,value)    设置指定对象的指定属性和值 
        
    #通过占位符来实现selenium与document的关联
    el = driver.find_element('link text','新闻')
    #定位元素，并修改元素的文本  arguments[0]在js中可以理解为占位符，.innerHTML文本的设置 
    js2 = 'arguments[0].innerHTML="刘世桐按钮"'  
    #执行js代码
    driver.execute_script(js2,el)   会把新闻替换成刘世桐按钮
    
    滚动条操作：核心在于元素的获取
        window.scrolloTo(x,y) x横标、y纵标 值为 0,500,1000,2000(x只有0,500，1000)支持同时拉动x、y坐标一起操作
        精确定位到元素并聚焦在页面中显示arguments[0].scrollIntoView():
            #定位到元素
            el = driver.find_element('link text','下一页 >')
            #定位元素并在页面中心显示
            js = 'return arguments[0].scrollIntoView()'
            driver.execute_script(js,el)
    在JS执行器执行过程中，如果想要获取执行结果，便于后续的使用，就一定要在js中添加return关键字
    
    get_attribute('属性的名称')  获取指定元素的属性值
        #定位到元素
        el = driver.find_element('link text','下一页 >')
        text = el.get_attribute('href')
        print(text)
        
    #解决反扒机制
    #通过修改webdriver属性为False，一定是在访问系统之前，在启动浏览器后第一步就是运行这个
    driver.execute_cdp_cmd("",{
        "scource":"""
         Object.defineProperty(navigator,'webdriver',{
            get: () => false
         })
        """
    })
'''

# #设置元素的属性    .setAttribute()
# js = "document.getElementById('kw').setAttribute('readonly','True')"
#
# #删除元素的属性    .removeAttribute()
# js1 = "document.getElementById('kw').removeAttribute('name')"
#
# #用于执行js语句的函数    .execute_script()
# driver.execute_script(js)

#定位新闻的元素
# el = driver.find_element('link text','新闻')
# #定位元素，并修改元素的文本  arguments[0]在js中可以理解为占位符
# js2 = 'return arguments[0].innerHTML="刘世桐按钮"'  el.text=='return arguments[0].innerHTML="刘世桐按钮"'
# #获取指定元素的文本信息
# js3 = 'arguments[0].innerHTML'
# #执行js代码
# driver.execute_script(js2,el)

#定位到元素
el = driver.find_element('link text','下一页 >')
el.get_attribute('href')
#定位元素并在页面中心显示
js = 'arguments[0].scrollIntoView()'
driver.execute_script(js,el)

#解决反扒机制
#通过修改webdriver属性为False，一定是在访问系统之前，在启动浏览器后第一步就是运行这个
# driver.execute_cdp_cmd("",{
#     "scource":"""
#      Object.defineProperty(navigator,'webdriver',{
#         get: () => false
#      })
#     """
# })