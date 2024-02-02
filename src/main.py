import sys

from PyQt6 import QtWidgets as qtw

from src.frontend.admin.adminController import AdminController
from src.frontend.inventory_manager.inventoryController import InventoryController
from src.frontend.loginFormController import LoginForm


class MainApp(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 800)

        self.stacked_widget = qtw.QStackedWidget()
        self.widgets = {}

        self.stacked_widget.setStyleSheet("border: 1px solid black;")
        self.login_form = LoginForm(self)
        self.addWidget(self.login_form, 'login')

        self.admin = AdminController()
        self.addWidget(self.admin, 'admin')

        self.inventory_manager = InventoryController()
        self.addWidget(self.inventory_manager, 'inventory_manager')

        layout = qtw.QVBoxLayout()

        layout.addWidget(self.stacked_widget)

        self.setLayout(layout)

    def addWidget(self, widget, identifier):
        self.widgets[identifier] = self.stacked_widget.addWidget(widget)

    def setCurrentWidget(self, identifier):
        if identifier in self.widgets:
            self.stacked_widget.setCurrentIndex(self.widgets[identifier])

    def nextWidget(self):
        self.stacked_widget.setCurrentIndex((self.stacked_widget.currentIndex() + 1) % self.stacked_widget.count())

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())