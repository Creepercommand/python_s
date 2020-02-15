import tkinter as tk
import random



def dislable():
    lotto_list = list(range(1, 46))
    random.shuffle(lotto_list)
    lbl.configure(text = lotto_list[:6])
    lbl1.configure(text=lotto_list[6:12])
    lbl2.configure(text=lotto_list[12:18])
    lbl3.configure(text=lotto_list[18:24])
    lbl4.configure(text=lotto_list[24:30])


root = tk.Tk()
root.geometry("200x200")

lbl = tk.Label(text = "")
lbl1 = tk.Label(text = "")
lbl2 = tk.Label(text = "")
lbl3 = tk.Label(text = "")
lbl4 = tk.Label(text = "")

btn = tk.Button(text = "클릭", command = dislable)

lbl.pack()
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
btn.pack()
tk.mainloop()


