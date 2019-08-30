# start.py
from scrapy import cmdline

key = '23us' # 
cmd = 'scrapy crawl %s -o scr_%s.jl -s CLOSESPIDER_ITEMCOUNT=500' % (key,key)
# 续爬模式
cmdParam='-s JOBDIR=crawls/storemySpider'
cmdline.execute( cmd.split())