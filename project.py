import sys
sys.path.insert(1, '../pyKinectAzure/')
import numpy as np
from pyKinectAzure import pyKinectAzure, _k4a
from hooks.HandTrackingModule import HandDetector
from hooks.PoseModule import PoseDetector
import cv2
import serial
import time

## 打开设备/模式设置

# 添加 Azure Kinect SDK 路径
modulePath = 'C:\\Program Files\\Azure Kinect SDK v1.4.1\\sdk\\windows-desktop\\amd64\\release\\bin\\k4a.dll'
pyK4A = pyKinectAzure(modulePath)
pyK4A.device_open()
device_config = pyK4A.config
device_config.color_format = _k4a.K4A_IMAGE_FORMAT_COLOR_BGRA32
device_config.color_resolution = _k4a.K4A_COLOR_RESOLUTION_720P
device_config.depth_mode = _k4a.K4A_DEPTH_MODE_WFOV_2X2BINNED

## 打开摄像头
pyK4A.device_start_cameras(device_config)

# 获取相机序列号
serial_number = pyK4A.device_get_serialnum()

serial_number

LH_Landmarks = []
RH_Landmarks = []
Pose_Landmarks = []

handDetector = HandDetector(detectionCon=0.8, maxHands=2)
poseDetector = PoseDetector(detectionCon=0.8, trackCon=0.9)

ser = serial.Serial('COM5', 9600, timeout=1)

def Projection(u0, v0, fx, fy, u, v, z):
    pixel_coordinate = np.array([[u], [v], [1]])
    intrix_matrix = [[fx, 0, u0], [0, fy, v0], [0, 0, 1]]
    matrix = np.linalg.inv(intrix_matrix)
    x = z * (matrix[0][0] * u + matrix[0][2]) / 10
    y = z * (matrix[1][1] * v + matrix[1][2]) / 10
    return x, y, z / 10

#对获取的深度图像进行颜色处理
def color_depth_image(depth_image):
    # 实现将原图片转换为uint8类型
    depth_color_image = cv2.convertScaleAbs(depth_image, alpha=0.05)
    # 赋予伪色彩
    depth_color_image = cv2.applyColorMap(depth_color_image, cv2.COLORMAP_JET)

    return depth_color_image

while (True):
    pyK4A.device_get_capture()  # Get capture

    # 获得三种数据
    depth_image_handle = pyK4A.capture_get_depth_image()
    color_image_handle = pyK4A.capture_get_color_image()

    if depth_image_handle and color_image_handle:
        # 将获取到的图像转换为numpy矩阵
        color_image = pyK4A.image_convert_to_numpy(color_image_handle)[:, :, :3]
        # depth_image = pyK4A.image_convert_to_numpy(depth_image_handle)
        image = pyK4A.transform_depth_to_color(depth_image_handle, color_image_handle)

        Hands, img = handDetector.findHands(color_image, draw=False)
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

        u, v = Poselist[12, 1], Poselist[12, 2]
        x, y, z = Projection(640.612671, 367.137726, 607.669800, 607.552429, u, v, image[v][u])

        # 生成x y z坐标，并用空格分隔
        coords = f"{x} {y} {z}\n"
        # 将字符串编码为字节，并发送给Arduino
        ser.write(coords.encode())
        # 打印发送的数据
        print(f"Sent: {coords}")

        # 等待0.5秒
        time.sleep(0.5)
        # 读取Arduino返回的数据，并解码为0.字符串
        data = ser.readline().decode()
        # 如果数据不为空，则打印接收到的数据
        if data:
            print(f"Received: {data}")

        # 等待0.5秒
        time.sleep(0.5)
        # 读取Arduino返回的数据，并解码为字符串
        data = ser.readline().decode()
        # 如果数据不为空，则打印接收到的数据
        if data:
            print(f"Transmitted: {data}")

        k = cv2.waitKey(25)
        if k == 27:  # Esc
            break
    k = k + 1
    pyK4A.image_release(depth_image_handle)
    pyK4A.image_release(color_image_handle)
    pyK4A.capture_release()

    k = cv2.waitKey(25)
    if k == 27:  # Esc
        break

pyK4A.device_stop_cameras()
pyK4A.device_close()

