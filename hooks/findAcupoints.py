# 各种标记
LH_Landmarks = []
RH_Landmarks = []
Pose_Landmarks = []
# 列表数据
global selectedAcupoints, selectedMeridians
from store.data import AcupointsPosition, Name
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def getPosition(acupointName=""):
    for i in range(2):
        for j in range(len(Name[i])):
            for k in range(len(Name[i][j])):

                # print(acupointName, Name[i][j][k])
                if Name[i][j][k] == acupointName:
                    return i, j, k


def showAcupointsCircle(img, text, textColor=(60,179,113), textSize=20):
    i, j, k = getPosition(text)
    image = img.copy()
    cv.circle(image, AcupointsPosition[i][j][k], 7, textColor, -1)
    return image, AcupointsPosition[i][j][k]


def showAcupointsText(img, text, position,textColor="#1DE9B6", textSize=20 ):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv.cvtColor(np.asarray(img), cv.COLOR_RGB2BGR)

