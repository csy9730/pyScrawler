# -*- coding: utf-8 -*-
import scrapy
import urllib
from PIL import Image


class DoubanLoginSpider(scrapy.Spider):
    name = 'douban_login'
    allowed_domains = ['douban.com']
#    start_urls = ['http://www.douban.com/']
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}

    def start_requests(self):
        '''
        重写start_requests，请求登录页面
        '''
        return [scrapy.FormRequest("https://accounts.douban.com/login", headers=self.headers, meta={"cookiejar":1}, callback=self.parse_before_login)]

    def parse_before_login(self, response):
        '''
        登录表单填充，查看验证码
        '''
        print("登录前表单填充")
        captcha_id = response.xpath('//input[@name="captcha-id"]/@value').extract_first()
        captcha_image_url = response.xpath('//img[@id="captcha_image"]/@src').extract_first()
        if captcha_image_url is None:
                print("登录时无验证码")
                formdata = {
                                "source": "index_nav",
                                "form_email": "yanggd1987@163.com",
                                #请填写你的密码
                                "form_password": "********",
                        }
        else:
                print("登录时有验证码")
                save_image_path = "/home/yanggd/python/scrapy/douban/douban/spiders/captcha.jpeg"
                #将图片验证码下载到本地
                urllib.urlretrieve(captcha_image_url, save_image_path)
                #打开图片，以便我们识别图中验证码
                try:
                        im = Image.open('captcha.jpeg')
                        im.show()
                except:
                        pass
        #手动输入验证码
                captcha_solution = raw_input('根据打开的图片输入验证码:')
                formdata = {
                                "source": "None",
                                "redir": "https://www.douban.com",
                                "form_email": "yanggd1987@163.com",
                                #此处请填写密码
                                "form_password": "********",
                                "captcha-solution": captcha_solution,
                                "captcha-id": captcha_id,
                                "login": "登录",
                        }


        print("登录中")
        #提交表单
        return scrapy.FormRequest.from_response(response, meta={"cookiejar":response.meta["cookiejar"]}, headers=self.headers, formdata=formdata, callback=self.parse_after_login)
    def parse_after_login(self, response):
        '''
        验证登录是否成功
        '''
        account = response.xpath('//a[@class="bn-more"]/span/text()').extract_first()
        if account is None:
                print("登录失败")
        else:
                print(u"登录成功,当前账户为 %s" %account)
