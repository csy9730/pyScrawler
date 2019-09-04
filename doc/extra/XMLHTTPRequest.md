# XMLHTTPRequest

XMLHttpRequest 是 AJAX 的基础。

　XMLHttpRequest 术语缩写为XHR，中文可以解释为可扩展超文本传输请求。 

　XMLHttpRequest 对象可以在不向服务器提交整个页面的情况下，实现局部更新网页。 

　XMLHttpRequest的对象用于客户端和服务器之间的异步通信。

　它执行以下操作：

1. 在后台从客户端发送数据
2. 从服务器接收数据
3. 更新网页而不重新加载。

## AJAX

AJAX = Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）。

　AJAX 教程涵盖了适用于初学者和专业人士的AJAX技术的概念和示例。 

　AJAX 不是新的编程语言，而是一种使用现有标准的新方法。

　AJAX 是与服务器交换数据并更新部分网页的艺术，在不重新加载整个页面的情况下。

　AJAX 允许您仅将重要信息发送到服务器而不是整个页面。因此，只有来自客户端的有价值数据才会路由到服务器端。它使您的应用程序具有交互性和更快。 

`XMLHttpRequest`对象来发送`Ajax`请求

 ``` javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://www.lovejavascript.com/learnLinkManager/getLearnLinkList', true);
xhr.send(null);
 ```

