# Python imports
import math
import sys
import threading  # 多线程


from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

# Others
import numpy as np
import cv2 as cv
from PIL import Image, ImageDraw, ImageFont
from hooks.utils import FindAcupoints
# Local imports
from gui import Ui_MainWindow
from hooks.utils import playVideo
from store.data import Name
from hooks.HandTrackingModule import HandDetector
from hooks.PoseModule import PoseDetector

# 添加 Azure Kinect SDK 路径
sys.path.insert(1, "./pyKinectAzure/")
from pyKinectAzure import pyKinectAzure, _k4a


image = np.ndarray((720, 1200, 3))

depth_image = np.ndarray((720, 1200, 3))

# 各种标记
LH_Landmarks = []
RH_Landmarks = []
Pose_Landmarks = []
# 列表数据
global selectedAcupoints, selectedMeridians
selectedAcupoints = []
selectedMeridians = []

handDetector = HandDetector(detectionCon=0.9, maxHands=2)
poseDetector = PoseDetector(detectionCon=0.9, trackCon=0.9)


# 一个UI希望集成上述函数，有一个720*1200的视频显示区域，有两个下拉式复选框组件，一个是穴位acupoints，另一个是经脉meridians，
# 其本身应该有众多共享的变量


# 并发线程一，调用深度摄像头并获得image和depth_image
def Kinect_Capture():
    global image, depth_image, flag, pyK4A, device_config
    # 添加 Azure Kinect SDK 路径
    modulePath = "C:\\Program Files\\Azure Kinect SDK v1.4.1\\\
sdk\\windows-desktop\\amd64\\release\\bin\\k4a.dll"
    pyK4A = pyKinectAzure(modulePath)
    pyK4A.device_open()
    device_config = pyK4A.config
    device_config.color_format = _k4a.K4A_IMAGE_FORMAT_COLOR_BGRA32
    device_config.color_resolution = _k4a.K4A_COLOR_RESOLUTION_720P
    device_config.depth_mode = _k4a.K4A_DEPTH_MODE_WFOV_2X2BINNED

    # 获取相机序列号
    # serial_number = pyK4A.device_get_serialnum()

    flag = True
    playVideo()


# 并发线程二，在得到image和depth_image后进行检测，数据更新在LH_Landmarks, RH_Landmarks, Pose_Landmarks
def MP():
    global LH_Landmarks, RH_Landmarks, Pose_Landmarks
    # cap = cv.VideoCapture(0)
    # success, image = cap.read()
    Hands, img = handDetector.findHands(image, draw=False)
    img = poseDetector.findPose(img, draw=False)
    Poselist, bboxInfo = poseDetector.findPosition(img, draw=False)

    if Hands:
        hand0 = Hands[0]

        if hand0["type"] == "Left":
            LH_Landmarks = hand0["lmList"]
        else:
            RH_Landmarks = hand0["lmList"]

        if len(Hands) > 1:
            hand1 = Hands[1]
            if hand1["type"] == "Left":
                LH_Landmarks = hand1["lmList"]
            else:
                RH_Landmarks = hand1["lmList"]

    if Poselist:
        Pose_Landmarks = Poselist


# 并发线程三，在更新LH_Landmarks, RH_Landmarks, Pose_Landmarks后进行计算，数据更新在AcupointsPosition
# 从hooks.findAcupoints 导入
# 图像上画穴位点
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if isinstance(img, np.ndarray):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype("simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv.cvtColor(np.asarray(img), cv.COLOR_RGB2BGR)


# 查询函数，输入穴位名，输出在Name中的位置下标
def FindAcupoint(acupointName=""):
    for i in range(2):
        for j in range(5):
            for k in range(len(Name[i][j])):
                if Name[i][j][k] == acupointName:
                    return i, j, k


# 预测
def Projection(u0, v0, fx, fy, u, v, z):
    pixel_coordinate = np.array([[u], [v], [1]])
    intrix_matrix = [[fx, 0, u0], [0, fy, v0], [0, 0, 1]]
    matrix = np.linalg.inv(intrix_matrix)
    x = z * (matrix[0][0] * u + matrix[0][2]) / 10
    y = z * (matrix[1][1] * v + matrix[1][2]) / 10
    return x, y, z / 10


# 计算差值
def delta(x, y, z, dx, dy, dz):
    return x - dx, y - dy, z - dz


# 计算角度
def pos_angle(x, y, z):
    theta_1 = math.atan2(x, z) * 180 / math.pi
    theta_2 = math.atan2(y, z) * 180 / math.pi
    return theta_1, theta_2


# 上色
def color_depth_image(depth_image):
    # 实现将原图片转换为uint8类型
    depth_color_image = cv.convertScaleAbs(depth_image, alpha=0.05)
    # 赋予伪色彩
    depth_color_image = cv.applyColorMap(depth_color_image, cv.COLORMAP_JET)

    return depth_color_image


if __name__ == "__main__":
    global ui
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(
        app, theme="dark_teal.xml", extra={"font_family": "Microsoft YaHei UI"}
    )  # 主题样式
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 线程开启
    first_thread = threading.Thread(target=Kinect_Capture)
    first_thread.start()
    second_thread = threading.Thread(target=MP)
    second_thread.start()

    third_thread = threading.Thread(target=FindAcupoints)
    third_thread.start()

    pyK4A.device_stop_cameras()
    pyK4A.device_close()
    sys.exit(app.exec_())
