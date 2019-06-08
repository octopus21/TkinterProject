from tkinter import *
from local import *
from girişprogramı import *
import tkinter as tk
from hesapm import *

genel1()


print("Panel için şifre oluşturunuz.")
gkullanici = input("Hesap Adı Oluştur:")
gsifre = input("Hesap şifresi oluştur:")

kullanici = input("Hesap Adınızı Giriniz:")
sifre = input("Şifrenizi girin:")

if ((gkullanici == kullanici) and (gsifre == sifre)):

    iskelet = Tk()
    Topiskelet2 = Frame(iskelet)
    Topiskelet2.pack()
    text = Label(iskelet, text="Hoşgeldiniz admin sayfasına!")
    label = Label(iskelet,text="LOGLAR", bg="green")
    def dugmebasma():
        iskelet.destroy()
        giris()
        pass
    dugme2 = Button(Topiskelet2, text="LOG KAYITLARINI AÇ", bg="blue", command=dugmebasma)
    dugme2.pack()
    label.pack()
    text.pack()
    iskelet.mainloop()


elif((gkullanici != kullanici) and (gsifre == sifre)):
    print("kullanici adınız yanlış!")
    uyarı = Tk()
    yazı = Label(uyarı, text="Yanlış Kullanıcı adı")
    uyarı.title("YANLIŞ")
    uyarı.mainloop()

elif((gkullanici == kullanici) and (gsifre != sifre)):
    print("Giriş engellendi")

else:
    yardımpaneli = Tk()
    Topiskelet = Frame(yardımpaneli)
    Topiskelet.pack()
    cerceve = Frame(yardımpaneli)
    cerceve.pack(side=BOTTOM)
    label = Label(yardımpaneli, bg="red", text="YARDIMPANELI V1.2.01")
    label.pack()
    """
    DUGMEYE BASMA EVENTİ UNUTMAYALIM
    """
    def buttonClick():
            print("GONDERİLİYOR DUGMEYE BASILDI!")
            pass
    dugme1 = Button(Topiskelet,text="YARDIM", fg="red", command=buttonClick)
    print("Hesap bilgileriniz sunucularımıza ulaştırıyor")
    dugme1.pack()
    dugme1.grid()
    yardımpaneli.mainloop()
