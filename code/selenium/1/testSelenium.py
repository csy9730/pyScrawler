import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
# 继承至TestCase，表示这是一个测试用例类
class BaiduCase(unittest.TestCase):
  # 初始化的一部分
  def setUp(self):
    self.driver = Chrome("..\chromedriver.exe")
  # 测试用例方法，名称可以自定义，方法名称始终以test开头
  def test_serch(self):
    self.driver.get("https://www.baidu.com/")
    assert "百度一下" in self.driver.title
    element = self.driver.find_element_by_id("kw")
    element.clear()
    element.send_keys("python")
    element.send_keys(Keys.RETURN)
    assert "No results found." not in self.driver.page_source
  # 在执行完各种测试用例方法之后会执行，为一个清理操作
  def tearDown(self):
    self.driver.close()
if __name__ == "__main__":
  unittest.main()