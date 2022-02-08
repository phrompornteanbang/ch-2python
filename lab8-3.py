def triangle():
    b = ing(base.get())
    h = int(high.get())
    area1/2*b*h
    messagebox.showinfo("พื้นที่สามเหลี่ยม","คำตอบ %.2f" % area)


from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สามเหลื่ยม โดย พรหมพร เทียนแดง")
base = StringVar()
high = StringVar()
area = StringVar()

lb1 = Label(main, text="รับค่าฐาน: ", font=("Tahoma",18))
lb1.place(x=20, y=20)
tb1 = Entry(main, textvariable=base)
tb1.place(x=200, y=20, width=300, height=40)

lb2 = Label(main, text="รับค่าสูง: ", font=("Tahoma",18))
lb2.place(x=20, y=80)
tb2 = Entry(main, textvariable=base)
tb2.place(x=200, y=80, width=300, height=40)

btn = Button(main, text="คำนวณ", font=("Tahoma",18),command= teingle)
btn.place(x=200, y=150)