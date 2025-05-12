from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x470")
root.resizable(width=False, height=False)

def clearf():
    ent.delete(0, "end")

def fresult():
    if ent.get() == "":
        pass
    elif ent.get()[0] == "0":
        ent.delete(0, "end")
    else:
        try:
            c_res = eval(ent.get())
            clearf()
            ent.insert("end", str(c_res))
        except Exception as e:
            clearf()
            ent.insert("end", "Error")

ent = Entry(root, font=("bold", 25))
ent.place(x=0, y=0, width=400, height=70)
ent['bg'] = "light blue"

def create_button(text, x, y, command=None):
    if command is None:
        command = lambda: ent.insert("end", text)
    btn = Button(root, text=text, font=("bold", 20), command=command)
    btn.place(x=x, y=y, width=100, height=80)
    return btn

btn_Parantez1 = create_button("(", 0, 70)
btn_Parantez2 = create_button(")", 100, 70)
btn_percent = create_button("%", 200, 70)
btn_Div = create_button("/", 300, 70)

btn7 = create_button("7", 0, 150)
btn8 = create_button("8", 100, 150)
btn9 = create_button("9", 200, 150)
btn_Mul = create_button("*", 300, 150)

btn4 = create_button("4", 0, 230)
btn5 = create_button("5", 100, 230)
btn6 = create_button("6", 200, 230)
btn_sub = create_button("-", 300, 230)

btn1 = create_button("1", 0, 310)
btn2 = create_button("2", 100, 310)
btn3 = create_button("3", 200, 310)
btn_sum = create_button("+", 300, 310)

btn_clear = Button(root, text="C", font=("bold", 20), command=clearf)
btn_clear.place(x=0, y=390, width=100, height=80)

btn0 = create_button("0", 100, 390)
btn_dot = create_button(".", 200, 390)

result = Button(root, text="=", font=("bold", 20), command=fresult)
result.place(x=300, y=390, width=100, height=80)

root.mainloop()