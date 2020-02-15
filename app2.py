import tkinter as tk
import random

def dis_lable():
    fortune = ["좋음","보통","별로","나쁨","많이 나쁨"]
    lbl.configure(text = random.choice(fortune))

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text = "")
btn = tk.Button(text = "오늘의 운세", command = dis_lable)

lbl.pack()
btn.pack()
tk.mainloop()