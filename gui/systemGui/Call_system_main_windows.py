from PyQt5.QtCore import pyqtSlot, QThread, QTimer, pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QHeaderView, QAbstractItemView
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_system_main_windows import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 连接数据库
        self.connectDB()

        #
        self.sqlModel_windPowerStation = QSqlQueryModel(self)
        self.setTableView(tableView=self.tableView_windPowerStation,
                           sqlModel=self.sqlModel_windPowerStation,
                           Query="SELECT 风电场名称, 风电场编号 FROM t_windPowerStation",
                           Header=["风电场名称","风电场编号"],
                           func=self.test
                           )

        # 隐藏机组详细信息
        self.scrollArea.setHidden(False)

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

    # P1
    # 对QTableView设置模型，列头，查询，单击槽函数
    def setTableView(self,tableView,sqlModel,Header,Query,func):
        tableView.setModel(sqlModel)
        tableView.verticalHeader().hide()
        tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sqlModel.setQuery("%s"%Query)
        for i in range(len(Header)):
            sqlModel.setHeaderData(i,Qt.Horizontal, Header[i])
        tableView.clicked.connect(func)

    def test(self, index):
        query = QSqlQuery()
        codeOfPowerStation = self.sqlModel_windPowerStation.index(index.row(),1).data()
        query.exec_(
            "select 集团名称,风场位置,总装机容量,装机台数 from t_windPowerStation where 风电场编号 = '%s' " % codeOfPowerStation
            )
        if query.first():
            self.lineEdit_groupCompany.setText(query.value(0))
            self.lineEdit_windField.setText(query.value(1))
            self.lineEdit_grossInstalledCapacity.setText(str(query.value(2)))
            self.lineEdit_numOfInstalledStations.setText(str(query.value(3)))



    @pyqtSlot()
    def on_unitLogo_1_clicked(self):
        self.scrollArea.setHidden(True)
        self.unitDetalFrame.setHidden(False)

    # 重载closeEvent函数，关闭数据库
    def closeEvent(self, *args, **kwargs):
        self.db.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
