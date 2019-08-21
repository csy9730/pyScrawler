# selenium
## 安装
``` bash
# pip install selenium
```

selenium支持多种浏览器，需要安装自动化测试驱动

## demo
与一个网页进行的真正的交互，具体的说，与网页的HTML元素进行交互。如果需要与之交互，那么久必须要查找到HTML的元素。WebDriver提供了多种查找HTML元素的方法。例如，给定一个元素为：

<input type="text" name="passwd" id="passwd-id"/>

``` python
# 我们可以使用下面任意方法查找到它：
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
elem.send_keys(Keys.ARROW_DOWN)
elem.clear() # 清除文本框

element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    option.click()

from selenium.webdriver.support.ui import Select
element = driver.find_element_by_xpath("//select[@name='name']")
select = Select(element)
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value("value")


# webDriver还提供取消选择所有选项的功能：

element = driver.find_element_by_id('id')
select = Select(element)
select.deselect_all()

# Select还具有获取所有已经选中的标签的方法：


element = driver.find_element_by_id('id')
select = Select(element)
all_options = select.all_selected_options

# 获取所有可用的选项:
options = select.options

# 完成后表格填写后，您可以需要提交，一种方法是找到submit按钮并点击它：
driver.find_element_by_id('submit').click()
# WebDriver在每个元素上都有一个submit的便利方法，如果你在一个表单的元素上调用它，Webdriver会遍历DOM直到包含表单，然后调用它：
element.submit()
# WebDriver还提供了前进与后退的操作：
driver.forward()
driver.back()
# WebDriver还可以进行设置Cookies和获取Cookies：
driver.get('https://www.baidu.com/')
driver.add_cookie({"name":"foo","value":"laozhang"})
print(driver.get_cookies()
```

