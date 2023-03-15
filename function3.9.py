import cv2 as cv
import numpy as np
import mediapipe as mp
from PoseModule import PoseDetector
from HandTrackingModule import HandDetector
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
# import tqdm
import time
meridians = ["1", "2", "3", "4", "5"]
# [0/1][1-5][1-20]
Name = [[["天泉（左）", "曲泽（左）", "郄门（左）", "间使（左）", "内关（左）", "大陵（左）", "天泉（右）", "曲泽（右）", "郄门（右）",
          "间使（右）", "内关（右）", "大陵（右）"],
         ["璇玑", "华盖", "紫宫", "玉堂", "膻中", "中庭", "鸠尾", "巨阙", "上脘", "中脘", "建里", "下脘", "水分",
          "神阙", "阴交", "气海", "石门", "关元", "中极"],
         ["气户(左)", "库房(左)", "屋翳(左)", "鹰窗(左)", "乳中(左)", "乳根(左)", "不容(左)", "承满(左)", "梁门(左)",
          "关门(左)", "太乙(左)", "滑肉门(左)", "太枢(左)", "外陵(左)", "大巨(左)", "水道(左)", "归来(左)", "髀关(左)",
          "伏兔(左)", "阴市(左)", "梁丘(左)", "犊鼻(左)", "足三里(左)", "上巨虚(左)", "下巨虚(左)", "解溪(左)",
          "气户(右)", "库房(右)", "屋翳(右)", "鹰窗(右)", "乳中(右)", "乳根(右)", "不容(右)", "承满(右)", "梁门(右)",
          "关门(右)", "太乙(右)", "滑肉门(右)", "太枢(右)", "外陵(右)", "大巨(右)", "水道(右)", "归来(右)", "髀关(右)",
          "伏兔(右)", "阴市(右)", "梁丘(右)", "犊鼻(右)", "足三里(右)", "上巨虚(右)", "下巨虚(右)", "解溪(右)"]],
        [["肩髎(左)", "臑会(左)", "消泺(左)","天井(左)",  "四渎(左)", "三阳络(左)", "支沟(左)", "外关(左)", "阳池(左)",
          "肩髎(右)", "臑会(右)", "消泺(右)","天井(右)",  "四渎(右)", "三阳络(右)", "支沟(右)", "外关(右)", "阳池(右)"],
         ["附分(左)", "魄户(左)", "膏肓(左)", "神堂(左)", "譩譆(左)", "隔关(左)", "魂门(左)", "意舍(左)", "胃仓(左)",
          "盲门(左)", "志室(左)", "胞肓(左)", "秩边(左)", "承扶殷门(左)", "委中(左)", "合阳(左)", "承筋(左)",
          "承山(左)", "跗阳(左)", "昆仑(左)", "附分(右)", "魄户(右)", "膏肓(右)", "神堂(右)", "譩譆(右)", "隔关(右)",
          "魂门(右)", "意舍(右)", "胃仓(右)", "盲门(右)", "志室(右)", "胞肓(右)", "秩边(右)", "承扶殷门(右)",
          "委中(右)", "合阳(右)", "承筋(右)", "承山(右)", "跗阳(右)", "昆仑(右)"]]]
