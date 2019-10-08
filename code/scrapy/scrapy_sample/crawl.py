# import robotparser
import os,sys 
import json
import scrapy.spiderloader
import scrapy.statscollectors
import scrapy.logformatter
import scrapy.dupefilters
import scrapy.squeues
 
import scrapy.extensions.spiderstate
import scrapy.extensions.corestats
import scrapy.extensions.telnet
import scrapy.extensions.logstats
import scrapy.extensions.memusage
import scrapy.extensions.memdebug
import scrapy.extensions.feedexport
import scrapy.extensions.closespider
import scrapy.extensions.debug
import scrapy.extensions.httpcache
import scrapy.extensions.statsmailer
import scrapy.extensions.throttle
 
import scrapy.core.scheduler
import scrapy.core.engine
import scrapy.core.scraper
import scrapy.core.spidermw
import scrapy.core.downloader
 
import scrapy.downloadermiddlewares.stats
import scrapy.downloadermiddlewares.httpcache
import scrapy.downloadermiddlewares.cookies
import scrapy.downloadermiddlewares.useragent
import scrapy.downloadermiddlewares.httpproxy
import scrapy.downloadermiddlewares.ajaxcrawl
import scrapy.downloadermiddlewares.chunked
import scrapy.downloadermiddlewares.decompression
import scrapy.downloadermiddlewares.defaultheaders
import scrapy.downloadermiddlewares.downloadtimeout
import scrapy.downloadermiddlewares.httpauth
import scrapy.downloadermiddlewares.httpcompression
import scrapy.downloadermiddlewares.redirect
import scrapy.downloadermiddlewares.retry
import scrapy.downloadermiddlewares.robotstxt
 
import scrapy.spidermiddlewares.depth
import scrapy.spidermiddlewares.httperror
import scrapy.spidermiddlewares.offsite
import scrapy.spidermiddlewares.referer
import scrapy.spidermiddlewares.urllength
 
import scrapy.pipelines
 
import scrapy.core.downloader.handlers.http
import scrapy.core.downloader.contextfactory
 
import scrapy.pipelines.images  # 用到图片管道
# import openpyxl  # 用到openpyxl库

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys
sys.path.append('scrapy_sample/spiders')

import PIL
import scrapy_sample.spiders
from scrapy_sample.spiders.mzitu import MzituSpider
from scrapy_sample.spiders.meizitu import MeizituSpider,MeizituSpider0
from scrapy_sample.spiders.mm131 import Mm131Spider
from scrapy_sample.spiders.dmzj_spider import dmzjSpider
import scrapy_sample.settings
import scrapy_sample.pipelines
import scrapy_sample.middlewares
import scrapy_sample.items
from scrapy_sample.utils import dict2cmdline

# todo
class crawlSetting(object):
    def __init__(self):
        self.custom = None
        self.set = None
        self.spider = "meizitu0"
        self.output = None
    def __dict__(self):
        return dict()
    
def main(cfg):
    spiderDict = {"mzitu": MzituSpider,"mm131":Mm131Spider,"dmzj":dmzjSpider,"meizitu0":MeizituSpider0,"meizitu":MeizituSpider}
    if cfg["spider"] in spiderDict.keys():
        spd = spiderDict[cfg["spider"]]
    settings =  get_project_settings()
    sett = cfg["set"]
    for c in sett:
        print(c,sett[c])
        if c.endswith('COUNT'):
            sett[c] = int(sett[c])
        settings.set(c,sett[c],priority='cmdline')
#    print(vars(settings))
#    settings.set("CLOSESPIDER_ITEMCOUNT", 3, priority='cmdline')
    process = CrawlerProcess( settings)
    process.crawl( spd ) # , domain='mzitu.com'
    process.start() # the script will block here until the crawling is finished

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(prog='scrapy')
    parser.add_argument('--custom','-c', default=[],action='append', help='custom setting help')
    parser.add_argument('--set','-s', default=[],action='append', help='setting help')
    parser.add_argument('--spider','-d',default='mzitu',action='store', help='spider help')
    parser.add_argument('--output','-o', action='append', help='output help')
    fCustom = lambda x:{f.split("=")[0]:f.split("=")[1] for f in x} if x is not None else None
    args  = parser.parse_args(['--spider', 'meizitu0', '-o', 'scr_abc.jl','-c','abc=werw',
            '-s','CLOSESPIDER_ITEMCOUNT=2','-s','JOBDIR=scr_job'])
    dct = vars(args)
    dct["custom"] = fCustom( dct ["custom"])
    dct["set"] = fCustom( dct ["set"])
    print(dct)
    lst = dict2cmdline(dct)
    print(lst)
    with open("tmp_1.scrproj","w") as fp:
        json.dump(dct,fp,indent=4)
    # main(dct)
# cmd = 'scrapy crawl %s -a book=%s -o scr_%s.jl -s CLOSESPIDER_ITEMCOUNT=3' % (keys,book,keys)
""" set: spider,spider_confg,setting,feedexport.
"""