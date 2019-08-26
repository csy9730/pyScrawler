# -*- coding: utf-8 -*-

# Scrapy settings for CpesecSpiers project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CpsecSpiders'

SPIDER_MODULES = ['CpsecSpiders.spiders']
NEWSPIDER_MODULE = 'CpsecSpiders.spiders'

#减慢爬取速度 为1s  
download_delay = 1
#爬取网站深度
DEPTH_LIMIT = 20
#禁止cookies,防止被ban  
COOKIES_ENABLED = False

#声明Pipeline，定义的pipeline必须在这声明
ITEM_PIPELINES = { 'CpsecSpiders.pipelines.CpsecspidersPipeline':300 }