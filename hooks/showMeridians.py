# cv库
import cv2 as cv

from store.data import meridians


def findMeridians(meridianName, AcupointsPosition, image):
    i = meridians.index(meridianName)
    # image = cv.imread("../res/logo.jpg")
    image = image.copy()
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
            for j in range(int((len(AcupointsPosition[0][i])) / 2) - 1):
                image = cv.line(
                    image,
                    AcupointsPosition[0][i][j],
                    AcupointsPosition[0][i][j + 1],
                    color=(255, 0, 3),
                    thickness=2,
                )
                image = cv.line(
                    image,
                    AcupointsPosition[0][i][j + int((len(AcupointsPosition[0][i])) / 2)],
                    AcupointsPosition[0][i][j + 1 + int((len(AcupointsPosition[0][i])) / 2)],
                    color=(255, 0, 3),
                    thickness=2,
                )
    else:
        for j in range(int((len(AcupointsPosition[0][i - 3]) - 2) / 2)):
            image = cv.line(
                image,
                AcupointsPosition[1][i - 3][j],
                AcupointsPosition[1][i - 3][j + 1],
                color=(255, 0, 3),
                thickness=2,
            )
            image = cv.line(
                image,
                AcupointsPosition[1][i - 3][j + int((len(AcupointsPosition[1][i - 3])) / 2)],
                AcupointsPosition[1][i - 3][j + 1 + int((len(AcupointsPosition[1][i - 3])) / 2)],
                color=(255, 0, 3),
                thickness=2,
            )
    return image
