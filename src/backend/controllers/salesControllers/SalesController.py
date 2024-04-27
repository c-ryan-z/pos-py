import time

from PyQt6 import QtWidgets as Qtw, QtCore

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

        self.history = CashierHistory(self, self.main_app)
        self.ui.sw_sales.addWidget(self.history)

        self.last_key_time = time.time()
        self.key_sequence = ""

        self.ui.pb_dashboard.clicked.connect(lambda: self.tab_change(0))
        self.ui.pb_history.clicked.connect(lambda: self.tab_change(1))

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
