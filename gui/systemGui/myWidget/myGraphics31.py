import pyqtgraph as pg
import pandas as pd
import numpy as np

class myGraphics31(object):
    def __init__(self, widget, address, key , threshold = 1.5):
        #设置阈值
        self.threshold = threshold


        self.dataset = pd.read_csv(address,header=0,)
        #选取数据名称, 如果数据不存在, 默认为
        residual1 = self.dataset[["残差红"]].iloc[:, 0].values
        residual2 = self.dataset[["残差蓝"]].iloc[:, 0].values
        residual3 = self.dataset[["残差黑"]].iloc[:, 0].values

        diff1 = self.dataset[["异常率红"]].iloc[:, 0].values[:312]*100
        diff2 = self.dataset[["异常率黑"]].iloc[:, 0].values[:312]*100


        # # 坐标变换为字符
        # x = ['当前时刻']
        # y = [0]
        # xdict = dict(enumerate(x))
        # stringaxis = pg.AxisItem(orientation='bottom')
        # stringaxis.setTicks([xdict.items()])
        #
        # x1 = ['当前时刻']
        # y1 = [0]
        # xdict = dict(enumerate(x))
        # stringaxis1 = pg.AxisItem(orientation='bottom')
        # stringaxis1.setTicks([xdict.items()]) axisItems={'bottom': stringaxis}

        # 如果视图不存在, 则在主程序中的graphicsView控件中加入视图, 并设置画布样式
        p31 = widget.addPlot(labels = {'left': "残差", })
        # p31.addLegend()
        x=np.arange(351)
        p31.plot(x=x,y=residual1, pen=(255, 0, 0), name="Red curve")
        p31.plot(x=x,y=residual2, pen=(0, 0, 255), name="Green curve")
        p31.plot(x=x,y=residual3, pen=(0,0,0), name="Black curve")
        p31.addLine(y=0.068, pen=pg.mkPen(color='g', width=2))
        p31.showGrid(x=True, y=True, alpha=0.4)

        xx=np.arange(312)
        p32 = widget.addPlot( labels={'left': "异常率%", })
        p32.plot(x=xx, y=diff1, pen=(255, 0, 0), name="Red curve")
        p32.plot(x=xx, y=diff2, pen=(0,0,0), name="Black curve")
        p32.addLine(y=70, pen=pg.mkPen(color='g', width=2))
        p32.showGrid(x=True, y=True, alpha=0.4)
        # p31.setDownsampling(mode='subsample')
        # p31.setClipToView(True)
        # p31.setRange(xRange=[-50, 0])
        # p31.setLimits(xMax=10)






