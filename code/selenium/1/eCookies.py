from selenium import webdriver
import os,sys
os.environ['PATH'] +=';../;'
import json

browser = webdriver.Chrome()

def loadCookies(browser,pfn):
    with open(pfn,"r") as fp:
        cookies = json.load(fp)        
        for ck in cookies:
            browser.add_cookie(ck)

def loginBaidu():
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com/')
    loadCookies(browser,"aCookie.json")
    browser.refresh()
    cookies = browser.get_cookies()
    print(cookies,type(cookies))
    with open("aCookies2.json","w") as fp:
        json.dump(cookies,fp,indent=4)
    # browser.close()
def loginDouban():
    global browser    
    cookieFile = "doubanCookies.json"
    if 0:# or os.exist(cookieFile):
        browser.get('https://accounts.douban.com')
        print("load cookies")
        loadCookies(browser,cookieFile)
        browser.refresh()
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
    return
    with open(cookieFile,"w") as fp:
        json.dump(cookies,fp,indent=4)
    # browser.close()
def main():
    loginDouban()
if __name__ == '__main__':
    main()






