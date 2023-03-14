
import numpy as np
import cv2 as cv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QHBoxLayout, QVBoxLayout, QLineEdit, QListWidget, \
    QCheckBox, QListWidgetItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from PIL import Image, ImageDraw, ImageFont

from PoseModule import PoseDetector
from store.data import merideans, acupoints, Name, AcupointsPosition, AcupointIsShow
import math
# import serial
import time
import threading
import sys

from HandTrackingModule import HandDetector

sys.path.insert(1, './pyKinectAzure/')
from pyKinectAzure import pyKinectAzure, _k4a

image = np.ndarray((720, 1200, 3))
depth_image = np.ndarray((720, 1200, 3))

# 各种标记
LH_Landmarks = []
RH_Landmarks = []
Pose_Landmarks = []

handDetector = HandDetector(detectionCon=0.9, maxHands=2)
poseDetector = PoseDetector(detectionCon=0.9, trackCon=0.9)

# 一个UI希望集成上述函数，有一个720*1200的视频显示区域，有两个下拉式复选框组件，一个是穴位acupoints，另一个是经脉meridians，
# 其本身应该有众多共享的变量


class GUI(QWidget):
    global image, depth_image

    def __init__(self):
        super().__init__()
        # self.image = np.ndarray((720, 1200))
        # self.depth_image = np.ndarray((720, 1200))

        self.setWindowTitle('PyQt5视频播放器')
        self.setGeometry(100, 100, 1350, 900)

        self.video_frame = QLabel()
        self.video_frame.resize(700, 1200)
        self.video_frame.setAlignment(Qt.AlignCenter)
        self.video_frame.setMinimumSize(1, 1)

        self.acupointsButtons = ComboCheckBox(acupoints)
        self.meridiansButtons = ComboCheckBox(merideans)

        vbox = QVBoxLayout()
        vbox.addWidget(self.video_frame)
        vbox.addWidget(self.acupointsButtons)
        self.setLayout(vbox)

        self.update_frame()

    def Kinect_Capture(self):
        global image, depth_image

        # 添加 Azure Kinect SDK 路径
        modulePath = 'C:\\Program Files\\Azure Kinect SDK v1.4.1\\sdk\\windows-desktop\\amd64\\release\\bin\\k4a.dll'
        pyK4A = pyKinectAzure(modulePath)
        pyK4A.device_open()
        device_config = pyK4A.config
        device_config.color_format = _k4a.K4A_IMAGE_FORMAT_COLOR_BGRA32
        device_config.color_resolution = _k4a.K4A_COLOR_RESOLUTION_720P
        device_config.depth_mode = _k4a.K4A_DEPTH_MODE_WFOV_2X2BINNED

        # 打开摄像头
        pyK4A.device_start_cameras(device_config)

        while (True):
            pyK4A.device_get_capture()  # Get capture

            # 获得三种数据
            depth_image_handle = pyK4A.capture_get_depth_image()
            color_image_handle = pyK4A.capture_get_color_image()

            if depth_image_handle and color_image_handle:
                # 将获取到的图像转换为numpy矩阵
                image = pyK4A.image_convert_to_numpy(
                    color_image_handle)[:, :, :3]
                depth_image = pyK4A.transform_depth_to_color(
                    depth_image_handle, color_image_handle)

                k = cv.waitKey(25)
                if k == 27:  # Esc
                    break

            pyK4A.image_release(depth_image_handle)
            pyK4A.image_release(color_image_handle)
            pyK4A.capture_release()

            k = cv.waitKey(25)
            if k == 27:  # Esc
                break

        pyK4A.device_stop_cameras()
        pyK4A.device_close()

    def MP(self):
        global image, depth_image, LH_Landmarks, RH_Landmarks, Pose_Landmarks

        handDetector = HandDetector(detectionCon=0.9, maxHands=2)
        poseDetector = PoseDetector(detectionCon=0.9, trackCon=0.9)

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

    def FindAcupoints(self):
        global LH_Landmarks, RH_Landmarks, Pose_Landmarks, AcupointsPosition

        if Pose_Landmarks:
            cx0, cy0 = Pose_Landmarks[0][1], Pose_Landmarks[0][2]
            cx1, cy1 = Pose_Landmarks[1][1], Pose_Landmarks[1][2]
            cx2, cy2 = Pose_Landmarks[2][1], Pose_Landmarks[2][2]
            cx3, cy3 = Pose_Landmarks[3][1], Pose_Landmarks[3][2]
            cx4, cy4 = Pose_Landmarks[4][1], Pose_Landmarks[4][2]
            cx5, cy5 = Pose_Landmarks[5][1], Pose_Landmarks[5][2]
            cx6, cy6 = Pose_Landmarks[6][1], Pose_Landmarks[6][2]
            cx7, cy7 = Pose_Landmarks[7][1], Pose_Landmarks[7][2]
            cx8, cy8 = Pose_Landmarks[8][1], Pose_Landmarks[8][2]
            cx9, cy9 = Pose_Landmarks[9][1], Pose_Landmarks[9][2]
            cx10, cy10 = Pose_Landmarks[10][1], Pose_Landmarks[10][2]
            cx11, cy11 = Pose_Landmarks[11][1], Pose_Landmarks[11][2]
            cx12, cy12 = Pose_Landmarks[12][1], Pose_Landmarks[12][2]
            cx13, cy13 = Pose_Landmarks[13][1], Pose_Landmarks[13][2]
            cx14, cy14 = Pose_Landmarks[14][1], Pose_Landmarks[14][2]
            cx15, cy15 = Pose_Landmarks[15][1], Pose_Landmarks[15][2]
            cx16, cy16 = Pose_Landmarks[16][1], Pose_Landmarks[16][2]
            cx23, cy23 = Pose_Landmarks[23][1], Pose_Landmarks[23][2]
            cx24, cy24 = Pose_Landmarks[24][1], Pose_Landmarks[24][2]
            cx25, cy25 = Pose_Landmarks[25][1], Pose_Landmarks[25][2]
            cx26, cy26 = Pose_Landmarks[26][1], Pose_Landmarks[26][2]
            cx27, cy27 = Pose_Landmarks[27][1], Pose_Landmarks[27][2]
            cx28, cy28 = Pose_Landmarks[28][1], Pose_Landmarks[28][2]

            if Pose_Landmarks[12][2] < Pose_Landmarks[24][2]:
                if Pose_Landmarks[12][1] < Pose_Landmarks[11][1]:
                    AcupointsPosition[0][0][0] = (
                        int((cx13 + cx11) // 2), int((cy13 + cy11) // 2))
                    AcupointsPosition[0][0][1] = (int(cx13), int(cy13))
                    AcupointsPosition[0][0][2] = (
                        int((cx13 + cx15) // 2), int((cy13 + cy15) // 2))
                    AcupointsPosition[0][0][3] = (
                        int((cx13 * 3 + cx15 * 7) // 10), int((cy13 * 3 + cy15 * 7) // 10))
                    AcupointsPosition[0][0][4] = (
                        int((cx13 + cx15 * 4) // 5), int((cy13 + cy15 * 4) // 5))
                    AcupointsPosition[0][0][5] = (int(cx15), int(cy15))

                    AcupointsPosition[0][0][6] = (
                        int((cx14 + cx12) // 2), int((cy14 + cy12) // 2))
                    AcupointsPosition[0][0][7] = (int(cx14), int(cy14))
                    AcupointsPosition[0][0][8] = (
                        int((cx14 + cx16) // 2), int((cy14 + cy16) // 2))
                    AcupointsPosition[0][0][9] = (
                        int((cx14 * 3 + cx16 * 7) // 10), int((cy14 * 3 + cy16 * 7) // 10))
                    AcupointsPosition[0][0][10] = (
                        int((cx14 + cx16 * 4) // 5), int((cy14 + cy16 * 4) // 5))
                    AcupointsPosition[0][0][11] = (int(cx16), int(cy16))

                    AcupointsPosition[0][1][0] = (
                        int((cx11 + cx12) // 2), int((cy11 + cy12) // 2))
                    AcupointsPosition[0][1][1] = (
                        int((cx11 + cx12) // 2), int((cy11 * 17 + cy23) // 18))
                    AcupointsPosition[0][1][2] = (
                        int((cx11 + cx12) // 2), int((cy11 * 16 + cy23 * 2) // 18))
                    AcupointsPosition[0][1][3] = (
                        int((cx11 + cx12) // 2), int((cy11 * 15 + cy23 * 3) // 18))
                    AcupointsPosition[0][1][4] = (
                        int((cx11 + cx12) // 2), int((cy11 * 14 + cy23 * 4) // 18))
                    AcupointsPosition[0][1][5] = (
                        int((cx11 + cx12) // 2), int((cy11 * 13 + cy23 * 5) // 18))
                    AcupointsPosition[0][1][6] = (
                        int((cx11 + cx12) // 2), int((cy11 * 12 + cy23 * 6) // 18))
                    AcupointsPosition[0][1][7] = (
                        int((cx11 + cx12) // 2), int((cy11 * 11 + cy23 * 7) // 18))
                    AcupointsPosition[0][1][8] = (
                        int((cx23 + cx24) // 2), int((cy11 * 10 + cy23 * 8) // 18))
                    AcupointsPosition[0][1][9] = (
                        int((cx23 + cx24) // 2), int((cy11 * 9 + cy23 * 9) // 18))
                    AcupointsPosition[0][1][10] = (
                        int((cx23 + cx24) // 2), int((cy11 * 8 + cy23 * 10) // 18))
                    AcupointsPosition[0][1][11] = (
                        int((cx23 + cx24) // 2), int((cy11 * 7 + cy23 * 11) // 18))
                    AcupointsPosition[0][1][12] = (
                        int((cx23 + cx24) // 2), int((cy11 * 6 + cy23 * 12) // 18))
                    AcupointsPosition[0][1][13] = (
                        int((cx23 + cx24) // 2), int((cy11 * 5 + cy23 * 13) // 18))
                    AcupointsPosition[0][1][14] = (
                        int(cx23), int((cy23 * 5 + cy11) // 6))
                    AcupointsPosition[0][1][15] = (
                        int((cx23 + cx24) // 2), int((cy11 * 3 + cy23 * 15) // 18))
                    AcupointsPosition[0][1][16] = (
                        int((cx23 + cx24) // 2), int((cy11 * 2 + cy23 * 16) // 18))
                    AcupointsPosition[0][1][17] = (
                        int((cx23 + cx24) // 2), int((cy11 + cy23 * 17) // 18))
                    AcupointsPosition[0][1][18] = (
                        int((cx23 + cx24) // 2), int((cy23 + cy24) // 2))

                    AcupointsPosition[0][2][0] = (
                        int((cx11 * 2 + cx12) // 3), int((cy11 * 2 + cy12) // 3))
                    AcupointsPosition[0][2][1] = (
                        int((cx11 * 2 + cx12) // 3), int((cy11 * 15 + cy23) // 16))
                    AcupointsPosition[0][2][2] = (
                        int((cx11 * 2 + cx12) // 3), int((cy11 * 14 + cy23 * 2) // 16))
                    AcupointsPosition[0][2][3] = (
                        int((cx11 * 2 + cx12) // 3), int((cy11 * 13 + cy23 * 3) // 16))
                    AcupointsPosition[0][2][4] = (
                        int((cx11 * 2 + cx12) // 3), int((cy11 * 12 + cy23 * 4) // 16))
                    AcupointsPosition[0][2][5] = (
                        int((cx11 * 2 + cx12) // 3), int((cy11 * 11 + cy23 * 5) // 16))
                    AcupointsPosition[0][2][6] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 10 + cy23 * 6) // 16))
                    AcupointsPosition[0][2][7] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 9 + cy23 * 7) // 16))
                    AcupointsPosition[0][2][8] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 8 + cy23 * 8) // 16))
                    AcupointsPosition[0][2][9] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 7 + cy23 * 9) // 16))
                    AcupointsPosition[0][2][10] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 6 + cy23 * 10) // 16))
                    AcupointsPosition[0][2][11] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 5 + cy23 * 11) // 16))
                    AcupointsPosition[0][2][12] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 4 + cy23 * 12) // 16))
                    AcupointsPosition[0][2][13] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 3 + cy23 * 13) // 16))
                    AcupointsPosition[0][2][14] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 2 + cy23 * 14) // 16))
                    AcupointsPosition[0][2][15] = (
                        int((cx23 * 3 + cx24) // 4), int((cy11 * 1 + cy23 * 15) // 16))
                    AcupointsPosition[0][2][16] = (
                        int((cx23 * 3 + cx24) // 4), int(cy23))
                    AcupointsPosition[0][2][17] = (
                        int((cx23 + cx25) // 2), int((cy23 * 4 + cy25) // 5))
                    AcupointsPosition[0][2][18] = (
                        int((cx23 + cx25) // 2), int((cy23 * 2 + cy25 * 3) // 5))
                    AcupointsPosition[0][2][19] = (
                        int((cx23 + cx25) // 2), int((cy23 + cy25 * 3) // 4))
                    AcupointsPosition[0][2][20] = (
                        int((cx23 + cx25) // 2), int((cy23 + cy25 * 4) // 5))
                    AcupointsPosition[0][2][21] = (int(cx25), int(cy25))
                    AcupointsPosition[0][2][22] = (
                        int((cx25 + cx27) // 2), int((cy25 * 5 + cy27) // 6))
                    AcupointsPosition[0][2][23] = (
                        int((cx25 + cx27) // 2), int((cy25 * 4 + cy27 * 2) // 6))
                    AcupointsPosition[0][2][24] = (
                        int((cx25 + cx27) // 2), int((cy25 + cy27) // 2))
                    AcupointsPosition[0][2][25] = (int(cx27), int(cy27))

                    AcupointsPosition[0][2][26] = (
                        int((cx12 * 2 + cx11) // 3), int((cy12 * 2 + cy11) // 3))
                    AcupointsPosition[0][2][27] = (
                        int((cx12 * 2 + cx11) // 3), int((cy12 * 15 + cy24) // 16))
                    AcupointsPosition[0][2][28] = (
                        int((cx12 * 2 + cx11) // 3), int((cy12 * 14 + cy24 * 2) // 16))
                    AcupointsPosition[0][2][29] = (
                        int((cx12 * 2 + cx11) // 3), int((cy12 * 13 + cy24 * 3) // 16))
                    AcupointsPosition[0][2][30] = (
                        int((cx12 * 2 + cx11) // 3), int((cy12 * 12 + cy24 * 4) // 16))
                    AcupointsPosition[0][2][31] = (
                        int((cx12 * 2 + cx11) // 3), int((cy12 * 11 + cy24 * 5) // 16))
                    AcupointsPosition[0][2][32] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 10 + cy24 * 6) // 16))
                    AcupointsPosition[0][2][33] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 9 + cy24 * 7) // 16))
                    AcupointsPosition[0][2][34] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 8 + cy24 * 8) // 16))
                    AcupointsPosition[0][2][35] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 7 + cy24 * 9) // 16))
                    AcupointsPosition[0][2][36] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 6 + cy24 * 10) // 16))
                    AcupointsPosition[0][2][37] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 5 + cy24 * 11) // 16))
                    AcupointsPosition[0][2][38] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 4 + cy24 * 12) // 16))
                    AcupointsPosition[0][2][39] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 3 + cy24 * 13) // 16))
                    AcupointsPosition[0][2][40] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 2 + cy24 * 14) // 16))
                    AcupointsPosition[0][2][41] = (
                        int((cx24 * 3 + cx23) // 4), int((cy12 * 1 + cy24 * 15) // 16))
                    AcupointsPosition[0][2][42] = (
                        int((cx24 * 3 + cx23) // 4), int(cy24))
                    AcupointsPosition[0][2][43] = (
                        int((cx24 + cx26) // 2), int((cy24 * 4 + cy26) // 5))
                    AcupointsPosition[0][2][44] = (
                        int((cx24 + cx26) // 2), int((cy24 * 2 + cy26 * 3) // 5))
                    AcupointsPosition[0][2][45] = (
                        int((cx24 + cx26) // 2), int((cy24 + cy26 * 3) // 4))
                    AcupointsPosition[0][2][46] = (
                        int((cx24 + cx26) // 2), int((cy24 + cy26 * 4) // 5))
                    AcupointsPosition[0][2][47] = (int(cx26), int(cy26))
                    AcupointsPosition[0][2][48] = (
                        int((cx26 + cx28) // 2), int((cy26 * 5 + cy28) // 6))
                    AcupointsPosition[0][2][49] = (
                        int((cx26 + cx28) // 2), int((cy26 * 4 + cy28 * 2) // 6))
                    AcupointsPosition[0][2][50] = (
                        int((cx26 + cx28) // 2), int((cy26 + cy28) // 2))
                    AcupointsPosition[0][2][51] = (int(cx28), int(cy28))

                else:
                    AcupointsPosition[1][0][0] = (int(cx11), int(cy11))
                    AcupointsPosition[1][0][1] = (
                        int((cx13 + cx11 * 2) // 3), int((cy13 + cy11 * 2) // 3))
                    AcupointsPosition[1][0][2] = (
                        int((cx13 * 2 + cx11) // 3), int((cy13 * 2 + cy11) // 3))
                    AcupointsPosition[1][0][3] = (int(cx13), int(cy13))
                    AcupointsPosition[1][0][4] = (
                        int((cx13 + cx15) // 2), int((cy13 + cy15) // 2))
                    AcupointsPosition[1][0][5] = (
                        int((cx13 + cx15 * 2) // 3), int((cy13 + cy15 * 2) // 3))
                    AcupointsPosition[1][0][6] = (
                        int((cx13 + cx15 * 3) // 4), int((cy13 + cy15 * 3) // 4))
                    AcupointsPosition[1][0][7] = (
                        int((cx13 * 2 + cx15) // 3), int((cy13 * 2 + cy15) // 3))
                    AcupointsPosition[1][0][8] = (int(cx15), int(cy15))

                    AcupointsPosition[1][0][9] = (int(cx12), int(cy12))
                    AcupointsPosition[1][0][10] = (
                        int((cx14 + cx12 * 2) // 3), int((cy14 + cy12 * 2) // 3))
                    AcupointsPosition[1][0][11] = (
                        int((cx14 * 2 + cx12) // 3), int((cy14 * 2 + cy12) // 3))
                    AcupointsPosition[1][0][12] = (int(cx14), int(cy14))
                    AcupointsPosition[1][0][13] = (
                        int((cx14 + cx16) // 2), int((cy14 + cy16) // 2))
                    AcupointsPosition[1][0][14] = (
                        int((cx14 + cx16 * 2) // 3), int((cy14 + cy16 * 2) // 3))
                    AcupointsPosition[1][0][15] = (
                        int((cx14 + cx16 * 3) // 4), int((cy14 + cy16 * 3) // 4))
                    AcupointsPosition[1][0][16] = (
                        int((cx14 * 2 + cx16) // 3), int((cy14 * 2 + cy16) // 3))
                    AcupointsPosition[1][0][17] = (int(cx16), int(cy16))

                    AcupointsPosition[1][1][0] = (int(cx23), int(cy11))
                    AcupointsPosition[1][1][1] = (
                        int(cx23), int((cy23 + cy11 * 17) // 18))
                    AcupointsPosition[1][1][2] = (
                        int(cx23), int((cy23 * 2 + cy11 * 16) // 18))
                    AcupointsPosition[1][1][3] = (
                        int(cx23), int((cy23 * 3 + cy11 * 15) // 18))
                    AcupointsPosition[1][1][4] = (
                        int(cx23), int((cy23 * 4 + cy11 * 14) // 18))
                    AcupointsPosition[1][1][5] = (
                        int(cx23), int((cy23 * 5 + cy11 * 13) // 18))
                    AcupointsPosition[1][1][6] = (
                        int(cx23), int((cy23 * 7 + cy11 * 11) // 18))
                    AcupointsPosition[1][1][7] = (
                        int(cx23), int((cy23 * 9 + cy11 * 9) // 18))
                    AcupointsPosition[1][1][8] = (
                        int(cx23), int((cy23 * 10 + cy11 * 8) // 18))
                    AcupointsPosition[1][1][9] = (
                        int(cx23), int((cy23 * 11 + cy11 * 7) // 18))
                    AcupointsPosition[1][1][10] = (
                        int(cx23), int((cy23 * 12 + cy11 * 6) // 18))
                    AcupointsPosition[1][1][11] = (
                        int(cx23), int((cy23 * 16 + cy11 * 2) // 18))
                    AcupointsPosition[1][1][12] = (int(cx23), int(cy23))
                    AcupointsPosition[1][1][13] = (
                        int((cx23 * 2 + cx25) // 3), int((cy23 * 2 + cy25) // 3))
                    AcupointsPosition[1][1][14] = (
                        int((cx23 + cx25 * 2) // 3), int((cy23 + cy25 * 2) // 3))
                    AcupointsPosition[1][1][15] = (int(cx25), int(cy25))
                    AcupointsPosition[1][1][16] = (
                        int((cx25 + cx27) // 2), int((cy27 + cy25 * 9) // 10))
                    AcupointsPosition[1][1][17] = (
                        int((cx25 + cx27) // 2), int((cy27 * 3 + cy25 * 7) // 10))
                    AcupointsPosition[1][1][18] = (
                        int((cx25 + cx27) // 2), int((cy27 + cy25) // 2))
                    AcupointsPosition[1][1][19] = (
                        int((cx25 + cx27) // 2), int((cy27 + cy25) // 2))
                    AcupointsPosition[1][1][20] = (int(cx27), int(cy27))
                    AcupointsPosition[1][1][21] = (
                        int(cx23), int((cy23 * 16 + cy11 * 2) // 18))
                    AcupointsPosition[1][1][22] = (int(cx24), int(cy12))
                    AcupointsPosition[1][1][23] = (
                        int(cx24), int((cy24 + cy12 * 17) // 18))
                    AcupointsPosition[1][1][24] = (
                        int(cx24), int((cy24 * 2 + cy12 * 16) // 18))
                    AcupointsPosition[1][1][25] = (
                        int(cx24), int((cy24 * 3 + cy12 * 15) // 18))
                    AcupointsPosition[1][1][26] = (
                        int(cx24), int((cy24 * 4 + cy12 * 14) // 18))
                    AcupointsPosition[1][1][27] = (
                        int(cx24), int((cy24 * 5 + cy12 * 13) // 18))
                    AcupointsPosition[1][1][28] = (
                        int(cx24), int((cy24 * 7 + cy12 * 11) // 18))
                    AcupointsPosition[1][1][29] = (
                        int(cx24), int((cy24 * 9 + cy12 * 9) // 18))
                    AcupointsPosition[1][1][30] = (
                        int(cx24), int((cy24 * 10 + cy12 * 8) // 18))
                    AcupointsPosition[1][1][31] = (
                        int(cx24), int((cy24 * 11 + cy12 * 7) // 18))
                    AcupointsPosition[1][1][32] = (
                        int(cx24), int((cy24 * 12 + cy12 * 6) // 18))
                    AcupointsPosition[1][1][33] = (
                        int(cx24), int((cy24 * 16 + cy12 * 2) // 18))
                    AcupointsPosition[1][1][34] = (int(cx24), int(cy24))
                    AcupointsPosition[1][1][35] = (
                        int((cx24 * 2 + cx26) // 3), int((cy24 * 2 + cy26) // 3))
                    AcupointsPosition[1][1][36] = (
                        int((cx24 + cx26 * 2) // 3), int((cy24 + cy26 * 2) // 3))
                    AcupointsPosition[1][1][37] = (int(cx26), int(cy26))
                    AcupointsPosition[1][1][38] = (
                        int((cx26 + cx28) // 2), int((cy28 + cy26 * 9) // 10))
                    AcupointsPosition[1][1][39] = (
                        int((cx26 + cx28) // 2), int((cy28 * 3 + cy26 * 7) // 10))
                    AcupointsPosition[1][1][40] = (
                        int((cx26 + cx28) // 2), int((cy28 + cy26) // 2))
                    AcupointsPosition[1][1][41] = (
                        int((cx26 + cx28) // 2), int((cy28 + cy26) // 2))
                    AcupointsPosition[1][1][42] = (int(cx28), int(cy28))

    def Display(self):

        frame = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
        h, w, _ = self.image.shape

        while (True):
            img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            h, w, _ = img.shape

            # for i in range(len(self.acupointsButtons.isShow)):
            #
            # for i in range(len(self.meridiansButtons.isShow)):

            qimage = QImage(img.data, w, h, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            self.video_frame.setPixmap(pixmap)

        QTimer.singleShot(1, self.update_frame)
    def Display(self):

        frame = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
        h, w, _ = self.image.shape

        while (True):
            img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            h, w, _ = img.shape

            # for i in range(len(self.acupointsButtons.isShow)):
            #
            # for i in range(len(self.meridiansButtons.isShow)):

            qimage = QImage(img.data, w, h, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            self.video_frame.setPixmap(pixmap)

        QTimer.singleShot(1, self.update_frame)

# 并发线程一，调用深度摄像头并获得image和depth_image


def Kinect_Capture():
    # 添加 Azure Kinect SDK 路径
    modulePath = 'C:\\Program Files\\Azure Kinect SDK v1.4.1\\sdk\\windows-desktop\\amd64\\release\\bin\\k4a.dll'
    pyK4A = pyKinectAzure(modulePath)
    pyK4A.device_open()
    device_config = pyK4A.config
    device_config.color_format = _k4a.K4A_IMAGE_FORMAT_COLOR_BGRA32
    device_config.color_resolution = _k4a.K4A_COLOR_RESOLUTION_720P
    device_config.depth_mode = _k4a.K4A_DEPTH_MODE_WFOV_2X2BINNED

    # # 打开摄像头
    pyK4A.device_start_cameras(device_config)

    # 获取相机序列号
    serial_number = pyK4A.device_get_serialnum()

    global image, depth_image

    while (True):
        pyK4A.device_get_capture()  # Get capture

        # 获得三种数据
        depth_image_handle = pyK4A.capture_get_depth_image()
        color_image_handle = pyK4A.capture_get_color_image()

        if depth_image_handle and color_image_handle:
            # 将获取到的图像转换为numpy矩阵
            image = pyK4A.image_convert_to_numpy(color_image_handle)[:, :, :3]
            depth_image = pyK4A.transform_depth_to_color(
                depth_image_handle, color_image_handle)

            MP(image)

            cv.imshow('image', image)
            FindAcupoints()

            k = cv.waitKey(25)
            if k == 27:  # Esc
                break

        pyK4A.image_release(depth_image_handle)
        pyK4A.image_release(color_image_handle)
        pyK4A.capture_release()

        k = cv.waitKey(25)
        if k == 27:  # Esc
            break

    pyK4A.device_stop_cameras()
    pyK4A.device_close()

# 并发线程二，在得到image和depth_image后进行检测，数据更新在LH_Landmarks, RH_Landmarks, Pose_Landmarks


def MP(image):
    global LH_Landmarks, RH_Landmarks, Pose_Landmarks

    # cap = cv.VideoCapture(0)
    #
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

    print(Pose_Landmarks)

# 并发线程三，在更新LH_Landmarks, RH_Landmarks, Pose_Landmarks后进行计算，数据更新在AcupointsPosition


def FindAcupoints():
    if Pose_Landmarks:
        cx0, cy0 = Pose_Landmarks[0][1], Pose_Landmarks[0][2]
        cx1, cy1 = Pose_Landmarks[1][1], Pose_Landmarks[1][2]
        cx2, cy2 = Pose_Landmarks[2][1], Pose_Landmarks[2][2]
        cx3, cy3 = Pose_Landmarks[3][1], Pose_Landmarks[3][2]
        cx4, cy4 = Pose_Landmarks[4][1], Pose_Landmarks[4][2]
        cx5, cy5 = Pose_Landmarks[5][1], Pose_Landmarks[5][2]
        cx6, cy6 = Pose_Landmarks[6][1], Pose_Landmarks[6][2]
        cx7, cy7 = Pose_Landmarks[7][1], Pose_Landmarks[7][2]
        cx8, cy8 = Pose_Landmarks[8][1], Pose_Landmarks[8][2]
        cx9, cy9 = Pose_Landmarks[9][1], Pose_Landmarks[9][2]
        cx10, cy10 = Pose_Landmarks[10][1], Pose_Landmarks[10][2]
        cx11, cy11 = Pose_Landmarks[11][1], Pose_Landmarks[11][2]
        cx12, cy12 = Pose_Landmarks[12][1], Pose_Landmarks[12][2]
        cx13, cy13 = Pose_Landmarks[13][1], Pose_Landmarks[13][2]
        cx14, cy14 = Pose_Landmarks[14][1], Pose_Landmarks[14][2]
        cx15, cy15 = Pose_Landmarks[15][1], Pose_Landmarks[15][2]
        cx16, cy16 = Pose_Landmarks[16][1], Pose_Landmarks[16][2]
        cx23, cy23 = Pose_Landmarks[23][1], Pose_Landmarks[23][2]
        cx24, cy24 = Pose_Landmarks[24][1], Pose_Landmarks[24][2]
        cx25, cy25 = Pose_Landmarks[25][1], Pose_Landmarks[25][2]
        cx26, cy26 = Pose_Landmarks[26][1], Pose_Landmarks[26][2]
        cx27, cy27 = Pose_Landmarks[27][1], Pose_Landmarks[27][2]
        cx28, cy28 = Pose_Landmarks[28][1], Pose_Landmarks[28][2]

        if Pose_Landmarks[12][2] < Pose_Landmarks[24][2]:
            if Pose_Landmarks[12][1] < Pose_Landmarks[11][1]:
                AcupointsPosition[0][0][0] = (
                    int((cx13 + cx11) // 2), int((cy13 + cy11) // 2))
                AcupointsPosition[0][0][1] = (int(cx13), int(cy13))
                AcupointsPosition[0][0][2] = (
                    int((cx13 + cx15) // 2), int((cy13 + cy15) // 2))
                AcupointsPosition[0][0][3] = (
                    int((cx13*3 + cx15*7) // 10), int((cy13*3+cy15*7) // 10))
                AcupointsPosition[0][0][4] = (
                    int((cx13 + cx15 * 4) // 5), int((cy13 + cy15 * 4) // 5))
                AcupointsPosition[0][0][5] = (int(cx15), int(cy15))

                AcupointsPosition[0][0][6] = (
                    int((cx14 + cx12) // 2), int((cy14 + cy12) // 2))
                AcupointsPosition[0][0][7] = (int(cx14), int(cy14))
                AcupointsPosition[0][0][8] = (
                    int((cx14 + cx16) // 2), int((cy14 + cy16) // 2))
                AcupointsPosition[0][0][9] = (
                    int((cx14 * 3 + cx16 * 7) // 10), int((cy14 * 3 + cy16 * 7) // 10))
                AcupointsPosition[0][0][10] = (
                    int((cx14 + cx16 * 4) // 5), int((cy14 + cy16 * 4) // 5))
                AcupointsPosition[0][0][11] = (int(cx16), int(cy16))

                AcupointsPosition[0][1][0] = (
                    int((cx11 + cx12) // 2), int((cy11 + cy12) // 2))
                AcupointsPosition[0][1][1] = (
                    int((cx11 + cx12) // 2), int((cy11*17 + cy23) // 18))
                AcupointsPosition[0][1][2] = (
                    int((cx11 + cx12) // 2), int((cy11 * 16 + cy23*2) // 18))
                AcupointsPosition[0][1][3] = (
                    int((cx11 + cx12) // 2), int((cy11 * 15 + cy23 * 3) // 18))
                AcupointsPosition[0][1][4] = (
                    int((cx11 + cx12) // 2), int((cy11 * 14 + cy23 * 4) // 18))
                AcupointsPosition[0][1][5] = (
                    int((cx11 + cx12) // 2), int((cy11 * 13 + cy23 * 5) // 18))
                AcupointsPosition[0][1][6] = (
                    int((cx11 + cx12) // 2), int((cy11 * 12 + cy23 * 6) // 18))
                AcupointsPosition[0][1][7] = (
                    int((cx11 + cx12) // 2), int((cy11 * 11 + cy23 * 7) // 18))
                AcupointsPosition[0][1][8] = (
                    int((cx23 + cx24) // 2), int((cy11 * 10 + cy23 * 8) // 18))
                AcupointsPosition[0][1][9] = (
                    int((cx23 + cx24) // 2), int((cy11 * 9 + cy23 * 9) // 18))
                AcupointsPosition[0][1][10] = (
                    int((cx23 + cx24) // 2), int((cy11 * 8 + cy23 * 10) // 18))
                AcupointsPosition[0][1][11] = (
                    int((cx23 + cx24) // 2), int((cy11 * 7 + cy23 * 11) // 18))
                AcupointsPosition[0][1][12] = (
                    int((cx23 + cx24) // 2), int((cy11 * 6 + cy23 * 12) // 18))
                AcupointsPosition[0][1][13] = (
                    int((cx23 + cx24) // 2), int((cy11 * 5 + cy23 * 13) // 18))
                AcupointsPosition[0][1][14] = (
                    int(cx23), int((cy23 * 5 + cy11) // 6))
                AcupointsPosition[0][1][15] = (
                    int((cx23 + cx24) // 2), int((cy11 * 3 + cy23 * 15) // 18))
                AcupointsPosition[0][1][16] = (
                    int((cx23 + cx24) // 2), int((cy11 * 2 + cy23 * 16) // 18))
                AcupointsPosition[0][1][17] = (
                    int((cx23 + cx24) // 2), int((cy11 + cy23 * 17) // 18))
                AcupointsPosition[0][1][18] = (
                    int((cx23 + cx24) // 2), int((cy23 + cy24) // 2))

                AcupointsPosition[0][2][0] = (
                    int((cx11*2 + cx12) // 3), int((cy11 * 2 + cy12) // 3))
                AcupointsPosition[0][2][1] = (
                    int((cx11 * 2 + cx12) // 3), int((cy11 * 15 + cy23) // 16))
                AcupointsPosition[0][2][2] = (
                    int((cx11 * 2 + cx12) // 3), int((cy11 * 14 + cy23*2) // 16))
                AcupointsPosition[0][2][3] = (
                    int((cx11 * 2 + cx12) // 3), int((cy11 * 13 + cy23*3) // 16))
                AcupointsPosition[0][2][4] = (
                    int((cx11 * 2 + cx12) // 3), int((cy11 * 12 + cy23 * 4) // 16))
                AcupointsPosition[0][2][5] = (
                    int((cx11 * 2 + cx12) // 3), int((cy11 * 11 + cy23 * 5) // 16))
                AcupointsPosition[0][2][6] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 10 + cy23 * 6) // 16))
                AcupointsPosition[0][2][7] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 9 + cy23 * 7) // 16))
                AcupointsPosition[0][2][8] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 8 + cy23 * 8) // 16))
                AcupointsPosition[0][2][9] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 7 + cy23 * 9) // 16))
                AcupointsPosition[0][2][10] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 6 + cy23 * 10) // 16))
                AcupointsPosition[0][2][11] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 5 + cy23 * 11) // 16))
                AcupointsPosition[0][2][12] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 4 + cy23 * 12) // 16))
                AcupointsPosition[0][2][13] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 3 + cy23 * 13) // 16))
                AcupointsPosition[0][2][14] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 2 + cy23 * 14) // 16))
                AcupointsPosition[0][2][15] = (
                    int((cx23 * 3 + cx24) // 4), int((cy11 * 1 + cy23 * 15) // 16))
                AcupointsPosition[0][2][16] = (
                    int((cx23 * 3 + cx24) // 4), int(cy23))
                AcupointsPosition[0][2][17] = (
                    int((cx23 + cx25) // 2), int((cy23*4 + cy25) // 5))
                AcupointsPosition[0][2][18] = (
                    int((cx23 + cx25) // 2), int((cy23*2 + cy25*3) // 5))
                AcupointsPosition[0][2][19] = (
                    int((cx23 + cx25) // 2), int((cy23 + cy25 * 3) // 4))
                AcupointsPosition[0][2][20] = (
                    int((cx23 + cx25) // 2), int((cy23 + cy25 * 4) // 5))
                AcupointsPosition[0][2][21] = (int(cx25), int(cy25))
                AcupointsPosition[0][2][22] = (
                    int((cx25 + cx27) // 2), int((cy25*5 + cy27) // 6))
                AcupointsPosition[0][2][23] = (
                    int((cx25 + cx27) // 2), int((cy25 * 4 + cy27*2) // 6))
                AcupointsPosition[0][2][24] = (
                    int((cx25 + cx27) // 2), int((cy25 + cy27) // 2))
                AcupointsPosition[0][2][25] = (int(cx27), int(cy27))

                AcupointsPosition[0][2][26] = (
                    int((cx12 * 2 + cx11) // 3), int((cy12 * 2 + cy11) // 3))
                AcupointsPosition[0][2][27] = (
                    int((cx12 * 2 + cx11) // 3), int((cy12 * 15 + cy24) // 16))
                AcupointsPosition[0][2][28] = (
                    int((cx12 * 2 + cx11) // 3), int((cy12 * 14 + cy24 * 2) // 16))
                AcupointsPosition[0][2][29] = (
                    int((cx12 * 2 + cx11) // 3), int((cy12 * 13 + cy24 * 3) // 16))
                AcupointsPosition[0][2][30] = (
                    int((cx12 * 2 + cx11) // 3), int((cy12 * 12 + cy24 * 4) // 16))
                AcupointsPosition[0][2][31] = (
                    int((cx12 * 2 + cx11) // 3), int((cy12 * 11 + cy24 * 5) // 16))
                AcupointsPosition[0][2][32] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 10 + cy24 * 6) // 16))
                AcupointsPosition[0][2][33] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 9 + cy24 * 7) // 16))
                AcupointsPosition[0][2][34] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 8 + cy24 * 8) // 16))
                AcupointsPosition[0][2][35] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 7 + cy24 * 9) // 16))
                AcupointsPosition[0][2][36] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 6 + cy24 * 10) // 16))
                AcupointsPosition[0][2][37] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 5 + cy24 * 11) // 16))
                AcupointsPosition[0][2][38] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 4 + cy24 * 12) // 16))
                AcupointsPosition[0][2][39] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 3 + cy24 * 13) // 16))
                AcupointsPosition[0][2][40] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 2 + cy24 * 14) // 16))
                AcupointsPosition[0][2][41] = (
                    int((cx24 * 3 + cx23) // 4), int((cy12 * 1 + cy24 * 15) // 16))
                AcupointsPosition[0][2][42] = (
                    int((cx24 * 3 + cx23) // 4), int(cy24))
                AcupointsPosition[0][2][43] = (
                    int((cx24 + cx26) // 2), int((cy24 * 4 + cy26) // 5))
                AcupointsPosition[0][2][44] = (
                    int((cx24 + cx26) // 2), int((cy24 * 2 + cy26 * 3) // 5))
                AcupointsPosition[0][2][45] = (
                    int((cx24 + cx26) // 2), int((cy24 + cy26 * 3) // 4))
                AcupointsPosition[0][2][46] = (
                    int((cx24 + cx26) // 2), int((cy24 + cy26 * 4) // 5))
                AcupointsPosition[0][2][47] = (int(cx26), int(cy26))
                AcupointsPosition[0][2][48] = (
                    int((cx26 + cx28) // 2), int((cy26 * 5 + cy28) // 6))
                AcupointsPosition[0][2][49] = (
                    int((cx26 + cx28) // 2), int((cy26 * 4 + cy28 * 2) // 6))
                AcupointsPosition[0][2][50] = (
                    int((cx26 + cx28) // 2), int((cy26 + cy28) // 2))
                AcupointsPosition[0][2][51] = (int(cx28), int(cy28))

            else:
                AcupointsPosition[1][0][0] = (int(cx11), int(cy11))
                AcupointsPosition[1][0][1] = (
                    int((cx13 + cx11 * 2) // 3), int((cy13 + cy11 * 2) // 3))
                AcupointsPosition[1][0][2] = (
                    int((cx13 * 2 + cx11) // 3), int((cy13 * 2 + cy11) // 3))
                AcupointsPosition[1][0][3] = (int(cx13), int(cy13))
                AcupointsPosition[1][0][4] = (
                    int((cx13 + cx15) // 2), int((cy13 + cy15) // 2))
                AcupointsPosition[1][0][5] = (
                    int((cx13 + cx15*2) // 3), int((cy13 + cy15*2) // 3))
                AcupointsPosition[1][0][6] = (
                    int((cx13 + cx15*3) // 4), int((cy13 + cy15*3) // 4))
                AcupointsPosition[1][0][7] = (
                    int((cx13*2 + cx15) // 3), int((cy13*2 + cy15) // 3))
                AcupointsPosition[1][0][8] = (int(cx15), int(cy15))

                AcupointsPosition[1][0][9] = (int(cx12), int(cy12))
                AcupointsPosition[1][0][10] = (
                    int((cx14 + cx12 * 2) // 3), int((cy14 + cy12 * 2) // 3))
                AcupointsPosition[1][0][11] = (
                    int((cx14 * 2 + cx12) // 3), int((cy14 * 2 + cy12) // 3))
                AcupointsPosition[1][0][12] = (int(cx14), int(cy14))
                AcupointsPosition[1][0][13] = (
                    int((cx14 + cx16) // 2), int((cy14 + cy16) // 2))
                AcupointsPosition[1][0][14] = (
                    int((cx14 + cx16 * 2) // 3), int((cy14 + cy16 * 2) // 3))
                AcupointsPosition[1][0][15] = (
                    int((cx14 + cx16 * 3) // 4), int((cy14 + cy16 * 3) // 4))
                AcupointsPosition[1][0][16] = (
                    int((cx14 * 2 + cx16) // 3), int((cy14 * 2 + cy16) // 3))
                AcupointsPosition[1][0][17] = (int(cx16), int(cy16))

                AcupointsPosition[1][1][0] = (int(cx23), int(cy11))
                AcupointsPosition[1][1][1] = (
                    int(cx23), int((cy23 + cy11*17) // 18))
                AcupointsPosition[1][1][2] = (
                    int(cx23), int((cy23*2 + cy11 * 16) // 18))
                AcupointsPosition[1][1][3] = (
                    int(cx23), int((cy23 * 3 + cy11 * 15) // 18))
                AcupointsPosition[1][1][4] = (
                    int(cx23), int((cy23*4 + cy11 * 14) // 18))
                AcupointsPosition[1][1][5] = (
                    int(cx23), int((cy23*5+cy11*13)//18))
                AcupointsPosition[1][1][6] = (
                    int(cx23), int((cy23 * 7 + cy11 * 11) // 18))
                AcupointsPosition[1][1][7] = (
                    int(cx23), int((cy23 * 9 + cy11*9) // 18))
                AcupointsPosition[1][1][8] = (
                    int(cx23), int((cy23 * 10 + cy11 * 8) // 18))
                AcupointsPosition[1][1][9] = (
                    int(cx23), int((cy23 * 11 + cy11 * 7) // 18))
                AcupointsPosition[1][1][10] = (
                    int(cx23), int((cy23 * 12 + cy11 * 6) // 18))
                AcupointsPosition[1][1][11] = (
                    int(cx23), int((cy23 * 16 + cy11 * 2) // 18))
                AcupointsPosition[1][1][12] = (int(cx23), int(cy23))
                AcupointsPosition[1][1][13] = (
                    int((cx23*2+cx25)//3), int((cy23*2+cy25)//3))
                AcupointsPosition[1][1][14] = (
                    int((cx23 + cx25*2) // 3), int((cy23 + cy25*2) // 3))
                AcupointsPosition[1][1][15] = (int(cx25), int(cy25))
                AcupointsPosition[1][1][16] = (
                    int((cx25 + cx27) // 2), int((cy27 + cy25 * 9) // 10))
                AcupointsPosition[1][1][17] = (
                    int((cx25 + cx27) // 2), int((cy27*3 + cy25 * 7) // 10))
                AcupointsPosition[1][1][18] = (
                    int((cx25 + cx27) // 2), int((cy27 + cy25) // 2))
                AcupointsPosition[1][1][19] = (
                    int((cx25 + cx27) // 2), int((cy27 + cy25) // 2))
                AcupointsPosition[1][1][20] = (int(cx27), int(cy27))
                AcupointsPosition[1][1][21] = (
                    int(cx23), int((cy23 * 16 + cy11*2) // 18))
                AcupointsPosition[1][1][22] = (int(cx24), int(cy12))
                AcupointsPosition[1][1][23] = (
                    int(cx24), int((cy24 + cy12 * 17) // 18))
                AcupointsPosition[1][1][24] = (
                    int(cx24), int((cy24 * 2 + cy12 * 16) // 18))
                AcupointsPosition[1][1][25] = (
                    int(cx24), int((cy24 * 3 + cy12 * 15) // 18))
                AcupointsPosition[1][1][26] = (
                    int(cx24), int((cy24 * 4 + cy12 * 14) // 18))
                AcupointsPosition[1][1][27] = (
                    int(cx24), int((cy24 * 5 + cy12*13) // 18))
                AcupointsPosition[1][1][28] = (
                    int(cx24), int((cy24 * 7 + cy12 * 11) // 18))
                AcupointsPosition[1][1][29] = (
                    int(cx24), int((cy24 * 9 + cy12 * 9) // 18))
                AcupointsPosition[1][1][30] = (
                    int(cx24), int((cy24 * 10 + cy12 * 8) // 18))
                AcupointsPosition[1][1][31] = (
                    int(cx24), int((cy24 * 11 + cy12 * 7) // 18))
                AcupointsPosition[1][1][32] = (
                    int(cx24), int((cy24 * 12 + cy12 * 6) // 18))
                AcupointsPosition[1][1][33] = (
                    int(cx24), int((cy24 * 16 + cy12 * 2) // 18))
                AcupointsPosition[1][1][34] = (int(cx24), int(cy24))
                AcupointsPosition[1][1][35] = (
                    int((cx24 * 2 + cx26) // 3), int((cy24 * 2 + cy26) // 3))
                AcupointsPosition[1][1][36] = (
                    int((cx24 + cx26 * 2) // 3), int((cy24 + cy26 * 2) // 3))
                AcupointsPosition[1][1][37] = (int(cx26), int(cy26))
                AcupointsPosition[1][1][38] = (
                    int((cx26 + cx28) // 2), int((cy28 + cy26 * 9) // 10))
                AcupointsPosition[1][1][39] = (
                    int((cx26 + cx28) // 2), int((cy28 * 3 + cy26 * 7) // 10))
                AcupointsPosition[1][1][40] = (
                    int((cx26 + cx28) // 2), int((cy28 + cy26) // 2))
                AcupointsPosition[1][1][41] = (
                    int((cx26 + cx28) // 2), int((cy28 + cy26) // 2))
                AcupointsPosition[1][1][42] = (int(cx28), int(cy28))

    #print(AcupointsPosition)

# 下拉复选框插件


class ComboCheckBox(QComboBox):
    def __init__(self, items):  # items==[str,str...]
        super(ComboCheckBox, self).__init__()
        self.items = items
        self.items.insert(0, '全部')
        self.isShow = list(len(self.items))

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
            self.qCheckBox[i].stateChanged.connect(
                lambda: self.isshow(self.items[i]))  # 槽函数关联 函数是show（）
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

    # 槽函数
    def isshow(self, acupointName):
        i, j, k, n = FindAcupoint(acupointName)
        self.isShow[n] = (self.isShow[n] + 1) % 2
        return self.isShow[n]

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

# 图像上画穴位点


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

# 查询函数，输入穴位名，输出在Name中的位置下标


def FindAcupoint(acupointName=""):
    n = 0
    for i in range(2):
        for j in range(5):
            for k in range(len(Name[i][j])):
                if Name[i][j][k] == acupointName:
                    return i, j, k, n
                n = n + 1

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

# 穴位连线


def Find_meridians(meridianName):
    i = merideans.index(meridianName)

    if i <= 2:
        if i == 1:
            for j in range(len(AcupointsPosition[0][i]) - 1):
                image = cv.line(image, AcupointsPosition[0][i][j], AcupointsPosition[0][i][j + 1], color=(255, 0, 3),
                                thickness=2)
        else:
            for j in range((len(AcupointsPosition[0][i]) - 2) / 2):
                image = cv.line(image, AcupointsPosition[0][i][j], AcupointsPosition[0][i][j + 1], color=(255, 0, 3),
                                thickness=2)
                image = cv.line(image, AcupointsPosition[0][i][j + len(AcupointsPosition[0][i])],
                                AcupointsPosition[0][i][j + 1 + len(AcupointsPosition[0][i])], color=(255, 0, 3), thickness=2)
    else:
        for j in range((len(AcupointsPosition[0][i]) - 2) / 2):
            image = cv.line(image, AcupointsPosition[1][i][j], AcupointsPosition[1][i][j + 1], color=(255, 0, 3),
                            thickness=2)
            image = cv.line(image, AcupointsPosition[1][i][j + len(AcupointsPosition[1][i])],
                            AcupointsPosition[1][i][j + 1 +
                                                    len(AcupointsPosition[1][i])], color=(255, 0, 3),
                            thickness=2)


if __name__ == '__main__':
    # cv.imshow('image', image)
    #Kinect_Capture()
    # lock = threading.Lock()
    first_thread = threading.Thread(target=Kinect_Capture)
    first_thread.start()
    # second_thread = threading.Thread(target=MP)
    # second_thread.start()
    third_thread = threading.Thread(target=FindAcupoints)
    third_thread.start()
