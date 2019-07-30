from PyQt5.QtCore import pyqtSlot, QThread, QTimer, pyqtSignal, QTime, Qt, QUrl, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QHeaderView, QAbstractItemView
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtGui import QPalette
from PyQt5 import QtCore, QtGui, QtWidgets

from myFunc.widgetFunc import *
from myFunc.setParameter import setParameter
from myDialog.Ui_myDialogSignalChange import Ui_myDialogSignalChange
from myDialog.Ui_myDialogSignalAdd import Ui_myDialogSignalAdd
from myDialog.Ui_myParameterTree import Ui_myParameterTree
from myDialog.Ui_myDialogLogin import Ui_login_dialog
from myDialog.Ui_myDialogDownload import Ui_myDialogDownload

from myWidget.myQTreeView import Ui_myQTreeViewUnit, Ui_myQTreeViewFault
from myWidget.myGraphics21 import myGraphics21
from myWidget.myGraphics31 import myGraphics31
from myWidget.myGraphics32 import myGraphics32

from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType
import pyqtgraph as pg
#from myWidget.Plotly_PyQt5 import Plotly_PyQt5
import re
import json
import numpy as np
import pandas as pd

from Ui_system_main_windows import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        pg.setConfigOption('background', '#ffffff')  # 设置背景为黑色
        pg.setConfigOption('foreground', '313134')  # 设置前景（包括坐标轴，线条，文本等等）为黑色。
        pg.setConfigOptions(antialias=True)  # 使曲线看起来更光滑，而不是锯齿状

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 预测暂停服务
        """
        self.ploty = Plotly_PyQt5(path_csv = r'D:\chaos\jobless\keras\Forcast_Fault\data\4year\seldata1_nset_4year.csv',
                                  file_name = 'nset_pic.html')

        self.widget_6.load(QUrl.fromLocalFile(self.ploty.get_plotly_path()))

        #self.widget_6.load(QUrl.fromLocalFile(r'D:\chaos\job\dataflow\gui\systemGui\plotly_html\if_hs300_bais.html'))
        """
        # TEST

        # 连接数据库
        self.connectDB()

        # T1.1风电场信息
        # 设置数据库的展示表格，增加修改和结束修改按钮
        self.sqlModel_windPowerStation = QSqlQueryModel(self)
        self.setTableView(tableView=self.tableView_windPowerStation,
                          sqlModel=self.sqlModel_windPowerStation,
                          Query="SELECT 风电场名称, 风电场编号 FROM t_windPowerStation",
                          Header=["风电场名称", "风电场编号"],
                          clicked_func=self.funcT11
                          )
        # QLineEdit控件名列表
        self.nameListT11 = [
            self.lineEdit_groupCompany,
            self.lineEdit_windField,
            self.lineEdit_grossInstalledCapacity,
            self.lineEdit_numOfInstalledStations]

        # 完成修改按钮，设置不可见
        self.pushButton_cancelT11.setVisible(False)

        # T1.2 机组及管辖人员信息
        # 创建机组下拉列表
        self.setComboBoxFromSql(comboBox=self.comboBox_unitT12,
                                column="机组名称",
                                table="t_baseInfo",
                                func=self.funcT12,
                                defaultadd=False)
        self.comboBox_unitT12.setCurrentIndex(0)

        # QLineEdit控件名列表
        self.nameList1T12 = [
            self.LineEdit_descriptionT12,
            self.LineEdit_converterT12,
            self.LineEdit_gearboxT12,
            self.LineEdit_controlSystemT12,
            self.LineEdit_generatorT12,
            self.LineEdit_pitchSystemT12,
            self.LineEdit_rpmT12]
        self.nameList2T12 = [
            self.LineEdit_nameT12,
            self.LineEdit_numberT12,
            self.LineEdit_telephoneT12,
            self.LineEdit_positionT12,
            self.LineEdit_departmentT12]

        # 完成修改按钮，设置不可见
        self.pushButton_cancelT12.setVisible(False)

        # T1.3 系统管理.设备信息
        self.setComboBoxFromSql(comboBox=self.comboBox_unitT13,
                                column="机组名称",
                                table="t_baseInfo",
                                func=self.funcT13)
        self.setComboBoxFromItems(comboBox=self.comboBox_systemT13,
                                  func=self.funcT13
                                  )

        self.buttonDictT13 = {
            'self.pushButton_facility_1': self.pushButton_facility_1,
            'self.pushButton_facility_2': self.pushButton_facility_2,
            'self.pushButton_facility_3': self.pushButton_facility_3,
            'self.pushButton_facility_4': self.pushButton_facility_4,
            'self.pushButton_facility_5': self.pushButton_facility_5,
            'self.pushButton_facility_6': self.pushButton_facility_6,
            'self.pushButton_facility_7': self.pushButton_facility_7,
            'self.pushButton_facility_8': self.pushButton_facility_8,
            'self.pushButton_facility_9': self.pushButton_facility_9,
            'self.pushButton_facility_10': self.pushButton_facility_10,
            'self.pushButton_facility_11': self.pushButton_facility_11,
            'self.pushButton_facility_12': self.pushButton_facility_12,
            'self.pushButton_facility_13': self.pushButton_facility_13,
            'self.pushButton_facility_14': self.pushButton_facility_14,
            'self.pushButton_facility_15': self.pushButton_facility_15,
            'self.pushButton_facility_16': self.pushButton_facility_16,
            'self.pushButton_facility_17': self.pushButton_facility_17,
            'self.pushButton_facility_18': self.pushButton_facility_18,
            'self.pushButton_facility_19': self.pushButton_facility_19,
            'self.pushButton_facility_20': self.pushButton_facility_20,
            'self.pushButton_facility_21': self.pushButton_facility_21,
            'self.pushButton_facility_22': self.pushButton_facility_22,
            'self.pushButton_facility_23': self.pushButton_facility_23,
            'self.pushButton_facility_24': self.pushButton_facility_24,
            'self.pushButton_facility_25': self.pushButton_facility_25,
            'self.pushButton_facility_26': self.pushButton_facility_26,
            'self.pushButton_facility_27': self.pushButton_facility_27,
            'self.pushButton_facility_28': self.pushButton_facility_28,
            'self.pushButton_facility_29': self.pushButton_facility_29}
        self.nameDictT13 = {
            'self.pushButton_facility_1': '风能捕捉系统基本信息',
            'self.pushButton_facility_2': '变桨系统基本信息',
            'self.pushButton_facility_3': '变桨控制与保护系统基本信息',
            'self.pushButton_facility_4': '雷电保护装置基本信息',
            'self.pushButton_facility_5': '限位开关基本信息',
            'self.pushButton_facility_6': '编码器基本信息',
            'self.pushButton_facility_7': '变频器与电池柜基本信息',
            'self.pushButton_facility_8': '变桨驱动系统基本信息',
            'self.pushButton_facility_9': '变桨电机基本信息',
            'self.pushButton_facility_10': '变桨轴承基本信息',
            'self.pushButton_facility_11': '桨叶基本信息',
            'self.pushButton_facility_12': '偏航系统基本信息',
            'self.pushButton_facility_13': '偏航制动系统基本信息',
            'self.pushButton_facility_14': '液压系统基本信息',
            'self.pushButton_facility_15': '制动部件基本信息',
            'self.pushButton_facility_16': '偏航控制系统基本信息',
            'self.pushButton_facility_17': '风速风向仪基本信息',
            'self.pushButton_facility_18': '偏航变频器基本信息',
            'self.pushButton_facility_19': '限位开关基本信息',
            'self.pushButton_facility_20': '接近开关基本信息',
            'self.pushButton_facility_21': '空气开关基本信息',
            'self.pushButton_facility_22': '手动控制盒基本信息',
            'self.pushButton_facility_23': '偏航驱动系统基本信息',
            'self.pushButton_facility_24': '偏航电机基本信息',
            'self.pushButton_facility_25': '侧面轴承基本信息',
            'self.pushButton_facility_26': '侧面轴承基本信息',
            'self.pushButton_facility_27': '偏航齿圈基本信息',
            'self.pushButton_facility_28': '刹车钳基本信息',
            'self.pushButton_facility_29': '刹车盘基本信息'}

        for key in [*self.buttonDictT13]:
            self.buttonDictT13[key].clicked.connect(
                lambda old, key=key: self.pushButton_facility(
                    self.nameDictT13[f"{key}"]))

        # T1.4 测点配置
        self.sqlModel_signal = QSqlQueryModel(self)
        self.setTableView(
            tableView=self.tableView_signal,
            sqlModel=self.sqlModel_signal,
            Query="SELECT 所属设备, 通道ID, 通道编码, 通道名称, 信号类型, 是否使用 FROM t_signal",
            Header=[
                '所属设备',
                '通道ID',
                '通道编码',
                '通道名称',
                '信号类型',
                '是否使用'],
            clicked_func=None)

        self.setComboBoxFromSql(comboBox=self.comboBox_unitT14,
                                column="机组名称",
                                table="t_baseInfo",
                                func=self.funcT14)
        self.setComboBoxFromItems(comboBox=self.comboBox_systemT14,
                                  func=self.funcT14
                                  )

        # T1.5 参数配置
        self.sqlModel_residualconf = QSqlQueryModel(self)
        self.setTableView(
            tableView=self.tableView_residualconf,
            sqlModel=self.sqlModel_residualconf,
            Query="SELECT `所属设备`, `关联参数`, `残差阈值`, `窗口长度`, `是否使用` FROM t_residualconf",
            Header=[
                '所属设备',
                '关联参数',
                '残差阈值',
                '窗口长度',
                '是否使用'],
            clicked_func=self.funcT15())

        self.sqlModel_trendconf = QSqlQueryModel(self)
        self.setTableView(
            tableView=self.tableView_trendconf,
            sqlModel=self.sqlModel_trendconf,
            Query="SELECT 所属设备, 参数名称, 阈值上限, 阈值下限, 参数状态, 是否使用 FROM t_trendconf",
            Header=[
                '所属设备',
                '参数名称',
                '阈值上限',
                '阈值下限',
                '参数状态',
                '是否使用'],
            clicked_func=self.funcT15)
        self.setComboBoxFromSql(comboBox=self.comboBox_unitT15,
                                column="机组名称",
                                table="t_baseInfo",
                                func=self.funcT15)
        self.setComboBoxFromItems(comboBox=self.comboBox_systemT15,
                                  func=self.funcT15
                                  )

        # T2 风电机组实时监测
        # 单击图标进入详情页面
        self.frame_detection.setHidden(True)
        self.pushButton_unit_name = [self.pushButton_unit1,
                                     self.pushButton_unit2,
                                     self.pushButton_unit3,
                                     self.pushButton_unit4,
                                     self.pushButton_unit5,
                                     self.pushButton_unit6,
                                     self.pushButton_unit7,
                                     self.pushButton_unit8,
                                     ]

        for i in range(8):
            k = i + 1
            self.pushButton_unit_name[i].clicked.connect(
                lambda old, k=k: self.shiftToDetail(k))

        # 返回主页面
        self.pushButton_backToMainT21.clicked.connect(self.shiftToMain)
        self.pushButton_backToMainT23.clicked.connect(self.shiftToMain)

        # 初始化树形列表
        self.unit_model = QtGui.QStandardItemModel()
        Ui_myQTreeViewUnit(self.treeView_unit, self.unit_model)
        # 设置当前时间
        self.timerT2 = QTimer(self)
        self.timerT2.timeout.connect(self.currentTime)
        self.timerT2.start(1000)
        # 属性列表单击函数
        self.treeView_unit.clicked.connect(self.funcT2)

        # 设置主检测图graphicsView_T21
        '''
        主检测图 is hid at the beginning to make space for the picture of measure point;
        myGraphics21 is my Widget for display picture
        pushButton_realTime is the function to show the real-time data 
        '''
        self.graphicsView_T21.hide()
        self.buttonDictT21 = {
            'self.BtnWindPowerT21_1': self.BtnWindPowerT21_1,
            'self.BtnWindPowerT21_2': self.BtnWindPowerT21_2,
            'self.BtnWindPowerT21_3': self.BtnWindPowerT21_3,
            'self.BtnWindPowerT21_4': self.BtnWindPowerT21_4,
            'self.BtnWindPowerT21_5': self.BtnWindPowerT21_5,
            'self.BtnWindPowerT21_6': self.BtnWindPowerT21_6,
            'self.BtnWindPowerT21_7': self.BtnWindPowerT21_7,
            'self.BtnWindPowerT21_8': self.BtnWindPowerT21_8,
            'self.BtnWindPowerT21_9': self.BtnWindPowerT21_9,
            'self.BtnWindPowerT21_10': self.BtnWindPowerT21_10,
            'self.BtnWindPowerT21_11': self.BtnWindPowerT21_11,
            'self.BtnWindPowerT21_12': self.BtnWindPowerT21_12,
            'self.BtnWindPowerT21_13': self.BtnWindPowerT21_13,
            'self.BtnWindPowerT21_14': self.BtnWindPowerT21_14,
            'self.BtnWindPowerT21_15': self.BtnWindPowerT21_15,
            'self.BtnTransT21_1': self.BtnTransT21_1,
            'self.BtnTransT21_2': self.BtnTransT21_2,
            'self.BtnTransT21_3': self.BtnTransT21_3,
            'self.BtnTransT21_4': self.BtnTransT21_4,
            'self.BtnTransT21_5': self.BtnTransT21_5,
            'self.BtnTransT21_6': self.BtnTransT21_6,
            'self.BtnTransT21_7': self.BtnTransT21_7,
            'self.BtnTransT21_8': self.BtnTransT21_8,
            'self.BtnTransT21_9': self.BtnTransT21_9,
            'self.BtnGeneratorT21_1': self.BtnGeneratorT21_1,
            'self.BtnGeneratorT21_2': self.BtnGeneratorT21_2,
            'self.BtnGeneratorT21_3': self.BtnGeneratorT21_3,
            'self.BtnGeneratorT21_4': self.BtnGeneratorT21_4,
            'self.BtnGeneratorT21_5': self.BtnGeneratorT21_5,
            'self.BtnGeneratorT21_6': self.BtnGeneratorT21_6,
            'self.BtnGeneratorT21_7': self.BtnGeneratorT21_7,
            'self.BtnGeneratorT21_8': self.BtnGeneratorT21_8,
            'self.BtnGeneratorT21_9': self.BtnGeneratorT21_9,
            'self.BtnGeneratorT21_10': self.BtnGeneratorT21_10,
            'self.BtnGeneratorT21_11': self.BtnGeneratorT21_11,
            'self.BtnGeneratorT21_12': self.BtnGeneratorT21_12,
            'self.BtnGeneratorT21_13': self.BtnGeneratorT21_13,
            'self.BtnGeneratorT21_14': self.BtnGeneratorT21_14,
            'self.BtnGeneratorT21_15': self.BtnGeneratorT21_15,
            'self.BtnGeneratorT21_16': self.BtnGeneratorT21_16,
            'self.BtnGeneratorT21_17': self.BtnGeneratorT21_17,
            'self.BtnGeneratorT21_18': self.BtnGeneratorT21_18}
        self.nameDictT21 = {
            'self.BtnWindPowerT21_1': '变桨启停使能信号',
            'self.BtnWindPowerT21_2': '环境温度',
            'self.BtnWindPowerT21_3': '桨叶角度1',
            'self.BtnWindPowerT21_4': '变桨电机转矩1',
            'self.BtnWindPowerT21_5': '变桨电机温度1',
            'self.BtnWindPowerT21_6': '桨叶角度2',
            'self.BtnWindPowerT21_7': '变桨电机转矩2',
            'self.BtnWindPowerT21_8': '变桨电机温度2',
            'self.BtnWindPowerT21_9': '桨叶角度3',
            'self.BtnWindPowerT21_10': '变桨电机转矩3',
            'self.BtnWindPowerT21_11': '变桨电机温度3',
            'self.BtnWindPowerT21_12': '风速',
            'self.BtnWindPowerT21_13': '风向',
            'self.BtnWindPowerT21_14': '偏航启停使能信号',
            'self.BtnWindPowerT21_15': '机舱位置',
            'self.BtnTransT21_1': '主轴轴承振动',
            'self.BtnTransT21_2': '一级行星轮系振动',
            'self.BtnTransT21_3': '二级行星轮系振动',
            'self.BtnTransT21_4': '输出端低速轮径向振动',
            'self.BtnTransT21_5': '输出端高速轮径向振动',
            'self.BtnTransT21_6': '输出端高速轮轴向振动',
            'self.BtnTransT21_7': '磨粒数',
            'self.BtnTransT21_8': '油液温度',
            'self.BtnTransT21_9': '油泵启停使能信号',
            'self.BtnGeneratorT21_1': '发电机上风向轴承径向振动',
            'self.BtnGeneratorT21_2': '发电机上风向轴承径向振动',
            'self.BtnGeneratorT21_3': '定子侧电流A',
            'self.BtnGeneratorT21_4': '定子侧电流B',
            'self.BtnGeneratorT21_5': '定子侧电流C',
            'self.BtnGeneratorT21_6': '转子侧电流A',
            'self.BtnGeneratorT21_7': '转子侧电流B',
            'self.BtnGeneratorT21_8': '转子侧电流C',
            'self.BtnGeneratorT21_9': '发电机转速',
            'self.BtnGeneratorT21_10': '发电机下风向轴承径向振动',
            'self.BtnGeneratorT21_11': '发电机定子温度',
            'self.BtnGeneratorT21_12': '发电机转子温度',
            'self.BtnGeneratorT21_13': '定子侧电压A',
            'self.BtnGeneratorT21_14': '定子侧电压B',
            'self.BtnGeneratorT21_15': '定子侧电压C',
            'self.BtnGeneratorT21_16': '转子侧电压A',
            'self.BtnGeneratorT21_17': '转子侧电压B',
            'self.BtnGeneratorT21_18': '转子侧电压C'}

        for key in [*self.buttonDictT21]:
            self.buttonDictT21[key].clicked.connect(
                lambda old, key=key: self.pushButton_realTime(
                    self.nameDictT21[f"{key}"]))


        # T3 机组故障预警
        self.setComboBoxFromItems(comboBox=self.comboBox_systemT3,
                                  func=self.func_systemT3,
                                  items=(
                                      "所有系统",
                                      "风能捕捉系统",
                                      "传动系统",
                                      "发电机系统",
                                    "齿轮箱")
                                  )
        self.setComboBoxFromSql(comboBox=self.comboBox_unitT3,
                                column="机组名称",
                                table="t_baseInfo",
                                func=self.func_unitT3)

        self.setComboBoxFromSql(comboBox=self.comboBox_channelT3,
                                column="通道名称",
                                table="t_signal",
                                func=self.func_unitT3,
                                defaultadd = '所有通道')
        # 直接显示图像
        self.pushButton_residual("")
        self.pushButton_trend("")

        # T4
        self.setComboBoxFromItems(comboBox=self.comboBox_systemT4,
                                  func=self.func_systemT3,
                                  items=(
                                      "所有系统",
                                      "风能捕捉系统",
                                      "传动系统",
                                      "发电机系统",
                                      )
                                  )
        self.setComboBoxFromSql(comboBox=self.comboBox_unitT4,
                                column="机组名称",
                                table="t_baseInfo",
                                func=self.func_unitT3)





        # 目前隐藏
        # T4 机组诊断与维修决策
        self.sqlModel_diagnosis = QSqlQueryModel(self)
        self.setTableView(
            tableView=self.tableView_diagnosis,
            sqlModel=self.sqlModel_diagnosis,
            Query="SELECT 流水号,机组ID,故障模式,故障位置,发生时间,严重等级,发展程度,维修建议,结果 FROM t_diagnosis",
            Header=[
                '流水号',
                '机组ID',
                '故障模式',
                '故障位置',
                '发生时间',
                '严重等级',
                '发展程度',
                '维修建议',
                '结果'],
            clicked_func=self.funcDiagnosisT3())

        # T4
        # 建立多级树
        Ui_myQTreeViewFault(self.treeView_fault)
        self.treeView_fault.clicked.connect(self.funcT4)

        # 设置征兆规则表格T41
        self.sqlModel_warningrule = QSqlQueryModel(self)
        self.setTableView(tableView=self.tableView_warningrule,
                          sqlModel=self.sqlModel_warningrule,
                          Query="SELECT 预警征兆,运算关系,阈值,逻辑关系 FROM t_warningrule",
                          Header=['预警征兆', '运算关系', '阈值', '逻辑关系'],
                          clicked_func=None
                          )

        self.sqlModel_diagnosisrule = QSqlQueryModel(self)
        self.setTableView(
            tableView=self.tableView_diagnosisrule,
            sqlModel=self.sqlModel_diagnosisrule,
            Query="SELECT 预警征兆,运算关系,阈值,逻辑关系 FROM t_diagnosisrule",
            Header=[
                '预警征兆',
                '运算关系',
                '阈值',
                '逻辑关系'],
            clicked_func=None)

        # 设置故障原因和措施表格T42
        self.sqlModel_faultcause = QSqlQueryModel(self)
        self.setTableView(
            tableView=self.tableView_faultcause,
            sqlModel=self.sqlModel_faultcause,
            Query="SELECT 故障原因, 概率重要度, 维修措施, 主要工具, 备注 FROM t_faultcause",
            Header=[
                '故障原因',
                '概率重要度',
                '维修措施',
                '主要工具',
                '备注'],
            clicked_func=None)

        # 设置故障影响表格T43
        self.sqlModel_faultimpact = QSqlQueryModel(self)
        self.setTableView(
            tableView=self.tableView_faultimpact,
            sqlModel=self.sqlModel_faultimpact,
            Query="SELECT 本级影响, 下级影响, 上级影响, 故障评述, 评价等级, 失效概率 FROM t_faultimpact",
            Header=[
                '本级影响',
                '下级影响',
                '上级影响',
                '故障评述',
                '评价等级',
                '失效概率'],
            clicked_func=None)

        # 窗口最大化
        self.setWindowState(Qt.WindowMaximized)
        # 隐藏tab4
        self.tabWidget.removeTab(4)
        # ploty 预测
        '''
        self.ploty = Plotly_PyQt5(path_csv = r'D:\chaos\jobless\keras\Forcast_Fault\data\4year\seldata1_nset_4year.csv',
                                  file_name = 'nset_pic.html')
        self.widget_6.load(QUrl.fromLocalFile(self.ploty.get_plotly_path()))
        #self.widget_6.load(QUrl.fromLocalFile(r'D:\chaos\job\dataflow\gui\systemGui\plotly_html\if_hs300_bais.html'))
        '''

    # 设置数据库的连接方式
    def connectDB(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName("localhost")
        self.db.setUserName("root")
        self.db.setPassword("password")
        self.db.setDatabaseName("db_system")
        self.db.open()
        if self.db.open():
            print("Success to connect SQL...")
        else:
            print("Failed to connect to SQL...")

    # 登入界面

    @pyqtSlot()
    def on_pushButton_log_clicked(self):
        myDialogLog = QtWidgets.QDialog()
        ui = Ui_login_dialog()
        ui.setupUi(myDialogLog)
        myDialogLog.exec_()



    # Tab11

    # 对QTableView设置模型，列头，查询，单击槽函数
    def setTableView(
            self,
            tableView,
            sqlModel,
            Header,
            Query,
            clicked_func=None):
        tableView.setModel(sqlModel)
        tableView.verticalHeader().hide()
        tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sqlModel.setQuery("%s" % Query)
        for i in range(len(Header)):
            sqlModel.setHeaderData(i, Qt.Horizontal, Header[i])
        if clicked_func is not None:
            tableView.clicked.connect(clicked_func)

    # 表格的单击动作，展示所选内容详情
    def funcT11(self, index):
        query = QSqlQuery()
        codeOfPowerStation = self.sqlModel_windPowerStation.index(
            index.row(), 1).data()
        sql = f"select 集团名称,风场位置,总装机容量,装机台数 from t_windPowerStation where 风电场编号 = '{codeOfPowerStation}' "
        query.exec_(sql)
        setEditText(self.nameListT11, query)

    # 修改按钮T11，单击动作
    @pyqtSlot()
    def on_pushButton_saveT11_clicked(self):
        if self.pushButton_saveT11.text() == "修改":
            self.pushButton_cancelT11.setVisible(True)
            self.pushButton_saveT11.setText("保存修改")
            setEditReadOnly(self.nameListT11, False)
            #QMessageBox.information(self, "提示", "请在文本框内输入修改内容")

        elif self.pushButton_saveT11.text() == "保存修改":
            reply = QMessageBox.question(
                self,
                "系统信息内容修改",
                "系统信息发生变化，是否确定修改？",
                QMessageBox.Cancel | QMessageBox.Save)
            if reply == QMessageBox.Save:
                query = QSqlQuery()
                codeOfPowerStation = self.sqlModel_windPowerStation.index(
                    self.tableView_windPowerStation.currentIndex().row(), 1).data()

                a = [getEditText(i) for i in self.nameListT11]
                b = f"update t_windPowerStation set 集团名称='{a[0]}',风场位置='{a[1]}',总装机容量={a[2]},装机台数={a[3]} where 风电场编号 = '{codeOfPowerStation}'"
                query.exec_(b)

                # query.exec_(
                #     "update t_windPowerStation set 集团名称='%s',风场位置='%s',总装机容量='%s',装机台数='%s' where 风电场编号 = '%s' " %
                #     tuple(a)
                # )
            else:
                pass

    # 取消修改按钮T11，单击动作，重新使用funcT11的setEditText设置文本框内容
    @pyqtSlot()
    def on_pushButton_cancelT11_clicked(self):
        self.pushButton_cancelT11.setVisible(False)
        self.pushButton_saveT11.setText("修改")
        setEditReadOnly(self.nameListT11, True)
        self.funcT11(self.tableView_windPowerStation.currentIndex())

    # Tab12

    # 两种方式创建下拉列表，可选择对应机组
    def setComboBoxFromSql(
            self,
            comboBox,
            column,
            table,
            func,
            defaultadd="所有机组"):
        if defaultadd:
            comboBox.addItem(defaultadd)
        query = QSqlQuery()
        query.exec_("select %s from %s" % (column, table))
        while query.next():
            unit_name = query.value(0)
            comboBox.addItem("%s" % unit_name)
        comboBox.activated.connect(func)

    def setComboBoxFromItems(
        self,
        comboBox,
        func,
        items=(
            "所有系统",
            "风能捕捉系统",
            "传动系统",
            "发电机系统")):
        comboBox.addItems(items)
        comboBox.activated.connect(func)

    # 机组下拉列表，选择改变后的动作
    def funcT12(self, index):
        unit_name = self.comboBox_unitT12.itemText(index)
        query = QSqlQuery()
        query.exec_(
            "select 风机型号,变频器,齿轮箱,控制系统,发电机,变桨系统,发电机额定转速 from t_baseinfo where 机组名称 = '%s' " %
            unit_name)
        setEditText(self.nameList1T12, query)

        '''
        查询结果测试
        if query.next():
            for i in range(3):
                print(str(query.value(i)))
        '''
        query.exec_(
            "select 姓名,工号,工作电话,岗位,部门 from t_staff where 负责机组名称 = '%s' " %
            unit_name)

        '''
        查询结果
        if query.first():
            for i in range(3):
                print([query.value(i)])

        ['李健']
        ['HAPPY002']
        ['13644522210']

        查询语句测试
        print("select 姓名,工号,工作电话,岗位,部门 from t_staff where 负责机组名称 = '%s' " %
        unit_name)
        '''
        setEditText(self.nameList2T12, query)

    # 修改按钮T12，单击动作
    @pyqtSlot()
    def on_pushButton_saveT12_clicked(self):
        if self.pushButton_saveT12.text() == "修改":
            self.pushButton_cancelT12.setVisible(True)
            self.pushButton_saveT12.setText("保存修改")
            setEditReadOnly(self.nameList1T12, False)
            setEditReadOnly(self.nameList2T12, False)
            QMessageBox.information(self, "提示", "请在文本框内输入修改内容")

        elif self.pushButton_saveT12.text() == "保存修改":
            reply = QMessageBox.question(
                self,
                "系统信息内容修改",
                "系统信息发生变化，是否确定修改？",
                QMessageBox.Cancel | QMessageBox.Save)

            if reply == QMessageBox.Save:
                query = QSqlQuery()
                unit_name = self.comboBox_unitT12.itemText(
                    self.comboBox_unitT12.currentIndex())
                a = [getEditText(i) for i in self.nameList1T12]
                a.append(unit_name)
                query.exec_(
                    "update t_baseinfo set 风机型号='%s',变频器='%s',齿轮箱='%s',控制系统='%s',发电机='%s',变桨系统='%s',发电机额定转速='%s' where 机组名称 = '%s' " %
                    tuple(a))

                a = [getEditText(i) for i in self.nameList2T12]
                a.append(unit_name)
                query.exec_(
                    "update t_baseinfo set 姓名='%s',工号='%s',工作电话='%s',岗位='%s',部门='%s' where 机组名称 = '%s' " %
                    tuple(a))

            else:
                pass

    # 取消修改按钮T12，单击动作
    @pyqtSlot()
    def on_pushButton_cancelT12_clicked(self):
        self.pushButton_cancelT12.setVisible(False)
        self.pushButton_saveT12.setText("修改")
        setEditReadOnly(self.nameList1T12, True)
        setEditReadOnly(self.nameList2T12, True)
        self.funcT12(self.comboBox_unitT12.currentIndex())

    # Tab13
    def pushButton_facility(self, key):
        # 加载弹窗界面
        myParameterTree = QtWidgets.QDialog()
        ui = Ui_myParameterTree()
        ui.setupUi(myParameterTree)

        # 读取数据库
        facility = key
        try:
            query = QSqlQuery()
            query.exec_(
                f"select 设备信息 from t_facilityinfo where 设备名称 = '{facility}' ")
        except BaseException as e:
            print(e)

        if query.first():
            data = json.loads(query.value(0))

        # 将json格式通过setParameter函数解释为参数树
        p = Parameter.create(
            name='params',
            type='group',
            children=setParameter(data))
        ui.tree.setParameters(p, showTop=False)

        # 显示弹窗
        myParameterTree.exec_()

    def funcT13(self):
        pass

    # Tab14
    def funcT14(self, index):
        # 匹配(n)#机组的n,匹配(所有)系统
        re_unit = re.compile(r'^(\d+)')
        re_sys = re.compile(r'^(所有)')
        result_unit = re_unit.match(self.comboBox_unitT14.currentText())
        result_sys = re_sys.match(self.comboBox_systemT14.currentText())

        if result_unit:
            f_unit = result_unit.group()
        else:
            f_unit = "."

        if result_sys:
            f_sys = "."
        else:
            f_sys = self.comboBox_systemT14.currentText()

        sql = f"SELECT 所属设备, 通道ID, 通道编码, 通道名称, 信号类型, 是否使用 FROM t_signal " \
              f"WHERE 所属机组 REGEXP '^{f_unit}[^0-9]' AND 所属一级系统 REGEXP '{f_sys}'"
        self.sqlModel_signal.setQuery(sql)

    # 添加按钮T14，单击动作
    @pyqtSlot()
    def on_pushButton_addT14_clicked(self):
        myDialogSignalAdd = QtWidgets.QDialog()
        ui = Ui_myDialogSignalAdd()
        ui.setupUi(myDialogSignalAdd)

        nameListT14 = [ui.LineEdit_channelID,
                       ui.LineEdit_channelName,
                       ui.LineEdit_usable,
                       ui.LineEdit_channelCode,
                       ui.LineEdit_signalType,
                       ui.LineEdit_multiple]

        # 确认修改数据后录入数据库
        if myDialogSignalAdd.exec_():
            a = [getEditText(i) for i in nameListT14]
            b = f"insert into t_signal (ID,通道ID,通道名称,是否使用,通道编码,信号类型,放大倍数,所属机组,所属一级系统,所属设备)" \
                f"values(NULL,'{a[0]}','{a[1]}','{a[2]}','{a[3]}','{a[4]}','{a[5]}','t','tt','ttt')"
            print(b)
            try:
                query = QSqlQuery()
                query.exec_(b)
            except BaseException as e:
                print(e)

    # 修改按钮T14，单击动作
    @pyqtSlot()
    def on_pushButton_changeT14_clicked(self):
        # 创建对话框
        myDialogSignalChange = QtWidgets.QDialog()
        ui = Ui_myDialogSignalChange()
        ui.setupUi(myDialogSignalChange)

        nameListT14 = [ui.LineEdit_channelID,
                       ui.LineEdit_channelName,
                       ui.LineEdit_usable,
                       ui.LineEdit_channelCode,
                       ui.LineEdit_signalType,
                       ui.LineEdit_multiple]

        # 对话框内展示所选数据的详细信息
        channelName = self.sqlModel_signal.index(
            self.tableView_signal.currentIndex().row(), 3).data()
        query = QSqlQuery()
        query.exec_(
            f"select 通道ID,通道名称,是否使用,通道编码,信号类型,放大倍数 from t_signal where 通道名称 = '{channelName}' ")
        setEditText(nameListT14, query)

        query.exec_(
            f"select 所属机组,所属一级系统,所属设备 from t_signal where 通道名称 = '{channelName}' ")
        if query.first():
            ui.LineEdit_belonged.setText(
                f"{query.value(0)}>>{query.value(1)}>>{query.value(2)}")

        # 确认修改数据后录入数据库
        if myDialogSignalChange.exec_():
            a = [getEditText(i) for i in nameListT14]
            b = f"update t_signal set 通道ID='{a[0]}',通道名称='{a[1]}',是否使用='{a[2]}',通道编码='{a[3]}',信号类型='{a[4]}',放大倍数='{a[5]}' " \
                f"where 通道名称 = '{channelName}'"
            query.exec_(b)

    # Tab15
    def funcT15(self):
        pass

    # Tab2
    # 主界面切换到详情界面
    def shiftToDetail(self, n):
        self.scrollArea_detection.setHidden(True)
        self.frame_detection.setHidden(False)
        self.treeView_unit.collapseAll()
        # 展开选择的机组项目
        a = self.unit_model.index(n - 1, 0)
        self.treeView_unit.setExpanded(a, True)
        # 展示选择的机组检测图

    def shiftToMain(self):
        self.graphicsView_T21.setHidden(True)
        self.scrollArea_detection.setHidden(False)
        self.frame_detection.setHidden(True)

    # Tab21

    # 显示实时时间
    def currentTime(self):
        a = QTime.currentTime()
        self.LineEdit_currentTimeT2.setText(a.toString())

    # 多级树点击函数
    def funcT2(self, index):
        re_unit = re.compile(r'^(\d+)')
        result_unit = re_unit.match(index.data())

        # 当点击系统时
        if result_unit is None:
            # 显示当前机组
            self.LineEdit_systemT2.setText(index.data())
            self.LineEdit_unitT2.setText(index.parent().data())
            # 主检测图，波形图，趋势图跟随index变化

        # 当点击机组时
        else:
            self.LineEdit_systemT2.setText('')
            self.LineEdit_unitT2.setText(index.data())

        self.treeView_unit.setExpanded(index, True)

        print(self.unit_model.index(1, 0).data())
        print(self.unit_model.index(1, 0, self.unit_model.index(1, 0)).data())

    '''
    主检测图 is hid at the beginning to make space for the picture of measure point
    '''

    def pushButton_realTime(self,key):
        self.graphicsView_T21.show()
        self.myGraphics21 = myGraphics21(
            self.graphicsView_T21,
            address=r'myData\realTimeDetection.csv',
            key = key,
            threshold=30)
        self.timerT21 = pg.QtCore.QTimer()
        self.timerT21.timeout.connect(self.myGraphics21.update)
        self.timerT21.start(200)

    # Tab3

    # 下拉菜单点击函数
    def funcDiagnosisT3(self):
        pass
    def func_unitT3(self):
        pass
    def func_systemT3(self):
        pass

    # 展示残差图和趋势图
    def pushButton_residual(self,key):
        self.myGraphics31 = myGraphics31(
            self.graphicsView_residualT31,
            address=r'myData\residual.csv',
            key = key,
            threshold=30)

    def pushButton_trend(self,key):
        self.myGraphics32 = myGraphics32(
            self.graphicsView_trendT32,
            address=r'myData\trend.csv',
            key=key,
            threshold=30)

    #Tab4
    @pyqtSlot()
    def on_pushButton_pic1T4_clicked(self):
        myDialogDownload = QtWidgets.QDialog()
        ui = Ui_myDialogDownload()
        ui.setupUi(myDialogDownload)

        address = r'myData\similarity.csv'
        dataset = pd.read_csv(address,header=0,)

        similiarity = dataset[["相似性因子"]].iloc[:, 0].values
        print("long:", len(similiarity))
        print("data", similiarity)

        p4 = ui.graphicsView.addPlot(labels={'left': "相似性因子", })
        # p31.addLegend()
        x = np.arange(130)
        p4.plot(x=x, y=similiarity, pen=(255, 0, 0), name="Red curve")
        # p31.addLine(y=0.068, pen=pg.mkPen(color='g', width=2))
        p4.showGrid(x=True, y=True, alpha=0.4)


        myDialogDownload.exec_()

    # Tab4  maybetab5
    # 多级树点击函数
    def funcT4(self, index):
        if index.data().startswith("故障"):
            self.LineEdit_systemT4.setText(index.parent().data())
            self.LineEdit_faultT4.setText(index.data())
        else:
            self.LineEdit_systemT4.setText('')
            self.LineEdit_faultT4.setText('')

    # 重载closeEvent函数，关闭数据库
    def closeEvent(self, *args, **kwargs):
        self.db.close()


if __name__ == "__main__":
    import sys
    #from PyQt5.Qt import QGuiApplication
    # GuiApplication.setAttribute(Qt.AA_UseOpenGLES)
    QCoreApplication.setAttribute(Qt.AA_UseOpenGLES)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
