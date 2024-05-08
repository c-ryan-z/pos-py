from PyQt6 import QtWidgets as Qtw, QtCore, QtGui

from src.backend.controllers.ActivityLogsModel import ActivityLogsModel
from src.frontend.__custom_widgets.ActivityLogs import Ui_activity_logs
from src.backend.database.activity_logs import get_all_activity_logs, search_activity_logs_by_user_id, get_row_info


class AdminLogs(Qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_activity_logs()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.model = None

        self.main_app.mainLoggedIn.connect(self.initialize_table)

        self.ui.le_sort.textChanged.connect(self.start_timer)
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.search_by_user_id(self.ui.le_sort.text()))

        self.ui.tv_activity_logs.clicked.connect(self.handle_row_click)

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

    def start_timer(self):
        self.timer.start(500)

    def search_by_user_id(self, user_id):
        if user_id == "":
            self.ui.tv_activity_logs.setModel(self.model)
            return

        filtered_data = self.model.filter_by_user_id(user_id)
        if not filtered_data:
            filtered_data = search_activity_logs_by_user_id(user_id)
        new_model = ActivityLogsModel(filtered_data)
        self.ui.tv_activity_logs.setModel(new_model)

    def handle_row_click(self, index):
        model = self.ui.tv_activity_logs.model()
        first_column_data = model.data(model.index(index.row(), 0))
        row = get_row_info(first_column_data)
        self.ui.lb_id.setText(str(row[0]))
        self.ui.lb_user_id.setText(str(row[1]))
        self.ui.lb_timestamp.setText(str(row[2]))
        self.ui.lb_category.setText(str(row[3]))
        self.ui.lb_type.setText(str(row[4]))
        self.ui.lb_session.setText(str(row[5]))
        self.ui.lb_details.setText(str(row[6]))
