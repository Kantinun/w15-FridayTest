# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'os.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from test import Osci

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(932, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 150, 20, 281))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 420, 281, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 140, 281, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(290, 150, 20, 281))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(330, 140, 281, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(320, 150, 20, 281))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(330, 420, 281, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(600, 150, 20, 281))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(910, 100, 20, 331))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(640, 420, 281, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(630, 100, 20, 331))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(640, 90, 281, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(750, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btn_ver_ne = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ver_ne.setGeometry(QtCore.QRect(30, 240, 121, 41))
        self.btn_ver_ne.setObjectName("btn_ver_ne")
        self.btn_ver_pos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ver_pos.setGeometry(QtCore.QRect(180, 240, 111, 41))
        self.btn_ver_pos.setObjectName("btn_ver_pos")
        self.btn_ver_neScale = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ver_neScale.setGeometry(QtCore.QRect(30, 370, 121, 41))
        self.btn_ver_neScale.setObjectName("btn_ver_neScale")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.btn_ver_posScale = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ver_posScale.setGeometry(QtCore.QRect(180, 370, 111, 41))
        self.btn_ver_posScale.setObjectName("btn_ver_posScale")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_hor_posScale = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hor_posScale.setGeometry(QtCore.QRect(490, 370, 111, 41))
        self.btn_hor_posScale.setObjectName("btn_hor_posScale")
        self.btn_hor_neScale = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hor_neScale.setGeometry(QtCore.QRect(340, 370, 121, 41))
        self.btn_hor_neScale.setObjectName("btn_hor_neScale")
        self.btn_hor_ne = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hor_ne.setGeometry(QtCore.QRect(340, 240, 121, 41))
        self.btn_hor_ne.setObjectName("btn_hor_ne")
        self.btn_hor_pos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hor_pos.setGeometry(QtCore.QRect(490, 240, 111, 41))
        self.btn_hor_pos.setObjectName("btn_hor_pos")
        self.btn_T_pos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_T_pos.setGeometry(QtCore.QRect(800, 190, 111, 41))
        self.btn_T_pos.setObjectName("btn_T_pos")
        self.btn_T_ne = QtWidgets.QPushButton(self.centralwidget)
        self.btn_T_ne.setGeometry(QtCore.QRect(650, 190, 121, 41))
        self.btn_T_ne.setObjectName("btn_T_ne")
        self.btn_couping = QtWidgets.QPushButton(self.centralwidget)
        self.btn_couping.setGeometry(QtCore.QRect(30, 100, 121, 41))
        self.btn_couping.setAutoExclusive(False)
        self.btn_couping.setObjectName("btn_couping")
        self.labelcoupling = QtWidgets.QLabel(self.centralwidget)
        self.labelcoupling.setGeometry(QtCore.QRect(170, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelcoupling.setFont(font)
        self.labelcoupling.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelcoupling.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.labelcoupling.setAcceptDrops(False)
        self.labelcoupling.setAlignment(QtCore.Qt.AlignCenter)
        self.labelcoupling.setWordWrap(False)
        self.labelcoupling.setObjectName("labelcoupling")
        self.btn_T_sweep = QtWidgets.QPushButton(self.centralwidget)
        self.btn_T_sweep.setGeometry(QtCore.QRect(650, 250, 121, 41))
        self.btn_T_sweep.setObjectName("btn_T_sweep")
        self.label_T_sweep = QtWidgets.QLabel(self.centralwidget)
        self.label_T_sweep.setGeometry(QtCore.QRect(800, 250, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_T_sweep.setFont(font)
        self.label_T_sweep.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_T_sweep.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_T_sweep.setAcceptDrops(False)
        self.label_T_sweep.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_sweep.setWordWrap(False)
        self.label_T_sweep.setObjectName("label_T_sweep")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 110, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(770, 260, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(770, 320, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.btn_T_source = QtWidgets.QPushButton(self.centralwidget)
        self.btn_T_source.setGeometry(QtCore.QRect(650, 310, 121, 41))
        self.btn_T_source.setObjectName("btn_T_source")
        self.label_T_source = QtWidgets.QLabel(self.centralwidget)
        self.label_T_source.setGeometry(QtCore.QRect(800, 310, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_T_source.setFont(font)
        self.label_T_source.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_T_source.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_T_source.setAcceptDrops(False)
        self.label_T_source.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_source.setWordWrap(False)
        self.label_T_source.setObjectName("label_T_source")
        self.label_T_slope = QtWidgets.QLabel(self.centralwidget)
        self.label_T_slope.setGeometry(QtCore.QRect(800, 370, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_T_slope.setFont(font)
        self.label_T_slope.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_T_slope.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_T_slope.setAcceptDrops(False)
        self.label_T_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_slope.setWordWrap(False)
        self.label_T_slope.setObjectName("label_T_slope")
        self.btn_T_slope = QtWidgets.QPushButton(self.centralwidget)
        self.btn_T_slope.setGeometry(QtCore.QRect(650, 370, 121, 41))
        self.btn_T_slope.setObjectName("btn_T_slope")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(770, 380, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(650, 10, 121, 31))
        self.btn_run.setAutoExclusive(False)
        self.btn_run.setObjectName("btn_run")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(800, 10, 111, 31))
        self.btn_stop.setAutoExclusive(False)
        self.btn_stop.setObjectName("btn_stop")
        self.btn_ch1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ch1.setGeometry(QtCore.QRect(340, 100, 61, 41))
        self.btn_ch1.setObjectName("btn_ch1")
        self.btn_ch2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ch2.setGeometry(QtCore.QRect(410, 100, 61, 41))
        self.btn_ch2.setObjectName("btn_ch2")
        self.btn_AUTO = QtWidgets.QPushButton(self.centralwidget)
        self.btn_AUTO.setGeometry(QtCore.QRect(340, 10, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.btn_AUTO.setFont(font)
        self.btn_AUTO.setObjectName("btn_AUTO")
        self.btn_CAP = QtWidgets.QPushButton(self.centralwidget)
        self.btn_CAP.setGeometry(QtCore.QRect(30, 10, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.btn_CAP.setFont(font)
        self.btn_CAP.setObjectName("btn_CAP")
        self.btn_ch3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ch3.setGeometry(QtCore.QRect(480, 100, 61, 41))
        self.btn_ch3.setObjectName("btn_ch3")
        self.btn_ch4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ch4.setGeometry(QtCore.QRect(550, 100, 61, 41))
        self.btn_ch4.setObjectName("btn_ch4")
        self.btn_on = QtWidgets.QPushButton(self.centralwidget)
        self.btn_on.setGeometry(QtCore.QRect(650, 60, 121, 31))
        self.btn_on.setAutoExclusive(False)
        self.btn_on.setObjectName("btn_on")
        self.btn_off = QtWidgets.QPushButton(self.centralwidget)
        self.btn_off.setGeometry(QtCore.QRect(800, 60, 121, 31))
        self.btn_off.setAutoExclusive(False)
        self.btn_off.setObjectName("btn_off")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 21))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Os"))
        self.label.setText(_translate("MainWindow", "Vertical"))
        self.label_2.setText(_translate("MainWindow", "Horizontal"))
        self.label_3.setText(_translate("MainWindow", "Trigger"))
        self.label_4.setText(_translate("MainWindow", "Position"))
        self.label_5.setText(_translate("MainWindow", "Position"))
        self.label_6.setText(_translate("MainWindow", "Position"))
        self.btn_ver_ne.setText(_translate("MainWindow", "-"))
        self.btn_ver_pos.setText(_translate("MainWindow", "+"))
        self.btn_ver_neScale.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "Scale"))
        self.btn_ver_posScale.setText(_translate("MainWindow", "+"))
        self.label_8.setText(_translate("MainWindow", "Scale"))
        self.btn_hor_posScale.setText(_translate("MainWindow", "+"))
        self.btn_hor_neScale.setText(_translate("MainWindow", "-"))
        self.btn_hor_ne.setText(_translate("MainWindow", "-"))
        self.btn_hor_pos.setText(_translate("MainWindow", "+"))
        self.btn_T_pos.setText(_translate("MainWindow", "+"))
        self.btn_T_ne.setText(_translate("MainWindow", "-"))
        self.btn_couping.setText(_translate("MainWindow", "Coupling"))
        self.labelcoupling.setText(_translate("MainWindow", "DC"))
        self.btn_T_sweep.setText(_translate("MainWindow", "SWEEP"))
        self.label_T_sweep.setText(_translate("MainWindow", "AUTO"))
        self.label_9.setText(_translate("MainWindow", "="))
        self.label_10.setText(_translate("MainWindow", "="))
        self.label_11.setText(_translate("MainWindow", "="))
        self.btn_T_source.setText(_translate("MainWindow", "SOURCE"))
        self.label_T_source.setText(_translate("MainWindow", "CHAN 1"))
        self.label_T_slope.setText(_translate("MainWindow", "Rising"))
        self.btn_T_slope.setText(_translate("MainWindow", "SLOPE"))
        self.label_12.setText(_translate("MainWindow", "="))
        self.btn_run.setText(_translate("MainWindow", "RUN"))
        self.btn_stop.setText(_translate("MainWindow", "STOP"))
        self.btn_ch1.setText(_translate("MainWindow", "CH 1"))
        self.btn_ch2.setText(_translate("MainWindow", "CH 2"))
        self.btn_AUTO.setText(_translate("MainWindow", "AUTO"))
        self.btn_CAP.setText(_translate("MainWindow", "CAPTURE"))
        self.btn_ch3.setText(_translate("MainWindow", "CH 3"))
        self.btn_ch4.setText(_translate("MainWindow", "CH 4"))
        self.btn_on.setText(_translate("MainWindow", "ON"))
        self.btn_off.setText(_translate("MainWindow", "OFF"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionExit.setText(_translate("MainWindow", "EXIT"))

if __name__ == "__main__":
    myOsci = Osci("4.3.2.1")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.btn_ch1.clicked.connect(lambda : myOsci.ch_display("1"))
    ui.btn_T_slope.clicked.connect(lambda : myOsci.setTrigSlope())
    ui.btn_run.clicked.connect(lambda: myOsci.run())
    sys.exit(app.exec_())
