from decimal import Decimal

from PyQt6 import QtCore


class InventoryModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def sort(self, column, order):
        self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=lambda x: x[column])
        if order == QtCore.Qt.SortOrder.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role != QtCore.Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == QtCore.Qt.Orientation.Horizontal:
            return ("Name", "Price", "Category", "Stock", "Active")[section]
        elif orientation == QtCore.Qt.Orientation.Vertical:
            return str(section + 1)
        return None

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, Decimal):
                return str(value)
            return value
        elif role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            return QtCore.Qt.AlignmentFlag.AlignCenter

    def update_data(self, new_data, sort_column, sort_order):
        old_row_count = self.rowCount()
        new_row_count = old_row_count + len(new_data)

        self.beginInsertRows(QtCore.QModelIndex(), old_row_count, new_row_count - 1)
        self._data += new_data
        self.endInsertRows()

        self.sort(sort_column, sort_order)

    def filter_by_id(self, item_id):
        filtered_data = [row for row in self._data if row[0] == item_id]
        return filtered_data

    def update_data_with_id(self, new_data):
        self.beginResetModel()
        self._data = new_data
        self.endResetModel()
