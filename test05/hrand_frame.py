'''
    新页面的访问：selenium访问新页面的时候，其实浏览器本身的句柄还是聚焦在老的页面中，所以我们使用切换句柄来操作    driver.title() 查看标头
                句柄切换的业务下，需要时刻记住，标签页最多保留不超过2个，一般在访问之前close()掉    操作步骤：1、获取标签页   driver.window_handles 2、关闭当前标签页   driver.close()    3、切换标签页 driver.switch_to.window(handles[1])
                句柄切换分两个步骤：1、获取标签页   driver.window_handles   2、切换标签页 driver.switch_to.window(handles[1])
    内嵌窗体的元素操作：有一种场景元素定位正确，并且再三确认过，但是运行到这里就是找不到元素，
                    也等待了，也排查了，还是找不到这个元素，这时就要思考下是不是有iframe呢。

                    如果元素在iframe中，需要先切换至iframe，在进行定位
                    driver.switch_to.frame('')
                    driver.find_element('','').click()

                    切换到iframe里面，可以继续操作里面的元素，如果想操作外面的元素，需要切换到默认窗体
                    只有切换回来以后才可以继续操作页面中iframe以外的内容
                    driver.switch_to.default_content()

                    自动生成新的标签页，并切换过去
                    driver.switch_to.new_window('tab') 新增标签页
                    driver.get('http://www.baidu.com')  这两行代码生成新的标签页并切换到新页面

                    自动生成浏览器，并切换过去
                    driver.switch_to.new_window('window')   新增浏览器
                    driver.get('http://www.baidu.com')  这两行代码弹出新的标签页并切换到新页面，两个页面分开显示

                    1：通过frame的id属性：driver.switch_to.frame(‘id属性’)
                    2：通过frame的name属性：driver.switch_to.frame(‘name属性’)
                    3：通过index来定位：driver.switch_to.frame(0) 其中0表示第一个iframe
'''
from time import sleep
from selenium import webdriver

#窗体最大化
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('http://www.baidu.com')

sleep(2)
driver.find_element('id','kw').send_keys('虚竹')
sleep(2)
driver.find_element('id','su').click()
sleep(2)
#访问新页面前查看句柄位置
print(driver.window_handles)#['CDwindow-27509D6E669BFD42639CF46623EFD7E9']
driver.find_element('xpath','//*[@id="2"]/div[1]/div[1]/h3/a').click()
print(driver.title) #查看标头，这是发现标头还是显示第一页的表头“虚竹_百度搜索”

# 访问新页面之后，有几个页面就有几个句柄（一般不能保留超过两个句柄，场景就是每打开一个关掉前一个）
handles = driver.window_handles #1、获取句柄
print(handles)  #['CDwindow-27509D6E669BFD42639CF46623EFD7E9', 'CDwindow-BA2E85B167F784D8B7A9A1F2780CBFE1']

#关闭当前句柄
driver.close()

# 切换句柄(切换之后句柄位置)
driver.switch_to.window(handles[1]) #2、切换句柄
print(driver.title)#查看标头，是否切换句柄成功   “虚竹后期无人可敌，他到底是被谁杀死的？金庸借郭靖给出答案”

# driver.quit()