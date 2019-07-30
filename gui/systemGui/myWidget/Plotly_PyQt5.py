# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:29:55 2017

@author: Administrator
"""
import pandas as pd
import os
import plotly.offline as pyof
import plotly.graph_objs as go

import numpy as np
import matplotlib.pyplot as plt
import xlrd
from method.lstm.prediction import ModelLSTM
from numpy import concatenate

class Plotly_PyQt5():
	def __init__(self, path_csv, file_name):
		self.file_name = file_name
		self.path_csv = path_csv

		# 新建图像存放目录 path_plotly_html
		plotly_html = 'plotly_html'
		if not os.path.isdir(plotly_html):
			os.mkdir(plotly_html)
		self.path_plotly_html = os.getcwd() + os.sep + plotly_html
	   
	def get_plotly_path(self):
		path_pic = self.path_plotly_html + os.sep + self.file_name
		df = pd.read_csv(self.path_csv, index_col=0)
		#df = df.iloc[94588:94598,:]
		df = df.iloc[80000:80010,:]
		pred,real = ModelLSTM.pred(df)
		x = np.arange(len(pred))
		pred = pred.flatten()
		#pred = concatenate((pred,np.array([[0]])))
		#df['pred'] = pred
		# 绘图
		print(pred,'\\',real)
		nset_real = go.Scatter(
			x=x,
			y=real,
			name='real',
			connectgaps=True, # 这个参数表示允许连接数据缺口
		)

		nset_pred = go.Scatter(
			x=x,
			y=pred,
			name='pred',
			connectgaps=True,
		)
		data = [nset_real,nset_pred]

		layout = dict(title='nset',
					  xaxis=dict(title='Date'),
					  yaxis=dict(title='nset'),
					  )

		fig = go.Figure(data=data, layout=layout)  
		pyof.plot(fig, filename=path_pic, auto_open=False)
		return path_pic
	   
	def get_plot_path_matplotlib_plotly(self,file_name='matplotlib_plotly.html'):
		path_pic = self.path_dir_plotly_html + os.sep + file_name

		N = 50
		x = np.random.rand(N)
		y = np.random.rand(N)
		colors = np.random.rand(N)
		area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radii
		scatter_mpl_fig = plt.figure()
		plt.scatter(x, y, s=area, c=colors, alpha=0.5)

		pyof.plot_mpl(scatter_mpl_fig, filename=path_pic, resize=True,auto_open=False)
		return path_pic
