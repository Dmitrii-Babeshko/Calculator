import tkinter as t
from decimal import Decimal as D
import operator as O

def button_click(text):
    enter.insert(t.END,str(text))

def button_clear():
    enter.delete(0,t.END)

def button_del_f():
    enter.delete(len(enter.get()) -1)

def brackets():
    enter.insert(t.END,str(')'))
    enter.insert(0,str('(')) 

def arithmetic_operation(operation):
    d = {'+':O.add, '-':O.sub, '*':O.mul, '/':O.truediv}
    return lambda x,y: d[operation](x,y)


def arithmetic_operation(operation, list_2):
    d = {'+':O.add, '-':O.sub, '*':O.mul, '/':O.truediv, '**':O.pow, '//':O.floordiv, '%':O.mod,}
    return d[operation](D(list_2[0]),D(list_2[1]))    

def calc():
    try:
        text=enter.get()
        opers = ['**','*', '//','/','%','-','+']
        for i in range(len(opers)):
            if opers[i] in text:
                list_ = text.split(opers[i])
                znak = opers[i]
                break
        result = arithmetic_operation(znak,list_)
        enter.insert(len(enter.get()), f'={result}')
    except:
        enter.delete(0, t.END)

def kor():
    try:
        text=enter.get()
        result = arithmetic_operation('**', [text, D(0.5)])
        enter.insert(len(enter.get()), f'={result}')
    except:
        enter.delete(0, t.END)

window = t.Tk()
window.title('Калькулятор')

enter = t.Entry(window, width=40,borderwidth=5 )
enter.grid(row=0, column=0,columnspan=4, padx=10, pady=10)

button_1 = t.Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = t.Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = t.Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = t.Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = t.Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = t.Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = t.Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = t.Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = t.Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = t.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_0.grid(row=5,column=1)

button_plus = t.Button(window, text="+", padx=20, pady=10, command=lambda: button_click('+'))
button_sub = t.Button(window, text="-", padx=20, pady=10, command=lambda: button_click('-'))
button_mul = t.Button(window, text="X", padx=20, pady=10, command=lambda: button_click('*'))
button_div = t.Button(window, text="/", padx=20, pady=10, command=lambda: button_click('/'))
button_exp = t.Button(window, text="^", padx=20, pady=10, command=lambda: button_click('**'))
button_dot = t.Button(window, text=".", padx=20, pady=10, command=lambda: button_click('.'))
button_del = t.Button(window, text="<", padx=20, pady=10, command=lambda: button_del_f())
button_del_all = t.Button(window, text="C", padx=20, pady=10, command=lambda: button_clear())
button_brack = t.Button(window, text="Корень", padx=20, pady=10, command=lambda: kor())
button_equal = t.Button(window, text="=", padx=20, pady=10, command=lambda: calc())

button_del_all.grid(row=1,column=0)
button_del.grid(row=1,column=1)
button_exp.grid(row=1,column=2)
button_div.grid(row=1,column=3)
button_mul.grid(row=2,column=3)
button_sub.grid(row=3,column=3)
button_plus.grid(row=4,column=3)
button_brack.grid(row=5,column=0)
button_dot.grid(row=5,column=2)
button_equal.grid(row=5,column=3)


window.bind("<Key>", lambda x: calc() if x.char=='\r'  else (x if x.char.isdigit() or x.char in ['+', '-', '*', '/', '%']  else enter.delete(len(enter.get()) -1)) )
enter.focus()
window.mainloop()