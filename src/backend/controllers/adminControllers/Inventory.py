from PyQt6 import QtWidgets as Qtw, QtGui, QtCore

from src.backend.controllers.__customWidget.CustomMessageBox import CustomMessageBox
from src.backend.controllers.adminControllers.admin_models.InventoryModel import InventoryModel
from src.backend.controllers.adminControllers.admin_popups.InventoryPopUp import InventoryPopUp
from src.backend.database.admin.inventory import get_inventory, get_inventory_by_name, get_inventory_by_id, \
    delete_product, log_delete
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
        self.user_info = None

        self.ui.pb_add.clicked.connect(self.handle_add)
        self.ui.pb_remove.clicked.connect(self.handle_remove)

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.search_by_name(self.ui.le_sort.text()))

        self.ui.le_sort.textChanged.connect(self.start_timer)

        self.ui.tv_items.setStyleSheet("""
            QTableView QTableCornerButton::section {
                background-color: #FCCCF4;
            }
        """)

        self.ui.tv_items.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #FCCCF4;
                border: none;
                height: 60px;
                font-weight: 500;
                font-size: 14px;
            }
        """)

        self.ui.tv_items.verticalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #FFFFFF;
                border: none;
            }
""")

    def initialize_table(self, user_info):
        self.user_info = user_info
        user_role = user_info[2]
        if user_role != "admin":
            return

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
        self.initialize_table(self.user_info)

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
        message = CustomMessageBox(self, self.main_app)
        if message.confirmAction("Delete", "Are you sure you want to delete this item?"):
            delete_product(item_name)
            log_delete(self.user_info[0], "Delete", f"Deleted item: {item_name}", str(self.user_info[6]))
            self.initialize_table(self.user_info)

    def clear_data(self):
        self.model.clear_data()
        self.ui.tv_items.setModel(None)

        self.ui.le_name.clear()
        self.ui.le_price.clear()
        self.ui.le_category.clear()
        self.ui.le_stock.clear()
        self.ui.lb_itemImg.clear()

        self.item_data = None

    def start_timer(self):
        self.timer.start(500)

    def search_by_name(self, item_name):
        if item_name == "":
            self.ui.tv_items.setModel(self.model)
            self.set_column_sizes()
            return

        filtered_data = self.model.filter_by_name(item_name)
        if not filtered_data:
            item = get_inventory_by_name(item_name)
            if item:
                filtered_data = [item]
        new_model = InventoryModel(filtered_data)
        self.ui.tv_items.setModel(new_model)
