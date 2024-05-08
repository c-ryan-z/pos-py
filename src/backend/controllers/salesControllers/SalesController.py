import time

from PyQt6 import QtWidgets as Qtw, QtCore

from src.backend.controllers.salesControllers.CashierLogs import CashierLogs
from src.backend.controllers.salesControllers.CashierDashboard import CashierDashboard
from src.backend.controllers.salesControllers.CashierHistory import CashierHistory
from src.frontend.sales.SalesController import Ui_w_cashier


class SalesController(Qtw.QWidget):
    barcodeSignal = QtCore.pyqtSignal(str)

    def __init__(self, main_app, user_widget):
        super().__init__()
        self.ui = Ui_w_cashier()
        self.ui.setupUi(self)
        self.main_app = main_app

        self.user_info_widget = user_widget
        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.user_info_widget)
        self.ui.userPlaceholder.setLayout(layout)
        self.main_app.mainLoggedIn.connect(self.user_info_widget.initialize_user_info)

        self.dashboard = CashierDashboard(self, self.main_app, self.user_info_widget)
        self.ui.sw_sales.addWidget(self.dashboard)

        self.history = CashierHistory(self, self.main_app, self.user_info_widget)
        self.ui.sw_sales.addWidget(self.history)

        self.activity_logs = CashierLogs(self.main_app, self.user_info_widget)
        self.ui.sw_sales.addWidget(self.activity_logs)

        self.last_key_time = time.time()
        self.key_sequence = ""

        self.buttons = {
            self.ui.pb_dashboard: self.ui.pb_dashboard.styleSheet(),
            self.ui.pb_history: self.ui.pb_history.styleSheet(),
            self.ui.pb_activity_logs: self.ui.pb_activity_logs.styleSheet()
        }

        self.ui.pb_dashboard.setStyleSheet("""
            background: #ff7cdc;
            border: 1px solid #c0c4cc;
            border-radius: 37px;
        """)

        for button in self.buttons.keys():
            button.clicked.connect(self.change_button_style)

        self.ui.pb_dashboard.clicked.connect(lambda: self.tab_change(0))
        self.ui.pb_history.clicked.connect(lambda: self.tab_change(1))
        self.ui.pb_activity_logs.clicked.connect(lambda: self.tab_change(2))

    def tab_change(self, index):
        self.ui.sw_sales.setCurrentIndex(index)

    def keyPressEvent(self, event):
        current_time = time.time()
        elapsed_time = current_time - self.last_key_time
        self.last_key_time = current_time

        if elapsed_time < 0.03:
            self.key_sequence += event.text()
        else:
            self.key_sequence = event.text()

        if event.key() == QtCore.Qt.Key.Key_Return and self.key_sequence and len(self.key_sequence) >= 7:
            self.barcodeSignal.emit(self.key_sequence)
            self.key_sequence = ""
        elif event.key() == QtCore.Qt.Key.Key_Return:
            self.key_sequence = ""

    def clear_data(self):
        self.dashboard.clear_data()
        self.history.clear_data()
        self.activity_logs.clear_data()
        print("Sales data cleared")

    def change_button_style(self):
        clicked_button_style = """
            background: #ff7cdc;
            border: 1px solid #c0c4cc;
            border-radius: 37px;
        """

        clicked_button = self.sender()

        for button, default_style in self.buttons.items():
            if button == clicked_button:
                button.setStyleSheet(clicked_button_style)
            else:
                button.setStyleSheet(default_style)
