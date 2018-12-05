
# -*- coding: utf-8 -*-

import sys
import time # 时间戳

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import qdarkstyle  # QSS样式表

from mainUI import Ui_Form #自动生成的界面

import serial
import serial.tools.list_ports

class MyMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        pg.setConfigOption('background', '#31363b')  # 设置背景为灰色
        pg.setConfigOption('foreground', 'w')  # 设置前景（包括坐标轴，线条，文本等等）为白色。
        #pg.setConfigOptions(antialias=True) # 使曲线看起来更光滑，而不是锯齿状

        self.ui = Ui_Form()
        self.ui.setupUi(self)     
                
        ##创建线程实例
        self.thread1 = Thread1()

        self.thread1.sinOut1.connect(self.slotThread1)
        self.thread1.sinOut2.connect(self.slotThread2)

    def linkSlot(self):
        pass

    def startSlot(self):
        pass

    def stopSlot(self):
        pass

    def slotThread1(self, text): # 结果输出
        # self.ui.textEdit.setPlainText(text)
        # 格式化时间
        timeText = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.ui.textEdit.append(timeText + " : " + text)  # 自动添加回车

    def slotThread2(self, value):  # 结果输出
        text = '{:.3f}'.format(value)
        self.ui.lcdNumber.display(text)
        if self.flag is "continuous" :
            #连续进行绘图
            self.ui.graphicsView.clear()  # 初始化图,不然似乎会发生不好的事情
            self.data.append(value)
            self.ui.graphicsView.plot(self.data, 
                pen=pg.mkPen(color='#3daee9', width=4))


class Thread1(QtCore.QThread):
    sinOut1 = QtCore.pyqtSignal(str)
    sinOut2 = QtCore.pyqtSignal(float)

    def _init_(self,parent=None):
        super(Thread1,self).__init__(parent)

    def link(self):
        pass

    def run(self):
        pass

if __name__=="__main__":  
    app = QtWidgets.QApplication(sys.argv)
    # 设置样式表
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myWin = MyMainWindow()
    myWin.show()#向框架添加绘制事件
    sys.exit(app.exec_())