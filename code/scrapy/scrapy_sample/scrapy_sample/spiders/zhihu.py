# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']

    start_urls = ['https://www.zhihu.com' ]
    custom_settings = {'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3026.3 Safari/537.36'}

    def parse(self, response):
        formadata = {
            'password': '密码',
            'phone_num': '手机号',
            'email': 'gd'
        }
        return FormRequest.from_response(
                                  url='https://www.zhihu.com/login/{}'.format('phone_num'
                                                                          if formadata['phone_num'] else 'email'), # post 的网址
                                  method="POST", # 也是默认值, 其实不需要指定
                                  response=response, 
                                  formxpath='//form[1]', # 使用第一个form, 其实就是默认的, 这里明确写出来
                                  formdata=formadata, # 我们填写的表单数据
                                  callback=self.after_login, # 登录完成之后的处理
                                  dont_click=True)