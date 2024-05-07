from PyQt6 import QtWidgets as Qtw, QtCore

from src.backend.controllers.__customWidget.CustomMessageBox import CustomMessageBox
from src.backend.database.admin.tax import get_tax, update_tax
from src.frontend.admin.AdminTax import Ui_admin_tax


class Tax(Qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_admin_tax()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.tax_rate = 0

        self.ui.verticalLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.main_app.mainLoggedIn.connect(self.initialize_tax)
        self.ui.pb_edit.clicked.connect(self.edit_tax)

    def initialize_tax(self):
        self.tax_rate = get_tax()[0]
        self.ui.le_tax.setText(str(self.tax_rate))

    def edit_tax(self):
        if self.ui.le_tax.isEnabled():
            if self.ui.le_tax.text() == "":
                message = CustomMessageBox(self, self.main_app)
                message.notifyAction("Empty Field", "Please input a value")
                return
            if float(self.ui.le_tax.text()) != float(self.tax_rate):
                message = CustomMessageBox(self, self.main_app)
                if message.confirmAction("Edit Tax", "Are you sure you want to edit the tax rate?"):
                    update_tax(float(self.ui.le_tax.text()))
                    self.tax_rate = str(self.ui.le_tax.text())
                    self.ui.le_tax.setEnabled(False)
            else:
                self.ui.le_tax.setEnabled(False)
        else:
            self.ui.le_tax.setEnabled(True)
            self.ui.le_tax.setFocus()
