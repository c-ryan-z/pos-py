from PyQt6 import QtWidgets as Qtw
from src.frontend.sales.salesForm import Ui_w_cashier


class SalesController(Qtw.QWidget):
    def __init__(self, main_app, user_widget):
        super().__init__()
        self.ui = Ui_w_cashier()
        self.ui.setupUi(self)
        self.main_app = main_app

        # user info placeholder
        self.user_info_widget = user_widget
        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.user_info_widget)
        self.ui.userPlaceholder.setLayout(layout)

        self.main_app.mainLoggedIn.connect(self.user_info_widget.initialize_user_info)
