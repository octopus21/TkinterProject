from tkinter import *
from local import *
import tkinter as tk

def girissayfasiv2():
    sayfa1 = Tk()
    sayfa1label = Label(sayfa1, text="Giriş yapmak için bu programı açtınız :3", bg="blue")
    sayfa1label.pack()
    def Tıklama():
        sayfa1.destroy()
        giris()
        pass
    sayfa1button = Button(sayfa1, text="Giriş yapma sayfası için tıklatın.", bg="red", command=Tıklama)
    sayfa1button.pack()

    
