import hashlib
import re

from PyQt6 import QtWidgets as Qtw, QtCore as Qtc, QtGui

from src.backend.database.admin.accounts import get_max_user_id, add_user, set_user_image, edit_initial_data, edit_user, \
    log_accounts
from src.frontend.admin.AccountEdit import Ui_account_popup
from src.setup_paths import Paths


class AccountPopUp(Qtw.QDialog):

    def __init__(self, parent=None, main_app=None, user_widget=None):
        super().__init__(parent, Qtc.Qt.WindowType.FramelessWindowHint)
        self.ui = Ui_account_popup()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.old_details = None
        self.image_path = None
        self.user_id = None
        self.mode = None
        self.user_widget = user_widget

        self.setModal(True)
        self.ui.le_userId.setEnabled(False)
        self.ui.pb_close.clicked.connect(self.close)
        self.ui.pb_img.clicked.connect(self.set_item_img)
        try:
            self.ui.pb_save.clicked.disconnect()
        except TypeError:
            pass
        self.ui.pb_save.clicked.connect(self.handle_save)

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

    def add_user(self):
        self.mode = "add"
        next_id = get_max_user_id() + 1
        self.ui.le_userId.setText(str(next_id))
        pixmap = QtGui.QPixmap(Paths.image("user.svg"))
        self.ui.lb_userImg.setPixmap(pixmap)

        self.ui.cb_role.setCurrentIndex(-1)
        self.ui.rb_bg.setExclusive(False)
        checked_button = self.ui.rb_bg.checkedButton()
        if checked_button is not None:
            checked_button.setChecked(False)
        self.ui.rb_bg.setExclusive(True)

        self.line_edit_listener()

        return self.exec() == Qtw.QDialog.DialogCode.Accepted

    def edit_user(self, user_id):
        if user_id is None:
            return

        self.user_id = user_id
        self.mode = "edit"
        self.ui.pb_save.setEnabled(False)
        editInfo = edit_initial_data(user_id)
        self.ui.le_userId.setText(str(user_id))
        self.ui.le_name.setText(editInfo[0])
        self.ui.le_phone.setText(editInfo[1])
        self.ui.le_email.setText(editInfo[2])
        self.ui.le_username.setText(editInfo[3])
        self.ui.cb_role.setCurrentIndex(editInfo[4] - 1)
        if editInfo[5]:
            self.ui.rb_true.setChecked(True)
        else:
            self.ui.rb_false.setChecked(True)
        self.line_edit_listener()

        self.old_details = (
            self.ui.le_name.text(),
            self.ui.le_email.text(),
            self.ui.le_phone.text(),
            self.ui.le_username.text(),
            self.ui.le_password.text(),
            self.ui.le_confirmPw.text(),
        )

        return self.exec() == Qtw.QDialog.DialogCode.Accepted

    def set_img(self, image):
        if image:
            image_data = image.tobytes()
            image = QtGui.QImage.fromData(image_data)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.ui.lb_userImg.setPixmap(pixmap)
        else:
            self.ui.lb_userImg.clear()

    def set_item_img(self):
        file_name, _ = Qtw.QFileDialog.getOpenFileName(self, "Upload User Image", "", "Images (*.png *.jpeg *.jpg)")
        if file_name:
            pixmap = QtGui.QPixmap(file_name)
            self.ui.lb_userImg.setPixmap(pixmap)
            self.image_path = file_name
            if self.mode == "edit":
                self.edit_validation()

    def line_edit_listener(self):
        validation_function = self.add_validation if self.mode == 'add' \
            else self.edit_validation
        self.ui.le_name.textChanged.connect(validation_function)
        self.ui.le_email.textChanged.connect(validation_function)
        self.ui.le_phone.textChanged.connect(validation_function)
        self.ui.le_username.textChanged.connect(validation_function)
        self.ui.le_password.textChanged.connect(validation_function)
        self.ui.le_confirmPw.textChanged.connect(validation_function)
        self.ui.cb_role.currentIndexChanged.connect(validation_function)
        self.ui.rb_bg.buttonClicked.connect(validation_function)

    def add_validation(self):
        fields = [self.ui.le_name, self.ui.le_email, self.ui.le_phone, self.ui.le_username, self.ui.le_password,
                  self.ui.le_confirmPw]

        for field in fields:
            if not field.text():
                self.ui.pb_save.setEnabled(False)
                return

        email = self.ui.le_email.text()
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            self.ui.pb_save.setEnabled(False)
            return

        phone = self.ui.le_phone.text()
        if not re.match(r"^\+?1?\d{9,15}$", phone):
            self.ui.pb_save.setEnabled(False)
            return

        password = self.ui.le_password.text()
        if len(password) < 10:
            self.ui.pb_save.setEnabled(False)
            return

        if self.ui.cb_role.currentIndex() == -1:
            self.ui.pb_save.setEnabled(False)
            return

        if self.ui.rb_bg.checkedButton() is None:
            self.ui.pb_save.setEnabled(False)
            return

        if self.ui.le_password.text() != self.ui.le_confirmPw.text():
            self.ui.pb_save.setEnabled(False)
            return

        self.ui.pb_save.setEnabled(True)

    def edit_validation(self):
        fields = [self.ui.le_name, self.ui.le_email, self.ui.le_phone, self.ui.le_username]

        for field in fields:
            if not field.text():
                self.ui.pb_save.setEnabled(False)
                return

        email = self.ui.le_email.text()
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            self.ui.pb_save.setEnabled(False)
            return

        phone = self.ui.le_phone.text()
        if not re.match(r"^\+?(\d{1,3})?[-. (]*(\d{1,3})?[-. )]*(\d{1,4})[-. ]*(\d{1,4})[-. ]*(\d{1,9})$", phone):
            self.ui.pb_save.setEnabled(False)
            return

        password = self.ui.le_password.text()
        if password and len(password) < 10:
            self.ui.pb_save.setEnabled(False)
            return

        if self.ui.le_password.text() != self.ui.le_confirmPw.text():
            self.ui.pb_save.setEnabled(False)
            return

        new_details = (
            self.ui.le_name.text(),
            self.ui.le_email.text(),
            self.ui.le_phone.text(),
            self.ui.le_username.text(),
            self.ui.le_password.text(),
            self.ui.le_confirmPw.text()
        )

        if self.image_path:
            self.ui.pb_save.setEnabled(True)
            return

        if new_details != self.old_details:
            self.ui.pb_save.setEnabled(True)
        else:
            self.ui.pb_save.setEnabled(False)

    def handle_save(self):
        if self.mode == "add":
            self.handle_save_add()
        elif self.mode == "edit":
            self.handle_save_edit()

    def handle_save_add(self):
        password = self.ui.le_password.text()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_id = add_user(
            self.ui.le_name.text(),
            self.ui.le_phone.text(),
            self.ui.le_email.text(),
            self.ui.le_username.text(),
            hashed_password,
            self.ui.cb_role.currentIndex() + 1,
            self.ui.rb_bg.checkedButton().text()
        )

        if self.image_path:
            set_user_image(user_id, self.image_path)

        log_accounts(self.user_widget.user_id, "Add", f"Added Account ID: {user_id}",
                     str(self.user_widget.session_id))

        self.close()
        self.image_path = None
        self.ui.pb_save.setEnabled(False)

    def handle_save_edit(self):
        fields = {}

        new_name = self.ui.le_name.text()
        if new_name != self.old_details[0]:
            fields["name"] = new_name

        new_email = self.ui.le_email.text()
        if new_email != self.old_details[1]:
            fields["email"] = new_email

        new_phone = self.ui.le_phone.text()
        if new_phone != self.old_details[2]:
            fields["phone"] = new_phone

        new_username = self.ui.le_username.text()
        if new_username != self.old_details[3]:
            fields["username"] = new_username

        password = self.ui.le_password.text()
        if password and password != self.old_details[4]:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            fields["password"] = hashed_password

        if fields:
            edit_user(fields, self.user_id)

        if self.image_path:
            set_user_image(self.user_id, self.image_path)

        log_accounts(self.user_widget.user_id, "Edit", f"Edited Account ID: {self.user_id} Edit Details: {fields}",
                     str(self.user_widget.session_id))

        self.close()
        self.ui.pb_save.setEnabled(False)
