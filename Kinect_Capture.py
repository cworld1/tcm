import sys
sys.path.insert(1, './pyKinectAzure/')
import numpy as np
from pyKinectAzure import pyKinectAzure, _k4a
import cv2

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

# 记录获得次数
k = 0

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

        # 显示
        #open3dVisualizer(points)
        cv2.namedWindow(' Color Image', cv2.WINDOW_NORMAL)
        cv2.imshow(' Color Image', color_image)
        cv2.namedWindow(' Depth-Color Image', cv2.WINDOW_NORMAL)
        cv2.imshow(' Depth-Color Image', color_depth_image(image))
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

