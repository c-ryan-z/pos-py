from PyQt6 import QtWidgets as Qtw, QtCore, QtGui

from src.backend.controllers.__customWidget.Receipt import Receipt
from src.backend.controllers.adminControllers.admin_models import HistoryModel
from src.backend.controllers.controller_utility import process_data
from src.backend.database.Scroll_Paginator import ScrollPaginator
from src.backend.database.admin.history import cashier_transactions, retrieve_admin_transaction
from src.frontend.sales.CashierHistory import Ui_cashier_history


class History(Qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_cashier_history()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.model = None
        self.paginator = None

        self.main_app.mainLoggedIn.connect(self.initialize_table)

        self.ui.tv_history.verticalHeader().setDefaultSectionSize(60)
        self.ui.tv_history.verticalScrollBar().valueChanged.connect(self.table_scroll_position)
        self.ui.tv_history.clicked.connect(self.handle_row_click)

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.search_by_id(self.ui.le_sort.text()))

        self.ui.le_sort.textChanged.connect(self.star_timer)
        self.ui.le_sort.setValidator(QtGui.QIntValidator(100090000, 999999999))

        self.receipt_widget = Receipt()
        layout = Qtw.QVBoxLayout()
        layout.addWidget(self.receipt_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        self.ui.receipt_placeholder.setLayout(layout)

        self.main_app.mainLoggedIn.connect(self.initialize_receipt)

        self.ui.tv_history.setStyleSheet("""
            QTableView QTableCornerButton::section {
                background-color: #FCCCF4;
            }
        """)

        self.ui.tv_history.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #FCCCF4;
                border: none;
                height: 60px;
                font-weight: 500;
                font-size: 14px;
            }
        """)

        self.ui.tv_history.verticalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #FFFFFF;
                border: none;
            }
        """)

    def initialize_table(self, user_info):
        cashier_id = user_info[0]
        query = cashier_transactions()
        params = (cashier_id,)
        self.paginator = ScrollPaginator(query, params, name="cashier_transactions")
        data = self.paginator.get_next_page()
        data = process_data(data, 3)
        self.model = HistoryModel(data)
        self.ui.tv_history.setModel(self.model)
        self.set_column_sizes()

    def table_scroll_position(self, val):
        max_val = self.ui.tv_history.verticalScrollBar().maximum()

        scroll_trigger = max_val * 0.80
        if val >= scroll_trigger and self.paginator.has_next():
            new_data = self.paginator.get_next_page()
            new_data = process_data(new_data, 3)
            self.update_table(new_data)

    def update_table(self, new_data):
        sort_column = self.ui.tv_history.horizontalHeader().sortIndicatorSection()
        sort_order = self.ui.tv_history.horizontalHeader().sortIndicatorOrder()
        self.model.update_data(new_data, sort_column, sort_order)

    def handle_row_click(self, index):
        model = self.ui.tv_history.model()
        first_column_data = model.data(model.index(index.row(), 0))
        self.receipt_widget.set_data(first_column_data)

    def set_column_sizes(self, search=False):
        if search:
            self.ui.tv_history.setColumnWidth(0, 161)
            self.ui.tv_history.setColumnWidth(1, 216)
            self.ui.tv_history.setColumnWidth(2, 216)
        else:
            self.ui.tv_history.setColumnWidth(0, 160)
            self.ui.tv_history.setColumnWidth(1, 200)
            self.ui.tv_history.setColumnWidth(2, 200)

        self.ui.tv_history.setColumnWidth(3, 103)
        self.ui.tv_history.setColumnWidth(4, 103)
        self.ui.tv_history.setColumnWidth(5, 105)
        self.ui.tv_history.setColumnWidth(6, 161)
        self.ui.tv_history.horizontalHeader().setSectionResizeMode(Qtw.QHeaderView.ResizeMode.Fixed)

        self.ui.tv_history.verticalHeader().setDefaultSectionSize(60)

    def star_timer(self):
        self.timer.start(500)

    def search_by_id(self, transaction_id):
        if transaction_id == "":
            self.ui.tv_history.setModel(self.model)
            self.set_column_sizes()
            return

        filtered_data = self.model.filter_by_id(transaction_id)
        if not filtered_data:
            transaction = retrieve_admin_transaction(transaction_id)
            if transaction:
                filtered_data = process_data(transaction, 3)
        new_model = HistoryModel(filtered_data)
        self.ui.tv_history.setModel(new_model)
        self.set_column_sizes(True)

    def initialize_receipt(self):
        model = self.ui.tv_history.model()
        if model is not None and model.rowCount() > 0:
            first_column_data = model.data(model.index(0, 0))
            self.receipt_widget.set_data(first_column_data)
        else:
            print("The table is empty.")
