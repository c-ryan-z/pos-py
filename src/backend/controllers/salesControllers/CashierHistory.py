from PyQt6 import QtWidgets as Qtw

from src.frontend.sales.CashierHistory import Ui_cashier_history


class CashierHistory(Qtw.QWidget):
    def __init__(self, sales_controller, main_app):
        super().__init__()
        self.ui = Ui_cashier_history()
        self.ui.setupUi(self)
        self.sales_controller = sales_controller
        self.main_app = main_app
