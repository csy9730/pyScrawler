# Crawler





## crawler

- 图片爬虫： 
  - baidu_img, 
  - meizitu,mzitu,mm131,
- 漫画爬虫：dmzj,sfacg
  文档爬虫: blog,
  小说：biquge，
  BBS爬虫： tieba，
  新闻爬虫：
- shop： 
  * jingdong，
  * taobao
- music：
  netease, spider163-master
  baidumusic
  video：biblbili
  - VIP 视频破解无名网站：http://www.administrator5.com/WMXZ.WANG/index.html
- Rss:
- movie: 
  - doubantop250,
  - maoyanboard
  - https://github.com/iawia002/annie
    12306
    知乎登录
    豆瓣登录
    微博登陆



使用状态机处理response。

层级： index-> list->(book/album)->article 
开始url： 指定url？如何判断当前页面parse函数
抓取策略： 几级深度？深度优先vs广度优先
结束策略： item_count, time_expire

**Q**:结构化搜索？
**A**:scrapy是扁平化解构，常规网站是多级结构。rule 是扁平化，没有结构，不好用.扁平化结构，不关心网站结构层次，所有内容都经过队列，队列后进先出，丢失了先后顺序，结构信息。常规网站有着鲜明的结构层次，入口页面包含多个列表页，列表页含有多个分页，列表页包含内容页，按照这个层次化结构抓取，上级页面包含了下级页面的部分信息。
采用分页计算权重方式，总列表页，列表页，文章页，三者对应关系为[1,5, 100],则可以令权重为[105,21,1],每次从三者中选取最低权重的url开始遍历。

**Q**: 如何设置翻页设置？添加翻页数
        通过翻页，限制页面数量。
        列表页翻页是否增加深度？
命令行配置： 
`spider -c abc`
**Q**: 如何配置pythonobject，例如item，middleware，pipeline等等

££ todo
- [ ] 添加类postman内容的request
- [ ] 查询参数拼接时是否有序？
- [ ] jupyter中调试request。
- [ ] scrapy markdown
- [ ] scrapy rss 
- [x]  readthedocs
- [ ] scrapy 通用爬虫,broadcrawler
- [ ] coolscrapy
- [-] docker & splash
- [ ] smtp
- [ ] add headless chrome options
- [ ] email 保存&接收&发送
- [ ] ss: celery
- [ ] ss:rpc 框架
- [ ] ss:事件循环
- [ ] https://www.51xs.org/info/1.html
- [ ]  http://www.girl13.com  