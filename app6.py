import tkinter as tk
import random as r

def make_quiz():
    num1 = r.randint(0,999)
    num2 = r.randint(1,999)
    quiz = "%d + %d" %(num1, num2)
    return quiz


root = tk.Tk()
root.geometry("200x100")

def disp_lable():
    if int(usr_ans.get()) == ans:
        lbl_judge.configure(text = "정답" )
    else:
        lbl_judge.configure(text = "틀림 정답은 %d임" % ans )


quiz = make_quiz()
ans = eval(quiz)
usr_ans = tk.StringVar()
lbl_quiz = tk.Label(text = quiz)
txt = tk.Entry(textvariable = usr_ans)
btn = tk.Button(text = "계산", command = disp_lable)
lbl_judge = tk.Label(text = "")

lbl_quiz.pack()
txt.pack()
btn.pack()
lbl_judge.pack()
tk.mainloop()