


def slot_init(self):  # 建立通信连接
    self.button_open_camera.clicked.connect(self.button_open_camera_click)
    self.timer_camera.timeout.connect(self.show_camera)
    self.button_close.clicked.connect(self.close)



def button_open_camera_click(self):
    if self.timer_camera.isActive() == False:
        flag = self.cap.open(self.CAM_NUM)
        if flag == False:
            msg = QtWidgets.QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
                                                buttons=QtWidgets.QMessageBox.Ok,
                                                defaultButton=QtWidgets.QMessageBox.Ok)
            # if msg==QtGui.QMessageBox.Cancel:
            #                     pass
        else:
            self.timer_camera.start(30)
            self.button_open_camera.setText(u'关闭相机')
    else:
        self.timer_camera.stop()
        self.cap.release()
        self.label_show_camera.clear()
        self.button_open_camera.setText(u'打开相机')


def show_camera(self):
    flag, self.image = self.cap.read()
    show = cv2.resize(self.image, (640, 480))
    # opencv格式不能直接显示，需要用下面代码转换一下
    show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
    showImage = QtGui.QImage(
        show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
    self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
