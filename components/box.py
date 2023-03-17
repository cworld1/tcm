import sys
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel, QLineEdit, QListWidget, QCheckBox, \
    QListWidgetItem
import cv2 as cv
from store.data import merideans, acupoints, Name, AcupointsPosition, AcupointIsShow

# 测试数据
Name = ["尺泽(左)", "孔最", "侠白", "天泉", "郄门", "大横", "归来", "天枢", "库房",
        "不容", "梁门", "太乙", "大巨", "府舍", "腹结", "伏兔", "阴市", "足三里", "条口"]


class ComboCheckBox(QComboBox):
    signa = pyqtSignal(list)

    def __init__(self, items):  # items==[str,str...]
        super(ComboCheckBox, self).__init__()
        self.items = items
        self.items.insert(0, '全部')

        self.row_num = len(self.items)
        self.Selectedrow_num = 0
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()
        self.addQCheckBox(0)
        self.qCheckBox[0].stateChanged.connect(self.All)
        for i in range(1, self.row_num):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(self.show0)
        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)
        self.setLineEdit(self.qLineEdit)
        self.setMaxVisibleItems(100)  # 避免滑条的出现引起滑条偷吃标签的问题

    def addQCheckBox(self, i):
        self.qCheckBox.append(QCheckBox())
        qItem = QListWidgetItem(self.qListWidget)
        self.qCheckBox[i].setText(self.items[i])
        self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])

    def Selectlist(self):
        Outputlist = []
        for i in range(1, self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        self.Selectedrow_num = len(Outputlist)

        return Outputlist

    def show0(self):
        show0 = ''
        Outputlist = self.Selectlist()
        self.signa.emit(Outputlist)
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in Outputlist:
            show0 += i + ';'
        if self.Selectedrow_num == 0:
            self.qCheckBox[0].setCheckState(0)
        elif self.Selectedrow_num == self.row_num - 1:
            self.qCheckBox[0].setCheckState(2)
        else:
            self.qCheckBox[0].setCheckState(1)
        self.qLineEdit.setText(show0)
        self.qLineEdit.setReadOnly(True)

    def All(self, zhuangtai):
        if zhuangtai == 2:
            for i in range(1, self.row_num):
                self.qCheckBox[i].setChecked(True)
        elif zhuangtai == 1:
            if self.Selectedrow_num == 0:
                self.qCheckBox[0].setCheckState(2)
        elif zhuangtai == 0:
            self.clear()

    def clear(self):
        for i in range(self.row_num):
            self.qCheckBox[i].setChecked(False)

    def changeitemlist(self, itemlist):

        self.items = itemlist
        self.items.insert(0, '全部')
        self.row_num = len(self.items)
        self.Selectedrow_num = 0
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()
        self.addQCheckBox(0)
        self.qCheckBox[0].stateChanged.connect(self.All)
        for i in range(1, self.row_num):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(self.show0)
        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)
        self.setLineEdit(self.qLineEdit)

    def Display(self):
        frame = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
        h, w, _ = self.image.shape
        while (True):
            img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            h, w, _ = img.shape

            # for i in range(len(self.acupointsButtons.isShow)):

            for i in range(len(self.meridiansButtons.isShow)):
                print(self.meridiansButtons.isShow[i])
            qimage = QImage(img.data, w, h, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            self.video_frame.setPixmap(pixmap)

        QTimer.singleShot(1, self.update_frame)


class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main')
        self.setGeometry(100, 100, 1350, 900)

        # 添加组件
        self.acupointsButtons = ComboCheckBox(Name)
        vbox = QVBoxLayout()
        vbox.addWidget(self.acupointsButtons)
        self.setLayout(vbox)


def printList(selectedList):
    print(selectedList)
    Find_meridians(selectedList)
# 穴位连线


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.acupointsButtons.signa.connect(printList)
    window.show()

    sys.exit(app.exec_())
