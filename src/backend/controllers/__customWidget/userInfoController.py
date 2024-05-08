from PyQt6 import QtWidgets as Qtw, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage, QBitmap, QPainter

from src.backend.controllers.__customWidget.CustomMessageBox import CustomMessageBox
from src.backend.controllers.controller_utility import shadow_effect
from src.backend.database.employee import get_employee_img, uploadEmployeeImage
from src.backend.database.login.record_logins import logout_session, activity_log
from src.frontend.__custom_widgets.userInfoWidget import Ui_Form
from src.setup_paths import Paths


class UserInfoWidget(Qtw.QWidget):
    loggedOut = QtCore.pyqtSignal()

    def __init__(self, main_app, instance, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.instance = instance
        self.user_info = None
        self.user_id = None
        self.session_id = None

        self.ui.pb_setImage.clicked.connect(self.uploadImage)
        self.ui.pb_logout.clicked.connect(self.handleLogout)

        shadow_effect(self.ui.lb_userImage)

    def initialize_user_info(self, user_info):
        if user_info[2] != self.instance:
            return
        self.user_info = user_info
        self.user_id = user_info[0]
        self.session_id = user_info[6]
        self.ui.lb_username.setText(user_info[1])
        self.ui.lb_role.setText(user_info[2].capitalize())
        self.initialize_img(self.user_info[0])
        print(self.user_info)

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

    def initialize_img(self, user_id):
        image_data = get_employee_img(user_id)
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
            uploadEmployeeImage(self.user_info[0], file_name)
            self.initialize_img(self.user_info[0])

    def handleLogout(self):
        message_box = CustomMessageBox(self, main_app=self.main_app)
        if message_box.confirmAction("Logout", "Are you sure you want to logout?"):
            self.logout()
            return True
        return False

    def logout(self):
        logout_session(self.user_info[6])
        activity_log(self.user_info[0], 'Log Out', 'Account', 'User logged out', self.user_info[6])

        self.user_info = None
        self.ui.lb_username.clear()
        self.ui.lb_role.clear()
        self.ui.lb_userImage.clear()
        self.main_app.setCurrentWidget('login')

        self.loggedOut.emit()
