import tkinter as tk
import random

def dis_lable():
    fortune = ["좋음", "보통", "별로", "나쁨", "매우나쁨"]
    lbl.configure(text = "%s님 오늘의 운세는 %s입니다."%(name.get(), random.choice(fortune)))

root = tk.Tk()
root.geometry("200x100")

name = tk.StringVar()

txt_name = tk.Entry(textvariable = name)
lbl = tk.Label(text = "")
btn = tk.Button(text = "오늘의 운세 보기", command = dis_lable)

txt_name.pack()
lbl.pack()
btn.pack()

tk.mainloop()