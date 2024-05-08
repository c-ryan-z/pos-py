from PyQt6 import QtWidgets as Qtw, QtCore
from src.backend.database.sales.receipt import retrieve_receipt, retrieve_items
from src.frontend.__custom_widgets.Receipt import Ui_receipt


class Receipt(Qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_receipt()
        self.ui.setupUi(self)
        self.items = None
        self.data = None

        self.ui.list_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.ui.items_list.setStyleSheet("border: none;")

    def set_data(self, transaction_id):
        self.data = retrieve_receipt(transaction_id)
        self.initialize_transaction(self.data)
        self.items = retrieve_items(transaction_id)
        self.clear_layout(self.ui.list_layout)
        self.initialize_list(self.items)

    def initialize_transaction(self, data):
        self.data = data
        self.ui.lb_date.setText(str(self.data[0]))
        self.ui.lb_transaction.setText(str(self.data[1]))
        self.ui.lb_cashier.setText(str(self.data[2]) + " (" + str(self.data[3]) + ")")
        self.ui.lb_subtotal.setText(str(self.data[4]))
        self.ui.lb_taxP.setText(str(self.data[5]) + "%")
        self.ui.lb_tax.setText(str(float(self.data[4]) * float(self.data[5]) / 100))
        self.ui.lb_discount.setText(str(self.data[6]))
        self.ui.lb_total.setText(str(self.data[7]))
        self.ui.lb_payment.setText(str(self.data[8]))
        self.ui.lb_change.setText(str(self.data[9]))

    def initialize_list(self, items):
        if not items:
            print("No items found")
            return

        for item in items:
            layout = Qtw.QHBoxLayout()

            qty = Qtw.QLabel(str(item[0]))
            qty.setFixedWidth(50)
            name = Qtw.QLabel(item[1])
            name.setFixedWidth(130)
            price = Qtw.QLabel(str(item[2]))
            price.setFixedWidth(100)
            total = Qtw.QLabel(str(float(item[0]) * float(item[2])))
            total.setFixedWidth(100)

            layout.addWidget(qty)
            layout.addWidget(name)
            layout.addWidget(price)
            layout.addWidget(total)
            self.ui.list_layout.addLayout(layout)

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget() is not None:
                item.widget().setParent(None)
            elif item.layout() is not None:
                self.clear_layout(item.layout())

