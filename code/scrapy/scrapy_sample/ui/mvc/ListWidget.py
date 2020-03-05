
#-*- coding:utf-8 -*- 
import os,sys,time
import json

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import  QAction, QApplication, QMessageBox, QVBoxLayout, QSizePolicy, QWidget,QFileDialog,QFileSystemModel ,QTableWidget,QListWidget
from qtpy.QtCore import QObject, Signal, Slot,QUrl,QProcess,Qt
from qtpy.QtWidgets import QFileDialog,QListWidgetItem,QTableWidgetItem,QApplication,qApp

import copy



class ListWidget(QListWidget):
    def setupMenu(self):
        @Slot() 
        def on_actionNewItem_triggered(listWidget):
            index = listWidget.currentRow();
            item = QListWidgetItem();
            item.setText("");
            listWidget.insertItem(index + 1, item);
        @Slot() 
        def on_actionDeleteItem_triggered(listWidget):
            item = listWidget.currentRow()        
            listWidget.takeItem(item)
        @Slot() 
        def on_actionClearItems_triggered(listWidget):
            listWidget.clear();
        @Slot() 
        def on_listWidget_itemDoubleClicked(listWidget):
            item = listWidget.currentItem() 
            item.setFlags(item.flags() | Qt.ItemIsEditable) 
        exitAct = QAction( self)        
        exitAct.setShortcut('Ctrl+N')
        exitAct.setText("newItem")
        exitAct.setStatusTip('new item')
        exitAct.triggered.connect(lambda :on_actionNewItem_triggered(self))
        self.addAction(exitAct)

        clearAct = QAction( self)        
        clearAct.setShortcut('Ctrl+C')
        clearAct.setText("clearItems")
        clearAct.setStatusTip('Exit application')
        clearAct.triggered.connect(lambda :on_actionClearItems_triggered(self))
        self.addAction(clearAct)        

        removeAct = QAction( self)        
        removeAct.setShortcut('Ctrl+D')
        removeAct.setText("removeItem")
        removeAct.setStatusTip('remove item')
        removeAct.triggered.connect(lambda :on_actionDeleteItem_triggered(self))
        self.addAction(removeAct)

        self.itemDoubleClicked.connect(lambda :  on_listWidget_itemDoubleClicked(self))
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
    def from_list(self,lst):
        self.clear()
        for s in lst:
            aItem = QListWidgetItem()
            aItem.setText(s);
            self.addItem( aItem)
    def to_list(self):
        return [ self.item(i).text() for i in range(self.count())  ]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ListWidget()
    dct = ["Tom","Amy","Jack","Lily"]

    ListWidget.setupMenu(mainWindow)
    mainWindow.from_list(dct)
    mainWindow.show()
    lst2 = mainWindow.to_list()
    print(lst2) 
    app.exec_()
