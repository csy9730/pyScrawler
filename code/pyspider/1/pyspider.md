# pyspider
``` bash
pip install pyspider
pyspider
```

**Q**:`alueError: Invalid configuration:  - Deprecated option 'domaincontroller': use 'http_authenticator.domain_controller' instead.`
**A**:
安装完爬虫框架pyspider之后，使用pyspider all 命令，输入http://localhost:5000运行就出现上述错误
原因是因为WsgiDAV发布了版本 pre-release 3.x。
解决方法如下：
在安装包中找到pyspider的资源包，然后找到webui文件里面的webdav.py文件打开，修改第209行即可。
把
'domaincontroller': NeedAuthController(app),
修改为：
'http_authenticator':{
        'HTTPAuthenticator':NeedAuthController(app),
    },
然后再执行pyspider all就能够通过http://localhost:5000打开页面了

**Q**:method not allowed!

[http://docs.pyspider.org/en/latest/Quickstart/](http://docs.pyspider.org/en/latest/Quickstart/)