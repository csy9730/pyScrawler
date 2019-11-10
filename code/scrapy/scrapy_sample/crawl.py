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
from scrapy_sample.spiders.sfacg_spider import SfacgSpider
from scrapy_sample.spiders.baiduImage_spider import DuduSpider
from scrapy_sample.spiders.doc_spider import DocScrapySpider
from scrapy_sample.spiders.a23us import A23usSpider


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
#  "3"  ==> 2
#  "[3,4,5]" ==> [3,4,5]
#  "{a:3,b:c}"==> {"a":"3","b":"c"}
def eJsonParse(ss):
    ss= ss.strip()
    if ss.startswith('['):
        s2 = ss.strip('[]')
        return s2.split(',')
    elif ss.startswith('{'):
        s2=ss.strip('{}')
        return { s.split(':')[0]:s.split(':')[1]  for s in s2.split(',')}
    elif ss.isdigit():
        return int(ss)
    else:
        return ss
# ['word=girl', 'pn=30', 'pg_range=2']  ==> {'word': 'girl', 'pn': '30', 'pg_range': '2'}
# fStrList2Dict = lambda x:{f.split("=")[0]:f.split("=")[1] for f in x} if x is not None else None
# ['word=girl', 'pn=[30,40]', 'pg_range={ab:45}']  ==>{'pg_range': {'ab': '45'}, 'pn': ['30', '40'], 'word': 'girl'}
fStrList2Dict = lambda x:{f.split("=")[0]:eJsonParse(f.split("=")[1]) for f in x} if x is not None else None
   
def main(spider,setting,**kwargs):
    spiderDict = {"mzitu": MzituSpider,"mm131":Mm131Spider,"meizitu0":MeizituSpider0,"meizitu":MeizituSpider,
                "dmzj":dmzjSpider,"doc_scrapy":DocScrapySpider,"sgacg":SfacgSpider,"baiduimage": DuduSpider,
                "23us":A23usSpider
                }
    if spider in spiderDict.keys():
        spd = spiderDict[spider]
    settings =  get_project_settings()
    for k,v in setting.items():  
        settings.set(k,v,priority='cmdline')

    process = CrawlerProcess( settings)
    SPD_ARG_LIST = ["name","allowed_domains","argument","start_urls","start_params"]
    spdArgDict= {k:v   for k,v in kwargs.items() if k in SPD_ARG_LIST and v is not None}
    print(spdArgDict)
    process.crawl( spd,**spdArgDict) # , domain='mzitu.com' ,start_urls=[baidu.com,]
    process.start() # the script will block here until the crawling is finished
""" argument 是 spider自定义配置，set是setting的自带配置。loadconfig从文件导入配置
    set: spider,spider_confg,feedexport."""   
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(prog='scrapy')

    parser.add_argument('--setting','-s', default=[],action='append', help='setting such as jobdir,CLOSESPIDER_ITEMCOUNT')
    parser.add_argument('--spider','-d',default='meizitu0',action='store', help='spider ,default is meizitu0')
    parser.add_argument('--output','-o', action='append', help='output help') # todo
    parser.add_argument('--start_urls','-u', action='append', help='start urls ')
    parser.add_argument('--name', action='store', help='spider name') # not important 
    parser.add_argument('--allowed_domains', action='append', help='domain')
    parser.add_argument('--argument','-a', default=[],action='append', help='argument setting ')
    parser.add_argument('--start_params','-p', action='store', help="""set start_params argument setting,
            eg [{"word":"moon","pn":0,"pg_range":1} ]""")
    parser.add_argument('--loadconfig','-l', action='store', help='load config file') # todo

    cmdline = ['--spider', 'meizitu0', '-o', 'scr_abc.jl','-a','abc=werw',
            '-s','CLOSESPIDER_ITEMCOUNT=2','-s','JOBDIR=scr_job','-u',"https://www.meizitu.com/a/5388.html",
            "--start_urls","https://www.meizitu.com/a/5378.html","--name","meizitu000","--allowed_domains","meizitu.com"]
    cmdline =  ['--spider', 'dmzj',"-u","https://manhua.dmzj.com/yaojingdeweibabainianrenwu",'-s','CLOSESPIDER_ITEMCOUNT=2',]
    cmdline =  ['--spider', 'baiduimage','--argument','word=猪八戒','--setting','CLOSESPIDER_ITEMCOUNT=2',
                '--start_urls','www.baidu.com'] # ,'--start_urls','word=moon',
    cmdline = ['-d','baiduimage','--start_params','[{"word":"moon","pn":0,"pg_range":1}]']
    # cmdlines = """ -d baiduimage --start_params "[{'word':'moon','pn':0,'pg_range':1}]"  """
    # dct0 = {'argument': {'word': 'moon\n==='}, 'set': {'CLOSESPIDER_ITEMCOUNT': '2'},
    #     'spider': 'baiduimage', 'output': None, 'start_urls': ['www.baidu.com'], 'name': None, 'allowed_domains': None, 'loadconfig': None}
    # dctstr = json.dumps(dct0,ensure_ascii=False)
    # lst = dict2cmdline(dct0)
    # print(lst)
    args  = parser.parse_args()
    print(args)
    dct = vars(args)
    for k in dct.keys():
        if k in ["setting","argument"]:
            dct[k] = fStrList2Dict( dct[k] )
        if k in ["start_params"] and dct[k]:
            print( dct[k].replace("'",'"') )
            dct[k] = json.loads(dct[k].replace("'",'"') )
    # print("dct2=",dct==dct0, dct)
    # lst = dict2cmdline(dct)
    # print(lst,set(lst)==set(cmdline))
    with open("tmp_1.scrproj","w") as fp:
        json.dump(dct,fp,indent=4)
    print("dct=",dct)
    main(**dct)
    # cmd = 'scrapy crawl %s -a book=%s -o scr_%s.jl -s CLOSESPIDER_ITEMCOUNT=3' % (keys,book,keys)
