# Form implementation generated from reading ui file 'C:\Users\abarq\PycharmProjects\POS-PY\ui/CashierDashboard.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_cashier_dashboard(object):
    def setupUi(self, cashier_dashboard):
        cashier_dashboard.setObjectName("cashier_dashboard")
        cashier_dashboard.resize(1599, 1023)
        cashier_dashboard.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        cashier_dashboard.setAutoFillBackground(False)
        cashier_dashboard.setStyleSheet("QWidget#cashier_dashboard {\n"
"    background: #FEFEFE;\n"
"}")
        self.items_list = QtWidgets.QScrollArea(parent=cashier_dashboard)
        self.items_list.setGeometry(QtCore.QRect(20, 50, 1055, 916))
        self.items_list.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.items_list.setStyleSheet("QScrollArea#items_list {\n"
"    background: #FEFEFE;\n"
"    border-radius: 12px;\n"
"    border: 3px solid #20242c;\n"
"}\n"
"\n"
"QWidget#list {\n"
"    border-radius:10px;\n"
"    background: #FEFEFE;\n"
"}")
        self.items_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.items_list.setWidgetResizable(True)
        self.items_list.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.items_list.setObjectName("items_list")
        self.list = QtWidgets.QWidget()
        self.list.setGeometry(QtCore.QRect(0, 0, 1049, 910))
        self.list.setObjectName("list")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.list)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_layout = QtWidgets.QVBoxLayout()
        self.list_layout.setObjectName("list_layout")
        self.verticalLayout.addLayout(self.list_layout)
        self.items_list.setWidget(self.list)
        self.pb_checkout = QtWidgets.QPushButton(parent=cashier_dashboard)
        self.pb_checkout.setGeometry(QtCore.QRect(1160, 940, 381, 58))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_checkout.setFont(font)
        self.pb_checkout.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    background: #ff64b4;\n"
