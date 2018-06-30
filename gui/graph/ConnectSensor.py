import pymysql
import serial
from PyQt5.QtCore import QThread


class Worker(QThread):

    def __int__(self):
        super(Worker, self).__init__(parent)

    def run(self):
        self.flag = 1
        print("线程已经启动")

        ser = serial.Serial("COM4", 9600)
        db = pymysql.connect(
            "localhost",
            "root",
            "password",
            "db_voice",
            charset='utf8')
        cursor = db.cursor()
        while self.flag == 1:
            # 读取串口数据，将byte型str型变为int型
            data = ser.readline()
            try:
                data = int(data.decode('utf-8'))
            except BaseException:
                data = -1
            # 执行sql语句插入数据
            sql = "insert into t_sound(`sound`) values (%d)" % data
            try:
                cursor.execute(sql)
                db.commit()
            except BaseException:
                db.rollback()
        # 关闭串口占用,指针和数据库
        cursor.close()
        ser.close()
        db.close()

    def stop(self):
        self.flag = 0
        print("线程即将关闭")