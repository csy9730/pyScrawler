# docker toolbox



## install

ubuntu 可以直接使用docker。win10安装docker，win7和win8使用docker toolbox。



一. 使用docker toolbox安装docker

对于Windows用户来说，使用docker toolbox来安装docker是最简单的方式

docker toolbox是一个工具集，它主要包含以下一些内容：

Docker CLI 客户端，用来运行docker引擎创建镜像和容器
Docker Machine. 可以让你在windows的命令行中运行docker引擎命令
Docker Compose. 用来运行docker-compose命令
Kitematic. 这是Docker的GUI版本
Docker QuickStart shell. 这是一个已经配置好Docker的命令行环境
Oracle VM Virtualbox. 虚拟机

## helloworld

``` bash

# 开启 service 
sudo service docker start
# systemctl 
sudo systemctl start docker

docker pull library/hello-world # 下载镜像
docker images  # 查看下载的jimages
docker run  
docker run -p 8050:8050 scrapinghub/splash # 相当于pull+run
```
浏览器打开localhost:8050可以看到服务


··· python
#Splash服务器地址
SPLASH_URL = 'http://localhost:8050'                                                                    
#开启两个下载中间件，并调整HttpCompressionMiddlewares的次序                                      
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware':725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':810,                         
}
#设置去重过滤器
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
#用来支持cache_args（可选）
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
}
DUPEFILTER_CLASS ='scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE ='scrapy_splash.SplashAwareFSCacheStorage'   
```
