# start.py
from scrapy import cmdline

# 续爬模式，会自动生成一个crawls文件夹，用于存放断点文件
# cmdline.execute('scrapy crawl mySpider -s JOBDIR=crawls/storemySpider'.split())
keysList = ["mm131","meizitu","meizitu0","ishuhui","sgacg","dmzj","mzitu","zuopinj"
                ,"bdmms"]
keys = keysList[8]
book = "tzdgzsnldydszldmfs"
cmd = 'scrapy crawl {0} -o scr_{0}.jl -a book={1}  -s CLOSESPIDER_ITEMCOUNT=3'.format (keys,book)

# 非续爬模式
cmdline.execute(cmd .split())
# cmd  =" scrapy runspider scrapy_sample/spiders/dmzj_spider.py  -a book=tzdgzsnldydszldmfs"