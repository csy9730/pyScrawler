# 动漫之家爬虫


## 图片抓取

``` js
var arr_img = new Array();
    var page = '';
    eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('P g=g=\'["y\\/%0%7%8%1%9%2%1%6%5%0%4%2%0%3%a\\/%0%7%8%1%9%2%1%6%5%0%4%2%0%3%a%e%1%f%c%0%d%3\\/Q.b","y\\/%0%7%8%1%9%2%1%6%5%0%4%2%0%3%a\\/%0%7%8%1%9%2%1%6%5%0%4%2%0%3%a%e%1%f%c%0%d%3\\/1o.b","y\\/%0%7%8%1%9%2%1%6%5%0%4%2%0%3%a\\/%0%7%8%1%9%2%1%6%5%0%4%2%0%3%a%e%1%f%c%0%d%3\\/1p.b"]\';',62,121,'E5|E7|BE|B7|B0|84|9A|A6|96|B2|B4|jpg|AC12|8D|20|AC|pages|0032|0033|0035|0034|0036|0028|0026|0037|0027|0029|0030|0031|0046|0025|0045|0047|0078|0077|0060|0058|0061|0062|0063|0057|0056|0052|0053|0054|0055|0064|0065|0073|0072|0074|0075|0076|0051|0071|0066|0067|0068|0070|0069'.split('|'),0,{}))
    ;
```
以上语句会生成pages变量，存储所有jpg的url。所以我们需要在python执行js语句。

## 全站抓取
index:[tag-page],callback= parse_index
tag-page: [ next-page],callback= parse_page
tag-page:[ book ] ,callback= parse_book
book: [article ] ,callback= parse_article
article: [ img  ],callback=parse_article

[ ] 防止抓取重复url

## 吐槽抓取

``` html
<script type="text/javascript">
    $(function () {
        var point_page = document.createElement('script');
        point_page.type = 'text/javascript';
        point_page.async = true;
        point_page.src = 'https://static.dmzj.com/module/js/dmzjpointView.js';
        point_page.charset = 'UTF-8';
        $("body").append(point_page);
    });
    var type = '0';
    var comic_id = 1081;
    var chapter_id = 21138;
</script>
```

以下是dmzjpointView.js生成吐槽内容的接口
``` javascript
var url = 'https://user.dmzj.com/';
var comicUrl ="https://interface.dmzj.com";//接口连接
var type = 0
var comic_id = 1081;
var chapter_id = 21138;
var url=comicUrl+'/viewpoint/'+type+"/"+comic_id%300+"/"+comic_id+"/"+chapter_id +".js",
// var g_comic_id = res_id = '1081';		
// https://interface.dmzj.com/viewpoint/0/181/1081/21138.js	
// https://interface.dmzj.com/viewpoint/0/181/1081/21138.js?callback=success_jsonpCallback_201508281117&_=1568516505487
https://interface.dmzj.com/api/viewpoint/getViewpoint?callback=success_jsonpCallback_201508281118&type=0&type_id=1081&chapter_id=21138&more=1&_=1568516555026
```
## 手机网站抓取


``` 
https://www.dmzj.com/
https://m.dmzj.com/


http://comic.sfacg.com/
https://manhua.sfacg.com/
https://ac.qq.com/
http://www.u17.com/
```


## misc

``` 

https://www.36mh.com/manhua/tianjisanguo/
https://www.36mh.com/manhua/tianjisanguo/2408.html


<body class="clearfix">
	<!--[if lte IE 8]>
<div class="ie8-warning-mask"></div>
<div id="ie8-warning"><p>本页面采用HTML5+CSS3，您正在使用老版本 Internet Explorer ，在本页面的显示效果可能有差异。建议您升级到 <a
    href="http://www.microsoft.com/china/windows/internet-explorer/" target="_blank">Internet Explorer 11</a> 或以下浏览器：
    <br>
    <a href="http://www.mozillaonline.com/"><img src="https://img001.yayxcc.com/images/etc/browser-firefox.png" alt=""></a> /
    <a href="http://www.baidu.com/s?wd=google%E6%B5%8F%E8%A7%88%E5%99%A8"><img src="https://img001.yayxcc.com/images/etc/browser-chrome.png" alt=""></a> /
    <a href="http://www.operachina.com/"><img src="https://img001.yayxcc.com/images/etc/browser-opera.png" alt=""></a></p>
</div>
<![endif]-->
	<script>
		;var siteName = "";var siteUrl = "https://www.36mh.com/";;var chapterImages = ["1520436736pelnokw2U3Vgtb3D.jpg","1520436737UIUdURQMB6Ez4TCv.jpg","1520436737nevdmcAFbEeMpPcu.jpg","1520436737YZHWxUkd6wg_LL0y.jpg","1520436738QIInrnfRs2fZeEvc.jpg","1520436738-c8DZg66HmLR6m3v.jpg","15204367380K3D1_xcX3LSiBzP.jpg","1520436738oz49MRLaeJe8ZgYo.jpg","1520436739oF7aqfrhnrGTyi7V.jpg","1520436739YudtWvWfrTRe-aBR.jpg","1520436739BBrnTqiuyu6G7XsQ.jpg","1520436740Nlj__u46hlDYrwTy.jpg","15204367404OcKQtO1TUr0qBiC.jpg","1520436740e6JqtcZfbW7FDM5-.jpg","1520436741Abm1IHnTO1eXNzEI.jpg"];var chapterPath = "images/comic/2/2408/";var chapterPrice = 0;var chapterCanRead = 1;var pageTitle = "天机三国008_免费阅读";var comicUrl = "https://www.36mh.com/manhua/tianjisanguo/";var pageUrl = "https://www.36mh.com/manhua/tianjisanguo/";var pageImage = "https://img001.yayxcc.com/images/cover/201806/1530326670xqMN_3TrBxnSIr_R.jpg";var pageDomain = "https://www.36mh.com/";var pageId = "comic.16";var prevChapterData = {"id":2407,"comic_id":16,"comic_name":"天机三国","status":1,"vip":0,"is_end":0,"name":"007","type":0,"rtl":0,"image_mode":0,"category":4,"link":"","link_name":"","image_type":0,"count":16,"sort":999,"price":0,"created_at":1520422998,"updated_at":1520436736};var nextChapterData = {"id":2409,"comic_id":16,"comic_name":"天机三国","status":1,"vip":0,"is_end":0,"name":"009","type":0,"rtl":0,"image_mode":0,"category":4,"link":"","link_name":"","image_type":0,"count":13,"sort":999,"price":0,"created_at":1520422998,"updated_at":1520436745};
	</script>
    

[
"1520436736pelnokw2U3Vgtb3D.jpg",
"1520436737UIUdURQMB6Ez4TCv.jpg",
"1520436737nevdmcAFbEeMpPcu.jpg",
"1520436737YZHWxUkd6wg_LL0y.jpg",
"1520436738QIInrnfRs2fZeEvc.jpg",
"1520436738-c8DZg66HmLR6m3v.jpg",
"15204367380K3D1_xcX3LSiBzP.jpg",
"1520436738oz49MRLaeJe8ZgYo.jpg",
"1520436739oF7aqfrhnrGTyi7V.jpg",
"1520436739YudtWvWfrTRe-aBR.jpg",
"1520436739BBrnTqiuyu6G7XsQ.jpg",
"1520436740Nlj__u46hlDYrwTy.jpg",
"15204367404OcKQtO1TUr0qBiC.jpg",
"1520436740e6JqtcZfbW7FDM5-.jpg",
"1520436741Abm1IHnTO1eXNzEI.jpg"
]
```