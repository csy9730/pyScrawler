# start.py
from scrapy import cmdline

key = 'tb3' # 
cmd = 'scrapy crawl %s -a tieba=dota -o scr_tb3.jl -s CLOSESPIDER_ITEMCOUNT=500' % key
# 续爬模式
cmdParam='-s JOBDIR=crawls/storemySpider'
cmdline.execute( cmd.split())