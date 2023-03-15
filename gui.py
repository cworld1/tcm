# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_origin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from hooks.utils import play_video, pause
# 用于展示视频（图像）
import cv2

# 用于读取数据
from store.data import merideans, acupoints

# 组件导入
from components.box import ComboCheckBox, printList



class Ui_MainWindow(object):
    # 更新图片


    def setupUi(self, MainWindow):
        # 设定主窗口
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1714, 772)
        # 初步建立布局
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 左侧布局 1，包含了两个 QComboBox
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 100, 421, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.b_verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.b_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.b_verticalLayout.setObjectName("b_verticalLayout")
        # ComboBox 1
        self.merideansBox = ComboCheckBox(merideans)
        self.merideansBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.merideansBox.setStyleSheet("ComboCheckBox {\n"
                                        "  background-color: #ffffff;\n"
                                        "  border: 1px solid #dcdfe6;\n"
                                        "  padding: 10px;\n"
                                        "  border-radius: 7px;\n"
                                        "  font: bold 17px;\n"
                                        "}")
        self.merideansBox.setObjectName("merideansBox")
        self.verticalLayout.addWidget(self.merideansBox)
        # ComboBox 2
        self.acupointsBox = ComboCheckBox(acupoints)
        self.acupointsBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.acupointsBox.setStyleSheet("ComboCheckBox {\n"
                                        "  background-color: #ffffff;\n"
                                        "  border: 1px solid #dcdfe6;\n"
                                        "  padding: 10px;\n"
                                        "  border-radius: 7px;\n"
                                        "  font: bold 17px;\n"
                                        "}")
        self.acupointsBox.setObjectName("acupointsBox")
        self.verticalLayout.addWidget(self.acupointsBox)

        # 左侧布局 2，包含了两个 QPushButton
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(100, 390, 281, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "  background-color: #ffffff;\n"
                                      "  border: 1px solid #dcdfe6;\n"
                                      "  padding: 10px;\n"
                                      "  border-radius: 7px;\n"
                                      "  font: bold 17px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "  background-color: #bff1d8;\n"
                                      "  color: #066335;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed,\n"
                                      "QPushButton:checked {\n"
                                      "  border-color: #44b17b;\n"
                                      "  color: #066335;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(play_video)

        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.clicked.connect(pause)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "  background-color: #ffffff;\n"
                                        "  border: 1px solid #dcdfe6;\n"
                                        "  padding: 10px;\n"
                                        "  border-radius: 7px;\n"
                                        "  font: bold 17px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "  background-color: #bff1d8;\n"
                                        "  color: #066335;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed,\n"
                                        "QPushButton:checked {\n"
                                        "  border-color: #44b17b;\n"
                                        "  color: #066335;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        # 展示图像，此处需要集成 Kinect 图像注入刷新
        # 设置展示控件
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 30, 1200, 720))
        self.label.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                 "border-radius:7px;")
        self.label.setObjectName("label")
        # 设置窗口尺寸

        # 添加深度图像放置位置
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 480, 431, 261))
        self.label_2.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                   "border-radius:7px;")
        self.label_2.setObjectName("label_2")

        # 添加图标
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 117, 67))
        self.label_3.setObjectName("label_3")

        # 主窗口
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1714, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 建立UI翻译，注入文本内容
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "播放"))
        self.pushButton_2.setText(_translate("MainWindow", "暂停"))
        self.label.setText(_translate("MainWindow", "CameraImage"))
        self.label_2.setText(_translate("MainWindow", "DeepthImage"))


# 执行主程序
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 测试
    # 图片路径
    img_path = "testRes/test.jpg"
    # 通过cv读取图片
    img = cv2.imread(img_path)
    ui.updateImage(img)
    ui.acupointsBox.signa.connect(printList)
    ui.merideansBox.signa.connect(printList)

    sys.exit(app.exec_())
