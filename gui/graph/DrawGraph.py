from pyqtgraph import PlotItem
import numpy as np
import pyqtgraph as pg
from select_data import fetch_data_id, fetch_data_updated
from PyQt5 import QtCore


class Graph(PlotItem):

    def __init__(self):

        super(Graph, self).__init__()

        self.setDownsampling(mode ='peak')
        self.setClipToView(True)
        self.setRange(xRange=[-100, 0])
        self.setLimits(xMax=0)
        self.curve = self.plot()
        self.data = np.empty(100)
        self.ptr = 0


    def test(self):
        self.timer_graph = pg.QtCore.QTimer(self)
        self.timer_graph.timeout.connect(self.update)
        self.timer_graph.start(100)

    def update(self):
        self.data[self.ptr] = np.array(fetch_data_updated(1)[0])
        self.ptr += 1
        if self.ptr >= self.data.shape[0]:
            tmp = self.data
            self.data = np.empty(self.data.shape[0] * 2)
            self.data[:tmp.shape[0]] = tmp
        self.curve.setData(self.data[:self.ptr])
        self.curve.setPos(-self.ptr, 0)
        self.curve.setPen(pg.mkPen((37,83,89), width=2, style=QtCore.Qt.DashLine) )  #mkPen设置线条样式

