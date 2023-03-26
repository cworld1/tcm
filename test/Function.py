import math
import cv2 as cv
import numpy as np
from hooks.PoseModule import PoseDetector
from hooks.HandTrackingModule import HandDetector
from PIL import Image, ImageDraw, ImageFont
import sys
sys.path.insert(1, '../pyKinectAzure/')
from pyKinectAzure import pyKinectAzure, _k4a
import serial
import time


Name = [["尺泽", "孔最", "侠白", "天泉", "郄门", "大横", "归来", "天枢", "库房", "不容", "梁门", "太乙", "大巨", "府舍", "腹结", "伏兔", "阴市", "足三里", "条口"],
        ["臑俞", "曲垣", "膏肓", "秩边", "胞肓", "盲门", "意舍", "魂门", "譩譆", "委中", "承扶", "殷门", "合阳", "承筋", "承山", "消泺", "臑会", "肘尖", "四渎"]]

AcupointsPosition = [[[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                      [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]],
                     [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                      [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]]]

LH_Landmarks = []
RH_Landmarks = []
Pose_Landmarks = []

handDetector = HandDetector(detectionCon=0.9, maxHands=2)
poseDetector = PoseDetector(detectionCon=0.9, trackCon=0.9)

def MP(image):
    global LH_Landmarks, RH_Landmarks, Pose_Landmarks

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
                AcupointsPosition[0][0][0] = (int(cx13), int(cy13))
                AcupointsPosition[0][0][1] = (int((cx13 + cx15) // 2), int((cy13 + cy15) // 2))
                AcupointsPosition[0][0][2] = (int((cx13 + cx11) // 2), int((cy13 + cy11) // 2))
                AcupointsPosition[0][0][3] = (int((cx13 + cx11 * 2) // 3), int((cy13 + cy11 * 2) // 3))
                AcupointsPosition[0][0][4] = (int((cx15 * 2 + cx13) // 3), int((cy15 * 2 + cy13) // 3))
                AcupointsPosition[0][0][5] = (int(cx23), int((cy23 * 3 + cy11) // 4))
                AcupointsPosition[0][0][6] = (int((cx23 * 3 + cx24) // 4), int((cy23 * 3 + cy24) // 4))
                AcupointsPosition[0][0][7] = (int((cx23 * 3 + cx24) // 4), int((cy23 * 3 + cy11) // 4))
                AcupointsPosition[0][0][8] = (int((cx11 * 3 + cx12) // 4), int((cy11 * 3 + cy12) // 4))
                AcupointsPosition[0][0][9] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 4 + cy12 + cy23 * 3) // 8))
                AcupointsPosition[0][0][10] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 5 + cy12 + cy23 * 6) // 12))
                AcupointsPosition[0][0][11] = (int((cx23 * 3 + cx24) // 4), int((cy23 * 15 + cy12 + cy11 * 8) // 24))
                AcupointsPosition[0][0][12] = (int((cx23 * 3 + cx24) // 4), int((cy23 * 6 + cy11 + cy24) // 8))
                AcupointsPosition[0][0][13] = (int(cx23), int(cy23))
                AcupointsPosition[0][0][14] = (int(cx23), int((cy23 * 5 + cy11) // 6))
                AcupointsPosition[0][0][15] = (int((cx23 + cx25) // 2), int((cy23 + cy25 * 2) // 3))
                AcupointsPosition[0][0][16] = (int((cx23 + cx25) // 2), int((cy23 + cy25 * 5) // 6))
                AcupointsPosition[0][0][17] = (int((cx25 * 2 + cx27) // 3), int((cy25 * 2 + cy27) // 3))
                AcupointsPosition[0][0][18] = (int((cx25 + cx27 * 2) // 3), int((cy25 + cy27 * 2) // 3))

                AcupointsPosition[0][1][0] = (int(cx14), int(cy14))
                AcupointsPosition[0][1][1] = (int((cx14 + cx16) // 2), int((cy14 + cy16) // 2))
                AcupointsPosition[0][1][2] = (int((cx14 + cx12) // 2), int((cy14 + cy12) // 2))
                AcupointsPosition[0][1][3] = (int((cx14 + cx12 * 2) // 3), int((cy13 + cy11 * 2) // 3))
                AcupointsPosition[0][1][4] = (int((cx24 * 3 + cx23) // 4), int((cy24 * 3 + cy11) // 4))
                AcupointsPosition[0][1][5] = (int((cx24 * 3 + cx23) // 4), int((cy24 * 3 + cy23) // 4))
                AcupointsPosition[0][1][6] = (int(cx24), int((cy24 * 3 + cy12) // 4))
                AcupointsPosition[0][1][7] = (int((cx16 * 2 + cx14) // 3), int((cy16 * 2 + cy14) // 3))
                AcupointsPosition[0][1][8] = (int((cx24 * 3 + cx23) // 4), int((cy24 * 15 + cy11 + cy12 * 8) // 24))
                AcupointsPosition[0][1][9] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 5 + cy11 + cy24 * 6) // 12))
                AcupointsPosition[0][1][10] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 4 + cy11 + cy24 * 3) // 8))
                AcupointsPosition[0][1][11] = (int((cx12 * 3 + cx11) // 4), int((cy12 * 3 + cy11) // 4))
                AcupointsPosition[0][1][12] = (int(cx24), int((cy24 * 5 + cy12) // 6))
                AcupointsPosition[0][1][13] = (int(cx24), int(cy24))
                AcupointsPosition[0][1][14] = (int((cx24 * 3 + cx23) // 4), int((cy24 * 6 + cy12 + cy23) // 8))
                AcupointsPosition[0][1][15] = (int((cx26 + cx28 * 2) // 3), int((cy26 + cy28 * 2) // 3))
                AcupointsPosition[0][1][16] = (int((cx26 * 2 + cx28) // 3), int((cy26 * 2 + cy28) // 3))
                AcupointsPosition[0][1][17] = (int((cx24 + cx26) // 2), int((cy24 + cy26 * 5) // 6))
                AcupointsPosition[0][1][18] = (int((cx24 + cx26) // 2), int((cy24 + cy26 * 2) // 3))

            else:
                AcupointsPosition[1][0][0] = (int(cx11), int(cy11))
                AcupointsPosition[1][0][1] = (int((cx11*3+cx12)//4), int((cy11*3+cy12)//4))
                AcupointsPosition[1][0][2] = (int(cx23), int(cy11))
                AcupointsPosition[1][0][3] = (int(cx23), int(cy23))
                AcupointsPosition[1][0][4] = (int(cx23), int((cy23*7+cy11)//8))
                AcupointsPosition[1][0][5] = (int(cx23), int((cy23 + cy11) // 2))
                AcupointsPosition[1][0][6] = (int(cx23), int((cy23 *3 + cy11*5) // 8))
                AcupointsPosition[1][0][7] = (int(cx23), int((cy23 * 2 + cy11 * 6) // 8))
                AcupointsPosition[1][0][8] = (int(cx23), int((cy23 + cy11 * 7) // 8))
                AcupointsPosition[1][0][9] = (int(cx25), int(cy25))
                AcupointsPosition[1][0][10] = (int((cx23*2+cx25)//3), int((cy23*2+cy25)//3))
                AcupointsPosition[1][0][11] = (int((cx23 + cx25*2) // 3), int((cy23 + cy25*2) // 3))
                AcupointsPosition[1][0][12] = (int((cx25 + cx27) //2), int((cy27 + cy25 * 4) // 5))
                AcupointsPosition[1][0][13] = (int((cx25 + cx27) // 2), int((cy27 *2+ cy25 *3) // 5))
                AcupointsPosition[1][0][14] = (int((cx25 + cx27) // 2), int((cy27*3 + cy25 * 2) // 5))
                AcupointsPosition[1][0][15] = (int( (cx13*2+cx11)//3), int((cy13*2+cy11)//3))
                AcupointsPosition[1][0][16] = (int((cx13+ cx11*2) // 3), int((cy13 + cy11*2) // 3))
                AcupointsPosition[1][0][17] = (int(cx13), int(cy13))
                AcupointsPosition[1][0][18] = (int((cx13*2+cx15)//3), int((cy13*2+cy15)//3))

                AcupointsPosition[1][1][0] = (int(cx24), int(cy24))
                AcupointsPosition[1][1][1] = (int(cx24), int(cy12))
                AcupointsPosition[1][1][2] = (int((cx12 * 3 + cx11) // 4), int((cy12 * 3 + cy11) // 4))
                AcupointsPosition[1][1][3] = (int(cx12), int(cy12))
                AcupointsPosition[1][1][4] = (int(cx24), int((cy24 + cy12 * 7) // 8))
                AcupointsPosition[1][1][5] = (int(cx24), int((cy24 * 2 + cy12 * 6) // 8))
                AcupointsPosition[1][1][6] = (int(cx24), int((cy24 * 3 + cy12 * 5) // 8))
                AcupointsPosition[1][1][7] = (int(cx24), int((cy24 + cy12) // 2))
                AcupointsPosition[1][1][8] = (int(cx24), int((cy24 * 7 + cy12) // 8))
                AcupointsPosition[1][1][9] = (int((cx26 + cx28) // 2), int((cy28 * 3 + cy26 * 2) // 5))
                AcupointsPosition[1][1][10] = (int((cx26 + cx28) // 2), int((cy28 + cy26 * 4) // 5))
                AcupointsPosition[1][1][11] = (int((cx24 + cx26 * 2) // 3), int((cy24 + cy26 * 2) // 3))
                AcupointsPosition[1][1][12] = (int((cx24 * 2 + cx26) // 3), int((cy24 * 2 + cy26) // 3))
                AcupointsPosition[1][1][13] = (int(cx26), int(cy26))
                AcupointsPosition[1][1][14] = (int((cx14 * 2 + cx16) // 3), int((cy14 * 2 + cy16) // 3))
                AcupointsPosition[1][1][15] = (int(cx14), int(cy14))
                AcupointsPosition[1][1][16] = (int((cx14 + cx12 * 2) // 3), int((cy14 + cy12 * 2) // 3))
                AcupointsPosition[1][1][17] = (int((cx14 * 2 + cx12) // 3), int((cy14 * 2 + cy12) // 3))
                AcupointsPosition[1][1][18] = (int((cx26 + cx28) // 2), int((cy28 * 2 + cy26 * 3) // 5))

# acupointName为Name数组中的穴位名，LorR=0时查找左侧穴位，LorR=1时查找右侧穴位，返回的是穴位在图像上的坐标，和一个有标注的图像
def FindAcupoint(image, acupointName="", LorR=0):
    if acupointName in Name[0]:
        img = cv2ImgAddText(image, acupointName, AcupointsPosition[0][LorR][Name[LorR].index(acupointName)][0], AcupointsPosition[0][LorR][Name[LorR].index(acupointName)][1], (0, 0, 0), 20)
        cv.circle(img, AcupointsPosition[0][LorR][Name[LorR].index(acupointName)], 7, (255, 0, 255), cv.FILLED)
        return AcupointsPosition[0][LorR][Name[LorR].index(acupointName)], img

def Projection(u0, v0, fx, fy, u, v, z):
    pixel_coordinate = np.array([[u], [v], [1]])
    intrix_matrix = [[fx, 0, u0], [0, fy, v0], [0, 0, 1]]
    matrix = np.linalg.inv(intrix_matrix)
    x = z * (matrix[0][0] * u + matrix[0][2]) / 10
    y = z * (matrix[1][1] * v + matrix[1][2]) / 10
    return x, y, z / 10

def delta(x, y, z, dx, dy, dz):
    return x - dx, y - dy, z - dz

def pos_angle(x, y, z):
    theta_1 = math.atan2(x, z) * 180 / math.pi
    theta_2 = math.atan2(y, z) * 180 / math.pi
    return theta_1, theta_2

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

# 记录获得次数
k = 0

ser = serial.Serial('COM4', 9600, timeout=1)

#对获取的深度图像进行颜色处理
def color_depth_image(depth_image):
    # 实现将原图片转换为uint8类型
    depth_color_image = cv.convertScaleAbs(depth_image, alpha=0.05)
    # 赋予伪色彩
    depth_color_image = cv.applyColorMap(depth_color_image, cv.COLORMAP_JET)

    return depth_color_image

while (True):
    pyK4A.device_get_capture()  # Get capture

    depth_image_handle = pyK4A.capture_get_depth_image()
    color_image_handle = pyK4A.capture_get_color_image()

    if depth_image_handle and color_image_handle:
        color_image = pyK4A.image_convert_to_numpy(color_image_handle)[:, :, :3]
        depth_image = pyK4A.image_convert_to_numpy(depth_image_handle)
        depth_color_image = pyK4A.transform_depth_to_color(depth_image_handle, color_image_handle)

        MP(color_image)
        FindAcupoints()
        xy, image = FindAcupoint(color_image, "库房", 0)
        u, v = AcupointsPosition[i][j][k][0], AcupointsPosition[i][j][k][1]
        # if xy[0] < 720 and xy[1] < 1200:
        x, y, z = Projection(640.612671, 367.137726, 607.669800, 607.552429, u, v, depth_color_image[v][u])

        x = int(x)
        y = int(y)
        z = int(z)

        r = math.sqrt(x * x + y * y + z * z);
        theta = math.atan2(y, x) * (180 / math.pi);
        phi = math.acos(z / r) * (180 / math.pi);

        # print("x: " + str(x) + '   y: ' + str(y) + '   z: ' + str(z))

        # img = color_image.astype(np.uint8).copy()
        # if xy[0] < 720 and xy[1] < 1200:
        #     cv.circle(img, xy, 7, (255, 0, 255), cv.FILLED)

        # 生成x y z坐标，并用空格分隔
        coords = f"{r} {theta} {phi}\n"
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

        # cv.namedWindow(' Color Image', cv.WINDOW_NORMAL)
        # cv.imshow(' Color Image', img)
        # cv.namedWindow(' Depth Color Image', cv.WINDOW_NORMAL)
        # cv.imshow(' Depth Color Image', depth_color_image)
        k = cv.waitKey(25)
        if k == 27:  # Esc
            break
    k = k + 1
    pyK4A.image_release(depth_image_handle)
    pyK4A.image_release(color_image_handle)
    pyK4A.capture_release()

    k = cv.waitKey(25)
    if k == 27:  # Esc
        break

pyK4A.device_stop_cameras()
pyK4A.device_close()