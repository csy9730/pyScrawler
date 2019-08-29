# start.py
from scrapy import cmdline

# 续爬模式，会自动生成一个crawls文件夹，用于存放断点文件
# cmdline.execute('scrapy crawl mySpider -s JOBDIR=crawls/storemySpider'.split())
keysList = ["mm131","meizitu"]
keys = keysList[1]
cmd = 'scrapy crawl %s -a tieba=dota -o scr_%s.jl -s CLOSESPIDER_ITEMCOUNT=100' % (keys,keys)
# 非续爬模式
cmdline.execute(cmd .split())