# Splash

为了加速页面的加载速度，页面的很多部分都是用JS生成的，而对于用scrapy爬虫来说就是一个很大的问题，因为scrapy没有JS engine，所以爬取的都是静态页面，对于JS生成的动态页面都无法获得。
解决方案：

利用第三方中间件来提供JS渲染服务： scrapy-splash 等。
利用webkit或者基于webkit库

Splash是一个Javascript渲染服务。它是一个实现了HTTP API的轻量级浏览器，Splash是用Python实现的，同时使用Twisted和QT。Twisted（QT）用来让服务具有异步处理能力，以发挥webkit的并发能力。

install_qtwebkit

## install
1. 使用docker安装
2. 直接安装

### docker 安装

``` bash
docker pull scrapinghub/splash
# 用docker运行scrapinghub/splash：
docker run -p 8050:8050 scrapinghub/splash
```

Clone the repo from GitHub:
``` bash
$ git clone https://github.com/scrapinghub/splash/
Install dependencies:

$ cd splash/dockerfiles/splash
$ sudo cp ./qt-installer-noninteractive.qs /tmp/script.qs
$ sudo ./provision.sh \
           prepare_install \
           install_msfonts \
           install_extra_fonts \
           install_deps \
           install_flash \
           install_qtwebkit_deps \
           install_official_qt \
           install_qtwebkit \
           install_pyqt5 \
           install_python_deps
```
By default, Splash API endpoints listen to port 8050 on all available IPv4 addresses. 