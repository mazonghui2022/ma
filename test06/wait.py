'''
    等待的实例
        等待作为ui自动化中及其核心的技术，是因为通过等待，才可以更好的保障自动化测试的稳定性。
    三类等待：
       1、强制等待
        sleep() 运行时 消耗时间 运行慢
        time.sleep()强制等待,运行机制不考虑代码任何情况，只要运行到sleep函数，
                            就基于参数进行无条件的等待，等待时间由参数决定，单位是秒。
                            等待结束之后会继续运行后边代码
        测试场景下极少应用，因为强制等待会造成大量的代码冗余
        优点：非常容易使用
        缺点：浪费时间，无法精准把控时间，只能选择尽可能大的时间周期来进行等待

        2、 隐式等待：位置 最好在创建webdriver时立刻去  设置
                本质意义而言是driver对象的一个设置项，
                设置一次，即全局(整个driver生命周期)生效
                进行一次页面等待的最大时间设置
                每一步操作都会执行这个隐士等待
                当页面加载完成以后，调用后续代码时，会进入隐士等待
                当等待最大时间超过时，会后续进行后续的操作，
                如果等待到元素，则会直接对该元素进行操作，
                没有获取到，则会进入隐士等待的等待时间中，当等待最大时间超过时会继续进行后续操作
                如果在最大时间内未找到元素，则会根据实际情况抛出异常
        driver.implictly_wait(5) 参数 是秒 为单位
        -优点：只需要在整个friver生命周期中设置一次即可
        -缺点：如果找不到元素，就不管了，效率会收到影响
        必须等到页面加载策略实现之后，才会执行开始

        3、显示等待：位置  在关键元素进行设置 对于元素 设置
            专门针对于元素进行等待的操作行为。
            用法与强制等待相同，需要关联的操作相对会更加复杂一些。
        显示等待指定元素，最大时间是*，没隔多久执行一次，一直到元素被找到为止，如果没找到，则显示Message的内容，抛出异常TimeException
        WebDiverWait(driver对象,"最大等待时间","策略，时隔多久执行一次").until(lambda el: driver.find_element('id','kw'),message='显示等待失败')
        通过until和until_not来进行调用
        分为Until()和Until_not()  Until_not()一直到元素找不到为止
        显示等待，当等待到指定的元素，会返回该元素对象，类似于find_element函数
        -优点：直接对单个元素进行等待操作，效率特别高
        -缺点：用起来会比较麻烦

        等待的应用：
            隐士等待与显示等待是共用的
            隐士等待设定driver的全局等待，便于所有的常规操作有等待机制存在
            显示等待针对某些特定的元素进行等待，便于验证整个流程是否正常，
            以及关键件性元素是否存在
            共用时，两种等待取决于谁的时间更长

    设置页面加载策略
    driver对象默认加载的页面，都是不加载本地缓存信息的。
    就会导致有时候遇到资源加载比较多的页面，加载速度就会很慢。
    可以调节页面的加载策略，从而实现更快速度的访问。
    Selenium提供有页面的加载策略，在ChromeOptions中进行配置
        options = webdriver.ChromeOptions()
        页面加载策略：
            selenium带有三种不同的加载策略：
            1、normal：是selenium默认的加载策略，不要指定，表示所有内同全部加载完成，包括静态资源、CSS样式、JS、dom树等一切内容。
            2、eager:放弃加载css样式、静态资源等，提升加载速度
            3、none：只等初始页面加载完成就直接操作
            所有的加载策略都在ChromeOptions中进行设置
            options.page_load_strategy = 'none'
'''

from selenium import webdriver

options = webdriver.ChromeOptions()
# options.page_load_strategy = 'none'
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
#隐士等待
driver.implicitly_wait(5)
