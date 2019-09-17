from selenium import webdriver
import os,sys
os.environ['PATH'] +=';../;'

import json
from  selenium.webdriver.chrome.options import  Options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--log-level=3")  # fatal
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})       
chrome_path = 'drivers/chromedriver.exe'
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()

# browser = webdriver.Chrome()

def loadCookies(browser,pfn):
    with open(pfn,"r") as fp:
        cookies = json.load(fp)        
        for ck in cookies:
            if isinstance(ck.get('expiry'), float):
                ck['expiry'] = int(ck['expiry'])
            browser.add_cookie(ck)

def loginBaidu():
    global browser 
    browser.get('http://www.baidu.com/')
    loadCookies(browser,"aCookies2.json")
    browser.refresh()
    cookies = browser.get_cookies()
    print(cookies,type(cookies))
    with open("aCookies2.json","w") as fp:
        json.dump(cookies,fp,indent=4)
    
    # browser.close()

    
def loginDouban():
    global browser    
    cookieFile = "doubanCookies.json"
    if os.path.exists(cookieFile):
        browser.get('https://accounts.douban.com')
        print("load cookies")
        loadCookies(browser,cookieFile)
        browser.refresh()
        browser.get("https://www.douban.com/")
    else:
        browser.get('https://accounts.douban.com/passport/login')
        browser.implicitly_wait(10)

        # 重点1要先切换到子框架
        # browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])
        # 重点2要先点击用账号密码登录的按钮，不然会找不到输入账号和密码的地方
        bottom1 = browser.find_element_by_xpath('.//ul//li[@class="account-tab-account"]')
        bottom1.click()

        browser.find_element_by_name("username").clear()
        browser.find_element_by_name("username").send_keys("abc@163.com") #修改为自己的用户名
        browser.find_element_by_name("password").clear()
        browser.find_element_by_name("password").send_keys("******") #修改为自己的密码
        bottom = browser.find_element_by_class_name('account-form-field-submit ')
        bottom.click()
    
    cookies = browser.get_cookies()
    print(cookies,type(cookies))
    with open(cookieFile,"w") as fp:
        json.dump(cookies,fp,indent=4)
    # browser.close()
    import time
    time.sleep(100)
def main():
    loginDouban()
    #loginBaidu()
if __name__ == '__main__':
    main()






