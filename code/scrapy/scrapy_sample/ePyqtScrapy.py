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
    def initProc(self):
        self.proc = QProcess(self)
        self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.proc.readyReadStandardOutput.connect(self.on_procReceived)
        # QObject::connect(m_process,SIGNAL(readyRead()),this,SLOT(readOutput()));
        self.proc.finished.connect(self.onFinished)
        
    @pyqtSlot() 
    def on_actionStart_triggered(self):
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
      
    
