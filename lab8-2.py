from tkinter import *
window = Tk()
window.geometry ("800x500")
window.title("โดย พรหมพร เทียนแดง")
lb = Label( window , text="ยินดีต้อนรับเข้าสู่ python", font=("Freesiaupc",24))
lb.place(x=50, y=10)

lb2 = Label( window , text="รับค่ารัศมี", font=(" Freesiaupc",18))
lb2.place(x=50, y=50)

tb1 = Entry()
tb1.place(x=150, y=60)

lb3 = Label( window , text="ผลลัพท์", font=(" Freesiaupc",18))
lb3.place(x=50, y=90)

tb2 = Entry()
tb2.place(x=150, y=100)

btn = Button(window , text="")