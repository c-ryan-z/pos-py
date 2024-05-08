from PyQt6 import QtWidgets as Qtw

from src.backend.controllers.adminControllers.Accounts import Accounts
from src.backend.controllers.adminControllers.History import History
from src.backend.controllers.adminControllers.Inventory import Inventory
from src.backend.controllers.adminControllers.Reports import Reports
from src.backend.controllers.adminControllers.Tax import Tax
from src.backend.controllers.adminControllers.AdminActivities import AdminLogs
from src.frontend.admin.AdminController import Ui_w_admin


class AdminController(Qtw.QWidget):
    def __init__(self, main_app, user_widget):
        super().__init__()
        self.timer = None
        self.ui = Ui_w_admin()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.user_widget = user_widget

        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.user_widget)
        self.ui.w_UserPlaceholder.setLayout(layout)
        self.main_app.mainLoggedIn.connect(self.user_widget.initialize_user_info)

        self.ui.pb_reports.clicked.connect(lambda: self.tab_change(0))
        self.ui.pb_inventory.clicked.connect(lambda: self.tab_change(1))
        self.ui.pb_tax.clicked.connect(lambda: self.tab_change(2))
        self.ui.pb_accounts.clicked.connect(lambda: self.tab_change(3))
        self.ui.pb_history.clicked.connect(lambda: self.tab_change(4))
        self.ui.pb_activity_logs.clicked.connect(lambda: self.tab_change(5))

        self.reports = Reports(self.main_app)
        self.ui.sw_admin.addWidget(self.reports)

        self.inventory = Inventory(self.main_app)
        self.ui.sw_admin.addWidget(self.inventory)

        self.tax = Tax(self.main_app)
        self.ui.sw_admin.addWidget(self.tax)

        self.accounts = Accounts(self.main_app)
        self.ui.sw_admin.addWidget(self.accounts)

        self.history = History(self.main_app)
        self.ui.sw_admin.addWidget(self.history)

        self.activity_logs = AdminLogs(self.main_app)
        self.ui.sw_admin.addWidget(self.activity_logs)

    def clear_data(self):
        self.reports.clear_data()
        self.inventory.clear_data()
        self.tax.clear_data()
        self.accounts.clear_data()
        self.history.clear_data()
        self.activity_logs.clear_data()

    def tab_change(self, index):
        self.ui.sw_admin.setCurrentIndex(index)
