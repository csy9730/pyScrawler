#-*- coding:utf-8 -*- 
import os,sys,time
import json
import configparser
sys.path.append('ui')
import subprocess, io

from PyQt5 import QtCore, QtGui, uic,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QVBoxLayout, QSizePolicy, QWidget,QListWidgetItem,QFileDialog,QFileSystemModel 
from PyQt5.QtCore import Qt,QTimer,QFile
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty,QUrl,QProcess
from PyQt5.QtWidgets import QFileDialog,QListWidgetItem,QTableWidgetItem
from PyQt5.QtWebEngineWidgets import QWebEngineView

from ui.pyscr_rc import  *
from ui.ui_mainwidow import  Ui_MainWindow
# Ui_MainWindow, QtBaseClass = uic.loadUiType("ui/mainwindow.ui")
from scrapy_sample.utils import dict2cmdline
import copy
# from scrapy import log
class scrapySetting(object):
    def __init__(self):
        self._cmd = 'scrapy crawl'
        self.spider = 'dmzj'
        self.job = 'crawl'
        self.setting = {"CLOSESPIDER_ITEMCOUNT":11,"JOBDIR":None}
        self.tagSetting = {"book":"sss","page":"sfsdfsdf"}
    def getCmd(self):
        self._cmd = 'scrapy {0} {1}'.format( self.job,self.spider)
        return self._cmd
        
class EmittingStream(QtCore.QObject):  
        textWritten = QtCore.pyqtSignal(str)  #定义一个发送str的信号
        def write(self, text):
            self.textWritten.emit(str(text)) 
