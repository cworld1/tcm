from PyQt5 import QtCore, QtGui, QtWidgets
from main import changeTime
# 用于展示视频（图像）
import cv2

def play_video():
    changeTime(25)


def pause():
    changeTime(200000)


def updateImage(ui, img):
    # 通道转化
    RGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 将图片转化成Qt可读格式
    image = QtGui.QImage(
        RGBImg, RGBImg.shape[1], RGBImg.shape[0], QtGui.QImage.Format_RGB888)
    # 加载图片,并自定义图片展示尺寸
    image = QtGui.QPixmap(image).scaled(1200, 720)
    # 显示图片
    ui.label.setPixmap(image)