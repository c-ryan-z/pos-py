from PyQt6 import QtWidgets as Qtw
from PyQt6.QtGui import QPixmap, QImage, QBitmap, QPainter
from PyQt6.QtCore import Qt

from src.backend.controllers.Utility import confirmAction
from src.backend.database.employee import getEmployeeImage, uploadEmployeeImage
from src.frontend.__custom_widgets.userInfoForm import Ui_Form

from src.setup_paths import Paths


class UserInfoWidget(Qtw.QWidget):
    def __init__(self, main_app, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.userId = None

        self.ui.pb_setImage.clicked.connect(self.uploadImage)
        self.ui.pb_logout.clicked.connect(self.handleLogout)

    def initialize_user_info(self, user_info):
        self.userId = user_info[0]
        self.ui.lb_username.setText(user_info[1])
        self.ui.lb_role.setText(user_info[2].capitalize())
        self.getEmployeeImage()

    def process_image(self, image):
        pixmap = QPixmap.fromImage(image)
        scaled_pixmap = pixmap.scaled(self.ui.lb_userImage.width(), self.ui.lb_userImage.height(),
                                      Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)

        mask = QBitmap(scaled_pixmap.size())
        mask.fill(Qt.GlobalColor.color0)

        painter = QPainter(mask)
        painter.setBrush(Qt.GlobalColor.color1)
        painter.drawEllipse(0, 0, self.ui.lb_userImage.width(), self.ui.lb_userImage.height())
        painter.end()

        scaled_pixmap.setMask(mask)

        self.ui.lb_userImage.setPixmap(scaled_pixmap)

    def getEmployeeImage(self):
        image_data = getEmployeeImage(self.userId)
        if image_data is not None:
            image = QImage()
            image.loadFromData(image_data)
            self.process_image(image)
        else:
            default_image_path = Paths.image('default.jpg')
            image = QImage(default_image_path)
            self.process_image(image)

    def uploadImage(self):
        file_name, _ = Qtw.QFileDialog.getOpenFileName(self, "Upload Image", "", "Images (*.png *.jpeg *.jpg)")
        if file_name:
            print(file_name)
            uploadEmployeeImage(self.userId, file_name)
            self.getEmployeeImage()

    def handleLogout(self):
        if confirmAction(self, 'Confirm Logout', 'Logout', 'Are you sure you want to logout?'):
            self.main_app.setCurrentWidget('login')
            self.userId = None

            self.ui.lb_username.clear()
            self.ui.lb_role.clear()
            self.ui.lb_userImage.clear()
