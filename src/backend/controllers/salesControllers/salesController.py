import time

from PyQt6 import QtWidgets as Qtw, QtCore

from src.backend.controllers.salesControllers.cashierDashboard import CashierDashboard
from src.frontend.sales.salesForm import Ui_w_cashier


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

        self.dashboard = CashierDashboard(main_app, self)
        self.ui.sw_sales.addWidget(self.dashboard)
        self.ui.sw_sales.currentChanged.connect(self.on_sw_sales_changed)

        self.last_key_time = time.time()
        self.key_sequence = ""

    def on_sw_sales_changed(self, index):
        if self.ui.sw_sales.widget(index) == self.dashboard:
            self.dashboard.setFocus()

    def keyPressEvent(self, event):
        current_time = time.time()
        elapsed_time = current_time - self.last_key_time
        self.last_key_time = current_time

        if elapsed_time < 0.03:
            self.key_sequence += event.text()

        if event.key() == QtCore.Qt.Key.Key_Return and self.key_sequence and len(self.key_sequence) >= 7:
            self.barcodeSignal.emit(self.key_sequence)
            self.key_sequence = ""
        elif event.key() == QtCore.Qt.Key.Key_Return:
            self.key_sequence = ""
