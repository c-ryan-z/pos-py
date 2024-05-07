from PyQt6 import QtWidgets as Qtw, QtGui

from src.backend.controllers.adminControllers.admin_models import AccountModel
from src.backend.database.admin.accounts import get_user_accounts, get_user_info
from src.frontend.admin.AdminAccounts import Ui_admin_accounts


class Accounts(Qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_admin_accounts()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.current_user = None
        self.model = None

        self.main_app.mainLoggedIn.connect(self.initialize_table)

    def initialize_table(self):
        data = get_user_accounts()
        self.model = AccountModel(data)
        self.ui.tv_accounts.setModel(self.model)
        self.set_column_sizes()
        self.ui.tv_accounts.clicked.connect(self.on_row_clicked)
        self.initialize_user()

    def set_column_sizes(self):
        self.ui.tv_accounts.setColumnWidth(0, 100)
        self.ui.tv_accounts.setColumnWidth(1, 175)
        self.ui.tv_accounts.setColumnWidth(2, 175)
        self.ui.tv_accounts.setColumnWidth(3, 350)
        self.ui.tv_accounts.setColumnWidth(4, 140)

    def initialize_user(self):
        first_id = self.model.data(self.model.index(0, 0))
        user_data = get_user_info(first_id)
        self.set_user_details(user_data)

    def set_user_details(self, user_data):
        self.current_user = user_data[0]
        self.ui.lb_name.setText(user_data[1])
        self.ui.lb_role.setText(user_data[2])

        if user_data[3]:
            image_data = user_data[3].tobytes()
            image = QtGui.QImage.fromData(image_data)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.ui.lb_img.setPixmap(pixmap)
        else:
            self.ui.lb_img.clear()

    def on_row_clicked(self, index):
        first_column_value = self.model.data(self.model.index(index.row(), 0))
        user_data = get_user_info(first_column_value)
        self.set_user_details(user_data)
