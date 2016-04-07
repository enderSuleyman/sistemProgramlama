from PyQt4 import QtCore, QtGui

import time
import subprocess

from time import strftime
import sys,os
import sqlite3 as sql

from PyQt4.QtCore import *

db_name = "data1.db"
bilgiler = ""

if not os.path.isfile(db_name):
    with sql.connect(db_name) as vt:
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS users("k_ad","k_sifre")""")
        im.execute("""INSERT INTO users VALUES("suleyman","1234")""")
        im.execute("""INSERT INTO users VALUES("ender","4321")""")
        im.execute("""INSERT INTO users VALUES("root","0000")""")
        vt.commit()
        im.execute("""SELECT * FROM users""")
        bilgiler = im.fetchall()
else:
    with sql.connect(db_name) as vt:
        im = vt.cursor()
        im.execute("""SELECT * FROM users""")
        bilgiler=im.fetchall()

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(387, 244)
        self.label_3=QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 15, 150, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 50, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.k_adi = QtGui.QLineEdit(Form)
        self.k_adi.setGeometry(QtCore.QRect(200, 50, 113, 27))
        self.k_adi.setObjectName(_fromUtf8("k_adi"))
        self.sifre = QtGui.QLineEdit(Form)
        self.sifre.setGeometry(QtCore.QRect(200, 100, 113, 27))
        self.sifre.setEchoMode(QtGui.QLineEdit.Password)
        self.sifre.setObjectName(_fromUtf8("sifre"))
        self.giris = QtGui.QPushButton(Form)
        self.giris.setGeometry(QtCore.QRect(140, 160, 98, 27))
        self.giris.setObjectName(_fromUtf8("giris"))
        self.giris.clicked.connect(self.yaz)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def yaz(self):
        for veri in bilgiler:
            kul_adi,sifre = veri
            if(self.k_adi.text().__eq__(kul_adi) and self.sifre.text().__eq__(sifre)):
                subprocess.Popen(uygulama_adi,shell=True,stdout=subprocess.PIPE)
                sys.exit()
            else:
             self.label_3.setText("yanlış bilgi girdiniz")


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Kullanici Adi :", None))
        self.label_2.setText(_translate("Form", "Sifre                :", None))
        self.giris.setText(_translate("Form", "Giris", None))

uygulama_adi = ""
vt = sql.connect("data1.db")
im = vt.cursor()
im.execute("""SELECT * FROM uygulama""")
uygulama_adi = ''.join(im.fetchone())  #bu kod olmadan çalışmıyor dönüştürme işlemi yapıyor.string
print(uygulama_adi)
vt.cursor()
vt.close()


while True:
    b = str(subprocess.Popen("ps x |grep -v grep |grep -c "+uygulama_adi, shell=True, stdout=subprocess.PIPE).stdout.read())
    if b.__contains__("1"):
        print(subprocess.Popen("pkill -9 "+uygulama_adi, shell=True, stdout=subprocess.PIPE).stdout.read())
        app = QtGui.QApplication(sys.argv)
        Dialog = QtGui.QDialog()
        ui = Ui_Form()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
        app.exec_()