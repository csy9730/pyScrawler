# coding=utf-8
# 导包
from selenium import webdriver
import time
if __name__ == '__main__':
    # 1. 创建浏览器对象
    driver = webdriver.Chrome()
    # 2. 发送请求
    driver.get('https://www.baidu.com')
    # 3. 获取数据
    # data = driver.page_source
    # with open('baidu.html', 'w') as f:
    #     f.write(data.encode('utf-8'))
    # 给搜索框 输入数据: 数据 必须是unicode
    driver.find_element_by_id('kw').send_keys(u'segmentfault')
    # 然后点击
    # driver.find_element_by_id('su').click()
    # webdriver 也支持xpath
    driver.find_element_by_xpath('//*[@id="su"]').click()
    time.sleep(3)
    # 浏览器有几个标签页
    print(driver.window_handles)
    
    # 屏幕快照
    driver.save_screenshot('baidu.png')
    # 点击搜索结果的第一条
    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
    # time.sleep(3)
    # 因为点击之后会打开一个新的标签，所以需要跳到新的标签
    # driver.switch_to_window(driver.window_handles[1])
    print(driver.window_handles)
    # 4. 屏幕快照
    driver.save_screenshot('baidu1.png') 