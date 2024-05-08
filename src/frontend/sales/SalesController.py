# Form implementation generated from reading ui file 'C:\Users\abarq\PycharmProjects\POS-PY\ui/SaleController.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_w_cashier(object):
    def setupUi(self, w_cashier):
        w_cashier.setObjectName("w_cashier")
        w_cashier.resize(1921, 1041)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/MINI-GRO.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        w_cashier.setWindowIcon(icon)
        self.gb_sidebar = QtWidgets.QGroupBox(parent=w_cashier)
        self.gb_sidebar.setGeometry(QtCore.QRect(40, 0, 231, 1040))
        self.gb_sidebar.setMinimumSize(QtCore.QSize(0, 1040))
        self.gb_sidebar.setStyleSheet("QPushButton {\n"
"    background: #ff7cdc;\n"
"    border: 1px solid #c0c4cc;\n"
"    border-radius: 37px;\n"
"}")
        self.gb_sidebar.setTitle("")
        self.gb_sidebar.setObjectName("gb_sidebar")
        self.layoutWidget = QtWidgets.QWidget(parent=self.gb_sidebar)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Logo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.Logo.setMaximumSize(QtCore.QSize(229, 137))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("./src/frontend/__image/logo_u1.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.verticalLayout.addWidget(self.Logo)
        spacerItem = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.pb_dashboard = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pb_dashboard.setMinimumSize(QtCore.QSize(220, 80))
        self.pb_dashboard.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_dashboard.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./src/frontend/__image/sales_elements/shopping-cart.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_dashboard.setIcon(icon1)
        self.pb_dashboard.setIconSize(QtCore.QSize(32, 32))
        self.pb_dashboard.setAutoDefault(False)
        self.pb_dashboard.setObjectName("pb_dashboard")
        self.verticalLayout.addWidget(self.pb_dashboard)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pb_history = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pb_history.setMinimumSize(QtCore.QSize(80, 80))
        self.pb_history.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_history.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./src/frontend/__image/sales_elements/time-past.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_history.setIcon(icon2)
        self.pb_history.setIconSize(QtCore.QSize(32, 32))
        self.pb_history.setObjectName("pb_history")
        self.verticalLayout.addWidget(self.pb_history)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.userPlaceholder = QtWidgets.QWidget(parent=self.gb_sidebar)
        self.userPlaceholder.setGeometry(QtCore.QRect(10, 670, 221, 311))
        self.userPlaceholder.setObjectName("userPlaceholder")
        self.sw_sales = QtWidgets.QStackedWidget(parent=w_cashier)
        self.sw_sales.setGeometry(QtCore.QRect(290, 0, 1600, 1040))
        self.sw_sales.setObjectName("sw_sales")

        self.retranslateUi(w_cashier)
        self.sw_sales.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(w_cashier)

    def retranslateUi(self, w_cashier):
        _translate = QtCore.QCoreApplication.translate
        w_cashier.setWindowTitle(_translate("w_cashier", "Form"))
        self.pb_dashboard.setText(_translate("w_cashier", "Transaction"))
        self.pb_history.setText(_translate("w_cashier", "History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w_cashier = QtWidgets.QWidget()
    ui = Ui_w_cashier()
    ui.setupUi(w_cashier)
    w_cashier.show()
    sys.exit(app.exec())
