import tkinter as tk

def bmi():
    h1 = int(txt_h.get())
    w1 = int(txt_w.get())
    bmi = w1 / (h1/100 * h1/100)
    if bmi <= 18.5:
        msg = "저체중"
    elif bmi <= 23:
        msg = "정상"
    elif bmi <= 25:
        msg = "과체중"
    else:
        msg = "비만"


    lbl_result.configure(text = "BMI지수:%.2f, 판정: %s" %(bmi, msg))

root = tk.Tk()
root.geometry("200x100")

h = tk.StringVar()
w = tk.StringVar()

txt_h = tk.Entry(textvariable = h)
txt_w = tk.Entry(textvariable = w)
lbl_result = tk.Label(text = "")
btn = tk.Button(text = "측정", command = bmi)

txt_h.pack()
txt_w.pack()
btn.pack()
lbl_result.pack()
tk.mainloop()

