from PyQt6 import QtWidgets as Qtw

from src.backend.controllers.ActivityLogsModel import ActivityLogsModel
from src.frontend.__custom_widgets.ActivityLogs import Ui_activity_logs
from src.backend.database.activity_logs import get_activity_logs_by_user_id


class CashierLogs(Qtw.QWidget):
    def __init__(self, main_app, user_widget):
        super().__init__()
        self.ui = Ui_activity_logs()
        self.ui.setupUi(self)
        self.model = None
        self.main_app = main_app
        self.user_widget = user_widget

        self.main_app.mainLoggedIn.connect(self.initialize_table)

    def initialize_table(self, user_info):
        user_role = user_info[2]
        if user_role != "cashier":
            return

        log_data = get_activity_logs_by_user_id(self.user_widget.user_id)
        self.model = ActivityLogsModel(log_data)
        self.ui.tv_activity_logs.setModel(self.model)
        self.set_column_sizes()

    def set_column_sizes(self):
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(0, Qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(1, Qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(2, Qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(3, Qtw.QHeaderView.ResizeMode.ResizeToContents)

    def clear_data(self):
        if self.model is not None:
            self.model.beginResetModel()
            self.model._data = []
            self.model.endResetModel()
            self.ui.tv_activity_logs.setModel(None)
