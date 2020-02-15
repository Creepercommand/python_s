import tkinter as tk
import random



def dislable():
    lotto_list = list(range(1, 46))
    random.shuffle(lotto_list)
    lbl.configure(text = lotto_list[:6])

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text = "")
btn = tk.Button(text = "클릭", command = dislable)

lbl.pack()
btn.pack()
tk.mainloop()


