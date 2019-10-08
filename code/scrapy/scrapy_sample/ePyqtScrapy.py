#-*- coding:utf-8 -*- 
import os,sys,time
import json
import configparser
sys.path.append('ui')
import subprocess, io

from PyQt5 import QtCore, QtGui, uic,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QVBoxLayout, QSizePolicy, QWidget,QListWidgetItem,QFileDialog
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty,QUrl,QProcess

from ui.ui_mainwidow import  Ui_MainWindow
# Ui_MainWindow, QtBaseClass = uic.loadUiType("ui/mainwindow.ui")
from scrapy_sample.utils import dict2cmdline

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

        self.config = { "custom": {"START_URLS":"www.abc.com"    },    "set": { "IMAGES_STORE":"images","CLOSESPIDER_ITEMCOUNT": "2","JOBDIR": "scr_job" },
            "spider": "meizitu0",    "output": [        "scr_abc.jl"    ]}
        self._configWrite( self.config  )
    def initProc(self):
        self.proc = QProcess(self)
        self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.proc.readyReadStandardOutput.connect(self.on_procReceived)
        # QObject::connect(m_process,SIGNAL(readyRead()),this,SLOT(readOutput()));
        self.proc.finished.connect(self.onFinished)

    def _configWrite(self,dct):
        self.comboBox.setCurrentIndex( self.comboBox.findText(dct['spider']))
        dct['set']['JOBDIR']
        if dct["set"].get("JOBDIR") is not None:
            self.chbAddScratch.setChecked(True)
            self.lineEdit.setText( dct["set"]["JOBDIR"])
        if dct["set"].get("CLOSESPIDER_ITEMCOUNT") is not None:
            self.chkMaxItem.setChecked(True)
            self.spbMaxItem.setValue( int( dct["set"]["CLOSESPIDER_ITEMCOUNT"]) )
        if dct["set"].get("CLOSESPIDER_TIMEOUT") is not None:
            self.chkMaxTime.setChecked(True)
            self.spbMaxTime.setValue( int( dct["set"]["CLOSESPIDER_TIMEOUT"]) )
        if dct["set"].get("CLOSESPIDER_PAGECOUNT") is not None:
            self.chkMaxPage.setChecked(True)
            self.spbMaxPage.setValue( int( dct["set"]["CLOSESPIDER_PAGECOUNT"]) )
    def _configRead(self):
        dct= self.config
        if self.chbAddScratch.isChecked():
            dct['set']['JOBDIR'] = self.lineEdit.text()
        else:
            del(dct['set']['JOBDIR'])
        if self.chkMaxItem.isChecked():
            dct['set']['CLOSESPIDER_ITEMCOUNT'] = self.spbMaxItem.value()
        else:
            if dct['set'].get("CLOSESPIDER_ITEMCOUNT"):
                del(dct['set']['CLOSESPIDER_ITEMCOUNT'])
        if self.chkMaxTime.isChecked():
            dct['set']['CLOSESPIDER_TIMEOUT'] = self.spbMaxItem.value()
        else:
            if dct['set'].get("CLOSESPIDER_TIMEOUT"):
                del(dct['set']['CLOSESPIDER_TIMEOUT'])
        if self.chkMaxPage.isChecked():
            dct['set']['CLOSESPIDER_PAGECOUNT'] = self.spbMaxPage.value()
        else:
            if dct['set'].get("CLOSESPIDER_PAGECOUNT"):
                del(dct['set']['CLOSESPIDER_PAGECOUNT'])

        dct["spider"] = self.comboBox.currentText() 
        return dct

    @pyqtSlot() 
    def on_actionStart_triggered(self):
        self.config = self._configRead()
        print(self.config)
        
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
        # self.actiondumpSetting
        print("stop")
        self.proc.terminate()
    @pyqtSlot() 
    def on_actionClear_triggered(self):
        self.textBrowser.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
      
    
