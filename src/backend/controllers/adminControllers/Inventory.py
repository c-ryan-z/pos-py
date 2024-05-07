from PyQt6 import QtWidgets as Qtw, QtGui

from src.backend.controllers.adminControllers.admin_models.InventoryModel import InventoryModel
from src.backend.controllers.adminControllers.admin_popups.InventoryPopUp import InventoryPopUp
from src.backend.database.admin.inventory import get_inventory, get_inventory_by_name, get_inventory_by_id, \
    delete_product
from src.frontend.admin.AdminInventory import Ui_admin_inventory


class Inventory(Qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_admin_inventory()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.model = None
        self.main_app.mainLoggedIn.connect(self.initialize_table)
        self.item_data = None

        self.ui.pb_add.clicked.connect(self.handle_add)
        self.ui.pb_remove.clicked.connect(self.handle_remove)

    def initialize_table(self):
        inventory_data = get_inventory()
        self.model = InventoryModel(inventory_data)
        self.ui.tv_items.setModel(self.model)
        self.set_column_sizes()
        self.ui.tv_items.clicked.connect(self.on_row_clicked)
        self.initialize_item_container()

    def initialize_item_container(self):
        self.ui.le_name.setEnabled(False)
        self.ui.le_price.setEnabled(False)
        self.ui.le_category.setEnabled(False)
        self.ui.le_stock.setEnabled(False)
        name = self.model.data(self.model.index(0, 0))

        self.item_data = get_inventory_by_name(name)
        self.set_item_details(self.item_data)

    def set_column_sizes(self):
        self.ui.tv_items.setColumnWidth(0, 175)
        self.ui.tv_items.setColumnWidth(1, 125)
        self.ui.tv_items.setColumnWidth(2, 125)
        self.ui.tv_items.setColumnWidth(3, 150)
        self.ui.tv_items.setColumnWidth(4, 100)

    def on_row_clicked(self, index):
        first_column_value = self.model.data(self.model.index(index.row(), 0))
        self.item_data = get_inventory_by_name(first_column_value)
        self.set_item_details(self.item_data)

    def popup_update(self):
        self.item_data = get_inventory_by_id(self.item_data[5])
        self.set_item_details(self.item_data)
        self.initialize_table()

    def set_item_details(self, item_data):
        self.ui.le_name.setText(item_data[0])
        self.ui.le_price.setText(str(item_data[1]))
        self.ui.le_category.setText(item_data[2])
        self.ui.le_stock.setText(str(item_data[3])) 

        if item_data[4]:
            image_data = item_data[4].tobytes()
            image = QtGui.QImage.fromData(image_data)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.ui.lb_itemImg.setPixmap(pixmap)
        else:
            self.ui.lb_itemImg.clear()

    def handle_add(self):
        pop_up = InventoryPopUp(self, self.main_app)
        pop_up.add_product(self.item_data)

    def handle_remove(self):
        item_name = self.ui.le_name.text()
        delete_product(item_name)
        self.initialize_table()
