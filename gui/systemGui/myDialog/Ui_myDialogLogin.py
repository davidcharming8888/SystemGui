# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myDialogLogin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(1200, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_dialog.sizePolicy().hasHeightForWidth())
        login_dialog.setSizePolicy(sizePolicy)
        login_dialog.setMinimumSize(QtCore.QSize(1200, 480))
        login_dialog.setMaximumSize(QtCore.QSize(1200, 480))
        login_dialog.setStyleSheet("QDialog{border-image:url(:/newPrefix/登入界面.jpg)}\n"
"\n"
"QLineEdit{\n"
"    border: solid ;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QFrame{\n"
"    border: solid ;\n"
"    border-radius: 12px;\n"
"    padding: 3px;\n"
"    outline: none;}\n"
"\n"
"QLabel{\n"
"    border: solid ;\n"
"    border-radius: 7px;\n"
"    padding: 3px;\n"
"    outline: none;}")
        self.gridLayout_2 = QtWidgets.QGridLayout(login_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(login_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(100, 170))
        self.frame.setMaximumSize(QtCore.QSize(500, 500))
        self.frame.setStyleSheet("QFrame{background-color: rgba(255, 255, 255, 80)}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(120, 112, 255, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setMinimumSize(QtCore.QSize(255, 25))
        self.login_button.setMaximumSize(QtCore.QSize(255, 25))
        self.login_button.setStyleSheet("QPushButton {\n"
"    background-color: #505F69 ;\n"
"    border: solid ;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}")
        self.login_button.setObjectName("login_button")
        self.pw_line_edit = QtWidgets.QLineEdit(self.frame)
        self.pw_line_edit.setGeometry(QtCore.QRect(170, 70, 205, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pw_line_edit.sizePolicy().hasHeightForWidth())
        self.pw_line_edit.setSizePolicy(sizePolicy)
        self.pw_line_edit.setMinimumSize(QtCore.QSize(205, 25))
        self.pw_line_edit.setMaximumSize(QtCore.QSize(200, 25))
        self.pw_line_edit.setText("")
        self.pw_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_line_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pw_line_edit.setPlaceholderText("")
        self.pw_line_edit.setObjectName("pw_line_edit")
        self.user_line_edit = QtWidgets.QLineEdit(self.frame)
        self.user_line_edit.setGeometry(QtCore.QRect(170, 30, 205, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_line_edit.sizePolicy().hasHeightForWidth())
        self.user_line_edit.setSizePolicy(sizePolicy)
        self.user_line_edit.setMinimumSize(QtCore.QSize(205, 25))
        self.user_line_edit.setMaximumSize(QtCore.QSize(200, 25))
        self.user_line_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.user_line_edit.setText("")
        self.user_line_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_line_edit.setDragEnabled(False)
        self.user_line_edit.setReadOnly(False)
        self.user_line_edit.setPlaceholderText("")
        self.user_line_edit.setObjectName("user_line_edit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 30, 61, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(25, 25))
        self.label.setMaximumSize(QtCore.QSize(70, 25))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 61, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(25, 25))
        self.label_2.setMaximumSize(QtCore.QSize(70, 25))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 128, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 128, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(login_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)

    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "登入信息"))
        self.login_button.setText(_translate("login_dialog", "登入"))
        self.label.setText(_translate("login_dialog", "用户"))
        self.label_2.setText(_translate("login_dialog", "密码"))

import picSourceDialog_rc
