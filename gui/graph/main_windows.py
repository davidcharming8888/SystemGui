# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QThread, QTimer, pyqtSignal
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main_windows import Ui_MainWindow

import pyqtgraph as pg
from pyqtgraph import PlotItem

import serial
from select_data import fetch_data_id, fetch_data_updated
import numpy as np
import time

from ConnectSensor import Worker
from DrawGraph import graph



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
        self.p1 = graph()
        self.graph1.addItem(self.p1)

        #线程类/变量
        self.work = Worker()
        self.workbreak.connect(self.work.stop)

    @pyqtSlot(bool)
    def on_checkBox_showdata_clicked(self, checked):
        """
        子线程开关，检查Arduino和COM口连接，从arduino读取数据
        """
        if checked:
            try:
                ser = serial.Serial("COM4", 9600)
            except:
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
