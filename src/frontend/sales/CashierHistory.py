# Form implementation generated from reading ui file 'C:\Users\abarq\PycharmProjects\POS-PY\ui/CashierHistory.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_cashier_history(object):
    def setupUi(self, cashier_history):
        cashier_history.setObjectName("cashier_history")
        cashier_history.resize(1600, 1030)
        cashier_history.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        cashier_history.setAutoFillBackground(False)
        cashier_history.setStyleSheet("QWidget#cashier_dashboard {\n"
"    background: #FFFFFF;\n"
"}")
        self.gb_container = QtWidgets.QGroupBox(parent=cashier_history)
        self.gb_container.setGeometry(QtCore.QRect(10, 40, 1120, 900))
        self.gb_container.setStyleSheet("QGroupBox {\n"
"    background: rgba(248,249,250, 1);\n"
"    border: 3px solid rgba(29,33,40, 1);\n"
"    border-radius:13px;\n"
"}")
        self.gb_container.setTitle("")
        self.gb_container.setObjectName("gb_container")
        self.tv_history = QtWidgets.QTableView(parent=self.gb_container)
        self.tv_history.setGeometry(QtCore.QRect(19, 150, 1081, 720))
        self.tv_history.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tv_history.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tv_history.setDefaultDropAction(QtCore.Qt.DropAction.IgnoreAction)
        self.tv_history.setAlternatingRowColors(False)
        self.tv_history.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tv_history.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tv_history.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.tv_history.setShowGrid(False)
        self.tv_history.setSortingEnabled(True)
        self.tv_history.setObjectName("tv_history")
        self.tv_history.horizontalHeader().setDefaultSectionSize(300)
        self.tv_history.horizontalHeader().setMinimumSectionSize(0)
        self.lb_transaction = QtWidgets.QLabel(parent=self.gb_container)
        self.lb_transaction.setGeometry(QtCore.QRect(50, 40, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(28)
        font.setBold(True)
        self.lb_transaction.setFont(font)
        self.lb_transaction.setObjectName("lb_transaction")
        self.le_sort = QtWidgets.QLineEdit(parent=self.gb_container)
        self.le_sort.setGeometry(QtCore.QRect(290, 40, 500, 50))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.le_sort.setFont(font)
        self.le_sort.setStyleSheet("QLineEdit {\n"
"    background: rgba(255,255,255,1); /* white */\n"
"  border-radius: 25px; \n"
"  border-width: 3px; \n"
"  border-color: rgba(29,33,40,1); /* neutral-800 */\n"
"  border-style: solid; \n"
"}")
        self.le_sort.setText("")
        self.le_sort.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_sort.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.le_sort.setObjectName("le_sort")
        self.receipt_placeholder = QtWidgets.QWidget(parent=cashier_history)
        self.receipt_placeholder.setGeometry(QtCore.QRect(1190, 170, 354, 754))
        self.receipt_placeholder.setObjectName("receipt_placeholder")

        self.retranslateUi(cashier_history)
        QtCore.QMetaObject.connectSlotsByName(cashier_history)

    def retranslateUi(self, cashier_history):
        _translate = QtCore.QCoreApplication.translate
        cashier_history.setWindowTitle(_translate("cashier_history", "Form"))
        self.lb_transaction.setText(_translate("cashier_history", "Transaction"))
        self.le_sort.setPlaceholderText(_translate("cashier_history", "Search Here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cashier_history = QtWidgets.QWidget()
    ui = Ui_cashier_history()
    ui.setupUi(cashier_history)
    cashier_history.show()
    sys.exit(app.exec())
