from PyQt6 import QtCore, QtWidgets as Qtw
from PyQt6.QtCore import QTimer, QDateTime
from pyqt6_plugins.examplebuttonplugin import QtGui

from src.backend.controllers.__customWidget.CustomCashierItem import CustomCashierItem
from src.backend.controllers.__customWidget.CustomMessageBox import CustomMessageBox
from src.backend.database.sales.cashier import retrieve_product, transaction_checkout, initialize_tax, \
    void_transaction, interleave_transaction, retrieve_interleaved_transactions, record_transaction_items, \
    retrieve_transaction_items, update_transaction
from src.frontend.sales.CashierDashboard import Ui_cashier_dashboard


class CashierDashboard(Qtw.QWidget):
    def __init__(self, sales_controller, main_app, user_widget):
        super().__init__()
        self.ui = Ui_cashier_dashboard()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.user_widget = user_widget
        self.sales_controller = sales_controller
        self.scanned_widgets = {}
        self.quantity_labels = {}
        self.overview_layouts = {}
        self.interleaved_transaction = None
        self.sub_total = 0
        self.system_tax = initialize_tax()
        self.discount = 0
        self.total = 0

        self.ui.list_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.ui.overview_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.ui.overview.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
        """)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)

        self.ui.le_cash.setValidator(QtGui.QDoubleValidator(0.99, 999999.99, 2))
        self.sales_controller.barcodeSignal.connect(self.handle_barcode)

        self.ui.pb_discount.clicked.connect(self.handle_discount)
        self.ui.pb_void_transac.clicked.connect(self.void)
        self.ui.pb_checkout.clicked.connect(self.handle_checkout)
        self.ui.pb_interleave.clicked.connect(self.handle_interleaving)
        self.ui.cb_transactions.currentIndexChanged.connect(self.retrieve_interleaved_transaction)
        self.ui.cb_transactions.installEventFilter(self)
        self.populate_transactions()

    def eventFilter(self, watched, event):
        if watched == self.ui.cb_transactions and event.type() == QtCore.QEvent.Type.Leave:
            self.ui.cb_transactions.parent().setFocus()
        return super().eventFilter(watched, event)

    def handle_barcode(self, barcode):
        print(barcode)
        product_details = retrieve_product(barcode)
        if product_details is None:
            print("Product not found: ", barcode)
            return

        product_id = product_details[0]
        if product_id in self.scanned_widgets:
            widget = self.scanned_widgets[product_id]
            widget.ui.sb_quantity.setValue(widget.ui.sb_quantity.value() + 1)
            self.overview_list(product_id, product_details[1], product_details[4], widget.ui.sb_quantity.value())
        else:
            widget = CustomCashierItem(product_details)
            widget.setFixedSize(1000, 225)
            self.ui.list_layout.insertWidget(0, widget)

            widget.delete_item.connect(self.remove_product)

            self.scanned_widgets[product_details[0]] = widget
            widget.quantity_changed.connect(self.calculate_total)
            widget.quantity_changed.connect(
                lambda: self.overview_list(product_id, product_details[1], product_details[4],
                                           widget.ui.sb_quantity.value()))
            self.overview_list(product_id, product_details[1], product_details[4], widget.ui.sb_quantity.value())

        self.calculate_total()

        if self.interleaved_transaction:
            checkout_items = [(product_id, widget.ui.sb_quantity.value())]
            record_transaction_items(self.interleaved_transaction, checkout_items)

    def populate_transactions(self):
        self.ui.cb_transactions.clear()
        self.ui.cb_transactions.addItem("Empty Transaction")
        paused_transactions = retrieve_interleaved_transactions()
        for transactions in paused_transactions:
            self.ui.cb_transactions.addItem(str(transactions[0]))

    def overview_list(self, product_id, name, price, quantity):
        if product_id in self.quantity_labels:
            self.quantity_labels[product_id].setText("x " + str(quantity))
        else:
            layout = Qtw.QHBoxLayout()

            name_label = Qtw.QLabel(name)
            name_label.setFixedWidth(200)
            price_label = Qtw.QLabel(str(price))
            price_label.setFixedWidth(100)
            quantity_label = Qtw.QLabel("x " + str(quantity))
            quantity_label.setFixedWidth(70)
            quantity_label.setStyleSheet("border-radius: 2x;")

            layout.addWidget(name_label)
            layout.addWidget(price_label)
            layout.addWidget(quantity_label)

            self.ui.overview_layout.addLayout(layout)
            self.quantity_labels[product_id] = quantity_label
            self.overview_layouts[product_id] = layout

    def remove_product(self, product_id):
        widget = self.scanned_widgets.get(int(product_id))
        if widget is not None:
            self.ui.list_layout.removeWidget(widget)
            widget.setParent(None)
            del self.scanned_widgets[int(product_id)]

        layout = self.overview_layouts.get(int(product_id))
        if layout is not None:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()
            self.ui.overview_layout.removeItem(layout)
            del self.overview_layouts[int(product_id)]

        if int(product_id) in self.quantity_labels:
            del self.quantity_labels[int(product_id)]

        self.calculate_total()

    def handle_discount(self):
        message = CustomMessageBox(self, self.main_app)
        self.discount = message.multipleChoices("Discount", "Choose discount type", (5, 10, 15, 20))
        self.ui.lb_discountP.setText(f"{self.discount}%")
        self.calculate_total()
        return self.discount

    def calculate_total(self):
        total = 0
        for item_id, item_widget in self.scanned_widgets.items():
            total += item_widget.price * item_widget.ui.sb_quantity.value()
        self.sub_total = float(total)
        self.ui.lb_subtotal.setText("{:.2f}".format(total))
        discount_amount = total * self.discount / 100
        self.ui.lb_discount.setText("{:.2f}".format(discount_amount))
        total -= discount_amount
        tax = float(total) * float(self.system_tax) / 100
        self.ui.lb_tax.setText("{:.2f}".format(tax))
        self.total += tax
        self.ui.lb_total.setText("{:.2f}".format(total))

    def handle_checkout(self):
        cash, change = self.handle_cash()
        if cash is None:
            return

        checkout_items = []
        for item_id, item_widget in self.scanned_widgets.items():
            print(item_id, item_widget.ui.sb_quantity.value())
            checkout_items.append((item_id, item_widget.ui.sb_quantity.value()))

        total = self.sub_total + (self.sub_total * float(self.system_tax) / 100)

        if self.interleaved_transaction:
            transaction_id = update_transaction(self.interleaved_transaction, self.sub_total, self.system_tax,
                                                self.discount, total, cash, change)
            self.interleaved_transaction = None
        else:
            transaction_id = transaction_checkout(self.user_widget.user_id, self.sub_total, self.system_tax,
                                                  self.discount, total, cash, change, checkout_items,
                                                  self.user_widget.session_id)

        if transaction_id is not None:
            message = CustomMessageBox(self, self.main_app)
            message.show_receipt(transaction_id)

        self.clear_transaction()
        self.ui.le_cash.clear()

        self.clear_transaction()
        self.ui.le_cash.clear()

    def handle_cash(self):
        cash_text = self.ui.le_cash.text()
        if not cash_text:
            message = CustomMessageBox(self, self.main_app)
            message.notifyAction("Invalid Input", "Please enter a valid cash amount")
            return None, None

        cash = float(self.ui.le_cash.text())
        if cash < float(self.sub_total):
            message = CustomMessageBox(self, self.main_app)
            message.notifyAction("Insufficient Cash", "Cash is less than the total amount")
            return None, None
        else:
            change = cash - float(self.sub_total)
            message = CustomMessageBox(self, self.main_app)
            message.notifyAction("Change", f"Change: {change:.2f}")
            return cash, change

    def clear_transaction(self):
        for item_id, item_widget in self.scanned_widgets.items():
            self.ui.list_layout.removeWidget(item_widget)
            item_widget.setParent(None)

        for product_id, layout in self.overview_layouts.items():
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()
            self.ui.overview_layout.removeItem(layout)

        self.scanned_widgets.clear()
        self.overview_layouts.clear()
        self.quantity_labels.clear()

        self.calculate_total()

    def update_date_time(self):
        current_date_time = QDateTime.currentDateTime()
        formatted_date_time = current_date_time.toString("dddd MMM dd, yyyy hh:mm:ss ap")
        self.ui.lb_date_no.setText(formatted_date_time)

    def clear_data(self):
        for item_id, item_widget in self.scanned_widgets.items():
            self.ui.list_layout.removeWidget(item_widget)
            item_widget.setParent(None)
        self.scanned_widgets.clear()

        for product_id, layout in self.overview_layouts.items():
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()
            self.ui.overview_layout.removeItem(layout)
        self.overview_layouts.clear()
        self.quantity_labels.clear()

        self.sub_total = 0
        self.total = 0
        self.ui.lb_subtotal.setText("0.00")
        self.ui.lb_tax.setText("0.00")
        self.ui.lb_total.setText("0.00")

        self.ui.le_cash.clear()

    def void(self):
        if not self.scanned_widgets:
            message = CustomMessageBox(self, self.main_app)
            message.notifyAction("Void Items", "No items to void")
        else:
            message = CustomMessageBox(self, self.main_app)
            if message.confirmAction("Void Items", "Are you sure you want to void all items?"):
                voided_product_ids = list(self.scanned_widgets.keys())
                voided_product_ids_str = ', '.join(map(str, voided_product_ids))
                void_transaction(self.user_widget.user_id, "Void Items", voided_product_ids_str,
                                 str(self.user_widget.session_id))
                self.clear_transaction()
                self.ui.le_cash.clear()

    def handle_interleaving(self):
        if not self.scanned_widgets:
            message = CustomMessageBox(self, self.main_app)
            message.notifyAction("Interleave Items", "No items to interleave")
        else:
            checkout_items = []
            for item_id, item_widget in self.scanned_widgets.items():
                checkout_items.append((item_id, item_widget.ui.sb_quantity.value()))

            total = self.sub_total + (self.sub_total * float(self.system_tax) / 100)
            transaction_id = interleave_transaction(self.user_widget.user_id, self.sub_total, self.system_tax,
                                                    self.discount, total)

            record_transaction_items(transaction_id, checkout_items)

            self.clear_transaction()
            self.ui.le_cash.clear()
            self.populate_transactions()

    def retrieve_interleaved_transaction(self):
        transaction_id = self.ui.cb_transactions.currentText()
        if transaction_id == "Empty Transaction":
            self.clear_transaction()
            return
        if transaction_id:
            self.clear_transaction()
            self.interleaved_transaction = transaction_id
            transaction_items = retrieve_transaction_items(transaction_id)
            for item in transaction_items:
                product_id = item[0]
                quantity = item[1]
                product_details = retrieve_product(product_id)
                if product_details is not None:
                    widget = CustomCashierItem(product_details)
                    widget.ui.sb_quantity.setValue(quantity)
                    widget.setFixedSize(1000, 225)
                    self.ui.list_layout.insertWidget(0, widget)

                    widget.delete_item.connect(self.remove_product)

                    self.scanned_widgets[product_details[0]] = widget
                    widget.quantity_changed.connect(self.calculate_total)
                    widget.quantity_changed.connect(
                        lambda: self.overview_list(product_id, product_details[1], product_details[4],
                                                   widget.ui.sb_quantity.value()))
                    self.overview_list(product_id, product_details[1], product_details[4], widget.ui.sb_quantity.value())

            self.calculate_total()
