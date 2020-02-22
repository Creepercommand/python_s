import tkinter as tk

def disp_lable():
    cal_age = int(txt_age.get())
    lbl.configure(text="hello %s, you are %d years old. you are %d in next year." % (txt_name.get(), cal_age, cal_age + 1))


root = tk.Tk()
root.geometry("200x100")

name = tk.StringVar()
age = tk.StringVar()

lbl = tk.Label(text="")
txt_name = tk.Entry(textvariable=name)
txt_age = tk.Entry(textvariable=age)
btn = tk.Button(text="PUSH", command=disp_lable)

lbl.pack()
txt_age.pack()
txt_name.pack()
btn.pack()

tk.mainloop()
