
#-*- coding:utf-8 -*- 
import os,sys,time
import json

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QVBoxLayout, QSizePolicy, QWidget,QListWidgetItem,QFileDialog,QFileSystemModel ,QTableWidget
from qtpy.QtCore import QObject, Signal, Slot,QUrl,QProcess,Qt
from qtpy.QtWidgets import QFileDialog,QListWidgetItem,QTableWidgetItem,QApplication

import copy

class TableWidget(QTableWidget):
    def setupMenu(self):
        @Slot() 
        def on_actionNewItem_triggered(tableWidget):
            index = tableWidget.currentRow();
            # tableWidget.insertItem(index + 1, item);
            tableWidget.insertRow(index+1)
        @Slot() 
        def on_actionDeleteItem_triggered(tableWidget):
            item = tableWidget.currentRow()        
            tableWidget.removeRow(item)
        @Slot() 
        def on_actionClearItems_triggered(tableWidget):
            tableWidget.clear();
        @Slot() 
        def on_tableWidget_itemDoubleClicked(tableWidget):
            item = tableWidget.currentItem() 
            item.setFlags(item.flags() | Qt.ItemIsEditable) 
        exitAct = QAction( self)        
        exitAct.setShortcut('Ctrl+N')
        exitAct.setText("newRow")
        exitAct.setStatusTip('new row')
        exitAct.triggered.connect(lambda :on_actionNewItem_triggered(self))
        self.addAction(exitAct)

        clearAct = QAction( self)        
        clearAct.setShortcut('Ctrl+C')
        clearAct.setText("clearRow")
        clearAct.setStatusTip('clear rows')
        clearAct.triggered.connect(lambda :on_actionClearItems_triggered(self))
        self.addAction(clearAct)        

        removeAct = QAction( self)        
        removeAct.setShortcut('Ctrl+D')
        removeAct.setText("removeRow")
        removeAct.setStatusTip('remove row')
        removeAct.triggered.connect(lambda :on_actionDeleteItem_triggered(self))
        self.addAction(removeAct)

        self.itemDoubleClicked.connect(lambda :  on_tableWidget_itemDoubleClicked(self))
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
    def from_dict(self,dct):        
        self.clear()
        if not dct:
            return
        row = len(dct)-1   
        col = len(dct[0])   
        self.setColumnCount(col); 
        self.setRowCount(row)
        for i,d in enumerate(dct[0]):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(d))
        for i in range(row):
            for j in range(col):
                aItem = QTableWidgetItem()
                aItem.setText( dct[i+1][j] )
                self.setItem( i,j,aItem)
    def to_dict(self):
        col = self.columnCount()
        row = self.rowCount()

        dat = [[]]
        for j in range(col):            
            dat[0].append( self.horizontalHeaderItem(j).text())
        for i in range(row):
            lst= []
            for j in range(col):
                aItem =self.item(i,j)
                lst.append(aItem.text())
            dat.append(lst)
        return dat
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = TableWidget()
    dct = [ ["name","tag","index"   ],["Tom","abc","0"],["Amy","bcd","1"],["Jack","def","2"],["Lily","fgh","3"]]
    mainWindow.from_dict(dct)
    dct2=mainWindow.to_dict()
    mainWindow.setupMenu()
    print(dct2)
    print(dct2==dct)
    mainWindow.show()
    app.exec_()
