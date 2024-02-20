import sys

from PyQt6 import QtWidgets as Qtw

from src.backend.controllers.adminControllers.adminController import AdminController
from src.backend.controllers.inventoryControllers.inventoryController import InventoryController
from src.backend.controllers.salesControllers.salesController import SalesController
from src.backend.controllers.loginFormController import LoginForm


class MainApp(Qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.userInfo = None
        self.setMinimumSize(1300, 900)

        self.stacked_widget = Qtw.QStackedWidget()
        self.widgets = {}

        self.login_form = LoginForm(self)
        self.login_form.userLoggedIn.connect(self.handleUserLoggedIn)  # Connect signal to slot
        self.addWidget(self.login_form, 'login')
        self.stacked_widget.setStyleSheet("border: 1px solid black;")

        self.admin = AdminController()
        self.addWidget(self.admin, 'admin')

        self.inventory_manager = InventoryController()
        self.addWidget(self.inventory_manager, 'inventory_manager')

        self.salesController = SalesController(self)
        self.addWidget(self.salesController, 'sales')

        layout = Qtw.QVBoxLayout()

        layout.addWidget(self.stacked_widget)

        self.setLayout(layout)

    def addWidget(self, widget, identifier):
        self.widgets[identifier] = self.stacked_widget.addWidget(widget)

    def setCurrentWidget(self, identifier):
        if identifier in self.widgets:
            self.stacked_widget.setCurrentIndex(self.widgets[identifier])

    def nextWidget(self):
        self.stacked_widget.setCurrentIndex((self.stacked_widget.currentIndex() + 1) % self.stacked_widget.count())

    def handleUserLoggedIn(self, user_info):
        self.userInfo = user_info
        user_role = user_info[2]

        if user_role == 'sales':
            self.setCurrentWidget('sales')
            self.salesController.initialize_user_info(user_info)
        # elif user_role == 'admin':
        #     self.admin.setUserId(user_id)
        # elif user_role == 'inventory_manager':
        #     self.inventory_manager.setUserId(user_id)kf


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
