# import robotparser
import os,sys 
import json
sys.path.append('scrapy_sample/spiders')

from scrapy_sample.utils import dict2cmdline
import argparse
def main():
    fStrList2Dict = lambda x:{f.split("=")[0]:f.split("=")[1] for f in x} if x is not None else None
    parser = argparse.ArgumentParser(prog='scrapy')
    parser.add_argument('--argument','-a', default=[],action='append', help='argument setting ')
    parser.add_argument('--set','-s', default=[],action='append', help='setting')
    parser.add_argument('--spider','-d',default='meizitu0',action='store', help='spider')
    parser.add_argument('--output','-o', action='append', help='output help')
    parser.add_argument('--start_urls','-u', action='append', help='start urls ')
    parser.add_argument('--name', action='store', help='spider name')
    parser.add_argument('--allowed_domains', action='append', help='domain')
    parser.add_argument('--loadconfig','-l', action='store', help='load config file')
    parser.add_argument('--jsonstr','-j',default='{}', action='store', help='load config file')

    dct0 = {'argument': [{'word': 'moon\n==='},{'word': '尔特瑞特人头\n==='}], 'set': {'CLOSESPIDER_ITEMCOUNT': '2'},
        'spider': 'baiduimage', 'output': None, 'start_urls': ['www.baidu.com'], 'name': None, 'allowed_domains': None, 'loadconfig': None}
    dctstr = json.dumps(dct0,ensure_ascii=False)
    print("dctstr=",dct0)
    cmdline = ['-j',dctstr]
    args  = parser.parse_args()
    dct = vars(args)
    print(  "dct['jsonstr']",dct['jsonstr'] )
    dct2 = json.loads( dct['jsonstr'].strip('"').replace("'",'"'))
    print("dct2=",dct2==dct0, dct2)
    print( dct2["argument"])
    # lst = dict2cmdline(dct)
    # print(lst,set(lst)==set(cmdline))

if __name__ == "__main__":
    main()

