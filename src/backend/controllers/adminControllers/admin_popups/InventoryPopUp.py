from PyQt6 import QtWidgets as Qtw, QtCore as Qtc, QtGui

from src.backend.database.admin.inventory import upsert_product, log_add_edit
from src.frontend.admin.InventoryPopUp import Ui_inventory_popup


class InventoryPopUp(Qtw.QDialog):

    def __init__(self, parent=None, main_app=None):
        super().__init__(parent, Qtc.Qt.WindowType.FramelessWindowHint)
        self.ui = Ui_inventory_popup()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.old_details = None
        self.image_path = None
        self.image_changed = False
        self.item_id = None

        self.setModal(True)
        self.line_edit_listener()
        self.ui.pb_close.clicked.connect(self.close)
        self.ui.pb_img.clicked.connect(self.set_item_img)
        self.ui.pb_save.clicked.connect(self.handle_save)

    def showEvent(self, event):
        super().showEvent(event)
        self.toggleDarkener()

    def done(self, result):
        self.toggleDarkener()
        super().done(result)

    def toggleDarkener(self):
        if self.main_app is not None:
            if self.main_app.darkener.isVisible():
                self.main_app.hideDarkener()
            else:
                self.main_app.showDarkener()

    def add_product(self, product_details):
        if self.old_details is None:
            self.old_details = product_details

        self.ui.le_name.setText(product_details[0])
        self.ui.le_price.setText(str(product_details[1]))
        self.ui.le_category.setText(product_details[2])
        self.ui.le_stock.setText(str(product_details[3]))
        self.set_img(product_details[4])
        self.item_id = product_details[5]

        return self.exec() == Qtw.QDialog.DialogCode.Accepted

    def set_img(self, image):
        if image:
            image_data = image.tobytes()
            image = QtGui.QImage.fromData(image_data)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.ui.lb_itemImg.setPixmap(pixmap)
        else:
            self.ui.lb_itemImg.clear()

    def set_item_img(self):
        file_name, _ = Qtw.QFileDialog.getOpenFileName(self, "Upload Image", "", "Images (*.png *.jpeg *.jpg)")
        if file_name:
            pixmap = QtGui.QPixmap(file_name)
            self.ui.lb_itemImg.setPixmap(pixmap)
            self.image_changed = True
            self.save_button()
            self.image_path = file_name

    def compare_details(self):
        if self.old_details is None:
            return False

        price_text = self.ui.le_price.text()
        stock_text = self.ui.le_stock.text()

        if not price_text or not price_text.replace('.', '', 1).isdigit() or not stock_text or not stock_text.isdigit():
            return False

        new_details = (
            self.ui.le_name.text(),
            float(self.ui.le_price.text()),
            self.ui.le_category.text(),
            int(self.ui.le_stock.text())
        )
        print(new_details, self.old_details)
        return new_details != self.old_details[:4] or self.image_changed

    def line_edit_listener(self):
        self.ui.le_name.textChanged.connect(self.save_button)
        self.ui.le_price.textChanged.connect(self.save_button)
        self.ui.le_category.textChanged.connect(self.save_button)
        self.ui.le_stock.textChanged.connect(self.save_button)

    def save_button(self):
        if self.compare_details():
            self.ui.pb_save.setEnabled(True)
            print("Enabled")
        else:
            print("Disabled")
            self.ui.pb_save.setEnabled(False)

    def handle_save(self):
        name = self.ui.le_name.text()
        price = float(self.ui.le_price.text())
        category = self.ui.le_category.text()
        stock = self.ui.le_stock.text()

        upsert_product(name, price, category, stock, image=self.image_path)
        log_add_edit(self.parent().user_info[0], "Add / Edit", f"Add / Edited {name}", str(self.parent().user_info[6]))
        self.close()
        self.ui.pb_save.setEnabled(False)
        self.parent().popup_update()
