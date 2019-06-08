from tkinter import *
tempkaydı = "tempf.temp"
def genel1():
    global genelentry
    genel = Tk()
    genelAmacBilgisi = Label(genel, text="Kullanım amacınız nedir?")
    genelAmacBilgisi.grid(row=1, column=0)
    genelentry = Entry(genel)
    genelentry.grid(row=1, column=1)
    def dugmebasıldıgında():
        with open(tempkaydı, "w") as f:
            f.write(genelentry.get())
            f.write("\n")
            f.close()
        genel.destroy()
        print(genelentry)
    geneldugme = Button(genel, text="Onay İste", bg="red", fg="black", command=dugmebasıldıgında)
    geneldugme.grid(sticky=W, columnspan=2)


    genel.mainloop()

    def genel2():
        with open(tempkaydı) as f:
            kayıt = f.readlines()
            sebep = data[0].rstrip()
            print(sebep)
