# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'components/gui_origin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 750)
        MainWindow.setStyleSheet("font-size: 16px; font-family: 'Microsoft YaHei UI'")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 20, 20, 0)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.sidebar_verticalLayout = QtWidgets.QVBoxLayout()
        self.sidebar_verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.sidebar_verticalLayout.setObjectName("sidebar_verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(117, 67))
        self.logo.setMaximumSize(QtCore.QSize(117, 67))
        self.logo.setStyleSheet("image: url(./res/logo_simple.png)")
        self.logo.setText("")
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.sidebar_verticalLayout.addLayout(self.horizontalLayout_2)
        self.meridiansBox = QtWidgets.QComboBox(self.centralwidget)
        self.meridiansBox.setMinimumSize(QtCore.QSize(420, 45))
        self.meridiansBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.meridiansBox.setStyleSheet("ComboCheckBox { color: #ffffff }")
        self.meridiansBox.setObjectName("meridiansBox")
        self.meridiansBox.addItem("")
        self.meridiansBox.addItem("")
        self.sidebar_verticalLayout.addWidget(self.meridiansBox)
        self.acupointsBox = QtWidgets.QComboBox(self.centralwidget)
        self.acupointsBox.setMinimumSize(QtCore.QSize(420, 45))
        self.acupointsBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.acupointsBox.setStyleSheet("ComboCheckBox { color: #ffffff }")
        self.acupointsBox.setObjectName("acupointsBox")
        self.acupointsBox.addItem("")
        self.acupointsBox.addItem("")
        self.sidebar_verticalLayout.addWidget(self.acupointsBox)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(420, 240))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.sidebar_verticalLayout.addWidget(self.textEdit)
        self.buttons_horizontalLayout = QtWidgets.QHBoxLayout()
        self.buttons_horizontalLayout.setObjectName("buttons_horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.buttons_horizontalLayout.addItem(spacerItem1)
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setMinimumSize(QtCore.QSize(120, 40))
        self.play.setMaximumSize(QtCore.QSize(16777215, 40))
        self.play.setObjectName("play")
        self.buttons_horizontalLayout.addWidget(self.play)
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setMinimumSize(QtCore.QSize(120, 40))
        self.pause.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pause.setObjectName("pause")
        self.buttons_horizontalLayout.addWidget(self.pause)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.buttons_horizontalLayout.addItem(spacerItem2)
        self.sidebar_verticalLayout.addLayout(self.buttons_horizontalLayout)
        self.deepthImage = QtWidgets.QLabel(self.centralwidget)
        self.deepthImage.setMinimumSize(QtCore.QSize(420, 180))
        self.deepthImage.setStyleSheet("background-color: #232629; border-radius: 7px")
        self.deepthImage.setAlignment(QtCore.Qt.AlignCenter)
        self.deepthImage.setObjectName("deepthImage")
        self.sidebar_verticalLayout.addWidget(self.deepthImage)
        self.gridLayout.addLayout(self.sidebar_verticalLayout, 0, 0, 1, 1)
        self.cameraImage = QtWidgets.QLabel(self.centralwidget)
        self.cameraImage.setStyleSheet("background-color: #232629; border-radius:7px")
        self.cameraImage.setScaledContents(True)
        self.cameraImage.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraImage.setObjectName("cameraImage")
        self.gridLayout.addWidget(self.cameraImage, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TCM"))
        self.checkBox.setText(_translate("MainWindow", "转置"))
        self.meridiansBox.setItemText(0, _translate("MainWindow", "1"))
        self.meridiansBox.setItemText(1, _translate("MainWindow", "2"))
        self.acupointsBox.setItemText(0, _translate("MainWindow", "1"))
        self.acupointsBox.setItemText(1, _translate("MainWindow", "2"))
        self.textEdit.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:16px; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.play.setText(_translate("MainWindow", "播放"))
        self.pause.setText(_translate("MainWindow", "暂停"))
        self.deepthImage.setText(_translate("MainWindow", "DeepthImage"))
        self.cameraImage.setText(_translate("MainWindow", "CameraImage"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
