from datetime import datetime

from PyQt6 import QtCore


class ActivityLogsModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%d %H:%M:%S')
            return value

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role != QtCore.Qt.ItemDataRole.DisplayRole:
            return None
        if orientation == QtCore.Qt.Orientation.Horizontal:
            if self.columnCount() == 5:
                return ("Id", "Session ID", "Timestamp", "Activity Category", "Activity Type")[section]
            elif self.columnCount() == 6:
                return ("Id", "User ID", "Session ID", "Timestamp", "Activity Category", "Activity Type")[section]
        return None

    def sort(self, column, order):
        self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=lambda x: x[column])
        if order == QtCore.Qt.SortOrder.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()

    def filter_by_user_id(self, user_id):
        return [log for log in self._data if log[1] == user_id]

    def filter_by_activity_type(self, activity_type):
        return [log for log in self._data if log[4] == activity_type]
