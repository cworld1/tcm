import sys
import numpy as np
import cv2 as cv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QHBoxLayout, QVBoxLayout, QLineEdit, QListWidget, \
    QCheckBox, QListWidgetItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image, ImageDraw, ImageFont

image = np.ndarray((1200, 800))

Name = [["尺泽(左)", "孔最", "侠白", "天泉", "郄门", "大横", "归来", "天枢", "库房", "不容", "梁门", "太乙", "大巨", "府舍", "腹结", "伏兔", "阴市", "足三里", "条口"],
        ["臑俞", "曲垣", "膏肓", "秩边", "胞肓", "盲门", "意舍", "魂门", "譩譆", "委中", "承扶", "殷门", "合阳", "承筋", "承山", "消泺", "臑会", "肘尖", "四渎"]]

AcupointsPosition = [[[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                      [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]],
                     [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                      [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]]]

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv.cvtColor(np.asarray(img), cv.COLOR_RGB2BGR)

class ComboCheckBox(QComboBox):
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
            self.qCheckBox[i].stateChanged.connect(lambda: self.show(self.items[i]))
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

    def show(self, acupointName):
        x = AcupointsPosition[0][0][Name.index(acupointName)][0]
        y = AcupointsPosition[0][0][Name.index(acupointName)][1]
        img = cv2ImgAddText(image, acupointName, x, y, (0, 0, 0), 20)
        cv.circle(img, AcupointsPosition[0][0][Name.index(acupointName)], 7, (255, 0, 255), cv.FILLED)
        print(x, y, acupointName)
        #return x, y, img

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

cap = cv.VideoCapture(0)

success, image = cap.read()

# 定义一个输入列表，用于生成复选框的选项
input_list = ["A", "B", "C", "D"]

# 创建一个应用程序对象
app = QApplication(sys.argv)

# 创建一个窗口对象
window = QWidget()

# 设置窗口的大小和标题
window.resize(1350, 1000)
window.setWindowTitle("PyQt5 Visual Interface Program")

# 创建一个标签对象，用于显示图像或视频流
label = QLabel()

# 设置标签的大小和对齐方式
label.resize(1200, 700)
label.setAlignment(Qt.AlignCenter)

# 如果全局变量image是一个numpy.ndarray类型，就将其转换为QPixmap类型并显示在标签上
if isinstance(image, np.ndarray):
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    h, w, _ = image.shape
    qimage = QImage(image.data, w, h, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(qimage)
    label.setPixmap(pixmap)

# 创建两个复选框对象，用于选择选项
combo_box_1 = ComboCheckBox(input_list)
combo_box_2 = ComboCheckBox(input_list)

# 设置复选框的大小
combo_box_1.resize(600, 200)
combo_box_2.resize(600, 200)

# 设置复选框为多选模式
combo_box_1.setDuplicatesEnabled(True)
combo_box_2.setDuplicatesEnabled(True)

# 创建一个水平布局对象，用于排列复选框
hbox = QHBoxLayout()

# 将复选框添加到水平布局中
hbox.addWidget(combo_box_1)
hbox.addWidget(combo_box_2)

# 创建一个垂直布局对象，用于排列标签和水平布局
vbox = QVBoxLayout()

# 将标签和水平布局添加到垂直布局中
vbox.addWidget(label)
vbox.addLayout(hbox)

# 将垂直布局设置为窗口的布局
window.setLayout(vbox)

# 显示窗口
window.show()

# 运行应用程序
sys.exit(app.exec_())
