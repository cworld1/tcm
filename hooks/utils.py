from PyQt5 import QtCore, QtGui, QtWidgets

import cv2 as cv
import sys

# 用于展示视频（图像）


def play_video():
    dict = sys.modules['__main__'].__dict__
    dict["flag"] = True
    pyK4A = dict["pyK4A"]

    # 打开摄像头
    pyK4A.device_start_cameras(dict["device_config"])
    while dict["flag"]:
        pyK4A.device_get_capture()  # Get capture
        # 获得三种数据
        depth_image_handle = pyK4A.capture_get_depth_image()
        color_image_handle = pyK4A.capture_get_color_image()
        if depth_image_handle and color_image_handle:
            # 将获取到的图像转换为numpy矩阵
            image = pyK4A.image_convert_to_numpy(color_image_handle)[:, :, :3]
            depth_image = pyK4A.transform_depth_to_color(
                depth_image_handle, color_image_handle)
            updateImage(dict["ui"], image)
            k = cv.waitKey(25)

        pyK4A.image_release(depth_image_handle)
        pyK4A.image_release(color_image_handle)
        pyK4A.capture_release()

# 暂停显示


def pause():
    test_dict = sys.modules['__main__'].__dict__
    test_dict["flag"] = False

# 更新图像


def updateImage(label, img, width, height):
    # 通道转化
    RGBImg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # 将图片转化成Qt可读格式
    image = QtGui.QImage(
        RGBImg, RGBImg.shape[1], RGBImg.shape[0], QtGui.QImage.Format_RGB888)
    # 加载图片,并自定义图片展示尺寸
    image = QtGui.QPixmap(image).scaled(width, height)
    # 显示图片
    label.setPixmap(image)
