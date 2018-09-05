# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QThread, QTimer, pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QHeaderView,QStyle
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_main_windows import Ui_MainWindow

import pyqtgraph as pg
from pyqtgraph import PlotItem

import serial
import re

from select_data import fetch_data_id, fetch_data_updated
import numpy as np
import time

from ConnectSensor import Worker
from DrawGraph import Graph


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    workbreak = pyqtSignal()

    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        pg.setConfigOption('background', '#ffffff')  # 设置背景为灰色'#ffffff'
        pg.setConfigOption('foreground', (37, 83, 89))
        pg.setConfigOptions(antialias=True)  # 使曲线看起来更光滑，而不是锯齿状
        self.setupUi(self)

        # 绘图类/变量
        self.p1 = Graph()
        self.graph1.addItem(self.p1)

        # 线程类/变量
        self.work = Worker()
        self.workbreak.connect(self.work.stop)

        # 数据库类
        #表格填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.PageRecordCount = 6
        self.setTableView()

        # 信号槽连接
        self.prevButton.clicked.connect(self.onPrevButtonClick)
        self.nextButton.clicked.connect(self.onNextButtonClick)
        self.switchPageButton.clicked.connect(self.onSwitchPageButtonClick)

    # 隐藏表格类
    # 初始化tableView图表展示页面
    def setTableView(self):

        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName("localhost")
        self.db.setUserName("root")
        self.db.setPassword("password")
        self.db.setDatabaseName("db_voice")

        # 打开数据库
        self.db.open()
        self._trytoConnect()

        # 声明查询模型
        self.queryModel = QSqlQueryModel(self)
        # 设置当前页
        self.currentPage = 1
        # 得到总记录数
        self.totalRecrodCount = self.getTotalRecordCount()
        # 得到总页数
        self.totalPage = self.getPageCount()
        # 刷新当前页码状态
        self.updateStatus()
        # 设置总页数文本Label
        self.setTotalPageLabel()
        # 设置总记录数Label
        self.setTotalRecordLabel()

        # 打开页面后的默认展示内容
        self.recordQuery(0)
        # 页面tableView控件和queryModel数据库实例合体
        self.tableView.setModel(self.queryModel)

        self.queryModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "音浪")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "时刻")

    # 检查数据库是否连接成功
    def _trytoConnect(self):
        if (self.db.open()):
            print("Connecting to ur deal SQL...")
        else:
            print("Failed to connect to mysql...")

    # 得到总记录条数
    def getTotalRecordCount(self):
        self.queryModel.setQuery("select * from t_sound")
        rowCount = self.queryModel.rowCount()
        return rowCount

    # 得到总页数
    def getPageCount(self):
        if self.totalRecrodCount % self.PageRecordCount == 0:
            return (self.totalRecrodCount / self.PageRecordCount)
        else:
            return (self.totalRecrodCount // self.PageRecordCount + 1)

    # 分页查询
    def recordQuery(self, limitIndex):
        szQuery = (
            "SELECT * FROM t_sound limit %d,%d" %
            (limitIndex, self.PageRecordCount))
        print('query sql=' + szQuery)
        self.queryModel.setQuery(szQuery)

    # 刷新当前页码状态
    def updateStatus(self):
        szCurrentText = ("当前第%d页" % self.currentPage)
        self.currentPageLabel.setText(szCurrentText)

        # 设置按钮是否可用
        if self.currentPage == 1:
            self.prevButton.setEnabled(False)
            self.nextButton.setEnabled(True)
        elif self.currentPage == self.totalPage:
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)
            self.nextButton.setEnabled(True)

    # 刷新当前总页数和总记录条数文本Label
    def updateStatusClicked(self):
        self.totalRecrodCount = self.getTotalRecordCount()
        self.setTotalRecordLabel()
        self.totalPage = self.getPageCount()
        self.setTotalPageLabel()

    # 设置总页文本Label
    def setTotalPageLabel(self):
        szPageCountText = ("总共%d页" % self.totalPage)
        self.totalPageLabel.setText(szPageCountText)

    # 设置总记录数文本Label
    def setTotalRecordLabel(self):
        szTotalRecordText = ("共%d条" % self.totalRecrodCount)
        self.totalRecordLabel.setText(szTotalRecordText)

    # 前一页按钮按下
    def onPrevButtonClick(self):
        print('*** onPrevButtonClick ')
        self.updateStatusClicked()
        limitIndex = (self.currentPage - 2) * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage -= 1
        self.updateStatus()

    # 后一页按钮按下
    def onNextButtonClick(self):
        print('*** onNextButtonClick ')
        self.updateStatusClicked()
        limitIndex = self.currentPage * self.PageRecordCount
        self.recordQuery(limitIndex)
        self.currentPage += 1
        self.updateStatus()

    # 转到页按钮按下
    def onSwitchPageButtonClick(self):
        # 得到输入字符串
        szText = self.switchPageLineEdit.text()
        # 数字正则表达式
        pattern = re.compile(r'^[0-9]+$')
        match = pattern.match(szText)
        # 判断是否为数字
        if not match:
            QMessageBox.information(self, "提示", "请输入数字")
            return
        # 得到页数
        pageIndex = int(szText)
        # 判断是否有指定页
        self.updateStatusClicked()
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页面，请重新输入")
            return

        # 得到查询起始行号
        limitIndex = (pageIndex - 1) * self.PageRecordCount
        # 记录查询
        self.recordQuery(limitIndex)
        # 设置当前页
        self.currentPage = pageIndex
        # 刷新状态
        self.updateStatus()

    # 重载closeEvent重载函数,关闭数据库
    def closeEvent(self, event):
        self.db.close()

    @pyqtSlot(bool)
    def on_checkBox_showdata_clicked(self, checked):
        """
        子线程开关，检查Arduino和COM口连接，从arduino读取数据
        """
        if checked:
            try:
                ser = serial.Serial("COM4", 9600)
            except BaseException:
                QMessageBox.warning(self, "Sad", "请检查Arduino和COM口连接")
            else:
                ser.close()
                self.work.start()
        elif checked == False:
            self.workbreak.emit()

    @pyqtSlot(bool)
    def on_checkBox_showgraph1_clicked(self, checked):
        if checked:
            self.p1.test()
        elif checked == False:
            self.p1.timer_graph.stop()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
