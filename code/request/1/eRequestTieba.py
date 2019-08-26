# -*- coding:utf-8 -*-
#!/user/bin/python

import urllib
import urllib.request as urllib2
import re



#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

    
class BDTB:
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ, floorTag=0):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        #全局file变量，文件写入操作对象
        self.file = None
        #楼层标号， 初始化为1
        self.floor = 1
        #默认标题
        self.defaultTitle = u"百度某某贴吧"
        #是否写入楼层分隔符标记
        self.floorTag = floorTag

    #传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError as e:
            if hasattr(e, "reason"):
                print (u"连接百度贴吧失败,错误原因", e.reason)
                return None

    #获得帖子标题
    def getTitle(self,page):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None

    #得到帖子页数
    def getPageNum(self,page):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?<span.*?>(.*?)</span',re.S)
        result = re.search(pattern, page)
        if result:
            #print "回复个数："
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None

    #获得帖子的内容
    def getContent(self,page):
        page = self.getPage(1)
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        floor = 1
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
            #print self.tool.replace(item)
            #floor += 1
        return contents
    
    def setFileTitle(self,title):
        if title is not None:
            self.file = open(title + ".txt", "wb+")
        else:
            self.file = open(self.defaultTitle + ".txt", "wb+")

    def writeData(self,contents):
        for item in contents:
            if self.floorTag == '1':
                floorline = "\n" + str(self.floor) + u"-------------------------------------\n"
                self.file.write(floorline)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print ("URL已失效，请重试")
            return
        try:
            print( "该帖子共有" + str(pageNum) + "页")
            for i in range(1,int(pageNum) + 1):
                print ("正在写入第" + str(i) + "页数据")
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print( "写入异常，原因" + e.message)
        finally:
            print( "Succeed~")
                               

baseURL = 'http://tieba.baidu.com/p/' + str( "4476501484")
seeLZ =  0 #raw_input("是否只看楼主，是输入1，否输入0\\n")
floorTag = 0 #raw_input("是否写入楼层信息，是输入1，否输入0\\n")
bdtb = BDTB(baseURL, seeLZ,floorTag)
bdtb.start()
