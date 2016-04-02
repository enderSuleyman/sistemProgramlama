# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uyg_sec.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import subprocess,sys




uygulama_adi = ""

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_uygulamasec(object):
    uygulama_adi = ""
    def setupUi(self, uygulamasec):
        uygulamasec.setObjectName(_fromUtf8("uygulamasec"))
        uygulamasec.setEnabled(True)
        uygulamasec.resize(398, 107)
        self.comboBox = QtGui.QComboBox(uygulamasec)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 351, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pushButton = QtGui.QPushButton(uygulamasec)
        self.pushButton.setGeometry(QtCore.QRect(140, 70, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.yaz)
        self.retranslateUi(uygulamasec)
        QtCore.QMetaObject.connectSlotsByName(uygulamasec)

    def retranslateUi(self, uygulamasec):
        uygulamasec.setWindowTitle(_translate("uygulamasec", "Form", None))
        self.pushButton.setText(_translate("uygulamasec", "Sec", None))


    def yaz(self):


        global  uygulama_adi
        uygulama_adi = str(self.comboBox.currentText())
        print(uygulama_adi)
        return  uygulama_adi

        sys.exit()





if __name__ == "__main__":
    komut = subprocess.Popen("cd /usr/share/applications/ && ls",shell=True,stdout=subprocess.PIPE)
    app = QtGui.QApplication(sys.argv)
    uygulamasec = QtGui.QWidget()
    ui = Ui_uygulamasec()
    ui.setupUi(uygulamasec)
    for uyg in komut.stdout.readlines():
        ui.comboBox.addItem(uyg.decode('utf-8').split(".")[0])
    uygulamasec.show()
    sys.exit(app.exec_())