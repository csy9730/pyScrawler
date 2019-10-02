# scrapyd

Scrapyd是一个服务，用来运行scrapy爬虫的
它允许你部署你的scrapy项目以及通过HTTP JSON的方式控制你的爬虫
官方文档：http://scrapyd.readthedocs.org/
scrapyd其实就是一个服务器端，运行我们通过网络监控scrapy部署和执行：
scrapyd是服务器端，scrapyd-client是客户端
## install

``` bash
pip install scrapyd
pip install scrapyd-client
```

## deploy
scrapy.cfg文件
``` ini
[deploy:demo]
url = http://localhost:6800/
```
url那一行取消注释，这个就是我们要部署到目标服务器的地址，
然后，把[deploy]这里改为[deploy:demo]，这里是命名为demo，命名可以任意。demo是客户端名？默认是default。
scrapy_sample就是我们的工程名，也可以任意取名。

scrapyd-deploy位于python/scripts目录下
上传项目，会在当前目录下添加eggs和dbs文件夹
``` bash
scrapyd　　＃　运行scrapyd服务
scrapyd-deploy -l # 检查配置
scrapyd-deploy demo -p scrapy_sample # 上传项目
curl http://localhost:6800/schedule.json -d project=scrapy_sample -d spider=doc_scrapy # 执行spider
curl http://localhost:6800/listjobs.json?project=scrapy_sample  
curl http://localhost:6800/daemonstatus.json  #
```

## misc
scrapyd相关工具
客户端Gerapy：SpiderKeeper,scrapydWeb,ScrapydApi,ScrapydWeb
服务端:scrapydArt