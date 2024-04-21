from PyQt6 import QtWidgets as Qtw


class CustomLeLeaveEvent(Qtw.QLineEdit):
    def leaveEvent(self, event):
        if self.parent() is not None:
            self.parent().setFocus()
