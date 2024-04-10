from PyQt6 import QtCore, QtWidgets as Qtw

from src.backend.controllers.__customWidget.CustomCashierItem import CustomCashierItem
from src.backend.controllers.__customWidget.CustomMessageBox import CustomMessageBox
from src.backend.database.sales.cashier import retrieve_product
from src.frontend.sales.cashierDashboard import Ui_cashier_dashboard


class CashierDashboard(Qtw.QWidget):
    def __init__(self, main_app, sales_controller):
        super().__init__()
        self.ui = Ui_cashier_dashboard()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.sales_controller = sales_controller
        self.scanned_ids = []
        self.scanned_widgets = {}

        self.ui.list_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.sales_controller.barcodeSignal.connect(self.handle_barcode)

        self.ui.pushButton_2.clicked.connect(self.handle_discount)

    def handle_barcode(self, barcode):
        barcode = "1" + str(barcode)
        product_details = retrieve_product(barcode)
        if product_details is None:
            print("Product not found: ", barcode)
            return

        product_id = product_details[0]
        if product_id in self.scanned_widgets:
            widget = self.scanned_widgets[product_id]
            widget.ui.sb_quantity.setValue(widget.ui.sb_quantity.value() + 1)
        else:
            self.scanned_ids.append(product_details[0])
            widget = CustomCashierItem(product_details)
            widget.setFixedSize(1000, 150)
            self.ui.list_layout.insertWidget(0, widget)

            widget.delete_item.connect(self.remove_product)

            self.scanned_widgets[product_details[0]] = widget

    def remove_product(self, product_id):
        self.scanned_ids.remove(int(product_id))

        widget = self.scanned_widgets.get(int(product_id))
        if widget is not None:
            self.ui.list_layout.removeWidget(widget)
            widget.setParent(None)
            del self.scanned_widgets[int(product_id)]

    def handle_discount(self):
        message = CustomMessageBox(self, self.main_app)
        discount = message.multipleChoices("Discount", "Choose discount type", (5, 10, 15, 20))

        print("Discount: ", discount)
        return
