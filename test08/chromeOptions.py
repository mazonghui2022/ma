'''
    ChromeOptions配置
    配置浏览器再启动之初，应该要附加的设置内容
    ChromeOptions专门用于配置对应的chrome浏览器
    浏览器配置项在实际应用中，用什么就去搜
    要查找新的options函数，因为旧的失效了
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

#创建chrome浏览器配置项,创建ChromeOptions对象
options = webdriver.ChromeOptions()

#页面加载策略
options.page_load_strategy = 'eager'
#浏览器最大化
options.add_argument('start-maximized')
#指定位置启动浏览器
options.add_argument('window-position=2000,500')
#设置窗体的启动大小
options.add_argument('window-size=200,100')

#去掉浏览器提示自动化黄条:没什么用处只是为了好看而已
options.add_experimental_option('excludeSwitches',['enable-automation'])
#只支持2.7版本的selenium，目前已经弃用
# options.add_experimental_option('disable-infobars')

#添加实验性质的配置项
# options.add_experimental_option()
# #添加常规设定
# options.add_argument()

#去掉账号密码弹出框
prefs = dict()
prefs['credentials_enable_service'] = False
prefs['profile.password_manager_enable'] = False
options.add_experimental_option('','')

#去掉控制台多余信息手段二，可作为保险的存在(当存在还有多余信息的时候)
options.add_argument('--log_level=3')
options.add_argument('--disable_gpu')
options.add_argument('--ignore-certificate-errors')

#隐身模式：注意隐身模式下无法使用selenium中的switch_to.new_window（）函数
options.add_argument('incognito')

#无头模式（没有可视化界面）,不在桌面浏览器运行，作为后台静默运行，虽然看不到，但是一切照旧运行
options.add_argument('--headless')

#读取本地缓存的操作：webdriver启动时候默认是不会加载本地缓存数据的，有时候想要饶过验证码或者登录流程，可以通过加载本地缓存来实现
#chrome浏览器输入chrome://version/  获取下方信息
# 个人资料路径	C:\Users\Mr.Ma\AppData\Local\Google\Chrome\User Data\Default  不要Default
#调用本地缓存必须关闭所有chrome浏览器，否则会报错
options.add_argument(r'--user-data-dir=C:\Users\Mr.Ma\AppData\Local\Google\Chrome\User Data')

#创建driver对象
driver = webdriver.Chrome(options=options) #表示python3及以上版本的浏览器配置
# driver1 = webdriver.Chrome(chrome_options=options)#表示python2.7版本的浏览器配置。不要使用
driver.get('http://www.baidu.com')

'''
    把options进行封装，webdriver进行调用，options需要return返回一个options对象，因为webdriver.Chrome(options=options) 调用了options对象
'''

#校验页面是否切换成功
WebDriverWait(driver,10,0.5).until(lambda el:driver.find_element('',''),message="元素切换失败")

#创建新的页
driver.switch_to.new_window()