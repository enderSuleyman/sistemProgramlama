#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tkinter import *
class Uygulama(object):
    def __init__(self):

        self.etiket = Label(text="şifrelemek istediğiniz uygulumayı aşağıdaki listeden seçin:\n netbeans \n libreoffice \n"
                                 "filezilla\nfirefox", fg="blue", bg="white"
                            , font="Times 20 italic", cursor="bottom_side")
        self.etiket2=Label(text="\nyeni kullanıcı adı:", fg="green")
        self.etiket3=Label(text="\nyeni şifre:", fg="green")
        def kaydet():
            dosya=open("yenikayit.txt","w")
            metin=giris.get()
            metin2=giris2.get()

            dosya.write(metin )

            dosya.write(metin2)
        giris2=Entry()
        giris=Entry()


        self.etiket.pack()
        self.etiket2.pack()
        giris.pack()
        self.etiket3.pack()
        giris2.pack()
        self.baslık=pencere.title("--Uygulama Şifreleme--")
        dugme2=Button(text="KAYDET", command=kaydet)
        dugme2.pack()
pencere=Tk()
pencere.geometry("625x350+300+200")

dugme = Button(text="Çıkış", fg="red", command = pencere.quit)
dugme.pack()
uyg = Uygulama()



mainloop()

