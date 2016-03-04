# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\gui_crest.ui'
#
# Created: Fri Mar 04 20:02:43 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CrestDialog(object):
    def setupUi(self, CrestDialog):
        CrestDialog.setObjectName("CrestDialog")
        CrestDialog.resize(400, 320)
        CrestDialog.setMinimumSize(QtCore.QSize(400, 320))
        CrestDialog.setMaximumSize(QtCore.QSize(400, 320))
        font = QtGui.QFont()
        font.setFamily("Arial")
        CrestDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CrestDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(CrestDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtGui.QLabel(CrestDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.label_4 = QtGui.QLabel(CrestDialog)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(CrestDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 0, 1, 2)
        self.label = QtGui.QLabel(CrestDialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/crest_banner.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.line = QtGui.QFrame(CrestDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)
        self.label_2 = QtGui.QLabel(CrestDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.lineEdit_client_id = QtGui.QLineEdit(CrestDialog)
        self.lineEdit_client_id.setObjectName("lineEdit_client_id")
        self.gridLayout.addWidget(self.lineEdit_client_id, 5, 1, 1, 1)
        self.lineEdit_client_secret = QtGui.QLineEdit(CrestDialog)
        self.lineEdit_client_secret.setObjectName("lineEdit_client_secret")
        self.gridLayout.addWidget(self.lineEdit_client_secret, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(CrestDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(CrestDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_implicit = QtGui.QRadioButton(self.groupBox)
        self.radioButton_implicit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_implicit.setChecked(True)
        self.radioButton_implicit.setObjectName("radioButton_implicit")
        self.horizontalLayout_2.addWidget(self.radioButton_implicit)
        self.radioButton_user = QtGui.QRadioButton(self.groupBox)
        self.radioButton_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_user.setObjectName("radioButton_user")
        self.horizontalLayout_2.addWidget(self.radioButton_user)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)

        self.retranslateUi(CrestDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CrestDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CrestDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CrestDialog)

    def retranslateUi(self, CrestDialog):
        CrestDialog.setWindowTitle(QtGui.QApplication.translate("CrestDialog", "CREST Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CrestDialog", "<html><head/><body><p><span style=\" font-weight:600;\">CREST Client Details</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CrestDialog", "<html><head/><body><p><a href=\"https://developers.eveonline.com/applications/\"><span style=\" text-decoration: underline; color:#0000ff;\">Get credentials</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CrestDialog", "Client ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CrestDialog", "Client Secret:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CrestDialog", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_implicit.setText(QtGui.QApplication.translate("CrestDialog", "Implicit", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_user.setText(QtGui.QApplication.translate("CrestDialog", "User-supplied details", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
