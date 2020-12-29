# Fiddler

[TOC]

Fiddler是一个HTTP调试[抓包](http://www.onlinedown.net/soft/971226.htm)工具。它通过代理的方式获取程序http通讯的数据，可以用其检测网页和服务器的交互情况，Fiddler可以帮您记录，调试Microsoft Internet Explorer与Web应用程序的交互，找到Web程序运行性能的瓶颈，还有如查看向Web服务器发送coo[kies](http://www.onlinedown.net/soft/419785.htm)的内容，下载内容的大小等功能。强烈推荐用户使用。

没有Fiddler时，本地应用与服务器通信，直接向服务器发送Request请求，待服务器处理之后将处理结果返回本地，本地应用接受响应Response。 有了Fiddler时，本地应用和服务器之间所有的Request，Response都将经过Fiddler，由Fiddler进行转发。由于所有的数据都会经过Fiddler，所以Fiddler能够截获这些数据没实现网络数据抓包。

## 浏览器设置

v5.0.20192.25091 for .NET 4.6.1 Built: 2019年6月4日版本的界面如下所示

1. 下载fiddler
2.  chrome设置proxy

## 开启https监听

Fiddler 默认下，Fiddler不会捕获HTTPS会话，需要你设置下。

1. 打开options-https
2. 下载FiddlerRoot.cer
3. 双击FiddlerRoot.cer,选择导入证书



![1567835502765](..\img\%5CUsers%5Ccsy_acer_win8%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5C1567835502765.png)



## Android 抓包设置

1. 确保电脑和手机都连在同一个 wifi 下
2. fiddle设置允许远程连接
3. 下载CA证书
4. 导入CA证书（可以先清除以前证书）
5. 安卓端wifi开启代理

![1567835575190](..\img\%5CUsers%5Ccsy_acer_win8%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5C1567835575190.png)

ip地址使用电脑端的IP地址和端口号。

![CA证书导入](..\img\CA证书下载.gif)

![CA证书导入](..\img\CA证书导入.gif)

![CA证书导入](..\img\wifi的proxy设置.gif)

## 使用

### 过滤器

可以基于DNS过滤会话

### 手机本机浏览器·过滤

`from all processes` : 抓取所有的 https 程序, 包括 本机 和 手机
`from browsers only` : 只抓取浏览器中的 https 请求
`from non-browsers only` : 只抓取除了浏览器之外的所有 https 请求
`from remote clients only` ： 抓取远程的客户端的 https ,可以代表手机

### 其他操作

清空会话

## 问题

**Q**:Fiddler抓包出现tunnel to 443

**A**: 如果是电脑端出现https的tunnel to 443，可以按照设置Decrypt https traffic。

了如果是安卓端接受app时出现https的443，可能是CA证书设置未成功，需要清理证书重新设置。

如果是出现http的443状态，http协议没有定义加密操作，这种情况难以处理。

**Q**:如何清除证书

**A**:PC端命令行中打开certmgr.msc,查找fiddler证书，手动删除即可。Android端打开设置-系统设置-证书管理，点击清除即可

**Q**: 证书无法生成

**A**： 在fiddler的根目录，打开命令行，输入`makecert.exe -r -ss my -n "CN=DO_NOT_TRUST_FiddlerRoot, O=DO_NOT_TRUST, OU=Created by http://www.fiddler2.com" -sky signature -eku 1.3.6.1.5.5.7.3.1 -h 1 -cy authority -a sha1 -m 120 -b 10/12/2030`

**Q**： 其他问题

**A**： 汉化版本，需要拷贝CertMaker.dll到fiddler根目录，才能生成证书

**Q**: 小米手机难以安装CA证书

**A**：小米手机里。在到设置——更多设置——系统安全——从SD卡安装或者设置——WiFi——高级设置——安装证书。或者可以下载Android 模拟器替代。

Mac 下请使用 Charles 代替 Fiddler。

fiddler使用完之后，记得把手机的代理设置回来，以免fiddler关闭之后无法联网。
重启fiddler



## 参考

[下载链接：https://www.telerik.com/download/fiddler/fiddler4](<https://www.telerik.com/download/fiddler/fiddler4>)



