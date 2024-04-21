from PyQt6 import QtWidgets as Qtw, QtGui, QtCore
from src.setup_paths import Paths


class CustomSpinBox(Qtw.QSpinBox):

    def __init__(self, *args, **kwargs):
        super(CustomSpinBox, self).__init__(*args, **kwargs)

        up_icon = Paths.getSalesElements("plus-small.svg")
        down_icon = Paths.getSalesElements("minus-small.svg")

        self.up_button_icon = QtGui.QIcon(up_icon)
        self.down_button_icon = QtGui.QIcon(down_icon)

        self.setButtonSymbols(Qtw.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.up_button = Qtw.QPushButton(self.up_button_icon, '', self)
        self.down_button = Qtw.QPushButton(self.down_button_icon, '', self)
        self.up_button.setMinimumSize(32, 32)
        self.down_button.setMinimumSize(32, 32)
        self.up_button.setMaximumSize(32, 32)
        self.down_button.setMaximumSize(32, 32)

        self.up_button.setIconSize(QtCore.QSize(20, 20))
        self.down_button.setIconSize(QtCore.QSize(20, 20))

        self.up_button.setStyleSheet("""
            background-color: #f044bc; border: none; border-radius: 4px; subcontrol-position: right;
            """)

        self.down_button.setStyleSheet("""
                    background-color: #f8f4f4; border: none; border-radius: 4px;
                    """)

        self.up_button.clicked.connect(self.increment)
        self.down_button.clicked.connect(self.decrement)

        self.button_layout = Qtw.QHBoxLayout()
        self.button_layout.setContentsMargins(5, 0, 5, 0)
        self.button_layout.addWidget(self.down_button)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.up_button)

        self.setLayout(self.button_layout)

    def increment(self):
        if self.value() < self.maximum():
            self.setValue(self.value() + 1)

    def decrement(self):
        if self.value() > self.minimum():
            self.setValue(self.value() - 1)

    def leaveEvent(self, event):
        if self.parent() is not None:
            self.parent().setFocus()