# [0/1][1-5][1-20]
AcupointsPosition = [[[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                       (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                      [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                       (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]],
                     [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                       (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                      [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                       (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]]]

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
                AcupointsPosition[0][0][0] = (int((cx13 + cx11) // 2), int((cy13 + cy11) // 2))
                AcupointsPosition[0][0][1] = (int(cx13), int(cy13))
                AcupointsPosition[0][0][2] = (int((cx13 + cx15) // 2), int((cy13 + cy15) // 2))
                AcupointsPosition[0][0][3] = (int((cx13*3 + cx15*7) // 10), int((cy13*3+cy15*7) // 10))
                AcupointsPosition[0][0][4] = (int((cx13 + cx15 * 4) // 5), int((cy13 + cy15 *4) //5))
                AcupointsPosition[0][0][5] = (int(cx15), int(cy15))

                AcupointsPosition[0][0][6] = (int((cx14 + cx12) // 2), int((cy14 + cy12) // 2))
                AcupointsPosition[0][0][7] = (int(cx14), int(cy14))
                AcupointsPosition[0][0][8] = (int((cx14 + cx16) // 2), int((cy14 + cy16) // 2))
                AcupointsPosition[0][0][9] = (int((cx14 * 3 + cx16 * 7) // 10), int((cy14 * 3 + cy16 * 7) // 10))
                AcupointsPosition[0][0][10] = (int((cx14 + cx16 * 4) // 5), int((cy14 + cy16 * 4) // 5))
                AcupointsPosition[0][0][11] = (int(cx16), int(cy16))

                AcupointsPosition[0][1][0] = (int((cx11 + cx12) // 2), int((cy11 + cy12) // 2))
                AcupointsPosition[0][1][1] = (int((cx11 + cx12) // 2), int((cy11*17+ cy23) //18))
                AcupointsPosition[0][1][2] = (int((cx11 + cx12) // 2), int((cy11 * 16 + cy23*2) // 18))
                AcupointsPosition[0][1][3] = (int((cx11 + cx12) // 2), int((cy11 * 15 + cy23 * 3) // 18))
                AcupointsPosition[0][1][4] = (int((cx11 + cx12) // 2), int((cy11 * 14 + cy23 * 4) // 18))
                AcupointsPosition[0][1][5] = (int((cx11 + cx12) // 2), int((cy11 * 13 + cy23 * 5) // 18))
                AcupointsPosition[0][1][6] = (int((cx11 + cx12) // 2), int((cy11 * 12 + cy23 * 6) // 18))
                AcupointsPosition[0][1][7] = (int((cx11 + cx12) // 2), int((cy11 * 11 + cy23 * 7) // 18))
                AcupointsPosition[0][1][8] = (int((cx23 + cx24) // 2), int((cy11 * 10 + cy23 * 8) // 18))
                AcupointsPosition[0][1][9] = (int((cx23 + cx24) // 2), int((cy11 * 9 + cy23 * 9) // 18))
                AcupointsPosition[0][1][10] = (int((cx23 + cx24) // 2), int((cy11 * 8 + cy23 * 10) // 18))
                AcupointsPosition[0][1][11] = (int((cx23 + cx24) // 2), int((cy11 *7 + cy23 * 11) // 18))
                AcupointsPosition[0][1][12] = (int((cx23 + cx24) // 2), int((cy11 * 6 + cy23 * 12) // 18))
                AcupointsPosition[0][1][13] = (int((cx23 + cx24) // 2), int((cy11 * 5 + cy23 *13) // 18))
                AcupointsPosition[0][1][14] = (int(cx23), int((cy23 * 5 + cy11) // 6))
                AcupointsPosition[0][1][15] = (int((cx23 + cx24) // 2), int((cy11 * 3 + cy23 *15) // 18))
                AcupointsPosition[0][1][16] = (int((cx23 + cx24) // 2), int((cy11 *2 + cy23 * 16) // 18))
                AcupointsPosition[0][1][17] = (int((cx23 + cx24) // 2), int((cy11 + cy23 *17) // 18))
                AcupointsPosition[0][1][18] = (int((cx23 + cx24) // 2), int((cy23 + cy24) // 2))

                AcupointsPosition[0][2][0] = (int( (cx11*2 + cx12) // 3), int((cy11 * 2 + cy12) // 3))
                AcupointsPosition[0][2][1] = (int((cx11 * 2 + cx12) // 3), int((cy11 * 15 + cy23) // 16))
                AcupointsPosition[0][2][2] = (int((cx11 * 2 + cx12) // 3), int((cy11 * 14 + cy23*2) //16))
                AcupointsPosition[0][2][3] = (int((cx11 * 2 + cx12) // 3), int((cy11 * 13 + cy23*3) //16))
                AcupointsPosition[0][2][4] = (int((cx11 * 2 + cx12) // 3), int((cy11 * 12 + cy23 *4) // 16))
                AcupointsPosition[0][2][5] = (int((cx11 * 2 + cx12) // 3), int((cy11 * 11 + cy23 * 5) // 16))
                AcupointsPosition[0][2][6] = (int((cx23 *3 + cx24) // 4), int((cy11 * 10 + cy23 * 6) // 16))
                AcupointsPosition[0][2][7] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 9 + cy23 * 7) // 16))
                AcupointsPosition[0][2][8] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 8 + cy23 * 8) // 16))
                AcupointsPosition[0][2][9] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 7 + cy23 * 9) // 16))
                AcupointsPosition[0][2][10] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 6 + cy23 * 10) // 16))
                AcupointsPosition[0][2][11] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 5 + cy23 * 11) // 16))
                AcupointsPosition[0][2][12] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 4 + cy23 * 12) // 16))
                AcupointsPosition[0][2][13] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 3 + cy23 * 13) // 16))
                AcupointsPosition[0][2][14] = (int((cx23 * 3 + cx24) // 4), int((cy11 * 2 + cy23 * 14) // 16))
                AcupointsPosition[0][2][15] = (int((cx23 * 3 + cx24) // 4), int((cy11 *1 + cy23 * 15) // 16))
                AcupointsPosition[0][2][16] = (int((cx23 * 3 + cx24) // 4), int(cy23))
                AcupointsPosition[0][2][17] = (int((cx23 + cx25) // 2), int((cy23*4+ cy25) //5))
                AcupointsPosition[0][2][18] = (int((cx23 + cx25) // 2), int((cy23*2+ cy25*3) //5))
                AcupointsPosition[0][2][19] = (int((cx23 + cx25) // 2), int((cy23 + cy25 * 3) //4))
                AcupointsPosition[0][2][20] = (int((cx23 + cx25) // 2), int((cy23 + cy25 * 4) // 5))
                AcupointsPosition[0][2][21] = (int(cx25 ), int(cy25))
                AcupointsPosition[0][2][22] = (int((cx25 + cx27) // 2), int((cy25*5 + cy27) // 6))
                AcupointsPosition[0][2][23] = (int((cx25 + cx27) // 2), int((cy25 * 4 + cy27*2) // 6))
                AcupointsPosition[0][2][24] = (int((cx25 + cx27) // 2), int((cy25+ cy27) // 2))
                AcupointsPosition[0][2][25] = (int(cx27), int(cy27))

                AcupointsPosition[0][2][26] = (int((cx12 * 2 + cx11) // 3), int((cy12 * 2 + cy11) // 3))
                AcupointsPosition[0][2][27] = (int((cx12 * 2 + cx11) // 3), int((cy12 * 15 + cy24) // 16))
                AcupointsPosition[0][2][28] = (int((cx12 * 2 + cx11) // 3), int((cy12 * 14 + cy24 * 2) // 16))
                AcupointsPosition[0][2][29] = (int((cx12 * 2 + cx11) // 3), int((cy12 * 13 + cy24 * 3) // 16))
                AcupointsPosition[0][2][30] = (int((cx12 * 2 + cx11) // 3), int((cy12 * 12 + cy24 * 4) // 16))
                AcupointsPosition[0][2][31] = (int((cx12 * 2 + cx11) // 3), int((cy12 * 11 + cy24 * 5) // 16))
                AcupointsPosition[0][2][32] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 10 + cy24 * 6) // 16))
                AcupointsPosition[0][2][33] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 9 + cy24 * 7) // 16))
                AcupointsPosition[0][2][34] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 8 + cy24 * 8) // 16))
                AcupointsPosition[0][2][35] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 7 + cy24 * 9) // 16))
                AcupointsPosition[0][2][36] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 6 + cy24 * 10) // 16))
                AcupointsPosition[0][2][37] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 5 + cy24 * 11) // 16))
                AcupointsPosition[0][2][38] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 4 + cy24 * 12) // 16))
                AcupointsPosition[0][2][39] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 3 + cy24 * 13) // 16))
                AcupointsPosition[0][2][40] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 2 + cy24 * 14) // 16))
                AcupointsPosition[0][2][41] = (int((cx24 * 3 + cx23) // 4), int((cy12 * 1 + cy24 * 15) // 16))
                AcupointsPosition[0][2][42] = (int((cx24 * 3 + cx23) // 4), int(cy24))
                AcupointsPosition[0][2][43] = (int((cx24 + cx26) // 2), int((cy24 * 4 + cy26) // 5))
                AcupointsPosition[0][2][44] = (int((cx24 + cx26) // 2), int((cy24 * 2 + cy26 * 3) // 5))
                AcupointsPosition[0][2][45] = (int((cx24 + cx26) // 2), int((cy24 + cy26 * 3) // 4))
                AcupointsPosition[0][2][46] = (int((cx24 + cx26) // 2), int((cy24 + cy26 * 4) // 5))
                AcupointsPosition[0][2][47] = (int(cx26), int(cy26))
                AcupointsPosition[0][2][48] = (int((cx26 + cx28) // 2), int((cy26 * 5 + cy28) // 6))
                AcupointsPosition[0][2][49] = (int((cx26 + cx28) // 2), int((cy26 * 4 + cy28 * 2) // 6))
                AcupointsPosition[0][2][50] = (int((cx26 + cx28) // 2), int((cy26 + cy28) // 2))
                AcupointsPosition[0][2][51] = (int(cx28), int(cy28))



            else:
                AcupointsPosition[1][0][0] = (int(cx11), int(cy11))
                AcupointsPosition[1][0][1] = (int((cx13 + cx11 * 2) // 3), int((cy13 + cy11 * 2) // 3))
                AcupointsPosition[1][0][2] = (int((cx13 * 2 + cx11) // 3), int((cy13 * 2 + cy11) // 3))
                AcupointsPosition[1][0][3] = (int(cx13), int(cy13))
                AcupointsPosition[1][0][4] = (int((cx13 + cx15) //2), int((cy13 + cy15) // 2))
                AcupointsPosition[1][0][5] = (int((cx13 + cx15*2) // 3), int((cy13 + cy15*2) // 3))
                AcupointsPosition[1][0][6] = (int((cx13 + cx15*3) // 4), int((cy13 + cy15*3) // 4))
                AcupointsPosition[1][0][7] = (int((cx13*2 + cx15) // 3), int((cy13*2 + cy15) // 3))
                AcupointsPosition[1][0][8] = (int(cx15), int(cy15))

                AcupointsPosition[1][0][9] = (int(cx12), int(cy12))
                AcupointsPosition[1][0][10] = (int((cx14 + cx12 * 2) // 3), int((cy14 + cy12* 2) // 3))
                AcupointsPosition[1][0][11] = (int((cx14 * 2 + cx12) // 3), int((cy14 * 2 + cy12) // 3))
                AcupointsPosition[1][0][12] = (int(cx14), int(cy14))
                AcupointsPosition[1][0][13] = (int((cx14+ cx16) // 2), int((cy14 + cy16) // 2))
                AcupointsPosition[1][0][14] = (int((cx14 + cx16 * 2) // 3), int((cy14 + cy16 * 2) // 3))
                AcupointsPosition[1][0][15] = (int((cx14 + cx16 * 3) // 4), int((cy14 + cy16 * 3) // 4))
                AcupointsPosition[1][0][16] = (int((cx14 * 2 + cx16) // 3), int((cy14 * 2 + cy16) // 3))
                AcupointsPosition[1][0][17] = (int(cx16), int(cy16))

                AcupointsPosition[1][1][0] = (int(cx23), int(cy11))
                AcupointsPosition[1][1][1] = (int(cx23), int((cy23 + cy11*17) // 18))
                AcupointsPosition[1][1][2] = (int(cx23), int((cy23*2 + cy11 * 16) // 18))
                AcupointsPosition[1][1][3] = (int(cx23), int((cy23 * 3 + cy11 * 15) // 18))
                AcupointsPosition[1][1][4] = (int(cx23), int((cy23*4 + cy11 * 14) // 18))
                AcupointsPosition[1][1][5] = (int(cx23), int((cy23*5+cy11*13)//18))
                AcupointsPosition[1][1][6] = (int(cx23), int((cy23 * 7 + cy11 * 11) // 18))
                AcupointsPosition[1][1][7] = (int(cx23), int((cy23 *9 + cy11*9) // 18))
                AcupointsPosition[1][1][8] = (int(cx23), int((cy23 * 10 + cy11 * 8) // 18))
                AcupointsPosition[1][1][9] = (int(cx23), int((cy23 * 11 + cy11 * 7) // 18))
                AcupointsPosition[1][1][10] = (int(cx23), int((cy23 * 12 + cy11 * 6) // 18))
                AcupointsPosition[1][1][11] = (int(cx23), int((cy23 * 16 + cy11 * 2) // 18))
                AcupointsPosition[1][1][12] = (int(cx23), int(cy23))
                AcupointsPosition[1][1][13] = (int((cx23*2+cx25)//3), int((cy23*2+cy25)//3))
                AcupointsPosition[1][1][14] = (int((cx23 + cx25*2) // 3), int((cy23 + cy25*2) // 3))
                AcupointsPosition[1][1][15] = (int(cx25), int(cy25))
                AcupointsPosition[1][1][16] = (int((cx25 + cx27) //2), int((cy27 + cy25 * 9) //10))
                AcupointsPosition[1][1][17] = (int((cx25 + cx27) // 2), int((cy27*3 + cy25 *7) //10))
                AcupointsPosition[1][1][18] = (int((cx25 + cx27) // 2), int((cy27 + cy25 ) // 2))
                AcupointsPosition[1][1][19] = (int((cx25 + cx27) // 2), int((cy27 + cy25) // 2))
                AcupointsPosition[1][1][20] = (int(cx27), int(cy27))
                AcupointsPosition[1][1][21] = (int(cx23), int((cy23 * 16 + cy11*2) // 18))
                AcupointsPosition[1][1][22] = (int(cx24), int(cy12))
                AcupointsPosition[1][1][23] = (int(cx24), int((cy24 + cy12 * 17) // 18))
                AcupointsPosition[1][1][24] = (int(cx24), int((cy24 * 2 + cy12 * 16) // 18))
                AcupointsPosition[1][1][25] = (int(cx24), int((cy24 * 3 + cy12 * 15) // 18))
                AcupointsPosition[1][1][26] = (int(cx24), int((cy24 * 4 + cy12 * 14) // 18))
                AcupointsPosition[1][1][27] = (int(cx24), int((cy24 * 5 + cy12*13) // 18))
                AcupointsPosition[1][1][28] = (int(cx24), int((cy24 * 7 + cy12 * 11) // 18))
                AcupointsPosition[1][1][29] = (int(cx24), int((cy24 * 9 + cy12 * 9) // 18))
                AcupointsPosition[1][1][30] = (int(cx24), int((cy24 * 10 + cy12 * 8) // 18))
                AcupointsPosition[1][1][31] = (int(cx24), int((cy24 * 11 + cy12 * 7) // 18))
                AcupointsPosition[1][1][32] = (int(cx24), int((cy24 * 12 + cy12 * 6) // 18))
                AcupointsPosition[1][1][33] = (int(cx24), int((cy24 * 16 + cy12 * 2) // 18))
                AcupointsPosition[1][1][34] = (int(cx24), int(cy24))
                AcupointsPosition[1][1][35] = (int((cx24 * 2 + cx26) // 3), int((cy24 * 2 + cy26) // 3))
                AcupointsPosition[1][1][36] = (int((cx24 + cx26 * 2) // 3), int((cy24 + cy26 * 2) // 3))
                AcupointsPosition[1][1][37] = (int(cx26), int(cy26))
                AcupointsPosition[1][1][38] = (int((cx26 + cx28) // 2), int((cy28 + cy26 * 9) // 10))
                AcupointsPosition[1][1][39] = (int((cx26 + cx28) // 2), int((cy28 * 3 + cy26 * 7) // 10))
                AcupointsPosition[1][1][40] = (int((cx26 + cx28) // 2), int((cy28 + cy26) // 2))
                AcupointsPosition[1][1][41] = (int((cx26 + cx28) // 2), int((cy28 + cy26) // 2))
                AcupointsPosition[1][1][42] = (int(cx28), int(cy28))

# acupointName为Name数组中的穴位名，LorR=0时查找左侧穴位，LorR=1时查找右侧穴位，返回的是穴位在图像上的坐标，和一个有标注的图像
def FindAcupoint(image, acupointName="", LorR=0):
    if acupointName in Name[0]:
        img = cv2ImgAddText(image, acupointName, AcupointsPosition[0][LorR][Name.index(acupointName)][0], AcupointsPosition[0][LorR][Name.index(acupointName)][1], (0, 0, 0), 20)
        cv.circle(img, AcupointsPosition[0][LorR][Name.index(acupointName)], 7, (255, 0, 255), cv.FILLED)
        return AcupointsPosition[0][LorR][Name.index(acupointName)], img



cap = cv.VideoCapture(0)

success, img = cap.read()
h, w, _ = img.shape

while cap.isOpened():  # 获取图像
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    MP(image)
    FindAcupoints()
    (x, y), img = FindAcupoint(image, "尺泽", 0)

    if cv.waitKey(1) & 0xFF == 27:
        break
cap.release()
