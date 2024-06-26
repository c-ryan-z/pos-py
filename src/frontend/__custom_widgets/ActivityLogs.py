# Form implementation generated from reading ui file 'C:\Users\abarq\PycharmProjects\POS-PY\ui/ActivityLogs.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_activity_logs(object):
    def setupUi(self, activity_logs):
        activity_logs.setObjectName("activity_logs")
        activity_logs.resize(1600, 1030)
        activity_logs.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        activity_logs.setAutoFillBackground(False)
        activity_logs.setStyleSheet("QWidget#cashier_dashboard {\n"
"    background: #FFFFFF;\n"
"}")
        self.gb_container = QtWidgets.QGroupBox(parent=activity_logs)
        self.gb_container.setGeometry(QtCore.QRect(459, 40, 1131, 900))
        self.gb_container.setStyleSheet("QGroupBox {\n"
"    background: rgba(248,249,250, 1);\n"
"    border: 3px solid rgba(29,33,40, 1);\n"
"    border-radius:13px;\n"
"}")
        self.gb_container.setTitle("")
        self.gb_container.setObjectName("gb_container")
        self.le_sort = QtWidgets.QLineEdit(parent=self.gb_container)
        self.le_sort.setGeometry(QtCore.QRect(290, 30, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.le_sort.setFont(font)
        self.le_sort.setStyleSheet("QLineEdit {\n"
"    background: rgba(255,255,255,1); /* white */\n"
"  border-radius: 20px; \n"
"  border-width: 3px; \n"
"  border-color: rgba(29,33,40,1); /* neutral-800 */\n"
"  border-style: solid; \n"
"}")
        self.le_sort.setText("")
        self.le_sort.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.le_sort.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.le_sort.setObjectName("le_sort")
        self.tv_activity_logs = QtWidgets.QTableView(parent=self.gb_container)
        self.tv_activity_logs.setGeometry(QtCore.QRect(30, 80, 1081, 791))
        self.tv_activity_logs.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tv_activity_logs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tv_activity_logs.setDefaultDropAction(QtCore.Qt.DropAction.IgnoreAction)
        self.tv_activity_logs.setAlternatingRowColors(False)
        self.tv_activity_logs.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tv_activity_logs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tv_activity_logs.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.tv_activity_logs.setShowGrid(False)
        self.tv_activity_logs.setSortingEnabled(True)
        self.tv_activity_logs.setObjectName("tv_activity_logs")
        self.tv_activity_logs.horizontalHeader().setDefaultSectionSize(300)
        self.tv_activity_logs.horizontalHeader().setMinimumSectionSize(0)
        self.lb_logs = QtWidgets.QLabel(parent=self.gb_container)
        self.lb_logs.setGeometry(QtCore.QRect(30, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(24)
        font.setBold(True)
        self.lb_logs.setFont(font)
        self.lb_logs.setObjectName("lb_logs")
        self.gb_logdetails = QtWidgets.QGroupBox(parent=activity_logs)
        self.gb_logdetails.setGeometry(QtCore.QRect(20, 250, 421, 541))
        self.gb_logdetails.setStyleSheet("QGroupBox#gb_logdetails {\n"
"    border: 4px dashed rgba(255,102,183,1);\n"
"    border-radius: 4px;\n"
"}")
        self.gb_logdetails.setTitle("")
        self.gb_logdetails.setObjectName("gb_logdetails")
        self.lb_logs_2 = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_logs_2.setGeometry(QtCore.QRect(10, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        font.setBold(True)
        self.lb_logs_2.setFont(font)
        self.lb_logs_2.setObjectName("lb_logs_2")
        self.lb_logs_3 = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_logs_3.setGeometry(QtCore.QRect(10, 70, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_logs_3.setFont(font)
        self.lb_logs_3.setObjectName("lb_logs_3")
        self.lb_id = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_id.setGeometry(QtCore.QRect(50, 70, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_id.setFont(font)
        self.lb_id.setObjectName("lb_id")
        self.lb_logs_4 = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_logs_4.setGeometry(QtCore.QRect(10, 100, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_logs_4.setFont(font)
        self.lb_logs_4.setObjectName("lb_logs_4")
        self.lb_user_id = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_user_id.setGeometry(QtCore.QRect(60, 100, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_user_id.setFont(font)
        self.lb_user_id.setObjectName("lb_user_id")
        self.lb_timestamp = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_timestamp.setGeometry(QtCore.QRect(60, 130, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_timestamp.setFont(font)
        self.lb_timestamp.setObjectName("lb_timestamp")
        self.lb_logs_5 = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_logs_5.setGeometry(QtCore.QRect(10, 130, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_logs_5.setFont(font)
        self.lb_logs_5.setObjectName("lb_logs_5")
        self.lb_type = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_type.setGeometry(QtCore.QRect(10, 200, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_type.setFont(font)
        self.lb_type.setObjectName("lb_type")
        self.lb_category = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_category.setGeometry(QtCore.QRect(210, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_category.setFont(font)
        self.lb_category.setObjectName("lb_category")
        self.lb_session = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_session.setGeometry(QtCore.QRect(80, 160, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_session.setFont(font)
        self.lb_session.setObjectName("lb_session")
        self.lb_logs_6 = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_logs_6.setGeometry(QtCore.QRect(10, 160, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_logs_6.setFont(font)
        self.lb_logs_6.setObjectName("lb_logs_6")
        self.lb_details = QtWidgets.QLabel(parent=self.gb_logdetails)
        self.lb_details.setGeometry(QtCore.QRect(10, 250, 391, 211))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(False)
        self.lb_details.setFont(font)
        self.lb_details.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lb_details.setWordWrap(True)
        self.lb_details.setObjectName("lb_details")

        self.retranslateUi(activity_logs)
        QtCore.QMetaObject.connectSlotsByName(activity_logs)

    def retranslateUi(self, activity_logs):
        _translate = QtCore.QCoreApplication.translate
        activity_logs.setWindowTitle(_translate("activity_logs", "Form"))
        self.le_sort.setPlaceholderText(_translate("activity_logs", "Search Here"))
        self.lb_logs.setText(_translate("activity_logs", "Activity Logs"))
        self.lb_logs_2.setText(_translate("activity_logs", "Log Details"))
        self.lb_logs_3.setText(_translate("activity_logs", "ID:"))
        self.lb_id.setText(_translate("activity_logs", "ID:"))
        self.lb_logs_4.setText(_translate("activity_logs", "User:"))
        self.lb_user_id.setText(_translate("activity_logs", "User Id"))
        self.lb_timestamp.setText(_translate("activity_logs", "Timestamp"))
        self.lb_logs_5.setText(_translate("activity_logs", "Date:"))
        self.lb_type.setText(_translate("activity_logs", "Type"))
        self.lb_category.setText(_translate("activity_logs", "Category"))
        self.lb_session.setText(_translate("activity_logs", "Session Id"))
        self.lb_logs_6.setText(_translate("activity_logs", "Session:"))
        self.lb_details.setText(_translate("activity_logs", "Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    activity_logs = QtWidgets.QWidget()
    ui = Ui_activity_logs()
    ui.setupUi(activity_logs)
    activity_logs.show()
    sys.exit(app.exec())
