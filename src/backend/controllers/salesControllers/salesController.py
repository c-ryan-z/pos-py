import importlib.resources

from PyQt6 import QtWidgets as Qtw
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap, QBitmap, QPainter, QImage

from src.frontend.sales.salesForm import Ui_Form
from src.backend.database import getCashierImage, uploadCashierImage


class SalesController(Qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.userId = None

        self.ui.setImage.clicked.connect(self.uploadImage)
        self.ui.logoutButton.clicked.connect(self.handleLogout)

    def initialize_user_info(self, user_info):
        self.userId = user_info[0]
        self.getCashierImage()

    def process_image(self, image):
        pixmap = QPixmap.fromImage(image)
        scaled_pixmap = pixmap.scaled(self.ui.cashierImage.width(), self.ui.cashierImage.height(),
                                      QtCore.Qt.AspectRatioMode.IgnoreAspectRatio,
                                      QtCore.Qt.TransformationMode.SmoothTransformation)

        mask = QBitmap(scaled_pixmap.size())
        mask.fill(QtCore.Qt.GlobalColor.color0)

        painter = QPainter(mask)
        painter.setBrush(QtCore.Qt.GlobalColor.color1)
        painter.drawEllipse(0, 0, self.ui.cashierImage.width(), self.ui.cashierImage.height())
        painter.end()

        scaled_pixmap.setMask(mask)

        self.ui.cashierImage.setPixmap(scaled_pixmap)

    def getCashierImage(self):
        image_data = getCashierImage(self.userId)
        if image_data is not None:
            image = QImage()
            image.loadFromData(image_data)
            self.process_image(image)
        else:
            with importlib.resources.path('frontend.images', 'default.jpg') as img_path:
                default_image = QImage(str(img_path))
                self.process_image(default_image)

    def uploadImage(self):
        file_name, _ = Qtw.QFileDialog.getOpenFileName(self, "Upload Image", "", "Images (*.png *.jpeg *.jpg)")
        if file_name:
            print(file_name)
            uploadCashierImage(self.userId, file_name)
            self.getCashierImage()

    def handleLogout(self):
        self.main_app.setCurrentWidget('login')
        self.userId = None
        self.ui.cashierImage.clear()
