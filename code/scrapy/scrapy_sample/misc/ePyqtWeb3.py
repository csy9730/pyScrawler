import sys
# from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUI()
    def setupUI(self):
        layout = QVBoxLayout()
        self.web_browser = QWebEngineView()
        # self.web_browser.load(QUrl('https://pan.baidu.com/s/17XlMuMzfQhwJ5R1Bn7yuiA#list/path=%2F'))
        btn = QPushButton('加载脚本')
        layout.addWidget(btn)
        layout.addWidget(self.web_browser)
        self.setLayout(layout)
        self.web_browser.load(QUrl('https://map.baidu.com'))
        btn.clicked.connect(self.add_script)
        # self.web_browser.loadFinished.connect(self.add_script)
    def add_script(self):
        print('按钮已被点击')
        # self.web_browser.page().toPlainText(lambda x: print(x))
        self.web_browser.page().toHtml(lambda x: print(x))
        # self.web_browser.page().runJavaScript('''function getname(){
        # var elem = document.getElementById("user-center");
        # elem.remove();
        # var elem2 = document.getElementById("message-center");
        # elem2.remove();
        # var elem3 = document.querySelector('.BMap_cpyCtrl');
        # elem3.remove();
        # var elem4 = document.querySelector('.BMap_scaleCtrl');
        # elem4.remove();
        # var elem5 = document.querySelector('#newuilogo');
        # elem5.remove();};
        # getname();
        # ''')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())