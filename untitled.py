# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import config

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 718)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(5, 10, 496, 706))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 69, 22))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setGeometry(QtCore.QRect(180, 50, 161, 271))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 141, 251))
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(250, 40, 201, 391))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 181, 371))
        self.label_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(360, 500, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 116, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.DI24_IsoCheck = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI24_IsoCheck.setFont(font)
        self.DI24_IsoCheck.setChecked(False)
        self.DI24_IsoCheck.setAutoRepeat(False)
        self.DI24_IsoCheck.setAutoExclusive(False)
        self.DI24_IsoCheck.setAutoRepeatDelay(1)
        self.DI24_IsoCheck.setAutoRepeatInterval(1)
        self.DI24_IsoCheck.setTristate(False)
        self.DI24_IsoCheck.setObjectName("DI24_IsoCheck")
        self.gridLayout.addWidget(self.DI24_IsoCheck, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.DI24 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI24.setFont(font)
        self.DI24.setObjectName("DI24")
        self.gridLayout.addWidget(self.DI24, 0, 1, 1, 1)
        self.DI24_ISO = QtWidgets.QSpinBox(self.layoutWidget)
        self.DI24_ISO.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI24_ISO.setFont(font)
        self.DI24_ISO.setObjectName("DI24_ISO")
        self.gridLayout.addWidget(self.DI24_ISO, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(15, 345, 116, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setMinimumSize(QtCore.QSize(68, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)
        self.DO110 = QtWidgets.QSpinBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DO110.sizePolicy().hasHeightForWidth())
        self.DO110.setSizePolicy(sizePolicy)
        self.DO110.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DO110.setFont(font)
        self.DO110.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DO110.setObjectName("DO110")
        self.gridLayout_6.addWidget(self.DO110, 0, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(15, 200, 116, 52))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.DI72 = QtWidgets.QSpinBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI72.setFont(font)
        self.DI72.setObjectName("DI72")
        self.gridLayout_4.addWidget(self.DI72, 0, 1, 1, 1)
        self.DI72_IsoCheck = QtWidgets.QCheckBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI72_IsoCheck.setFont(font)
        self.DI72_IsoCheck.setChecked(False)
        self.DI72_IsoCheck.setAutoRepeat(False)
        self.DI72_IsoCheck.setAutoExclusive(False)
        self.DI72_IsoCheck.setAutoRepeatDelay(1)
        self.DI72_IsoCheck.setAutoRepeatInterval(1)
        self.DI72_IsoCheck.setTristate(False)
        self.DI72_IsoCheck.setObjectName("DI72_IsoCheck")
        self.gridLayout_4.addWidget(self.DI72_IsoCheck, 1, 0, 1, 1)
        self.DI72_ISO = QtWidgets.QSpinBox(self.layoutWidget2)
        self.DI72_ISO.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI72_ISO.setFont(font)
        self.DI72_ISO.setObjectName("DI72_ISO")
        self.gridLayout_4.addWidget(self.DI72_ISO, 1, 1, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(15, 255, 116, 24))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setMinimumSize(QtCore.QSize(68, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.DO72 = QtWidgets.QSpinBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DO72.setFont(font)
        self.DO72.setObjectName("DO72")
        self.gridLayout_3.addWidget(self.DO72, 0, 1, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget4.setGeometry(QtCore.QRect(15, 285, 116, 52))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(68, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)
        self.DI110 = QtWidgets.QSpinBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI110.setFont(font)
        self.DI110.setObjectName("DI110")
        self.gridLayout_5.addWidget(self.DI110, 0, 1, 1, 1)
        self.DI110_IsoCheck = QtWidgets.QCheckBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI110_IsoCheck.setFont(font)
        self.DI110_IsoCheck.setChecked(False)
        self.DI110_IsoCheck.setAutoRepeat(False)
        self.DI110_IsoCheck.setAutoExclusive(False)
        self.DI110_IsoCheck.setAutoRepeatDelay(1)
        self.DI110_IsoCheck.setAutoRepeatInterval(1)
        self.DI110_IsoCheck.setTristate(False)
        self.DI110_IsoCheck.setObjectName("DI110_IsoCheck")
        self.gridLayout_5.addWidget(self.DI110_IsoCheck, 1, 0, 1, 1)
        self.DI110_ISO = QtWidgets.QSpinBox(self.layoutWidget4)
        self.DI110_ISO.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI110_ISO.setFont(font)
        self.DI110_ISO.setObjectName("DI110_ISO")
        self.gridLayout_5.addWidget(self.DI110_ISO, 1, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(15, 410, 126, 148))
        self.widget.setObjectName("widget")
        self.AILayout = QtWidgets.QVBoxLayout(self.widget)
        self.AILayout.setContentsMargins(0, 0, 0, 0)
        self.AILayout.setObjectName("AILayout")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(68, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)
        self.AI = QtWidgets.QSpinBox(self.widget)
        self.AI.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AI.setFont(font)
        self.AI.setObjectName("AI")
        self.gridLayout_7.addWidget(self.AI, 0, 1, 1, 1)
        self.AI_IsoCheck = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AI_IsoCheck.setFont(font)
        self.AI_IsoCheck.setChecked(False)
        self.AI_IsoCheck.setAutoRepeat(False)
        self.AI_IsoCheck.setAutoExclusive(False)
        self.AI_IsoCheck.setAutoRepeatDelay(1)
        self.AI_IsoCheck.setAutoRepeatInterval(1)
        self.AI_IsoCheck.setTristate(False)
        self.AI_IsoCheck.setObjectName("AI_IsoCheck")
        self.gridLayout_7.addWidget(self.AI_IsoCheck, 1, 0, 1, 1)
        self.AI_ISO = QtWidgets.QSpinBox(self.widget)
        self.AI_ISO.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AI_ISO.setFont(font)
        self.AI_ISO.setObjectName("AI_ISO")
        self.gridLayout_7.addWidget(self.AI_ISO, 1, 1, 1, 1)
        self.AILayout.addLayout(self.gridLayout_7)
        self.AICheckboxes = QtWidgets.QFormLayout()
        self.AICheckboxes.setObjectName("AICheckboxes")
        self.AIUni10V = QtWidgets.QCheckBox(self.widget)
        self.AIUni10V.setObjectName("AIUni10V")
        self.AICheckboxes.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.AIUni10V)
        self.AICurrent = QtWidgets.QCheckBox(self.widget)
        self.AICurrent.setObjectName("AICurrent")
        self.AICheckboxes.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.AICurrent)
        self.AIBi10V = QtWidgets.QCheckBox(self.widget)
        self.AIBi10V.setObjectName("AIBi10V")
        self.AICheckboxes.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.AIBi10V)
        self.AINTC = QtWidgets.QCheckBox(self.widget)
        self.AINTC.setObjectName("AINTC")
        self.AICheckboxes.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AINTC)
        self.AIUni36V = QtWidgets.QCheckBox(self.widget)
        self.AIUni36V.setObjectName("AIUni36V")
        self.AICheckboxes.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.AIUni36V)
        self.AIPT100 = QtWidgets.QCheckBox(self.widget)
        self.AIPT100.setObjectName("AIPT100")
        self.AICheckboxes.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.AIPT100)
        self.AIBi36V = QtWidgets.QCheckBox(self.widget)
        self.AIBi36V.setObjectName("AIBi36V")
        self.AICheckboxes.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.AIBi36V)
        self.AIPT1000 = QtWidgets.QCheckBox(self.widget)
        self.AIPT1000.setObjectName("AIPT1000")
        self.AICheckboxes.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.AIPT1000)
        self.AILayout.addLayout(self.AICheckboxes)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(15, 565, 118, 74))
        self.widget1.setObjectName("widget1")
        self.AOLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.AOLayout.setContentsMargins(0, 0, 0, 0)
        self.AOLayout.setObjectName("AOLayout")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_9 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(68, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)
        self.AO = QtWidgets.QSpinBox(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AO.setFont(font)
        self.AO.setObjectName("AO")
        self.gridLayout_8.addWidget(self.AO, 0, 1, 1, 1)
        self.AOLayout.addLayout(self.gridLayout_8)
        self.AOCheckboxes = QtWidgets.QVBoxLayout()
        self.AOCheckboxes.setObjectName("AOCheckboxes")
        self.AOUni10V = QtWidgets.QCheckBox(self.widget1)
        self.AOUni10V.setObjectName("AOUni10V")
        self.AOCheckboxes.addWidget(self.AOUni10V)
        self.AOCurrent = QtWidgets.QCheckBox(self.widget1)
        self.AOCurrent.setObjectName("AOCurrent")
        self.AOCheckboxes.addWidget(self.AOCurrent)
        self.AOLayout.addLayout(self.AOCheckboxes)
        self.widget2 = QtWidgets.QWidget(self.tab)
        self.widget2.setGeometry(QtCore.QRect(12, 108, 118, 74))
        self.widget2.setObjectName("widget2")
        self.DO24Layout = QtWidgets.QVBoxLayout(self.widget2)
        self.DO24Layout.setContentsMargins(0, 0, 0, 0)
        self.DO24Layout.setObjectName("DO24Layout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setMinimumSize(QtCore.QSize(68, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.DO24 = QtWidgets.QSpinBox(self.widget2)
        self.DO24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DO24.setFont(font)
        self.DO24.setObjectName("DO24")
        self.gridLayout_2.addWidget(self.DO24, 0, 1, 1, 1)
        self.DO24Layout.addLayout(self.gridLayout_2)
        self.DO24Checkboxes = QtWidgets.QFormLayout()
        self.DO24Checkboxes.setObjectName("DO24Checkboxes")
        self.DO_A05 = QtWidgets.QCheckBox(self.widget2)
        self.DO_A05.setObjectName("DO_A05")
        self.DO24Checkboxes.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.DO_A05)
        self.DO_A15 = QtWidgets.QCheckBox(self.widget2)
        self.DO_A15.setObjectName("DO_A15")
        self.DO24Checkboxes.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.DO_A15)
        self.DO_A10 = QtWidgets.QCheckBox(self.widget2)
        self.DO_A10.setObjectName("DO_A10")
        self.DO24Checkboxes.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.DO_A10)
        self.DO24Layout.addLayout(self.DO24Checkboxes)
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        self.AI_IsoCheck.clicked['bool'].connect(self.AI_ISO.setEnabled)
        self.DI110_IsoCheck.clicked['bool'].connect(self.DI110_ISO.setEnabled)
        self.DI24_IsoCheck.clicked['bool'].connect(self.DI24_ISO.setEnabled)
        self.DI72_IsoCheck.clicked['bool'].connect(self.DI72_ISO.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.runConfig)
        self.comboBox.activated.connect(self.listComms)
        self.commDrop()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PC3 Configurator"))
        self.label_11.setText(_translate("Dialog", "Please specify model of Processor Module:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Processor Module"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Communications"))
        self.label_10.setText(_translate("Dialog", "Run me"))
        self.label_2.setText(_translate("Dialog", "Please specify number of:"))
        self.pushButton.setText(_translate("Dialog", "Do the thing"))
        self.DI24_IsoCheck.setText(_translate("Dialog", "Isolated"))
        self.label.setText(_translate("Dialog", "24V DI"))
        self.label_7.setText(_translate("Dialog", "110V DO"))
        self.label_4.setText(_translate("Dialog", "72V DI"))
        self.DI72_IsoCheck.setText(_translate("Dialog", "Isolated"))
        self.label_5.setText(_translate("Dialog", "72V DO"))
        self.label_6.setText(_translate("Dialog", "110V DI"))
        self.DI110_IsoCheck.setText(_translate("Dialog", "Isolated"))
        self.label_8.setText(_translate("Dialog", "AI"))
        self.AI_IsoCheck.setText(_translate("Dialog", "Isolated"))
        self.AIUni10V.setText(_translate("Dialog", "Uni10V"))
        self.AICurrent.setText(_translate("Dialog", "Current"))
        self.AIBi10V.setText(_translate("Dialog", "Bi10V"))
        self.AINTC.setText(_translate("Dialog", "NTC"))
        self.AIUni36V.setText(_translate("Dialog", "Uni36V"))
        self.AIPT100.setText(_translate("Dialog", "PT100"))
        self.AIBi36V.setText(_translate("Dialog", "Bi36V"))
        self.AIPT1000.setText(_translate("Dialog", "PT1000"))
        self.label_9.setText(_translate("Dialog", "AO"))
        self.AOUni10V.setText(_translate("Dialog", "Uni10V"))
        self.AOCurrent.setText(_translate("Dialog", "Current"))
        self.label_3.setText(_translate("Dialog", "24V DO"))
        self.DO_A05.setText(_translate("Dialog", "0.5A"))
        self.DO_A15.setText(_translate("Dialog", "1.5A"))
        self.DO_A10.setText(_translate("Dialog", "1.0A"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "I/Os"))
        commList = config.populateComms()
        count = 0
        for entry in commList:
          self.comboBox.addItem("")
          self.comboBox.setItemText(count, _translate("Dialog", entry))
          count += 1

    def runConfig(self):
      DI24 = self.DI24.value()
      if self.DI24_IsoCheck.isChecked() is True:
        ISODI24 = self.DI24_ISO.value()
      else:
        ISODI24 = 0
      DO24 = self.DO24.value()

      DI72 = self.DI72.value()
      if self.DI72_IsoCheck.isChecked() is True:
        ISODI72 = self.DI72_ISO.value()
      else:
        ISODI72 = 0
      DO72 = self.DO72.value()

      DI110 = self.DI110.value()
      if self.DI110_IsoCheck.isChecked() is True:
        ISODI110 = self.DI110_ISO.value()
      else:
        ISODI110 = 0
      DO110 = self.DO110.value()

      AI = self.AI.value()
      if self.DI24_IsoCheck.isChecked() is True:
        AIISO = self.AI_ISO.value()
      else:
        AIISO = 0
      AO = self.AO.value()

      AI_bool, AO_bool, DO24_bool = self.IOCheckboxes()
      AI_check = False
      AO_check = False
      if self.AI.value() == 0:
        AI_check = True
      if self.AO.value() == 0:
        AO_check = True
      if self.AI.value() != 0:
        for key in AI_bool:
          if AI_bool[key] is True:
            AI_check = True
      if self.AO.value() != 0:
        for key in AO_bool:
          if AO_bool[key] is True:
            AO_check = True

      if AI_check == True and AO_check == True:
        labeltext = config.IOconfigure(DI24, ISODI24, DO24, DI72, ISODI72, DO72, DI110, ISODI110, DO110, AI, AIISO, AO,
                                       AI_bool, AO_bool, DO24_bool)
        self.label_10.setText(labeltext)
      else:
        self.label_10.setText("Please select at least one analog type for both input and output")

    def listComms(self):
      text = self.comboBox.currentText()
      comms = config.getComms(text)
      commstring = "Modules with selected communications protocol: \n"
      for entry in comms:
        commstring += (entry + "\n")
      self.label_12.setText(commstring)

    # Populates communication protocol drop down list
    def commDrop(self):
      _translate = QtCore.QCoreApplication.translate
      commList = config.populateComms()
      count = 0
      for entry in commList:
        self.comboBox.addItem("")
        self.comboBox.setItemText(count, _translate("Dialog", entry))
        count += 1
      self.listComms()

    def IOCheckboxes(self):
        AIBool = dict()
        AOBool = dict()
        DOBool = dict()
        for i in range(self.AICheckboxes.count()):
            AIBool[self.AICheckboxes.itemAt(i).widget().objectName()] = self.AICheckboxes.itemAt(i).widget().isChecked()
        for j in range(self.AOCheckboxes.count()):
            AOBool[self.AOCheckboxes.itemAt(j).widget().objectName()] = self.AOCheckboxes.itemAt(j).widget().isChecked()
        for k in range(self.DO24Checkboxes.count()):
            DOBool[self.DO24Checkboxes.itemAt(k).widget().objectName()] = self.DO24Checkboxes.itemAt(k).widget().isChecked()
        return AIBool, AOBool, DOBool


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
