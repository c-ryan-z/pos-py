from PyQt6 import QtWidgets as Qtw, QtCore

from src.backend.controllers.ActivityLogsModel import ActivityLogsModel
from src.frontend.__custom_widgets.ActivityLogs import Ui_activity_logs
from src.backend.database.activity_logs import get_activity_logs_by_user_id, search_activity_logs_by_activity_type, \
    get_row_info


class CashierLogs(Qtw.QWidget):
    def __init__(self, main_app, user_widget):
        super().__init__()
        self.ui = Ui_activity_logs()
        self.ui.setupUi(self)
        self.model = None
        self.main_app = main_app
        self.user_widget = user_widget

        self.ui.le_sort.textChanged.connect(self.start_timer)
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.search_by_activity_type(self.ui.le_sort.text()))

        self.main_app.mainLoggedIn.connect(self.initialize_table)
        self.ui.tv_activity_logs.clicked.connect(self.handle_row_click)

        self.ui.tv_activity_logs.setStyleSheet("""
            QTableView QTableCornerButton::section {
                background-color: #FCCCF4;
            }
        """)

        self.ui.tv_activity_logs.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #FCCCF4;
                border: none;
                height: 60px;
                font-weight: 500;
                font-size: 14px;
            }
        """)

        self.ui.tv_activity_logs.verticalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #FFFFFF;
                border: none;
            }
        """)

    def initialize_table(self, user_info):
        user_role = user_info[2]
        if user_role != "cashier":
            return

        log_data = get_activity_logs_by_user_id(self.user_widget.user_id)
        self.model = ActivityLogsModel(log_data)
        self.ui.tv_activity_logs.setModel(self.model)
        self.set_column_sizes()

    def set_column_sizes(self):
        self.ui.tv_activity_logs.setColumnWidth(0, 50)
        self.ui.tv_activity_logs.setColumnWidth(1, 300)
        self.ui.tv_activity_logs.setColumnWidth(2, 210)
        self.ui.tv_activity_logs.setColumnWidth(3, 210)

    def clear_data(self):
        if self.model is not None:
            self.model.beginResetModel()
            self.model._data = []
            self.model.endResetModel()
            self.ui.tv_activity_logs.setModel(None)

    def start_timer(self):
        self.timer.start(500)

    def search_by_activity_type(self, activity_type):
        if activity_type == "":
            self.ui.tv_activity_logs.setModel(self.model)
            return

        filtered_data = self.model.filter_by_activity_type(activity_type)
        if not filtered_data:
            filtered_data = search_activity_logs_by_activity_type(activity_type)
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
