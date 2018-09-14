from PyQt5.QtWidgets import QTreeView,QFileSystemModel,QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QModelIndex,pyqtSignal

class Ui_myQTreeViewUnit(object):

    # parent声明隶属于哪一个控件，unit_num声明机组个数
    def __init__(self,myQTreeViewUnit,model,parent=None,unit_num=8):


        model.setHorizontalHeaderLabels(["机组"])


        for i in range(unit_num):
            unit_name = QtGui.QStandardItem("%d号机组" % (i+1))

            sys_name1 = QtGui.QStandardItem("风能捕捉系统")
            sys_name2 = QtGui.QStandardItem("传动系统")
            sys_name3 = QtGui.QStandardItem("发电机系统")
            unit_name.setChild(0, sys_name1)
            unit_name.setChild(1, sys_name2)
            unit_name.setChild(2, sys_name3)
            model.setItem(i,0,unit_name)

        myQTreeViewUnit.setModel(model)
        myQTreeViewUnit.clicked.connect(self.show_graph)

    def show_graph(self,index):
        pass


class Ui_myQTreeViewFault(QTreeView):

    # parent声明隶属于哪一个控件，unit_num声明机组个数
    def __init__(self,myQTreeViewFault,parent=None,fault_num=3):
        QTreeView.__init__(self,parent=None)

        self.fault_model = QtGui.QStandardItemModel()
        self.fault_model.setHorizontalHeaderLabels(["故障知识库"])

        #knowledge_base = QtGui.QStandardItem("故障知识库")
        sys_name = ["风能捕捉系统","传动系统","发电机系统"]

        for k in range(3):
            system = QtGui.QStandardItem(sys_name[k])
            self.fault_model.setItem(k ,0, system)

            for i in range(fault_num):
                fault_name = QtGui.QStandardItem("故障模式%d" % (i+1))
                system.setChild(i, fault_name)

        myQTreeViewFault.setModel(self.fault_model)
        myQTreeViewFault.clicked.connect(self.show_graph)

    def show_graph(self,index):
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = QTreeView()
    Ui_myQTreeViewUnit(w,unit_num=8)
    w.show()
    sys.exit(app.exec_())