from src.backend.controllers.__customWidget.Receipt import Receipt
from src.frontend.__custom_widgets.CustomMessageBox import Ui_custom_modal
from src.backend.controllers.controller_utility import shadow_effect
from PyQt6 import QtWidgets as Qtw, QtGui, QtCore as Qtc
from src.setup_paths import Paths


class CustomMessageBox(Qtw.QDialog):
    def __init__(self, parent=None, main_app=None):
        super().__init__(parent, Qtc.Qt.WindowType.FramelessWindowHint)
        self.ui = Ui_custom_modal()
        self.ui.setupUi(self)
        self.movie = None
        self.receipt = None
        self.main_app = main_app

        self.ui.pb_yes.clicked.connect(self.accept)
        self.ui.pb_no.clicked.connect(self.reject)
        self.ui.pb_close.clicked.connect(self.close)
        self.setModal(True)

        shadow_effect(self.ui.pb_yes)
        shadow_effect(self.ui.pb_no)

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

    def confirmAction(self, title, question, movie=None):
        self.ui.sw_messagebox.setCurrentIndex(0)
        self.disableChoices()

        self.ui.pb_yes.setText("Yes")
        self.ui.pb_yes.setStyleSheet("background-color: #00CC00; color: #FEFEFE;")
        self.ui.pb_no.setVisible(True)

        self.ui.lb_title.setText(title)
        self.ui.lb_message.setText(question)
        self.ui.lb_element.setVisible(True)

        if movie is None:
            self.ui.lb_element.setVisible(False)
        else:
            self.movie = QtGui.QMovie(Paths.getGif(movie))

        return self.exec() == Qtw.QDialog.DialogCode.Accepted

    def notifyAction(self, title, message, movie=None):
        self.ui.sw_messagebox.setCurrentIndex(0)
        self.disableChoices()

        self.ui.pb_yes.setText("OK")
        self.ui.pb_yes.setStyleSheet("background-color: #FF66B7; color: #FEFEFE;")
        self.ui.pb_no.setVisible(False)

        self.ui.lb_title.setText(title)
        self.ui.lb_message.setText(message)

        if movie is None:
            self.ui.lb_element.setVisible(False)
        else:
            self.movie = QtGui.QMovie(Paths.getGif(movie))
            self.movie.setScaledSize(self.ui.lb_element.size())
            self.ui.lb_element.setMovie(self.movie)
            self.movie.start()

        return self.exec() == Qtw.QDialog.DialogCode.Accepted

    def multipleChoices(self, title, question, choices):
        self.ui.sw_messagebox.setCurrentIndex(0)
        self.ui.lb_title.setText(title)
        self.ui.lb_message.setText(question)
        self.ui.lb_element.setVisible(False)
        self.ui.pb_yes.setVisible(False)
        self.ui.pb_no.setVisible(False)

        self.ui.pb_choice_1.setText(str(choices[0]))
        self.ui.pb_choice_2.setText(str(choices[1]))
        self.ui.pb_choice_3.setText(str(choices[2]))
        self.ui.pb_choice_4.setText(str(choices[3]))

        self.ui.pb_choice_1.clicked.connect(lambda: self.done(choices[0]))
        self.ui.pb_choice_2.clicked.connect(lambda: self.done(choices[1]))
        self.ui.pb_choice_3.clicked.connect(lambda: self.done(choices[2]))
        self.ui.pb_choice_4.clicked.connect(lambda: self.done(choices[3]))

        return self.exec()

    def disableChoices(self):
        self.ui.pb_choice_1.setVisible(False)
        self.ui.pb_choice_2.setVisible(False)
        self.ui.pb_choice_3.setVisible(False)
        self.ui.pb_choice_4.setVisible(False)

    def show_receipt(self, transaction_id):
        self.ui.sw_messagebox.setCurrentIndex(1)
        self.receipt = Receipt(self)
        self.receipt.set_data(transaction_id)

        vbox = Qtw.QVBoxLayout()
        vbox.addWidget(self.receipt)
        self.ui.receipt_layout.addLayout(vbox)

        return self.exec()
