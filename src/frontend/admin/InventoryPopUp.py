# Form implementation generated from reading ui file 'C:\Users\abarq\PycharmProjects\POS-PY\ui/InventoryPopUp.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_inventory_popup(object):
    def setupUi(self, inventory_popup):
        inventory_popup.setObjectName("inventory_popup")
        inventory_popup.resize(971, 565)
        inventory_popup.setStyleSheet("QWidget#custom_modal {\n"
"    background-color: #FFFFFF;\n"
"    border: 4px solid rgba(29,33,41,1);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius:5px;\n"
"    border: 1px solid #5E5E5E;\n"
"    padding: 5px 5px;\n"
"}")
        self.pb_close = QtWidgets.QPushButton(parent=inventory_popup)
        self.pb_close.setGeometry(QtCore.QRect(930, 10, 30, 30))
        self.pb_close.setStyleSheet("QPushButton {\n"
"    background: #00000000;\n"
"    border: none;\n"
"}")
        self.pb_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/frontend/__image/circle-xmark.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_close.setIcon(icon)
        self.pb_close.setIconSize(QtCore.QSize(30, 30))
        self.pb_close.setObjectName("pb_close")
        self.lb_itemImg = QtWidgets.QLabel(parent=inventory_popup)
        self.lb_itemImg.setGeometry(QtCore.QRect(110, 110, 251, 251))
        self.lb_itemImg.setScaledContents(True)
        self.lb_itemImg.setObjectName("lb_itemImg")
        self.pb_img = QtWidgets.QPushButton(parent=inventory_popup)
        self.pb_img.setGeometry(QtCore.QRect(130, 410, 171, 51))
        self.pb_img.setObjectName("pb_img")
        self.le_stock = QtWidgets.QLineEdit(parent=inventory_popup)
        self.le_stock.setGeometry(QtCore.QRect(570, 320, 113, 22))
        self.le_stock.setObjectName("le_stock")
        self.lb_1 = QtWidgets.QLabel(parent=inventory_popup)
        self.lb_1.setGeometry(QtCore.QRect(570, 300, 71, 16))
        self.lb_1.setObjectName("lb_1")
        self.le_price = QtWidgets.QLineEdit(parent=inventory_popup)
        self.le_price.setGeometry(QtCore.QRect(570, 260, 113, 22))
        self.le_price.setObjectName("le_price")
        self.lb_3 = QtWidgets.QLabel(parent=inventory_popup)
        self.lb_3.setGeometry(QtCore.QRect(570, 240, 61, 16))
        self.lb_3.setObjectName("lb_3")
        self.lb_4 = QtWidgets.QLabel(parent=inventory_popup)
        self.lb_4.setGeometry(QtCore.QRect(570, 180, 81, 16))
        self.lb_4.setObjectName("lb_4")
        self.le_category = QtWidgets.QLineEdit(parent=inventory_popup)
        self.le_category.setGeometry(QtCore.QRect(570, 200, 113, 22))
        self.le_category.setObjectName("le_category")
        self.le_name = QtWidgets.QLineEdit(parent=inventory_popup)
        self.le_name.setGeometry(QtCore.QRect(570, 140, 113, 22))
        self.le_name.setObjectName("le_name")
        self.lb_2 = QtWidgets.QLabel(parent=inventory_popup)
        self.lb_2.setGeometry(QtCore.QRect(570, 120, 61, 16))
        self.lb_2.setObjectName("lb_2")
        self.lb_ = QtWidgets.QLabel(parent=inventory_popup)
        self.lb_.setGeometry(QtCore.QRect(70, 50, 71, 21))
        self.lb_.setObjectName("lb_")
        self.pb_save = QtWidgets.QPushButton(parent=inventory_popup)
        self.pb_save.setGeometry(QtCore.QRect(640, 430, 171, 51))
        self.pb_save.setObjectName("pb_save")

        self.retranslateUi(inventory_popup)
        QtCore.QMetaObject.connectSlotsByName(inventory_popup)

    def retranslateUi(self, inventory_popup):
        _translate = QtCore.QCoreApplication.translate
        inventory_popup.setWindowTitle(_translate("inventory_popup", "Form"))
        self.lb_itemImg.setText(_translate("inventory_popup", "Placeholder"))
        self.pb_img.setText(_translate("inventory_popup", "Select Image"))
        self.lb_1.setText(_translate("inventory_popup", "Item Stock"))
        self.lb_3.setText(_translate("inventory_popup", "Item Price"))
        self.lb_4.setText(_translate("inventory_popup", "Item Category"))
        self.lb_2.setText(_translate("inventory_popup", "Item Name"))
        self.lb_.setText(_translate("inventory_popup", "Item Details"))
        self.pb_save.setText(_translate("inventory_popup", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventory_popup = QtWidgets.QWidget()
    ui = Ui_inventory_popup()
    ui.setupUi(inventory_popup)
    inventory_popup.show()
    sys.exit(app.exec())
