import tkinter as tk

def displable():
    lbl.configure(text = " 안녕하세요")

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text = "")
btn = tk.Button(text = "클릭하세요", command = displable)

lbl.pack()
btn.pack()
tk.mainloop()