"    color: #181c1c;\n"
"}")
        self.pb_checkout.setObjectName("pb_checkout")
        self.gb_order_tag_2 = QtWidgets.QGroupBox(parent=cashier_dashboard)
        self.gb_order_tag_2.setGeometry(QtCore.QRect(1160, 31, 381, 141))
        self.gb_order_tag_2.setStyleSheet("QGroupBox#gb_order_tag_2 {\n"
"    border:none;\n"
"}")
        self.gb_order_tag_2.setTitle("")
        self.gb_order_tag_2.setObjectName("gb_order_tag_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.gb_order_tag_2)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 80, 381, 51))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    background: #f064d0;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gb_order_tag = QtWidgets.QGroupBox(parent=self.gb_order_tag_2)
        self.gb_order_tag.setGeometry(QtCore.QRect(0, 0, 381, 101))
        self.gb_order_tag.setStyleSheet("QGroupBox#gb_order_tag {\n"
"    background: #F8F9FA;\n"
"    border: 3px dashed #ff64b4;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLabel#gb_order, QLabel#gb_order_no {\n"
"    color:#181c1c;\n"
"}\n"
"\n"
"QLabel#date, QLabel#date_no {\n"
"    color:#9894a4;\n"
"}\n"
"")
        self.gb_order_tag.setTitle("")
        self.gb_order_tag.setObjectName("gb_order_tag")
        self.lb_order = QtWidgets.QLabel(parent=self.gb_order_tag)
        self.lb_order.setGeometry(QtCore.QRect(20, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(24)
        font.setBold(True)
        self.lb_order.setFont(font)
        self.lb_order.setObjectName("lb_order")
        self.lb_order_no = QtWidgets.QLabel(parent=self.gb_order_tag)
        self.lb_order_no.setGeometry(QtCore.QRect(240, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(24)
        font.setBold(True)
        self.lb_order_no.setFont(font)
        self.lb_order_no.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_order_no.setObjectName("lb_order_no")
        self.lb_date = QtWidgets.QLabel(parent=self.gb_order_tag)
        self.lb_date.setGeometry(QtCore.QRect(20, 70, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.lb_date.setFont(font)
        self.lb_date.setObjectName("lb_date")
        self.lb_date_no = QtWidgets.QLabel(parent=self.gb_order_tag)
        self.lb_date_no.setGeometry(QtCore.QRect(70, 70, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.lb_date_no.setFont(font)
        self.lb_date_no.setObjectName("lb_date_no")
        self.items_overview = QtWidgets.QScrollArea(parent=cashier_dashboard)
        self.items_overview.setGeometry(QtCore.QRect(1160, 180, 381, 481))
        self.items_overview.setStyleSheet("QScrollArea#items_overview {\n"
"    background: #FEFEFE;\n"
"    border-radius: 12px;\n"
"    border: 3px solid #20242c;\n"
"}\n"
"\n"
"QWidget#overview {\n"
"    border-radius:10px;\n"
"    background: #FEFEFE;\n"
"}")
        self.items_overview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.items_overview.setWidgetResizable(True)
        self.items_overview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.items_overview.setObjectName("items_overview")
        self.overview = QtWidgets.QWidget()
        self.overview.setGeometry(QtCore.QRect(0, 0, 375, 475))
        self.overview.setObjectName("overview")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.overview)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.overview_layout = QtWidgets.QVBoxLayout()
        self.overview_layout.setObjectName("overview_layout")
        self.verticalLayout_2.addLayout(self.overview_layout)
        self.items_overview.setWidget(self.overview)
        self.gb_invoice = QtWidgets.QGroupBox(parent=cashier_dashboard)
        self.gb_invoice.setGeometry(QtCore.QRect(1160, 660, 381, 241))
        self.gb_invoice.setStyleSheet("QGroupBox {\n"
"    border:none;\n"
"}")
        self.gb_invoice.setTitle("")
        self.gb_invoice.setObjectName("gb_invoice")
        self.TotalAmount = QtWidgets.QLabel(parent=self.gb_invoice)
        self.TotalAmount.setGeometry(QtCore.QRect(10, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(18)
        font.setBold(True)
        self.TotalAmount.setFont(font)
        self.TotalAmount.setObjectName("TotalAmount")
        self.Tax = QtWidgets.QLabel(parent=self.gb_invoice)
        self.Tax.setGeometry(QtCore.QRect(10, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.Tax.setFont(font)
        self.Tax.setObjectName("Tax")
        self.Sale = QtWidgets.QLabel(parent=self.gb_invoice)
        self.Sale.setGeometry(QtCore.QRect(10, 70, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.Sale.setFont(font)
        self.Sale.setObjectName("Sale")
        self.Discount = QtWidgets.QLabel(parent=self.gb_invoice)
        self.Discount.setGeometry(QtCore.QRect(10, 40, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.Discount.setFont(font)
        self.Discount.setObjectName("Discount")
        self.SubTotal = QtWidgets.QLabel(parent=self.gb_invoice)
        self.SubTotal.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.SubTotal.setFont(font)
        self.SubTotal.setObjectName("SubTotal")
        self.lb_subtotal = QtWidgets.QLabel(parent=self.gb_invoice)
        self.lb_subtotal.setGeometry(QtCore.QRect(300, 10, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.lb_subtotal.setFont(font)
        self.lb_subtotal.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_subtotal.setObjectName("lb_subtotal")
        self.lb_discount = QtWidgets.QLabel(parent=self.gb_invoice)
        self.lb_discount.setGeometry(QtCore.QRect(300, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.lb_discount.setFont(font)
        self.lb_discount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_discount.setObjectName("lb_discount")
        self.lb_sale = QtWidgets.QLabel(parent=self.gb_invoice)
        self.lb_sale.setGeometry(QtCore.QRect(300, 70, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.lb_sale.setFont(font)
        self.lb_sale.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_sale.setObjectName("lb_sale")
        self.lb_tax = QtWidgets.QLabel(parent=self.gb_invoice)
        self.lb_tax.setGeometry(QtCore.QRect(300, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.lb_tax.setFont(font)
        self.lb_tax.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_tax.setObjectName("lb_tax")
        self.lb_total = QtWidgets.QLabel(parent=self.gb_invoice)
        self.lb_total.setGeometry(QtCore.QRect(260, 130, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(18)
        font.setBold(True)
        self.lb_total.setFont(font)
        self.lb_total.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_total.setObjectName("lb_total")
        self.label = QtWidgets.QLabel(parent=self.gb_invoice)
        self.label.setGeometry(QtCore.QRect(270, 10, 20, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./src/frontend/__image/peso-sign.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.gb_invoice)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 20, 20))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./src/frontend/__image/peso-sign.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.gb_invoice)
        self.label_3.setGeometry(QtCore.QRect(270, 70, 20, 20))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./src/frontend/__image/peso-sign.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.gb_invoice)
        self.label_4.setGeometry(QtCore.QRect(230, 130, 20, 20))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./src/frontend/__image/peso-sign.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lb_discountP = QtWidgets.QLabel(parent=self.gb_invoice)
        self.lb_discountP.setGeometry(QtCore.QRect(110, 40, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Inter Light")
        font.setPointSize(12)
        self.lb_discountP.setFont(font)
        self.lb_discountP.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_discountP.setObjectName("lb_discountP")
        self.layoutWidget = QtWidgets.QWidget(parent=self.gb_invoice)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 150, 371, 73))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gb_button_2 = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.gb_button_2.setMinimumSize(QtCore.QSize(91, 71))
        self.gb_button_2.setMaximumSize(QtCore.QSize(91, 71))
        self.gb_button_2.setTitle("")
        self.gb_button_2.setObjectName("gb_button_2")
        self.Discount_4 = QtWidgets.QLabel(parent=self.gb_button_2)
        self.Discount_4.setGeometry(QtCore.QRect(0, 50, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.Discount_4.setFont(font)
        self.Discount_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Discount_4.setObjectName("Discount_4")
        self.pb_void_transac = QtWidgets.QPushButton(parent=self.gb_button_2)
        self.pb_void_transac.setGeometry(QtCore.QRect(-1, 0, 91, 41))
        self.pb_void_transac.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/frontend/__image/sales_elements/rectangle-xmark.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_void_transac.setIcon(icon)
        self.pb_void_transac.setIconSize(QtCore.QSize(32, 32))
        self.pb_void_transac.setDefault(False)
        self.pb_void_transac.setFlat(True)
        self.pb_void_transac.setObjectName("pb_void_transac")
        self.horizontalLayout.addWidget(self.gb_button_2)
        self.gb_button_3 = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.gb_button_3.setMinimumSize(QtCore.QSize(91, 71))
        self.gb_button_3.setMaximumSize(QtCore.QSize(91, 71))
        self.gb_button_3.setTitle("")
        self.gb_button_3.setObjectName("gb_button_3")
        self.Discount_5 = QtWidgets.QLabel(parent=self.gb_button_3)
        self.Discount_5.setGeometry(QtCore.QRect(0, 50, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.Discount_5.setFont(font)
        self.Discount_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Discount_5.setObjectName("Discount_5")
        self.pb_discount = QtWidgets.QPushButton(parent=self.gb_button_3)
        self.pb_discount.setGeometry(QtCore.QRect(0, 0, 91, 40))
        self.pb_discount.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./src/frontend/__image/sales_elements/discount.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_discount.setIcon(icon1)
        self.pb_discount.setIconSize(QtCore.QSize(32, 32))
        self.pb_discount.setFlat(True)
        self.pb_discount.setObjectName("pb_discount")
        self.horizontalLayout.addWidget(self.gb_button_3)
        self.gb_button = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.gb_button.setMinimumSize(QtCore.QSize(91, 71))
        self.gb_button.setMaximumSize(QtCore.QSize(91, 71))
        self.gb_button.setTitle("")
        self.gb_button.setObjectName("gb_button")
        self.pb_interleave = QtWidgets.QPushButton(parent=self.gb_button)
        self.pb_interleave.setGeometry(QtCore.QRect(0, 0, 91, 40))
        self.pb_interleave.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pb_interleave.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./src/frontend/__image/sales_elements/hourglass-end.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_interleave.setIcon(icon2)
        self.pb_interleave.setIconSize(QtCore.QSize(32, 32))
        self.pb_interleave.setFlat(True)
        self.pb_interleave.setObjectName("pb_interleave")
        self.Discount_3 = QtWidgets.QLabel(parent=self.gb_button)
        self.Discount_3.setGeometry(QtCore.QRect(0, 50, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.Discount_3.setFont(font)
        self.Discount_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Discount_3.setObjectName("Discount_3")
        self.horizontalLayout.addWidget(self.gb_button)
        self.le_cash = CustomLeLeaveEvent(parent=cashier_dashboard)
        self.le_cash.setGeometry(QtCore.QRect(1180, 890, 341, 41))
        self.le_cash.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #2F2F2F;\n"
"    background: rgba(243,244,246,1);\n"
"    padding: 4px;\n"
"    border-radius: 12px;\n"
"}")
        self.le_cash.setObjectName("le_cash")
        self.cb_transactions = QtWidgets.QComboBox(parent=cashier_dashboard)
        self.cb_transactions.setGeometry(QtCore.QRect(840, 0, 231, 41))
        self.cb_transactions.setStyleSheet("QComboBox {\n"
"  font-family: Inter; \n"
"  font-size: 16px; \n"
"  color: rgba(23,26,31,1); \n"
"  background: rgba(243,244,246,1);\n"
"    border-radius: 8px;\n"
"    border: 2px solid rgba(50, 50,50, 0.7)\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(./src/frontend/__image/angle-down.svg);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    margin-right: 3px;\n"
"}")
        self.cb_transactions.setEditable(False)
        self.cb_transactions.setObjectName("cb_transactions")

        self.retranslateUi(cashier_dashboard)
        QtCore.QMetaObject.connectSlotsByName(cashier_dashboard)

    def retranslateUi(self, cashier_dashboard):
        _translate = QtCore.QCoreApplication.translate
        cashier_dashboard.setWindowTitle(_translate("cashier_dashboard", "Form"))
        self.pb_checkout.setText(_translate("cashier_dashboard", "Checkout"))
        self.lb_order.setText(_translate("cashier_dashboard", "Transaction #"))
        self.lb_order_no.setText(_translate("cashier_dashboard", "1"))
        self.lb_date.setText(_translate("cashier_dashboard", "Date:"))
        self.lb_date_no.setText(_translate("cashier_dashboard", "September 11, 2001"))
        self.TotalAmount.setText(_translate("cashier_dashboard", "Total Amount"))
        self.Tax.setText(_translate("cashier_dashboard", "Tax"))
        self.Sale.setText(_translate("cashier_dashboard", "Sale"))
        self.Discount.setText(_translate("cashier_dashboard", "Discount %"))
        self.SubTotal.setText(_translate("cashier_dashboard", "Sub Total"))
        self.lb_subtotal.setText(_translate("cashier_dashboard", "0"))
        self.lb_discount.setText(_translate("cashier_dashboard", "0"))
        self.lb_sale.setText(_translate("cashier_dashboard", "0"))
        self.lb_tax.setText(_translate("cashier_dashboard", "0"))
        self.lb_total.setText(_translate("cashier_dashboard", "0"))
        self.lb_discountP.setText(_translate("cashier_dashboard", "0"))
        self.Discount_4.setText(_translate("cashier_dashboard", "Void"))
        self.pb_void_transac.setToolTip(_translate("cashier_dashboard", "<html><head/><body><p><span style=\" font-weight:700;\">Void Transaction</span></p></body></html>"))
        self.Discount_5.setText(_translate("cashier_dashboard", "Discount"))
        self.pb_discount.setToolTip(_translate("cashier_dashboard", "<html><head/><body><p><span style=\" font-weight:700;\">Add Discount</span></p></body></html>"))
        self.pb_interleave.setToolTip(_translate("cashier_dashboard", "<html><head/><body><p><span style=\" font-weight:700;\">Dismiss the current transaction and continue the transaction later.</span></p></body></html>"))
        self.Discount_3.setText(_translate("cashier_dashboard", "Interleave"))
        self.le_cash.setPlaceholderText(_translate("cashier_dashboard", "Enter Cash"))
        self.cb_transactions.setPlaceholderText(_translate("cashier_dashboard", "Interleaved Transactions"))
from src.backend.controllers.__customWidget.CustomLeLeaveEvent import CustomLeLeaveEvent


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cashier_dashboard = QtWidgets.QWidget()
    ui = Ui_cashier_dashboard()
    ui.setupUi(cashier_dashboard)
    cashier_dashboard.show()
    sys.exit(app.exec())