class MainWindow(QMainWindow, Ui_MainWindow):
    sgnDat = pyqtSignal(list) ###
    sgnLabel = pyqtSignal(list) ###
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(u'爬虫工具')
        self.initProc()  

        self._default_config = { "argument": {"START_URLS":"www.abc.com"    },    "set": { "IMAGES_STORE":"images","CLOSESPIDER_ITEMCOUNT": "2","JOBDIR": "scr_job" },
            "spider": "meizitu0",    "output": [        "scr_abc.jl"    ]}
        self.config = copy.copy(self._default_config)
        self.loadConfig()
        self._configWrite( self.config  )
        self.project_name = 'setting.scrproj'
        self.spider_info=[
            {"name":"meizitu","tag":["图片"],"base_url":"https://www.meizitu.com","description":"..."},
            {"name":"meizitu0","tag":["图片"],"base_url":"https://www.meizitu.com","description":"..."},
            {"name":"mm131","tag":["图片"],"base_url":"https://www.mm131.net","description":"..."},
            {"name":"mzitu","tag":["图片"],"base_url":"https://www.mzitu.net","description":"..."},
            {"name":"dmzj","tag":["漫画"],"base_url":"https://manhua.dmzj.com","description":"..."},
            {"name": "sfacg","tag":["漫画"],"base_url":"https://manhua.sfacg.com","description":"..."},
        ]
        if os.path.exists('spider_info.json'):
            with open('spider_info.json','r',encoding="utf-8")as fp:
                self.spider_info = json.load(fp)
        spiderList = [d["name"] for d in self.spider_info ]
        self.comboBox.clear()
        self.comboBox.addItems(spiderList)  

        self.listWidget.addAction(self.actionNewItem)
        self.listWidget.addAction(self.actionDeleteItem)        
        self.listWidget.addAction(self.actionClearItems)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.listWidget.itemDoubleClicked.connect( self.on_listWidget_itemDoubleClicked)

        self.tableWidget_import(self.spider_info)
        self._recordRecent = {"recentProject":["setting.scrproj"],}
        self.dirModel = QFileSystemModel()
        self.treeView.setModel(self.dirModel )  
        self.setDir()
        QTimer.singleShot(200, self.setDir)
        self.addStyleSheet("ui/qss/black_green.qss")
        # self.tmrTime = QtCore.QTimer()
        # self.tmrTime.setInterval(1000)
        # self.tmrTime.timeout.connect( self.on_tmrTime_timeout)
        # self.tmrTime.start()
        self.install_web()
    def addStyleSheet(self,pfn):
        with open(pfn,"rb") as fp:
            styleSheet = fp.read()
            print(styleSheet)
            self.setStyleSheet( styleSheet.decode("utf-8"))

    def initProc(self):
        self.proc = QProcess(self)
        self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.proc.readyReadStandardOutput.connect(self.on_procReceived)
        # QObject::connect(m_process,SIGNAL(readyRead()),this,SLOT(readOutput()));
        self.proc.finished.connect(self.onFinished)
    def setDir(self,pth= "images"):    
        self.dirModel.setRootPath(pth)             
        self.treeView.setRootIndex(self.dirModel.index(pth))

    def _configWrite(self,dct):
        self.comboBox.setCurrentIndex( self.comboBox.findText(dct['spider']))
        
        self.ledImagedir.setText( dct["set"].get("IMAGES_STORE",""))
        if dct["set"].get("JOBDIR") is not None:
            self.chbAddScratch.setChecked(True)
            self.ledJobdir.setText( dct["set"]["JOBDIR"])
        if dct["set"].get("CLOSESPIDER_ITEMCOUNT") is not None:
            self.chkMaxItem.setChecked(True)
            self.spbMaxItem.setValue( int( dct["set"]["CLOSESPIDER_ITEMCOUNT"]) )
        if dct["set"].get("CLOSESPIDER_TIMEOUT") is not None:
            self.chkMaxTime.setChecked(True)
            self.spbMaxTime.setValue( int( dct["set"]["CLOSESPIDER_TIMEOUT"]) )
        if dct["set"].get("CLOSESPIDER_PAGECOUNT") is not None:
            self.chkMaxPage.setChecked(True)
            self.spbMaxPage.setValue( int( dct["set"]["CLOSESPIDER_PAGECOUNT"]) )  

        if dct["set"].get("LOG_LEVEL") is not None:
            self.cmbLogLevel.setCurrentIndex( self.cmbLogLevel.findText( dct["set"]["LOG_LEVEL"] ) )
        if dct["set"].get("LOG_ENABLED") is not None:
            self.chkLogEnable.setChecked( dct["set"].get("LOG_ENABLED") )
        if dct["set"].get("LOG_FILE") is not None:
            self.ledLogFile.setText( dct["set"].get("LOG_FILE") )    
        if dct["set"].get("LOG_STDOUT") is not None:
            self.chkLogStdout.setChecked( dct["set"].get("LOG_STDOUT") )


        if dct.get('start_urls'):
            self.listWidget_import( dct['start_urls']  )
            # self.ledBookname.setText(dct['start_urls'][0])
            # self.ledBookname.setText("")
                   
        self.spbMaxDepth.setValue(  dct["set"].get("DEPTH_LIMIT",0) )
        self.spbMaxDepthWeight.setValue(  dct["set"].get("DEPTH_PRIORITY",0) )

    def _configRead(self):
        dct= self.config
        if self.chbAddScratch.isChecked():
            dct['set']['JOBDIR'] = self.ledJobdir.text()
        else:
            if dct['set'].get("JOBDIR"):
                del(dct['set']['JOBDIR'])

        dct['set']['IMAGES_STORE'] = self.ledImagedir.text()
        
        if self.chkMaxItem.isChecked():
            dct['set']['CLOSESPIDER_ITEMCOUNT'] = self.spbMaxItem.value()
        else:
            if dct['set'].get("CLOSESPIDER_ITEMCOUNT"):
                del(dct['set']['CLOSESPIDER_ITEMCOUNT'])
        if self.chkMaxTime.isChecked():
            dct['set']['CLOSESPIDER_TIMEOUT'] = self.spbMaxTime.value()
        else:
            if dct['set'].get("CLOSESPIDER_TIMEOUT"):
                del(dct['set']['CLOSESPIDER_TIMEOUT'])
        if self.chkMaxPage.isChecked():
            dct['set']['CLOSESPIDER_PAGECOUNT'] = self.spbMaxPage.value()
        else:
            if dct['set'].get("CLOSESPIDER_PAGECOUNT"):
                del(dct['set']['CLOSESPIDER_PAGECOUNT'])
        
        lst = self.listWidget_export()
        if lst!=[]:
            dct['start_urls'] = lst
        else:
            if dct.get("start_urls"):
                del(dct['start_urls'])

        if self.spbMaxDepth.value():
            dct["set"]["DEPTH_LIMIT"] = self.spbMaxDepth.value()
        if self.spbMaxDepthWeight.value():
            dct["set"]["DEPTH_PRIORITY"] = self.spbMaxDepth.value()    

        dct["set"]["LOG_LEVEL"] = self.cmbLogLevel.currentText()
        dct["set"]["LOG_ENABLED"] = self.chkLogEnable.isChecked()
        if self.ledLogFile.text() !="":
            dct["set"]["LOG_FILE"] = self.ledLogFile.text() 
        else:
            if dct["set"].get("LOG_FILE"):
                del(dct["set"]["LOG_FILE"])
        dct["set"]["LOG_STDOUT"] = self.chkLogStdout.isChecked()

        dct["spider"] = self.comboBox.currentText() 
        return dct
    def saveConfig(self,project_name='setting.scrproj'):
        self.config.update(self._configRead())        
        with open(project_name,'w') as fp:
            json.dump(self.config,fp,indent=4)
        self.showConfig()
    
    def loadConfig(self,project_name =  'setting.scrproj'):
        if os.path.exists(project_name):
            with open(project_name, 'r')   as fp:                           
                dct = json.load(fp)
                self.config.update( dct)
                self.showConfig()
    def showConfig(self):
        self.txtConfig.setText( json.dumps( self.config,indent=4,ensure_ascii=False))
    def importConfig(self):
        try:
            txt = self.txtConfig.toPlainText()
            self.config = json.loads( txt )
        except:
            QMessageBox.warning(self,"error","配置导入出错")
    @pyqtSlot() 
    def on_btnImportConfig_clicked(self):
        self.importConfig()
        self._configWrite(self.config) 
    @pyqtSlot() 
    def on_btnExportConfig_clicked(self):
        self.showConfig()
    @pyqtSlot() 
    def on_actionNewProj_triggered(self):
        print("on_actionNewProj_triggered")
        self.config = self._default_config  
        self._configWrite(self.config)
    @pyqtSlot()
    def on_actionSave_triggered(self):
        fileName1, filetype = QFileDialog.getSaveFileName(self,
                  "选取保存文件路径",
                  "./",
                  "Text Files (*.scrproj);;All Files (*)")  #设置文件扩展名过滤,注意用双分号间隔
        if fileName1!='':
            print(fileName1,filetype)
            self.ledProjectpath.setText( fileName1 )
            self.project_name = fileName1
            self.saveConfig()
    @pyqtSlot()
    def on_actionOpenProj_triggered(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                  "打开文件",
                  "./",
                  "Text Files (*.scrproj);;All Files (*)")  
        if fileName1!='':
            print(fileName1,filetype)
            self.ledProjectpath.setText( fileName1 )
            self.project_name = fileName1
            self.loadConfig(self.project_name)
    
    @pyqtSlot() 
    def on_btnProjectpath_clicked(self):        
        fileName1, filetype = QFileDialog.getSaveFileName(self,
                  "选取保存文件路径",
                  "./",
                  "Text Files (*.scrproj);;All Files (*)")  #设置文件扩展名过滤,注意用双分号间隔
        if fileName1:
            print(fileName1,filetype)
            self.ledProjectpath.setText( fileName1 )
            self.project_name = fileName1            
    @pyqtSlot() 
    def on_btnImagedir_clicked(self):
        folder_path  = QFileDialog.getExistingDirectory(self,"打开文件夹", "./") 
        if folder_path:
            print(folder_path)
            self.ledImagedir.setText( folder_path )
            self.setDir( folder_path )
    @pyqtSlot() 
    def on_btnJobdir_clicked(self):
        folder_path  = QFileDialog.getExistingDirectory(self,"打开文件夹", "./") 
        if folder_path:
            print(folder_path)
            self.ledJobdir.setText( folder_path )
            
    @pyqtSlot() 
    def on_actionStart_triggered(self):
        self.config = self._configRead()
        # print(self.config)
        self.showConfig()
        param = dict2cmdline(self.config)
        if os.path.exists('crawl.exe'):
            cmdline =  [ 'crawl'  ]
        else:
            cmdline =  [ 'python','crawl.py' ]
        cmdline.extend( param)
        print(cmdline)
        self.proc.start(cmdline[0],cmdline[1:] )
        return 
        print("start")        
        book = self.ledBookname.text()
        if book=='':
            QMessageBox.warning(self,'警告',' 请输入书名(拼音形式)')
            return
        cmd = 'scrapy crawl dmzj -a book={0} '.format( book ).split(' ')
        cmd = list(filter(str.strip,cmd))
        print(cmd)
        self.proc.start(cmd[0],cmd[1:] )

    @pyqtSlot() 
    def on_btnRun_clicked(self):
        self.btnRun.setEnabled(0)
        cmd = self.ledRunstring.text()
        cmdSp = list( filter(lambda x:x!='',cmd.split(' ')) )
        print(cmdSp) 
        self.textBrowser.append(cmd)    
        self.proc.start(cmdSp[0], cmdSp[1:] )
    #@pyqtSlot() a
    def onFinished(self, exitCode, exitStatus):
        print("onFinished ")
        self.btnRun.setEnabled(True)
    @pyqtSlot()
    def on_procReceived(self):
        # st = self.proc.readAllStandardOutput().data()        
        st= bytes(self.proc.readAll()).decode('gbk').strip()  
        print("on_procReceived",st )
        self.textBrowser.append( st)        
        
    @pyqtSlot() 
    def on_actionStop_triggered(self):       
        # self.proc.terminate()
        self.proc.kill()
        print("stop")
    @pyqtSlot() 
    def on_actionClear_triggered(self):
        self.textBrowser.clear()
    @pyqtSlot()     
    def on_btnNewItem_clicked(self):
        self.on_actionNewItem_triggered()
    @pyqtSlot() 
    def on_actionNewItem_triggered(self):
        index = self.listWidget.currentRow();
        item = QListWidgetItem();
        item.setText(self.ledBookname.text());
        self.listWidget.insertItem(index + 1, item);
    @pyqtSlot() 
    def on_actionDeleteItem_triggered(self):
        item = self.listWidget.currentRow()        
        self.listWidget.takeItem(item)
    @pyqtSlot() 
    def on_actionClearItems_triggered(self):
        self.listWidget.clear();
    @pyqtSlot() 
    def on_listWidget_itemDoubleClicked(self):
        item = self.listWidget.currentItem() 
        item.setFlags(item.flags() | Qt.ItemIsEditable)
    def listWidget_import(self,lst):
        self.listWidget.clear()
        for s in lst:
            aItem = QListWidgetItem()
            aItem.setText(s);
            self.listWidget.addItem( aItem);
    def listWidget_export(self):
        return [ self.listWidget.item(i).text() for i in range(self.listWidget.count())  ]
    
    @pyqtSlot() 
    def on_tableWidget_itemDoubleClicked(self):
        item = self.tableWidget.currentItem() 
        item.setFlags(item.flags() | Qt.ItemIsEditable)

    def tableWidget_import(self,lst):        
        self.tableWidget.clear()
        if not lst:
            return 
        row = len(lst);
        col = len(lst[0].keys() );
        
        self.tableWidget.setRowCount(row);
        self.tableWidget.setColumnCount(col);
        
        for i,s in enumerate(lst):
            for j,k in enumerate(s.keys()):
                aItem = QTableWidgetItem()
                v=   lst[i][k]
                if isinstance(v,list):
                    v= ','.join(v)
                aItem.setText( v )
                self.tableWidget.setItem( i,j,aItem);

    @pyqtSlot() 
    def on_btnTmp_clicked(self):
        pass
        # print( lst)
    @pyqtSlot() 
    def on_btnTmp2_clicked(self):
        pass
    # 过滤表格的spider
    @pyqtSlot(int) 
    def on_cmbTagFilter_currentIndexChanged(self, index):
        st = self.cmbTagFilter.itemText(index )        
        lst = self.spider_info
        lst = list( filter( lambda x: (st=="全部") or (st in x["tag"]), lst))                
        self.tableWidget_import(lst)
    # 从表格选定spider
    @pyqtSlot(QTableWidgetItem)     
    def on_tableWidget_itemClicked(self,item):
        row = item.row()
        spd =  self.tableWidget.item( row,0).text()
        base_url =  self.tableWidget.item( row,2).text()
        self.comboBox.setCurrentIndex( self.comboBox.findText( spd ))
        self.lbBaseurl.setText( base_url )
        print( spd)

    @pyqtSlot()     
    def on_btnViewUrl_clicked(self):
        url = self.ledViewUrl.text()
        print( url)
        self.webview.load(QUrl(url))
    def install_web(self,url="https://www.baidu.com"):        
        self.webview = QWebEngineView()
        self.webview.load(QUrl(url))
        self.hbl = QtWidgets.QHBoxLayout(self.wdgWeb)
        self.hbl.setSpacing(6)
        self.hbl.setContentsMargins(11, 11, 11, 11)
        self.hbl.addWidget(self.webview,0)
        # self.wdgWeb.addWidget(self.webview)    
        # self.webview.setParent(self.wdgWeb)  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('ui/img/icons8-spider-64.png'))
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
      
    
