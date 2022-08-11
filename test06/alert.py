'''
     Alert弹框操作
        首先搞清楚，不是每个弹框都是Alert，只有浏览器弹出的才是alert
        三类alert：
            1.alert弹框：显示文本，只有确定按钮
            2.confirm弹框：显示文本，有确认和取消按钮
            3.prompt弹框：显示文本、输入框，有确认和取消按钮
'''
from selenium import webdriver

webdriver = webdriver.Chrome()

#切换到弹框
alert = webdriver.switch_to.alert
#确认
alert.accept()
#取消
alert.dismiss()
#输入文本
alert.send_keys("输入的文本")
#获取弹框中的文本文字
text = alert.text