# Chrome开发者工具



面板上包含了Elements面板、Console面板、Sources面板、Network面板、
Timeline面板、Profiles面板、Application面板、Security面板、Audits面板这些功能面板。



- Elements:查找网页源代码HTML中的任一元素,手动修改任一元素的属性和样式且能实时在浏览器里面得到反馈。

- Console:记录开发者开发过程中的日志信息，且可以作为与JS进行交互的命令行Shell。

- Sources:断点调试JS。

- Network:从发起网页页面请求Request后分析HTTP请求后得到的各个请求资源信息（包括状态、资源类型、大小、所用时间等），可以根据这个进行网络性能优化。

- Timeline:记录并分析在网站的生命周期内所发生的各类事件，以此可以提高网页的运行时间的性能。

- Profiles:如果你需要Timeline所能提供的更多信息时，可以尝试一下Profiles,比如记录JS CPU执行时间细节、显示JS对象和相关的DOM节点的内存消耗、记录内存的分配细节。

- Application:记录网站加载的所有资源信息，包括存储数据（Local Storage、Session Storage、IndexedDB、Web SQL、Cookies）、缓存数据、字体、图片、脚本、样式表等。

- Security:判断当前网页是否安全。

- Audits:对当前网页进行网络利用情况、网页性能方面的诊断，并给出一些优化建议。比如列出所有没有用到的CSS文件等。

  注： 这一篇主要讲解前三个面板Elements、Console、Sources。

## Console面板

| $()  | 返回与指定的CSS选择器相匹配的第一个元素，等同于`document.querySelector()` |
| ---- | ------------------------------------------------------------ |
| $$() | 返回与指定的CSS选择器相匹配的所有元素的数组，等同于`document.querySelectorAll()` |
| $x() | 返回与指定的XPath相匹配的所有元素的数组                      |

## Sources面板

你可以在这个面板里面调试你的JS代码，也可以在工作区打开你的本地文件。

### 调试JS代码

 DOM元素节点发生改变时

在Elements面板中指定的DOM节点上右击，在弹出的菜单中选择`Break on...`，可以看到三个选择项，比如我们选择`Subtree modifications`，
那么当选择的节点里面的子节点被添加、删除、修改，则断点就会被触发。设置方式如下图：

当XHR生命周期状态发生改变或者XHR的URL与Sources面板右侧的XHR Breakpoints栏设置的字符串匹配时，则断点就会有触发。

指定的事件执行时

在Sources面板右侧的XHR Breakpoints栏下面是Event Listener Breakpoints,列出了各种类型的事件，勾选你要监听的事件，
在指定的事件执行时，断点就会有触发。



`Network`面板可以记录页面上的网络请求的详情信息，从发起网页页面请求Request后分析HTTP请求后得到的各个请求资源信息（包括状态、资源类型、大小、所用时间、Request和Response等），可以根据这个进行网络性能优化。

我把Google官方网站上介绍Network面板的图贴到这里，该面板主要包括5大块窗格(Pane)：

1. Controls 控制Network的外观和功能。
2. Filters 控制Requests Table具体显示哪些内容。
3. Overview 显示获取到资源的时间轴信息。
4. Requests Table 按资源获取的前后顺序显示所有获取到的资源信息，点击资源名可以查看该资源的详细信息。
5. Summary 显示总的请求数、数据传输量、加载时间信息。