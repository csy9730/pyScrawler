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
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty,QUrl

from ui.ui_mainwidow import  Ui_MainWindow
# qtCreatorFile = "mainwindow.ui"
# 使用uic加载
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class scrapySetting(object):
    def __init__(self):
        self.cmd = 'scrapy crawl'
        self.job = 'dmzj'
        
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
        self.proc = None
        self.tmrCmd = QtCore.QTimer()
        self.tmrCmd.setInterval(200)
        self.tmrCmd.timeout.connect(self.on_tmrCmd_timeout)
#下面将输出重定向到textEdit中
        # sys.stdout = EmittingStream(textWritten=self.outputWritten)  
        # sys.stderr = EmittingStream(textWritten=self.outputWritten)  
#接收信号str的信号槽
    def outputWritten(self, text):
        print("outputWritten")  
        return
        cursor = self.textEdit.textCursor()  
        cursor.movePosition(QtGui.QTextCursor.End)  
        cursor.insertText(text)  
        self.textBrowser.setTextCursor(cursor)  
        self.textBrowser.ensureCursorVisible()
    @pyqtSlot() 
    def on_actionStart_triggered(self):
        # self.actiondumpSetting
        print("start")        
        book = self.ledBookname.text().split(' ')[0]
        if book=='':
            print("empty")
            return
        cmd = 'scrapy crawl dmzj -a book={0} '.format( book )
        proc = subprocess.Popen(cmd,
                                stdout= None,#subprocess.STDOUT,
                                bufsize=1)
    @pyqtSlot() 
    def on_tmrCmd_timeout(self):
        if self.proc is not None:            
            for s in iter(self.proc.stdout.readline, ''):
                if len(s) < 1:
                    break
                self.textBrowser.append( s.decode('gbk').strip() )
            # print(s.decode('gbk').strip())
    @pyqtSlot() 
    def on_btnRun_clicked(self):
        cmd = self.ledRunstring.text()
        print(" on_btnRun_clicked",cmd)
        #ss= os.popen(cmd,"w")
        self.proc = subprocess.Popen(cmd,
            shell=True,
            bufsize=9999, #
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        self.tmrCmd.start()
        
        
    @pyqtSlot() 
    def on_actionStop_triggered(self):
        # self.actiondumpSetting
        print("stop")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
      
    
