# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myParameterTree.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myParameterTree(object):
    def setupUi(self, myParameterTree):
        myParameterTree.setObjectName("myParameterTree")
        myParameterTree.resize(640, 473)
        self.verticalLayout = QtWidgets.QVBoxLayout(myParameterTree)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tree = ParameterTree(myParameterTree)
        self.tree.setObjectName("tree")
        self.verticalLayout.addWidget(self.tree)

        self.retranslateUi(myParameterTree)
        QtCore.QMetaObject.connectSlotsByName(myParameterTree)

    def retranslateUi(self, myParameterTree):
        _translate = QtCore.QCoreApplication.translate
        myParameterTree.setWindowTitle(_translate("myParameterTree", "设备信息"))

from pyqtgraph.parametertree import ParameterTree
