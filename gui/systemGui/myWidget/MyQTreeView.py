from PyQt5.QtWidgets import QTreeView,QFileSystemModel,QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QModelIndex,pyqtSignal

class QTreeViewUnit(QTreeView):

    # parent声明隶属于哪一个控件，unit_num声明机组个数
    def __init__(self,parent=None,unit_num=10):
        QTreeView.__init__(self,parent=None)

        self.unit_model = QtGui.QStandardItemModel()
        self.unit_model.setHorizontalHeaderLabels(["机组"])

        for i in range(unit_num):
            unit_name = QtGui.QStandardItem("%d号机组" % (i+1))

            sys_name1 = QtGui.QStandardItem("风能捕捉系统")
            sys_name2 = QtGui.QStandardItem("传动系统")
            sys_name3 = QtGui.QStandardItem("发电机系统")
            unit_name.setChild(0, sys_name1)
            unit_name.setChild(1, sys_name2)
            unit_name.setChild(2, sys_name3)
            self.unit_model.setItem(i,0,unit_name)

        self.setModel(self.unit_model)
        self.clicked.connect(self.show_graph)

    def show_graph(self,index):
        print("你正在查看{}".format(index.data()))
        #print(self.unit_model.itemFromIndex(index).setText("666"))


class QTreeViewFault(QTreeView):

    # parent声明隶属于哪一个控件，unit_num声明机组个数
    def __init__(self,parent=None,fault_num=3):
        QTreeView.__init__(self,parent=None)

        self.unit_model = QtGui.QStandardItemModel()
        self.unit_model.setHorizontalHeaderLabels(["故障知识库"])

        knowledge_base = QtGui.QStandardItem("故障知识库")
        sys_name = ["风能捕捉系统","传动系统","发电机系统"]

        for k in range(3):
            system = QtGui.QStandardItem(sys_name[k])
            knowledge_base.setChild(k, system)

            for i in range(fault_num):
                fault_name = QtGui.QStandardItem("故障模式%d" % (i+1))
                system.setChild(i, fault_name)


        self.unit_model.setItem(0,knowledge_base)
        self.setModel(self.unit_model)
        self.clicked.connect(self.show_graph)

    def show_graph(self,index):
        print("你正在查看{}".format(index.data()))
        #print(self.unit_model.itemFromIndex(index).setText("666"))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = QTreeViewFault()
    w.show()
    sys.exit(app.exec_())