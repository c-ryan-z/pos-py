from PyQt6 import QtWidgets as qtw

from src.frontend.inventory_manager.inventoryForm import Ui_Form


class InventoryController(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def setUserId(self, user_id):
        pass
