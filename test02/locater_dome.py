''''
    八种元素定位法则：
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text" 超链接:针对于a标签实现的定位，查找所有a标签所匹配的text文本内容信息
            PARTIAL_LINK_TEXT = "partial link text" 超链接，针对于a标签实现的定位，基于a标签的text内容进行模糊查找，类似于sql中的like，如果定位的元素有多个，则默认返回第一个定位到的元素
            NAME = "name"
            TAG_NAME = "tag name"   标签名：一般用在爬虫，测试用不到，基于标签名称来进行元素定位
            CLASS_NAME = "class name"   类名称：基于class属性进行元素定位     不推荐使用 如果class值只有一个，可以考虑使用，前提是避免重复
            CSS_SELECTOR = "css selector"   CSS选择器：基于css样式来对元素进行定位，也是传说中定位最快的方法。
'''

from selenium import webdriver

#创建driver驱动，启动浏览器
driver = webdriver.Chrome()

#打开网页
driver.get('http://www.baidu.com')

#id 一般不会有重复的
driver.find_element('id','su')

#name 概率性的有重复属性
driver.find_element('name','rn')

# xpath元素的语法规则
# 语法规则：//*[@id="kw"]    表示从根路径下开始查找任意一个元素，该语速具备有id的属性，值为kw
#//表示从根路径下开始查找
#*表示任意元素
#[]表示添加筛选条件
#@表示基于属性来进行查找
#id表示属性的名称
#kw标书属性的值
#基于text文本来定位    //*[text()='新闻']
#xpth提供的几个函数：
                # contains() 包含     //a[contains(text()='新闻')] 基于函数里面写的属性进行定位查找
                #                   //a[contains(@id，‘kw’)] 基于函数里面写的属性进行定位查找
                # following-sibling::标签名
                #//a[contains(text()='新闻')]/following-sibling::标签名      首先定位到前面的元素，/following-sibling为定位到元素的相邻元素，同级元素
                #定位元素的上级节点 //a[contains(text()='新闻')]/..
                #定位元素的下级级节点 //a[contains(text()='新闻')]/class

# 可以写多个属性 //*[@id='kw' and @name and @class]
# 相对路径+绝对路径 先定位到父级，加下级的路径      //div[@id='s-top-left']/a[1]

# xpath手写的方式，除去避免绝对路径以外，还可以避免动态元素导致的元素定位失败

#伪元素(控制台看不到，页面定位鼠标放上面可以看的见，可以通过定位到周围的元素进行定位)  ::before::    ::after::

#css与xpath区别
# 1.CSS定位语法比Xpath简洁，定位方式更灵活多样
#
# 2.CSS不支持根据子元素查找元素
#
# 3.使用Xpath能够屏蔽掉其他页面元素改变