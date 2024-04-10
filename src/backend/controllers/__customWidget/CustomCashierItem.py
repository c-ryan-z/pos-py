from PyQt6 import QtWidgets as Qtw, QtCore
from src.frontend.__custom_widgets.CustomCashierItems import Ui_cashier_item


class CustomCashierItem(Qtw.QWidget):
    delete_item = QtCore.pyqtSignal(str)

    def __init__(self, product_details=None):
        super().__init__()
        self.ui = Ui_cashier_item()
        self.ui.setupUi(self)
        self.product_details = product_details
        self.id = product_details[0]

        self.ui.lb_name.setText(str(product_details[1]))
        self.ui.lb_price.setText(str(product_details[4]))
        self.ui.lb_description.setText(str(product_details[6]) + " " + str(product_details[3]))
        self.ui.sb_quantity.setMinimum(1)
        self.ui.sb_quantity.setMaximum(product_details[7])
        self.ui.sb_quantity.setValue(1)

        self.ui.pb_del.clicked.connect(self.remove_item)

    def remove_item(self):
        self.delete_item.emit(str(self.product_details[0]))
