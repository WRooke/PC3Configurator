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
        Dialog.resize(510, 602)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 511, 601))
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
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 40, 111, 411))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(52)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.DI24 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI24.setFont(font)
        self.DI24.setObjectName("DI24")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DI24)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.DO24 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DO24.setFont(font)
        self.DO24.setObjectName("DO24")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DO24)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.label_4)
        self.DI72 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI72.setFont(font)
        self.DI72.setObjectName("DI72")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.DI72)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.label_5)
        self.DO72 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DO72.setFont(font)
        self.DO72.setObjectName("DO72")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.DO72)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.DI110 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DI110.setFont(font)
        self.DI110.setObjectName("DI110")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.DI110)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.label_7)
        self.DO110 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DO110.setFont(font)
        self.DO110.setObjectName("DO110")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.DO110)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.AI = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AI.setFont(font)
        self.AI.setObjectName("AI")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.AI)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.AO = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AO.setFont(font)
        self.AO.setObjectName("AO")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.AO)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(130, 40, 201, 391))
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
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.runConfig)
        self.comboBox.activated.connect(self.listComms)
        self.commDrop()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_11.setText(_translate("Dialog", "Please specify model of Processor Module:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Processor Module"))
        self.comboBox.setCurrentText(_translate("Dialog", "Dummy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Communications"))
        self.label.setText(_translate("Dialog", "24V DI"))
        self.label_3.setText(_translate("Dialog", "24V DO"))
        self.label_4.setText(_translate("Dialog", "72V DI"))
        self.label_5.setText(_translate("Dialog", "72V DO"))
        self.label_6.setText(_translate("Dialog", "110V DI"))
        self.label_7.setText(_translate("Dialog", "110V DO"))
        self.label_8.setText(_translate("Dialog", "AI"))
        self.label_9.setText(_translate("Dialog", "AO"))
        self.label_10.setText(_translate("Dialog", "Run me"))
        self.label_2.setText(_translate("Dialog", "Please specify number of:"))
        self.pushButton.setText(_translate("Dialog", "Do the thing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "I/Os"))

    # Gets I/O numbers and runs configurator. Outputs to label
    def runConfig(self):
      DI24 = self.DI24.value()
      DO24 = self.DO24.value()
      DI72 = self.DI72.value()
      DO72 = self.DO72.value()
      DI110 = self.DI110.value()
      DO110 = self.DO110.value()
      AI = self.AI.value()
      AO = self.AO.value()
      SolFound, PCA_output, numPCAs, finalIO = config.IOconfigure(DI24, DO24, DI72, DO72, DI110, DO110, AI, AO)
      labeltext = str()
      if SolFound is True:
        for key in PCA_output:
          labeltext += (key + ": " + str(PCA_output[key]) + "\n")
        labeltext += ("Total number of PCAs: " + str(numPCAs) + "\n")
        labeltext += "I/O breakdown of controller: \n"
        for key in finalIO:
          labeltext += (key + ": " + str(finalIO[key]) + "\n")
      else:
        labeltext += ("Optimal controller not found, please adjust parameters" + "</body></html>")
      self.label_10.setText(labeltext)

    # Lists modules with selected communications protocols
    def listComms(self):
      text = self.comboBox.currentText()
      comms = config.getComms(text)
      commstring = "Modules with selected communications protocol: \n"
      for entry in comms:
        commstring += (entry + "\n")
      self.label_12.setText(commstring)


    def commDrop(self):
      _translate = QtCore.QCoreApplication.translate
      commList = config.populateComms()
      count = 0
      for entry in commList:
        self.comboBox.addItem("")
        self.comboBox.setItemText(count, _translate("Dialog", entry))
        count += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
