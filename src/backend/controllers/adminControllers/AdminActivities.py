from PyQt6 import QtWidgets as Qtw

from src.backend.controllers.ActivityLogsModel import ActivityLogsModel
from src.frontend.__custom_widgets.ActivityLogs import Ui_activity_logs
from src.backend.database.activity_logs import get_all_activity_logs


class AdminLogs(Qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_activity_logs()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.model = None

        self.main_app.mainLoggedIn.connect(self.initialize_table)

    def initialize_table(self, user_info):
        user_role = user_info[2]
        if user_role != "admin":
            return

        log_data = get_all_activity_logs()
        self.model = ActivityLogsModel(log_data)
        self.ui.tv_activity_logs.setModel(self.model)
        self.set_column_sizes()

    def set_column_sizes(self):
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(0, Qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(1, Qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(2, Qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(3, Qtw.QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tv_activity_logs.horizontalHeader().setSectionResizeMode(4, Qtw.QHeaderView.ResizeMode.ResizeToContents)

    def clear_data(self):
        self.model.beginResetModel()
        self.model._data = []
        self.model.endResetModel()
        self.ui.tv_activity_logs.setModel(None)
