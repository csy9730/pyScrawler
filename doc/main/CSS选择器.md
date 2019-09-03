# CSS选择器

## 常用语法

``` css

.page-ch /* class选择器 */
span.page-ch /* class选择器 */
#page-navigator /* id 选择器*/
a::text    /* text属性提取*/
img::attr(src) /* src属性提取*/
*::text
[attribute]   /* attr的选择器*/
div  p		/*div 内的p元素*/
```



CSS选择器用于选择你想要的元素的样式的模式。"CSS"列表示在CSS版本的属性定义（CSS1，CSS2，或对CSS3）。

## CSS 高级用法

| 选择器                                                       | 示例                  | 示例说明                                                  | CSS  |
| :----------------------------------------------------------- | :-------------------- | :-------------------------------------------------------- | :--- |
| [.*class*](http://www.scrapyd.cn/doc/sel-class.html)         | .intro                | 选择所有class="intro"的元素                               | 1    |
| [#*id*](http://www.scrapyd.cn/doc/sel-id.html)               | #firstname            | 选择所有id="firstname"的元素                              | 1    |
| [*](http://www.scrapyd.cn/doc/sel-all.html)                  | *                     | 选择所有元素                                              | 2    |
| *element*                                                    | p                     | 选择所有<p>元素                                           | 1    |
| *element,element*                                            | div,p                 | 选择所有<div>元素和<p>元素                                | 1    |
| [*element* *element*](http://www.scrapyd.cn/doc/sel-element-element.html) | div p                 | 选择<div>元素内的所有<p>元素                              | 1    |
| [*element*>*element*](http://www.scrapyd.cn/doc/sel-element-gt.html) | div>p                 | 选择所有父级是 <div> 元素的 <p> 元素                      | 2    |
| [*element*+*element*](http://www.scrapyd.cn/doc/sel-element-pluss.html) | div+p                 | 选择所有紧接着<div>元素之后的<p>元素                      | 2    |
| [[*attribute*\]](http://www.scrapyd.cn/doc/sel-attribute.html) | [target]              | 选择所有带有target属性元素                                | 2    |
| [[*attribute*=*value*\]](http://www.scrapyd.cn/doc/sel-attribute-value.html) | [target=-blank]       | 选择所有使用target="-blank"的元素                         | 2    |
| [[*attribute*~=*value*\]](http://www.scrapyd.cn/doc/sel-attribute-value-contains.html) | [title~=flower]       | 选择标题属性包含单词"flower"的所有元素                    | 2    |
| [[*attribute*\|=*language*\]](http://www.scrapyd.cn/doc/sel-attribute-value-lang.html) | [lang\|=en]           | 选择一个lang属性的起始值="EN"的所有元素                   | 2    |
| [:link](http://www.scrapyd.cn/doc/sel-link.html)             | a:link                | 选择所有未访问链接                                        | 1    |
| [:visited](http://www.scrapyd.cn/doc/sel-visited.html)       | a:visited             | 选择所有访问过的链接                                      | 1    |
| [:active](http://www.scrapyd.cn/doc/sel-active.html)         | a:active              | 选择活动链接                                              | 1    |
| [:hover](http://www.scrapyd.cn/doc/sel-hover.html)           | a:hover               | 选择鼠标在链接上面时                                      | 1    |
| [:focus](http://www.scrapyd.cn/doc/sel-focus.html)           | input:focus           | 选择具有焦点的输入元素                                    | 2    |
| [:first-letter](http://www.scrapyd.cn/doc/sel-firstletter.html) | p:first-letter        | 选择每一个<P>元素的第一个字母                             | 1    |
| [:first-line](http://www.scrapyd.cn/doc/sel-firstline.html)  | p:first-line          | 选择每一个<P>元素的第一行                                 | 1    |
| [:first-child](http://www.scrapyd.cn/doc/sel-firstchild.html) | p:first-child         | 指定只有当<p>元素是其父级的第一个子级的样式。             | 2    |
| [:before](http://www.scrapyd.cn/doc/sel-before.html)         | p:before              | 在每个<p>元素之前插入内容                                 | 2    |
| [:after](http://www.scrapyd.cn/doc/sel-after.html)           | p:after               | 在每个<p>元素之后插入内容                                 | 2    |
| [:lang(*language*)](http://www.scrapyd.cn/doc/sel-lang.html) | p:lang(it)            | 选择一个lang属性的起始值="it"的所有<p>元素                | 2    |
| [*element1*~*element2*](http://www.scrapyd.cn/doc/sel-gen-sibling.html) | p~ul                  | 选择p元素之后的每一个ul元素                               | 3    |
| [[*attribute*^=*value*\]](http://www.scrapyd.cn/doc/sel-attr-begin.html) | a[src^="https"]       | 选择每一个src属性的值以"https"开头的元素                  | 3    |
| [[*attribute*$=*value*\]](http://www.scrapyd.cn/doc/sel-attr-end.html) | a[src$=".pdf"]        | 选择每一个src属性的值以".pdf"结尾的元素                   | 3    |
| [[*attribute**=*value*\]](http://www.scrapyd.cn/doc/sel-attr-contain.html) | a[src*="runoob"]      | 选择每一个src属性的值包含子字符串"runoob"的元素           | 3    |
| [:first-of-type](http://www.scrapyd.cn/doc/sel-first-of-type.html) | p:first-of-type       | 选择每个p元素是其父级的第一个p元素                        | 3    |
| [:last-of-type](http://www.scrapyd.cn/doc/sel-last-of-type.html) | p:last-of-type        | 选择每个p元素是其父级的最后一个p元素                      | 3    |
| [:only-of-type](http://www.scrapyd.cn/doc/sel-only-of-type.html) | p:only-of-type        | 选择每个p元素是其父级的唯一p元素                          | 3    |
| [:only-child](http://www.scrapyd.cn/doc/sel-only-child.html) | p:only-child          | 选择每个p元素是其父级的唯一子元素                         | 3    |
| [:nth-child(*n*)](http://www.scrapyd.cn/doc/sel-nth-child.html) | p:nth-child(2)        | 选择每个p元素是其父级的第二个子元素                       | 3    |
| [:nth-last-child(*n*)](http://www.scrapyd.cn/doc/sel-nth-last-child.html) | p:nth-last-child(2)   | 选择每个p元素的是其父级的第二个子元素，从最后一个子项计数 | 3    |
| [:nth-of-type(*n*)](http://www.scrapyd.cn/doc/sel-nth-of-type.html) | p:nth-of-type(2)      | 选择每个p元素是其父级的第二个p元素                        | 3    |
| [:nth-last-of-type(*n*)](http://www.scrapyd.cn/doc/sel-nth-last-of-type.html) | p:nth-last-of-type(2) | 选择每个p元素的是其父级的第二个p元素，从最后一个子项计数  | 3    |
| [:last-child](http://www.scrapyd.cn/doc/sel-last-child.html) | p:last-child          | 选择每个p元素是其父级的最后一个子级。                     | 3    |
| [:root](http://www.scrapyd.cn/doc/sel-root.html)             | :root                 | 选择文档的根元素                                          | 3    |
| [:empty](http://www.scrapyd.cn/doc/sel-empty.html)           | p:empty               | 选择每个没有任何子级的p元素（包括文本节点）               | 3    |
| [:target](http://www.scrapyd.cn/doc/sel-target.html)         | #news:target          | 选择当前活动的#news元素（包含该锚名称的点击的URL）        | 3    |
| [:enabled](http://www.scrapyd.cn/doc/sel-enabled.html)       | input:enabled         | 选择每一个已启用的输入元素                                | 3    |
| [:disabled](http://www.scrapyd.cn/doc/sel-disabled.html)     | input:disabled        | 选择每一个禁用的输入元素                                  | 3    |
| [:checked](http://www.scrapyd.cn/doc/sel-checked.html)       | input:checked         | 选择每个选中的输入元素                                    | 3    |
| [:not(*selector*)](http://www.scrapyd.cn/doc/sel-not.html)   | :not(p)               | 选择每个并非p元素的元素                                   | 3    |
| [::selection](http://www.scrapyd.cn/doc/sel-selection.html)  | ::selection           | 匹配元素中被用户选中或处于高亮状态的部分                  | 3    |
| [:out-of-range](http://www.scrapyd.cn/doc/sel-out-of-range.html) | :out-of-range         | 匹配值在指定区间之外的input元素                           | 3    |
| [:in-range](http://www.scrapyd.cn/doc/sel-in-range.html)     | :in-range             | 匹配值在指定区间之内的input元素                           | 3    |
| [:read-write](http://www.scrapyd.cn/doc/sel-read-write.html) | :read-write           | 用于匹配可读及可写的元素                                  | 3    |
| [:read-only](http://www.scrapyd.cn/doc/sel-read-only.html)   | :read-only            | 用于匹配设置 "readonly"（只读） 属性的元素                | 3    |
| [:optional](http://www.scrapyd.cn/doc/sel-optional.html)     | :optional             | 用于匹配可选的输入元素                                    | 3    |
| [:required](http://www.scrapyd.cn/doc/sel-required.html)     | :required             | 用于匹配设置了 "required" 属性的元素                      | 3    |
| [:valid](http://www.scrapyd.cn/doc/sel-valid.html)           | :valid                | 用于匹配输入值为合法的元素                                | 3    |
| [:invalid](http://www.scrapyd.cn/doc/sel-invalid.html)       | :invalid              | 用于匹配输入值为非法的元素                                | 3    |







