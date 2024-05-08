from PyQt6 import QtWidgets as Qtw, QtGui

from src.backend.controllers.__customWidget.CustomMessageBox import CustomMessageBox
from src.backend.controllers.adminControllers.admin_models.AccountModel import AccountModel
from src.backend.controllers.adminControllers.admin_popups.AccountPopUp import AccountPopUp
from src.backend.database.admin.accounts import get_user_accounts, get_user_info, deactivate_user, log_accounts
from src.frontend.admin.AdminAccounts import Ui_admin_accounts
from src.setup_paths import Paths


class Accounts(Qtw.QWidget):
    def __init__(self, main_app, user_widget):
        super().__init__()
        self.ui = Ui_admin_accounts()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.current_user = None
        self.model = None
        self.user_widget = user_widget

        self.main_app.mainLoggedIn.connect(self.initialize_table)
        self.ui.pb_add.clicked.connect(self.handle_add)
        self.ui.pb_edit.clicked.connect(self.handle_edit)
        self.ui.pb_remove.clicked.connect(self.handle_delete)

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
            pixmap = QtGui.QPixmap(Paths.image("user.svg"))
            self.ui.lb_img.setPixmap(pixmap)

    def on_row_clicked(self, index):
        first_column_value = self.model.data(self.model.index(index.row(), 0))
        user_data = get_user_info(first_column_value)
        self.set_user_details(user_data)

    def update_table(self):
        self.initialize_table()
        self.initialize_user()

    def handle_add(self):
        pop_up = AccountPopUp(self, self.main_app, self.user_widget)
        pop_up.finished.connect(self.update_table)
        pop_up.add_user()

    def handle_edit(self):
        pop_up = AccountPopUp(self, self.main_app, self.user_widget)
        pop_up.finished.connect(self.update_table)
        pop_up.edit_user(self.current_user)

    def handle_delete(self):
        user_id = self.current_user

        message = CustomMessageBox(self, self.main_app)
        if message.confirmAction("Delete User", "Are you sure you want to delete this user?"):
            deactivate_user(user_id)
            log_accounts(self.user_widget.user_id, "Deleted user", f"Deactivated user with ID: "
                                                                   f"{user_id}", str(self.user_widget.session_id))
            self.initialize_table()
            self.initialize_user()
            self.update_table()

    def clear_data(self):
        self.model.beginResetModel()
        self.model._data = []
        self.model.endResetModel()
        self.ui.tv_accounts.setModel(None)

        self.ui.lb_name.clear()
        self.ui.lb_role.clear()
        self.ui.lb_img.clear()

        self.current_user = None
