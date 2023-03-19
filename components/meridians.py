# cv库
import cv2 as cv

from store.data import merideans, acupoints, Name, AcupointIsShow, sampleAcupoints


def Find_meridians(meridianName):
    i = merideans.index(meridianName)
    image = cv.imread("../res/logo.png")
    AcupointsPosition = sampleAcupoints
    if i <= 2:
        if i == 1:
            for j in range(len(AcupointsPosition[0][i]) - 1):
                image = cv.line(
                    image,
                    AcupointsPosition[0][i][j],
                    AcupointsPosition[0][i][j + 1],
                    color=(255, 0, 3),
                    thickness=2,
                )
        else:
            for j in range((len(AcupointsPosition[0][i]) - 2) / 2):
                image = cv.line(
                    image,
                    AcupointsPosition[0][i][j],
                    AcupointsPosition[0][i][j + 1],
                    color=(255, 0, 3),
                    thickness=2,
                )
                image = cv.line(
                    image,
                    AcupointsPosition[0][i][j + len(AcupointsPosition[0][i])],
                    AcupointsPosition[0][i][j + 1 + len(AcupointsPosition[0][i])],
                    color=(255, 0, 3),
                    thickness=2,
                )
    else:
        for j in range((len(AcupointsPosition[0][i]) - 2) / 2):
            image = cv.line(
                image,
                AcupointsPosition[1][i][j],
                AcupointsPosition[1][i][j + 1],
                color=(255, 0, 3),
                thickness=2,
            )
            image = cv.line(
                image,
                AcupointsPosition[1][i][j + len(AcupointsPosition[1][i])],
                AcupointsPosition[1][i][j + 1 + len(AcupointsPosition[1][i])],
                color=(255, 0, 3),
                thickness=2,
            )

    cv.imshow("image", image)
    cv.waitKey(10000)


Find_meridians("任脉穴")
