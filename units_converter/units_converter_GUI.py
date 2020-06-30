# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'units_converter_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(264, 182)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.E_nm_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.E_nm_sb.setMaximumSize(QtCore.QSize(100, 16777215))
        self.E_nm_sb.setDecimals(2)
        self.E_nm_sb.setMinimum(0.0)
        self.E_nm_sb.setMaximum(1000000000.0)
        self.E_nm_sb.setSingleStep(0.01)
        self.E_nm_sb.setProperty("value", 628.0)
        self.E_nm_sb.setObjectName("E_nm_sb")
        self.gridLayout.addWidget(self.E_nm_sb, 0, 0, 1, 1)
        self.E_cm_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.E_cm_sb.setMaximumSize(QtCore.QSize(100, 16777215))
        self.E_cm_sb.setDecimals(2)
        self.E_cm_sb.setMaximum(1000000000000000.0)
        self.E_cm_sb.setSingleStep(0.1)
        self.E_cm_sb.setObjectName("E_cm_sb")
        self.gridLayout.addWidget(self.E_cm_sb, 0, 1, 1, 1)
        self.E_eV_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.E_eV_sb.setMaximumSize(QtCore.QSize(100, 16777215))
        self.E_eV_sb.setDecimals(3)
        self.E_eV_sb.setMaximum(5000000.0)
        self.E_eV_sb.setSingleStep(0.001)
        self.E_eV_sb.setProperty("value", 1.55)
        self.E_eV_sb.setObjectName("E_eV_sb")
        self.gridLayout.addWidget(self.E_eV_sb, 1, 0, 1, 1)
        self.E_Hz_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.E_Hz_sb.setMaximumSize(QtCore.QSize(100, 16777215))
        self.E_Hz_sb.setDecimals(2)
        self.E_Hz_sb.setMaximum(1e+21)
        self.E_Hz_sb.setSingleStep(1.0)
        self.E_Hz_sb.setObjectName("E_Hz_sb")
        self.gridLayout.addWidget(self.E_Hz_sb, 1, 1, 1, 1)
        self.E_J_sb = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.E_J_sb.setMaximumSize(QtCore.QSize(100, 16777215))
        self.E_J_sb.setDecimals(2)
        self.E_J_sb.setMaximum(1e+16)
        self.E_J_sb.setSingleStep(0.01)
        self.E_J_sb.setObjectName("E_J_sb")
        self.gridLayout.addWidget(self.E_J_sb, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.E_nm_ref_sb = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.E_nm_ref_sb.setMaximumSize(QtCore.QSize(100, 16777215))
        self.E_nm_ref_sb.setDecimals(2)
        self.E_nm_ref_sb.setMinimum(-1e+17)
        self.E_nm_ref_sb.setMaximum(1e+17)
        self.E_nm_ref_sb.setSingleStep(0.01)
        self.E_nm_ref_sb.setProperty("value", 628.0)
        self.E_nm_ref_sb.setObjectName("E_nm_ref_sb")
        self.verticalLayout.addWidget(self.E_nm_ref_sb)
        self.E_cm_fom_nm_sb = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.E_cm_fom_nm_sb.setMaximumSize(QtCore.QSize(100, 16777215))
        self.E_cm_fom_nm_sb.setDecimals(3)
        self.E_cm_fom_nm_sb.setMinimum(-10000000000.0)
        self.E_cm_fom_nm_sb.setMaximum(10000000000.0)
        self.E_cm_fom_nm_sb.setSingleStep(1.0)
        self.E_cm_fom_nm_sb.setObjectName("E_cm_fom_nm_sb")
        self.verticalLayout.addWidget(self.E_cm_fom_nm_sb)
        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Units Converter"))
        self.E_nm_sb.setSuffix(_translate("Form", "nm"))
        self.E_cm_sb.setSuffix(_translate("Form", "cm-1"))
        self.E_eV_sb.setSuffix(_translate("Form", "eV"))
        self.E_Hz_sb.setSuffix(_translate("Form", "e14 Hz"))
        self.E_J_sb.setSuffix(_translate("Form", "J"))
        self.groupBox_2.setTitle(_translate("Form", "Relative cm-1"))
        self.E_nm_ref_sb.setSuffix(_translate("Form", "nm"))
        self.E_cm_fom_nm_sb.setSuffix(_translate("Form", "cm-1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

