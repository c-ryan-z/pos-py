# Form implementation generated from reading ui file 'C:\Users\abarq\PycharmProjects\POS-PY\ui/AdminController.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_w_admin(object):
    def setupUi(self, w_admin):
        w_admin.setObjectName("w_admin")
        w_admin.resize(1921, 1041)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/MINI-GRO.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        w_admin.setWindowIcon(icon)
        self.gb_sidebar = QtWidgets.QGroupBox(parent=w_admin)
        self.gb_sidebar.setGeometry(QtCore.QRect(10, 10, 231, 1040))
        self.gb_sidebar.setMinimumSize(QtCore.QSize(0, 1040))
        self.gb_sidebar.setStyleSheet("QPushButton {\n"
"    background: #ff7cdc;\n"
"    border: 1px solid #c0c4cc;\n"
"    border-radius: 37px;\n"
"}")
        self.gb_sidebar.setTitle("")
        self.gb_sidebar.setObjectName("gb_sidebar")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.gb_sidebar)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 231, 627))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Logo_2 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.Logo_2.setMaximumSize(QtCore.QSize(229, 137))
        self.Logo_2.setText("")
        self.Logo_2.setPixmap(QtGui.QPixmap("C:\\Users\\abarq\\PycharmProjects\\POS-PY\\ui\\../src/frontend/__image/logo_u1.png"))
        self.Logo_2.setScaledContents(True)
        self.Logo_2.setObjectName("Logo_2")
        self.verticalLayout_2.addWidget(self.Logo_2)
        self.pb_reports = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.pb_reports.setMinimumSize(QtCore.QSize(220, 80))
        self.pb_reports.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_reports.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\abarq\\PycharmProjects\\POS-PY\\ui\\../src/frontend/__image/admin_elements/chart-histogram.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_reports.setIcon(icon1)
        self.pb_reports.setIconSize(QtCore.QSize(32, 32))
        self.pb_reports.setAutoDefault(False)
        self.pb_reports.setObjectName("pb_reports")
        self.verticalLayout_2.addWidget(self.pb_reports)
        self.pb_inventory = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.pb_inventory.setMinimumSize(QtCore.QSize(80, 80))
        self.pb_inventory.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_inventory.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\abarq\\PycharmProjects\\POS-PY\\ui\\../src/frontend/__image/admin_elements/supplier-alt.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_inventory.setIcon(icon2)
        self.pb_inventory.setIconSize(QtCore.QSize(32, 32))
        self.pb_inventory.setObjectName("pb_inventory")
        self.verticalLayout_2.addWidget(self.pb_inventory)
        self.pb_tax = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.pb_tax.setMinimumSize(QtCore.QSize(80, 80))
        self.pb_tax.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_tax.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\abarq\\PycharmProjects\\POS-PY\\ui\\../src/frontend/__image/admin_elements/calculator-math-tax.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_tax.setIcon(icon3)
        self.pb_tax.setIconSize(QtCore.QSize(32, 32))
        self.pb_tax.setObjectName("pb_tax")
        self.verticalLayout_2.addWidget(self.pb_tax)
        self.pb_accounts = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.pb_accounts.setMinimumSize(QtCore.QSize(80, 80))
        self.pb_accounts.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_accounts.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\abarq\\PycharmProjects\\POS-PY\\ui\\../src/frontend/__image/admin_elements/users.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_accounts.setIcon(icon4)
        self.pb_accounts.setIconSize(QtCore.QSize(32, 32))
        self.pb_accounts.setObjectName("pb_accounts")
        self.verticalLayout_2.addWidget(self.pb_accounts)
        self.pb_history = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.pb_history.setMinimumSize(QtCore.QSize(80, 80))
        self.pb_history.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_history.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\abarq\\PycharmProjects\\POS-PY\\ui\\../src/frontend/__image/sales_elements/time-past.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_history.setIcon(icon5)
        self.pb_history.setIconSize(QtCore.QSize(32, 32))
        self.pb_history.setObjectName("pb_history")
        self.verticalLayout_2.addWidget(self.pb_history)
        self.w_UserPlaceholder = QtWidgets.QWidget(parent=self.gb_sidebar)
        self.w_UserPlaceholder.setGeometry(QtCore.QRect(10, 670, 221, 311))
        self.w_UserPlaceholder.setObjectName("w_UserPlaceholder")
        self.sw_admin = QtWidgets.QStackedWidget(parent=w_admin)
        self.sw_admin.setGeometry(QtCore.QRect(259, 0, 1701, 1040))
        self.sw_admin.setObjectName("sw_admin")

        self.retranslateUi(w_admin)
        self.sw_admin.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(w_admin)

    def retranslateUi(self, w_admin):
        _translate = QtCore.QCoreApplication.translate
        w_admin.setWindowTitle(_translate("w_admin", "Form"))
        self.pb_reports.setText(_translate("w_admin", "Reports"))
        self.pb_inventory.setText(_translate("w_admin", "Inventory"))
        self.pb_tax.setText(_translate("w_admin", "Tax"))
        self.pb_accounts.setText(_translate("w_admin", "Accounts"))
        self.pb_history.setText(_translate("w_admin", "History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w_admin = QtWidgets.QWidget()
    ui = Ui_w_admin()
    ui.setupUi(w_admin)
    w_admin.show()
    sys.exit(app.exec())
