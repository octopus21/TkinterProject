from tkinter import *
import tkinter as tk
import os

temp = 'tempfile.temp'

def giris():
    global isimE
    global sifreE
    global roots
    global main

    main = Tk()
    main.title('Giriş')
    intruction = Label(main, text='Hesap bilgilerini oluşturunuz\n',)
    intruction.grid(row=0, column=0, sticky=E)

    nameL = Label(main, text='Panel Hesabı Adı: ')
    pwordL = Label(main, text='Panel hesabı şifresi: ') # ^^
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)
    isimE = Entry(main)
    sifreE = Entry(main,show="*")
    sifreE.grid(row=2, column=1)
    isimE.grid(row=1, column=1)
    def click():
        with open(temp, 'w') as f:
            f.write(isimE.get())
            f.write("\n")
            f.write(sifreE.get())
            f.close()

        main.destroy()
        panel()
        pass
    dugme = Button(main, text="Üyel ol", command=click)
    dugme.grid(columnspan=2, sticky=W)

    def panel():
            global isimgiris1
            global sifregiris1

            panel1 = Tk()
            panel1.title("LPANELV1.1.2")
            isimgiris = Label(panel1, text="Hesabınızın İsmi tekrar:")
            sifregiris = Label(panel1, text="Hesabınızın şifresi tekrar:")
            isimgiris.grid(row=1, column=0, sticky=W)
            sifregiris.grid(row=2, column=0, sticky=W)
            sifregiris1 = Entry(panel1, show="*")
            isimgiris1 = Entry(panel1)
            isimgiris1.grid(row=1, column=1)
            sifregiris1.grid(row=2, column=1)
            dugmex = Button(panel1, text="Giriş", bg="red", command=panel2)
            dugmex.grid(columnspan=2, sticky=W)

            panel1.mainloop()
    def panel2():
        with open(temp) as f:
            data = f.readlines()
            isim = data[0].rstrip()
            sifre = data[1].rstrip()
            """
            anim = data[2]
            """
            print(isim)
            print(sifre)
            if sifregiris1.get() == sifre and isimgiris1.get() == isim:
                print("Giriş yapıldı ip alınıyor...")
                den = Tk()
                den.title("test v.5.0.1.")
                serverpanelv1 = Label(den, text="Sunucularınızı girin /Source/")
                serverpanelg = Entry(den)
                serverpanelv1.grid(row=1, column=0)
                serverpanelg.grid(row=1, column=1)
