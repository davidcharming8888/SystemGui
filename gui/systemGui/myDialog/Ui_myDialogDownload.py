# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myDialogDownload.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myDialogDownload(object):
    def setupUi(self, myDialogDownload):
        myDialogDownload.setObjectName("myDialogDownload")
        myDialogDownload.resize(765, 485)
        self.verticalLayout = QtWidgets.QVBoxLayout(myDialogDownload)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = GraphicsLayoutWidget(myDialogDownload)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(myDialogDownload)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(myDialogDownload)
        QtCore.QMetaObject.connectSlotsByName(myDialogDownload)

    def retranslateUi(self, myDialogDownload):
        _translate = QtCore.QCoreApplication.translate
        myDialogDownload.setWindowTitle(_translate("myDialogDownload", "相似性因子"))
        self.pushButton.setText(_translate("myDialogDownload", "下载数据"))

from pyqtgraph import GraphicsLayoutWidget
