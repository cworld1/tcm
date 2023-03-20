# cv库
import cv2 as cv

from store.data import meridians


def findMeridians(meridianName, AcupointsPosition, img):
    i = meridians.index(meridianName) - 1
    # image = cv.imread("../res/logo.png")
    image = img.copy()
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
    return image
    # cv.imshow("image", image)
    # cv.waitKey(10000)


# findMeridians("任脉穴")
