# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QThread, QTimer, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main_windows import Ui_MainWindow

import pyqtgraph as pg
from pyqtgraph import PlotItem
import numpy as np
import time

from ConnectSensor import Worker
from DrawGraph import graph
from select_data import fetch_data_id, fetch_data_updated


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
        pg.setConfigOption('background', '#ffffff')  #设置背景为灰色'#ffffff'
        pg.setConfigOption('foreground', (37,83,89))
        pg.setConfigOptions(antialias=True)  #使曲线看起来更光滑，而不是锯齿状

        self.setupUi(self)

        #绘图类/变量
        self.p1 = self.graph1.addPlot(colspan=2)   # colspans是什么
        print(isinstance(self.p1,PlotItem))

        #test
        self.p2 = graph()
        self.graph2.addItem(self.p2)

        self.p1.setDownsampling(mode='peak')
        self.p1.setClipToView(True)
        self.p1.setRange(xRange=[-100, 0])
        self.p1.setLimits(xMax=0)
        self.curve1 = self.p1.plot()
        self.data1 = np.empty(100)
        self.ptr1 = 0

        #线程类/变量
        self.work = Worker()
        self.workbreak.connect(self.work.stop)

    #绘图函数
    def test(self):
        self.timer_graph1 = pg.QtCore.QTimer(self)
        self.timer_graph1.timeout.connect(self.update)
        self.timer_graph1.start(100)

    def update(self):
        self.data1[self.ptr1] = np.array(fetch_data_updated(1)[0])
        self.ptr1 += 1
        if self.ptr1 >= self.data1.shape[0]:
            tmp = self.data1
            self.data1 = np.empty(self.data1.shape[0] * 2)
            self.data1[:tmp.shape[0]] = tmp
        self.curve1.setData(self.data1[:self.ptr1])
        self.curve1.setPos(-self.ptr1, 0)
        self.curve1.setPen(pg.mkPen((37,83,89), width=2, style=QtCore.Qt.DashLine) )  #mkPen设置线条样式



    @pyqtSlot(bool)
    def on_checkBox_showdata_clicked(self, checked):
        """
        子线程开关，从arduino读取数据
        """
        if checked:
            self.work.start()
        elif checked == False:
            self.workbreak.emit()

    @pyqtSlot(bool)
    def on_checkBox_showgraph1_clicked(self, checked):
        if checked:
            self.test()
            self.p2.test()
        elif checked == False:
            self.timer_graph1.stop()
            self.p2.timer_graph.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
