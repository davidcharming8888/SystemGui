import pyqtgraph as pg
import pandas as pd
import numpy as np

class myGraphics21(object):
    def __init__(self, widget, address, key , threshold = 1.5):
        #设置阈值
        self.threshold = threshold
        #读取数据
        self.dataset = pd.read_csv(address,
                              header=0,
                              )
        #选取数据名称, 如果数据不存在, 默认为 -
        try:
            message = self.dataset[[key]]
        except:
            message = self.dataset[["桨叶角度1"]]

        self.message = message.iloc[:, 0].values

        # if widget.getItem(0,0):
        #     widget.removeItem(widget.getItem(0,0))

        # 坐标变换为字符
        x = ['当前时刻']
        y = [0]
        xdict = dict(enumerate(x))
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])
        # 如果视图不存在, 则在主程序中的graphicsView控件中加入视图, 并设置画布样式
        if widget.getItem(0, 0) == None :
            p21 = widget.addPlot(axisItems={'bottom': stringaxis}, title=key)
        else:
            p21 = widget.getItem(0, 0)
            p21.setTitle(key)
            p21.clear()
        p21.setDownsampling(mode='subsample')
        p21.setClipToView(True)
        p21.setRange(xRange=[-50, 0])
        p21.setLimits(xMax=10)

        # 画出阈值线
        p21.addLine(y=threshold, pen=pg.mkPen(color='r', width=2))
        # p21画布上画画,设置画笔样式
        self.curve1 = p21.plot(pen=pg.mkPen(color='313134', width=1))

        # self.curve2 = p21.plot(pen=pg.mkPen(color='r', width=2))
        self.data = np.empty(100)
        self.ptr = 0



    def update(self):
        # 当有存在时,画图
        if len(self.message) > self.ptr:
            self.data[self.ptr] = self.message[self.ptr]
        else:
            self.data[self.ptr] = 0

        self.ptr += 1
        if self.ptr >= self.data.shape[0]:
            tmp = self.data
            self.data = np.empty(self.data.shape[0] * 2)
            self.data[:tmp.shape[0]] = tmp
        self.curve1.setData(self.data[:self.ptr])
        self.curve1.setPos(-self.ptr, 0)          #print(self.data[:self.ptr])

        # self.curve2.setData([self.threshold for i in range(self.ptr)])
        # self.curve2.setPos(-self.ptr, 0)

