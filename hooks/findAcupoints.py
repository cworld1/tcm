# 各种标记
LH_Landmarks = []
RH_Landmarks = []
Pose_Landmarks = []
# 列表数据
global selectedAcupoints, selectedMeridians
from store.data import AcupointsPosition

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
                    int((cx13 + cx11) // 2),
                    int((cy13 + cy11) // 2),
                )
                AcupointsPosition[0][0][1] = (int(cx13), int(cy13))
                AcupointsPosition[0][0][2] = (
                    int((cx13 + cx15) // 2),
                    int((cy13 + cy15) // 2),
                )
                AcupointsPosition[0][0][3] = (
                    int((cx13 * 3 + cx15 * 7) // 10),
                    int((cy13 * 3 + cy15 * 7) // 10),
                )
                AcupointsPosition[0][0][4] = (
                    int((cx13 + cx15 * 4) // 5),
                    int((cy13 + cy15 * 4) // 5),
                )
                AcupointsPosition[0][0][5] = (int(cx15), int(cy15))
                AcupointsPosition[0][0][6] = (
                    int((cx14 + cx12) // 2),
                    int((cy14 + cy12) // 2),
                )
                AcupointsPosition[0][0][7] = (int(cx14), int(cy14))
                AcupointsPosition[0][0][8] = (
                    int((cx14 + cx16) // 2),
                    int((cy14 + cy16) // 2),
                )
                AcupointsPosition[0][0][9] = (
                    int((cx14 * 3 + cx16 * 7) // 10),
                    int((cy14 * 3 + cy16 * 7) // 10),
                )
                AcupointsPosition[0][0][10] = (
                    int((cx14 + cx16 * 4) // 5),
                    int((cy14 + cy16 * 4) // 5),
                )
                AcupointsPosition[0][0][11] = (int(cx16), int(cy16))

                AcupointsPosition[0][1][0] = (
                    int((cx11 + cx12) // 2),
                    int((cy11 + cy12) // 2),
                )
                AcupointsPosition[0][1][1] = (
                    int((cx11 + cx12) // 2),
                    int((cy11 * 17 + cy23) // 18),
                )
                AcupointsPosition[0][1][2] = (
                    int((cx11 + cx12) // 2),
                    int((cy11 * 16 + cy23 * 2) // 18),
                )
                AcupointsPosition[0][1][3] = (
                    int((cx11 + cx12) // 2),
                    int((cy11 * 15 + cy23 * 3) // 18),
                )
                AcupointsPosition[0][1][4] = (
                    int((cx11 + cx12) // 2),
                    int((cy11 * 14 + cy23 * 4) // 18),
                )
                AcupointsPosition[0][1][5] = (
                    int((cx11 + cx12) // 2),
                    int((cy11 * 13 + cy23 * 5) // 18),
                )
                AcupointsPosition[0][1][6] = (
                    int((cx11 + cx12) // 2),
                    int((cy11 * 12 + cy23 * 6) // 18),
                )
                AcupointsPosition[0][1][7] = (
                    int((cx11 + cx12) // 2),
                    int((cy11 * 11 + cy23 * 7) // 18),
                )
                AcupointsPosition[0][1][8] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 * 10 + cy23 * 8) // 18),
                )
                AcupointsPosition[0][1][9] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 * 9 + cy23 * 9) // 18),
                )
                AcupointsPosition[0][1][10] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 * 8 + cy23 * 10) // 18),
                )
                AcupointsPosition[0][1][11] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 * 7 + cy23 * 11) // 18),
                )
                AcupointsPosition[0][1][12] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 * 6 + cy23 * 12) // 18),
                )
                AcupointsPosition[0][1][13] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 * 5 + cy23 * 13) // 18),
                )
                AcupointsPosition[0][1][14] = (int(cx23), int((cy23 * 5 + cy11) // 6))
                AcupointsPosition[0][1][15] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 * 3 + cy23 * 15) // 18),
                )
                AcupointsPosition[0][1][16] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 * 2 + cy23 * 16) // 18),
                )
                AcupointsPosition[0][1][17] = (
                    int((cx23 + cx24) // 2),
                    int((cy11 + cy23 * 17) // 18),
                )
                AcupointsPosition[0][1][18] = (
                    int((cx23 + cx24) // 2),
                    int((cy23 + cy24) // 2),
                )

                AcupointsPosition[0][2][0] = (
                    int((cx11 * 2 + cx12) // 3),
                    int((cy11 * 2 + cy12) // 3),
                )
                AcupointsPosition[0][2][1] = (
                    int((cx11 * 2 + cx12) // 3),
                    int((cy11 * 15 + cy23) // 16),
                )
                AcupointsPosition[0][2][2] = (
                    int((cx11 * 2 + cx12) // 3),
                    int((cy11 * 14 + cy23 * 2) // 16),
                )
                AcupointsPosition[0][2][3] = (
                    int((cx11 * 2 + cx12) // 3),
                    int((cy11 * 13 + cy23 * 3) // 16),
                )
                AcupointsPosition[0][2][4] = (
                    int((cx11 * 2 + cx12) // 3),
                    int((cy11 * 12 + cy23 * 4) // 16),
                )
                AcupointsPosition[0][2][5] = (
                    int((cx11 * 2 + cx12) // 3),
                    int((cy11 * 11 + cy23 * 5) // 16),
                )
                AcupointsPosition[0][2][6] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 10 + cy23 * 6) // 16),
                )
                AcupointsPosition[0][2][7] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 9 + cy23 * 7) // 16),
                )
                AcupointsPosition[0][2][8] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 8 + cy23 * 8) // 16),
                )
                AcupointsPosition[0][2][9] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 7 + cy23 * 9) // 16),
                )
                AcupointsPosition[0][2][10] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 6 + cy23 * 10) // 16),
                )
                AcupointsPosition[0][2][11] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 5 + cy23 * 11) // 16),
                )
                AcupointsPosition[0][2][12] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 4 + cy23 * 12) // 16),
                )
                AcupointsPosition[0][2][13] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 3 + cy23 * 13) // 16),
                )
                AcupointsPosition[0][2][14] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 2 + cy23 * 14) // 16),
                )
                AcupointsPosition[0][2][15] = (
                    int((cx23 * 3 + cx24) // 4),
                    int((cy11 * 1 + cy23 * 15) // 16),
                )
                AcupointsPosition[0][2][16] = (int((cx23 * 3 + cx24) // 4), int(cy23))
                AcupointsPosition[0][2][17] = (
                    int((cx23 + cx25) // 2),
                    int((cy23 * 4 + cy25) // 5),
                )
                AcupointsPosition[0][2][18] = (
                    int((cx23 + cx25) // 2),
                    int((cy23 * 2 + cy25 * 3) // 5),
                )
                AcupointsPosition[0][2][19] = (
                    int((cx23 + cx25) // 2),
                    int((cy23 + cy25 * 3) // 4),
                )
                AcupointsPosition[0][2][20] = (
                    int((cx23 + cx25) // 2),
                    int((cy23 + cy25 * 4) // 5),
                )
                AcupointsPosition[0][2][21] = (int(cx25), int(cy25))
                AcupointsPosition[0][2][22] = (
                    int((cx25 + cx27) // 2),
                    int((cy25 * 5 + cy27) // 6),
                )
                AcupointsPosition[0][2][23] = (
                    int((cx25 + cx27) // 2),
                    int((cy25 * 4 + cy27 * 2) // 6),
                )
                AcupointsPosition[0][2][24] = (
                    int((cx25 + cx27) // 2),
                    int((cy25 + cy27) // 2),
                )
                AcupointsPosition[0][2][25] = (int(cx27), int(cy27))

                AcupointsPosition[0][2][26] = (
                    int((cx12 * 2 + cx11) // 3),
                    int((cy12 * 2 + cy11) // 3),
                )
                AcupointsPosition[0][2][27] = (
                    int((cx12 * 2 + cx11) // 3),
                    int((cy12 * 15 + cy24) // 16),
                )
                AcupointsPosition[0][2][28] = (
                    int((cx12 * 2 + cx11) // 3),
                    int((cy12 * 14 + cy24 * 2) // 16),
                )
                AcupointsPosition[0][2][29] = (
                    int((cx12 * 2 + cx11) // 3),
                    int((cy12 * 13 + cy24 * 3) // 16),
                )
                AcupointsPosition[0][2][30] = (
                    int((cx12 * 2 + cx11) // 3),
                    int((cy12 * 12 + cy24 * 4) // 16),
                )
                AcupointsPosition[0][2][31] = (
                    int((cx12 * 2 + cx11) // 3),
                    int((cy12 * 11 + cy24 * 5) // 16),
                )
                AcupointsPosition[0][2][32] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 10 + cy24 * 6) // 16),
                )
                AcupointsPosition[0][2][33] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 9 + cy24 * 7) // 16),
                )
                AcupointsPosition[0][2][34] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 8 + cy24 * 8) // 16),
                )
                AcupointsPosition[0][2][35] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 7 + cy24 * 9) // 16),
                )
                AcupointsPosition[0][2][36] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 6 + cy24 * 10) // 16),
                )
                AcupointsPosition[0][2][37] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 5 + cy24 * 11) // 16),
                )
                AcupointsPosition[0][2][38] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 4 + cy24 * 12) // 16),
                )
                AcupointsPosition[0][2][39] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 3 + cy24 * 13) // 16),
                )
                AcupointsPosition[0][2][40] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 2 + cy24 * 14) // 16),
                )
                AcupointsPosition[0][2][41] = (
                    int((cx24 * 3 + cx23) // 4),
                    int((cy12 * 1 + cy24 * 15) // 16),
                )
                AcupointsPosition[0][2][42] = (int((cx24 * 3 + cx23) // 4), int(cy24))
                AcupointsPosition[0][2][43] = (
                    int((cx24 + cx26) // 2),
                    int((cy24 * 4 + cy26) // 5),
                )
                AcupointsPosition[0][2][44] = (
                    int((cx24 + cx26) // 2),
                    int((cy24 * 2 + cy26 * 3) // 5),
                )
                AcupointsPosition[0][2][45] = (
                    int((cx24 + cx26) // 2),
                    int((cy24 + cy26 * 3) // 4),
                )
                AcupointsPosition[0][2][46] = (
                    int((cx24 + cx26) // 2),
                    int((cy24 + cy26 * 4) // 5),
                )
                AcupointsPosition[0][2][47] = (int(cx26), int(cy26))
                AcupointsPosition[0][2][48] = (
                    int((cx26 + cx28) // 2),
                    int((cy26 * 5 + cy28) // 6),
                )
                AcupointsPosition[0][2][49] = (
                    int((cx26 + cx28) // 2),
                    int((cy26 * 4 + cy28 * 2) // 6),
                )
                AcupointsPosition[0][2][50] = (
                    int((cx26 + cx28) // 2),
                    int((cy26 + cy28) // 2),
                )
                AcupointsPosition[0][2][51] = (int(cx28), int(cy28))

            else:
                AcupointsPosition[1][0][0] = (int(cx11), int(cy11))
                AcupointsPosition[1][0][1] = (
                    int((cx13 + cx11 * 2) // 3),
                    int((cy13 + cy11 * 2) // 3),
                )
                AcupointsPosition[1][0][2] = (
                    int((cx13 * 2 + cx11) // 3),
                    int((cy13 * 2 + cy11) // 3),
                )
                AcupointsPosition[1][0][3] = (int(cx13), int(cy13))
                AcupointsPosition[1][0][4] = (
                    int((cx13 + cx15) // 2),
                    int((cy13 + cy15) // 2),
                )
                AcupointsPosition[1][0][5] = (
                    int((cx13 + cx15 * 2) // 3),
                    int((cy13 + cy15 * 2) // 3),
                )
                AcupointsPosition[1][0][6] = (
                    int((cx13 + cx15 * 3) // 4),
                    int((cy13 + cy15 * 3) // 4),
                )
                AcupointsPosition[1][0][7] = (
                    int((cx13 * 2 + cx15) // 3),
                    int((cy13 * 2 + cy15) // 3),
                )
                AcupointsPosition[1][0][8] = (int(cx15), int(cy15))
                AcupointsPosition[1][0][9] = (int(cx12), int(cy12))
                AcupointsPosition[1][0][10] = (
                    int((cx14 + cx12 * 2) // 3),
                    int((cy14 + cy12 * 2) // 3),
                )
                AcupointsPosition[1][0][11] = (
                    int((cx14 * 2 + cx12) // 3),
                    int((cy14 * 2 + cy12) // 3),
                )
                AcupointsPosition[1][0][12] = (int(cx14), int(cy14))
                AcupointsPosition[1][0][13] = (
                    int((cx14 + cx16) // 2),
                    int((cy14 + cy16) // 2),
                )
                AcupointsPosition[1][0][14] = (
                    int((cx14 + cx16 * 2) // 3),
                    int((cy14 + cy16 * 2) // 3),
                )
                AcupointsPosition[1][0][15] = (
                    int((cx14 + cx16 * 3) // 4),
                    int((cy14 + cy16 * 3) // 4),
                )
                AcupointsPosition[1][0][16] = (
                    int((cx14 * 2 + cx16) // 3),
                    int((cy14 * 2 + cy16) // 3),
                )
                AcupointsPosition[1][0][17] = (int(cx16), int(cy16))

                AcupointsPosition[1][1][0] = (int(cx23), int(cy11))
                AcupointsPosition[1][1][1] = (int(cx23), int((cy23 + cy11 * 17) // 18))
                AcupointsPosition[1][1][2] = (
                    int(cx23),
                    int((cy23 * 2 + cy11 * 16) // 18),
                )
                AcupointsPosition[1][1][3] = (
                    int(cx23),
                    int((cy23 * 3 + cy11 * 15) // 18),
                )
                AcupointsPosition[1][1][4] = (
                    int(cx23),
                    int((cy23 * 4 + cy11 * 14) // 18),
                )
                AcupointsPosition[1][1][5] = (
                    int(cx23),
                    int((cy23 * 5 + cy11 * 13) // 18),
                )
                AcupointsPosition[1][1][6] = (
                    int(cx23),
                    int((cy23 * 7 + cy11 * 11) // 18),
                )
                AcupointsPosition[1][1][7] = (
                    int(cx23),
                    int((cy23 * 9 + cy11 * 9) // 18),
                )
                AcupointsPosition[1][1][8] = (
                    int(cx23),
                    int((cy23 * 10 + cy11 * 8) // 18),
                )
                AcupointsPosition[1][1][9] = (
                    int(cx23),
                    int((cy23 * 11 + cy11 * 7) // 18),
                )
                AcupointsPosition[1][1][10] = (
                    int(cx23),
                    int((cy23 * 12 + cy11 * 6) // 18),
                )
                AcupointsPosition[1][1][11] = (
                    int(cx23),
                    int((cy23 * 16 + cy11 * 2) // 18),
                )
                AcupointsPosition[1][1][12] = (int(cx23), int(cy23))
                AcupointsPosition[1][1][13] = (
                    int((cx23 * 2 + cx25) // 3),
                    int((cy23 * 2 + cy25) // 3),
                )
                AcupointsPosition[1][1][14] = (
                    int((cx23 + cx25 * 2) // 3),
                    int((cy23 + cy25 * 2) // 3),
                )
                AcupointsPosition[1][1][15] = (int(cx25), int(cy25))
                AcupointsPosition[1][1][16] = (
                    int((cx25 + cx27) // 2),
                    int((cy27 + cy25 * 9) // 10),
                )
                AcupointsPosition[1][1][17] = (
                    int((cx25 + cx27) // 2),
                    int((cy27 * 3 + cy25 * 7) // 10),
                )
                AcupointsPosition[1][1][18] = (
                    int((cx25 + cx27) // 2),
                    int((cy27 + cy25) // 2),
                )
                AcupointsPosition[1][1][19] = (
                    int((cx25 + cx27) // 2),
                    int((cy27 * 8 + cy25 * 2) // 10),
                )
                AcupointsPosition[1][1][20] = (int(cx27), int(cy27))
                AcupointsPosition[1][1][21] = (int(cx24), int(cy12))
                AcupointsPosition[1][1][22] = (int(cx24), int((cy24 + cy12 * 17) // 18))
                AcupointsPosition[1][1][23] = (
                    int(cx24),
                    int((cy24 * 2 + cy12 * 16) // 18),
                )
                AcupointsPosition[1][1][24] = (
                    int(cx24),
                    int((cy24 * 3 + cy12 * 15) // 18),
                )
                AcupointsPosition[1][1][25] = (
                    int(cx24),
                    int((cy24 * 4 + cy12 * 14) // 18),
                )
                AcupointsPosition[1][1][26] = (
                    int(cx24),
                    int((cy24 * 5 + cy12 * 13) // 18),
                )
                AcupointsPosition[1][1][27] = (
                    int(cx24),
                    int((cy24 * 7 + cy12 * 11) // 18),
                )
                AcupointsPosition[1][1][28] = (
                    int(cx24),
                    int((cy24 * 9 + cy12 * 9) // 18),
                )
                AcupointsPosition[1][1][29] = (
                    int(cx24),
                    int((cy24 * 10 + cy12 * 8) // 18),
                )
                AcupointsPosition[1][1][30] = (
                    int(cx24),
                    int((cy24 * 11 + cy12 * 7) // 18),
                )
                AcupointsPosition[1][1][31] = (
                    int(cx24),
                    int((cy24 * 12 + cy12 * 6) // 18),
                )
                AcupointsPosition[1][1][32] = (
                    int(cx24),
                    int((cy24 * 16 + cy12 * 2) // 18),
                )
                AcupointsPosition[1][1][33] = (int(cx24), int(cy24))
                AcupointsPosition[1][1][34] = (
                    int((cx24 * 2 + cx26) // 3),
                    int((cy24 * 2 + cy26) // 3),
                )
                AcupointsPosition[1][1][35] = (
                    int((cx24 + cx26 * 2) // 3),
                    int((cy24 + cy26 * 2) // 3),
                )
                AcupointsPosition[1][1][36] = (int(cx26), int(cy26))
                AcupointsPosition[1][1][37] = (
                    int((cx26 + cx28) // 2),
                    int((cy28 + cy26 * 9) // 10),
                )
                AcupointsPosition[1][1][38] = (
                    int((cx26 + cx28) // 2),
                    int((cy28 * 3 + cy26 * 7) // 10),
                )
                AcupointsPosition[1][1][39] = (
                    int((cx26 + cx28) // 2),
                    int((cy28 + cy26) // 2),
                )
                AcupointsPosition[1][1][40] = (
                    int((cx26 + cx28) // 2),
                    int((cy28 * 8 + cy26 * 2) // 10),
                )
                AcupointsPosition[1][1][41] = (int(cx28), int(cy28))

