from PyQt6 import QtWidgets as qtw

from src.frontend.admin.adminForm import Ui_Form


class AdminController(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def setUserId(self, user_id):
        pass
