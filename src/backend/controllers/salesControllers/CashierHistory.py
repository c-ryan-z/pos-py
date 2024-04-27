from PyQt6 import QtWidgets as Qtw, QtCore, QtGui

from src.backend.controllers.__customWidget.Receipt import Receipt
from src.backend.controllers.salesControllers.CashierHistoryModel import CashierHistoryModel
from src.backend.database.Scroll_Paginator import ScrollPaginator
from src.backend.database.sales.cashier import transactions_query, retrieve_transaction
from src.frontend.sales.CashierHistory import Ui_cashier_history


class CashierHistory(Qtw.QWidget):
    def __init__(self, sales_controller, main_app):
        super().__init__()
        self.model = None
        self.paginator = None
        self.ui = Ui_cashier_history()
        self.ui.setupUi(self)
        self.sales_controller = sales_controller
        self.main_app = main_app

        self.main_app.mainLoggedIn.connect(self.initialize_table)

        self.ui.tv_history.verticalHeader().setDefaultSectionSize(60)

        self.ui.tv_history.clicked.connect(self.handle_row_click)

        self.ui.tv_history.verticalScrollBar().valueChanged.connect(self.table_scroll_position)

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
        query = transactions_query()
        params = (cashier_id,)
        self.paginator = ScrollPaginator(query, params, name="cashier_transactions")
        data = self.paginator.get_next_page()
        data = self.process_data(data)
        self.model = CashierHistoryModel(data)
        self.ui.tv_history.setModel(self.model)
        self.set_column_sizes()

    def table_scroll_position(self, val):
        max_val = self.ui.tv_history.verticalScrollBar().maximum()

        scroll_trigger = max_val * 0.80
        if val >= scroll_trigger and self.paginator.has_next():
            new_data = self.paginator.get_next_page()
            new_data = self.process_data(new_data)
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
            self.ui.tv_history.setColumnWidth(2, 119)
            self.ui.tv_history.setColumnWidth(3, 119)
            self.ui.tv_history.setColumnWidth(4, 106)
        else:
            self.ui.tv_history.setColumnWidth(2, 103)
            self.ui.tv_history.setColumnWidth(3, 103)
            self.ui.tv_history.setColumnWidth(4, 105)

        self.ui.tv_history.setColumnWidth(0, 280)
        self.ui.tv_history.setColumnWidth(1, 280)
        self.ui.tv_history.setColumnWidth(5, 161)
        self.ui.tv_history.horizontalHeader().setSectionResizeMode(Qtw.QHeaderView.ResizeMode.Fixed)

        self.ui.tv_history.verticalHeader().setDefaultSectionSize(60)

    def process_data(self, tbl_data):
        processed_data = []
        for row in tbl_data:
            row = list(row)
            row[2] = "Done" if row[2] else "Voided"
            row.append("Detail")
            processed_data.append(tuple(row))
        return processed_data

    def star_timer(self):
        self.timer.start(500)

    def search_by_id(self, transaction_id):
        if transaction_id == "":
            self.ui.tv_history.setModel(self.model)
            self.set_column_sizes()
            return

        filtered_data = self.model.filter_by_id(transaction_id)
        if not filtered_data:
            transaction = retrieve_transaction(transaction_id)
            if transaction:
                filtered_data = self.process_data(transaction)
        new_model = CashierHistoryModel(filtered_data)
        self.ui.tv_history.setModel(new_model)
        self.set_column_sizes(True)

    def initialize_receipt(self):
        model = self.ui.tv_history.model()
        if model is not None and model.rowCount() > 0:
            first_column_data = model.data(model.index(0, 0))
            self.receipt_widget.set_data(first_column_data)
        else:
            print("The table is empty.")
