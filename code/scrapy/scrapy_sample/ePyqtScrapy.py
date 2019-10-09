#-*- coding:utf-8 -*- 
import os,sys,time
import json
import configparser
sys.path.append('ui')
import subprocess, io

from PyQt5 import QtCore, QtGui, uic,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QVBoxLayout, QSizePolicy, QWidget,QListWidgetItem,QFileDialog,QDirModel
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty,QUrl,QProcess
from PyQt5.QtWidgets import QFileDialog

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

        self._default_config = { "custom": {"START_URLS":"www.abc.com"    },    "set": { "IMAGES_STORE":"images","CLOSESPIDER_ITEMCOUNT": "2","JOBDIR": "scr_job" },
            "spider": "meizitu0",    "output": [        "scr_abc.jl"    ]}
        self.config = copy.copy(self._default_config)
        self.loadConfig()
        self._configWrite( self.config  )
        self.project_name = 'setting.scrproj'
        
        self.spider_info={
            "meizitu":{"tag":["图片"],"base_url":"https://www.meizitu.com","description":"..."},
            "meizitu0":{"tag":["图片"],"base_url":"https://www.meizitu.com","description":"..."},
            "mm131":{"tag":["图片"],"base_url":"https://www.mm131.net","description":"..."},
            "mzitu":{"tag":["图片"],"base_url":"https://www.mzitu.net","description":"..."},
            "dmzj":{"tag":["漫画"],"base_url":"https://manhua.dmzj.com","description":"..."},
        }
        self._recordRecent = {"recentProject":["setting.scrproj"],}
        self.setDir("images")
    def initProc(self):
        self.proc = QProcess(self)
        self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.proc.readyReadStandardOutput.connect(self.on_procReceived)
        # QObject::connect(m_process,SIGNAL(readyRead()),this,SLOT(readOutput()));
        self.proc.finished.connect(self.onFinished)
    def setDir(self,pth):
        self.dirModel = QDirModel()
        self.treeView.setModel(self.dirModel )
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
        if dct.get('start_urls'):
            self.ledBookname.setText(dct['start_urls'][0])
        else:
            self.ledBookname.setText("")
                   
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
        
        if self.ledBookname.text()!='':
            dct['start_urls'] = [self.ledBookname.text() ]
        else:
            if dct.get("start_urls"):
                del(dct['start_urls'])
        if self.spbMaxDepth.value():
            dct["set"]["DEPTH_LIMIT"] = self.spbMaxDepth.value()
        if self.spbMaxDepthWeight.value():
            dct["set"]["DEPTH_PRIORITY"] = self.spbMaxDepth.value()    

        dct["spider"] = self.comboBox.currentText() 
        return dct
    def saveConf(self,project_name='setting.scrproj'):
        self.config.update(self._configRead())
        with open(project_name,'w') as fp:
            json.dump(self.config,fp,indent=4)
    
    def loadConfig(self,project_name =  'setting.scrproj'):
        if os.path.exists(project_name):
            with open(project_name, 'r')   as fp:              
                dct = json.load(fp)
                self.config.update( dct)
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
            self.saveConf()
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
            self.loadConfig()
    
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
        print(self.config)
        self.saveConf()
        conf = json.dumps( self.config,indent=4)
        self.txtConfig.setText(conf)
        cmdline = dict2cmdline(self.config)
        print(cmdline)
        self.proc.start("crawl",cmdline )
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
    #@pyqtSlot() 
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('ui/img/icons8-spider-64.png'))
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
      
    
