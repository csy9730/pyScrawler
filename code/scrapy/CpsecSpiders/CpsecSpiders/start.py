# start.py
from scrapy import cmdline

key = 'tianya' # 
cmd = 'scrapy crawl %s -s CLOSESPIDER_ITEMCOUNT=50' % key
# 续爬模式
cmdParam='-s JOBDIR=crawls/storemySpider'
cmdline.execute( cmd.split())