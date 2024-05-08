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

        self.tax = Tax(self.main_app, self.user_widget)
        self.ui.sw_admin.addWidget(self.tax)

        self.accounts = Accounts(self.main_app, self.user_widget)
        self.ui.sw_admin.addWidget(self.accounts)

        self.history = History(self.main_app)
        self.ui.sw_admin.addWidget(self.history)

        self.activity_logs = AdminLogs(self.main_app)
        self.ui.sw_admin.addWidget(self.activity_logs)

        self.buttons = {
            self.ui.pb_reports: self.ui.pb_reports.styleSheet(),
            self.ui.pb_inventory: self.ui.pb_inventory.styleSheet(),
            self.ui.pb_tax: self.ui.pb_tax.styleSheet(),
            self.ui.pb_accounts: self.ui.pb_accounts.styleSheet(),
            self.ui.pb_history: self.ui.pb_history.styleSheet(),
            self.ui.pb_activity_logs: self.ui.pb_activity_logs.styleSheet()
        }

        self.ui.pb_reports.setStyleSheet("""
                    background: #ff7cdc;
                    border: 1px solid #c0c4cc;
                    border-radius: 37px;
                """)

        for button in self.buttons.keys():
            button.clicked.connect(self.change_button_style)

    def clear_data(self):
        self.reports.clear_data()
        self.inventory.clear_data()
        self.tax.clear_data()
        self.accounts.clear_data()
        self.history.clear_data()
        self.activity_logs.clear_data()

    def tab_change(self, index):
        self.ui.sw_admin.setCurrentIndex(index)

    def change_button_style(self):
        clicked_button_style = """
            background: #ff7cdc;
            border: 1px solid #c0c4cc;
            border-radius: 28px;
        """

        clicked_button = self.sender()

        for button, default_style in self.buttons.items():
            if button == clicked_button:
                button.setStyleSheet(clicked_button_style)
            else:
                button.setStyleSheet(default_style)
