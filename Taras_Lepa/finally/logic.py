
from tkinter import *
import math

tk_calc = Tk()
tk_calc.configure(bg="#293C4A", bd=10)
calc_operator = ""
text_input = StringVar()
text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(columnspan=5, padx = 10, pady = 15)


sin, cos, tan = math.sin, math.cos, math.tan
p = math.pi


#main finction


def button_equal():
    global calc_operator
    try:
        temp_op = str(eval(calc_operator))
        text_input.set(temp_op)
        calc_operator = temp_op
    except ZeroDivisionError:
        temp_op = " 42 "
        text_input.set(temp_op)
        calc_operator = temp_op
    except:
        temp_op = "Try again "
        text_input.set(temp_op)
        calc_operator = temp_op


#set simbols
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)



#delete chars

# delete one char
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

#delete all char
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")


#trigonometry

def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)




#my function for factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)


def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)


def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+ calc_operator
    calc_operator = temp
    text_input.set(temp)    


#layout

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}
              
#first row

pi_num = Button(tk_calc, button_params, text='π',
                command=lambda:button_click(str(math.pi))).grid(row=2, column=0, sticky="nsew")

sine = Button(tk_calc, button_params, text='sin',
             command=trig_sin).grid(row=2, column=1, sticky="nsew")

cosine = Button(tk_calc, button_params, text='cos',
             command=trig_cos).grid(row=2, column=2, sticky="nsew")

tangent = Button(tk_calc, button_params, text='tan',
             command=trig_tan).grid(row=2, column=3, sticky="nsew")

cotangent = Button(tk_calc, button_params, text='cot',
             command=trig_cot).grid(row=2, column=4, sticky="nsew")

#second row

left_par = Button(tk_calc, button_params, text='(',
                  command=lambda:button_click('(')).grid(row=3, column=0, sticky="nsew")

right_par = Button(tk_calc, button_params, text=')',
                   command=lambda:button_click(')')).grid(row=3, column=1, sticky="nsew")   
int_div = Button(tk_calc, button_params, text='div',
                 command=lambda:button_click('//')).grid(row=3, column=2, sticky="nsew")
abs_value = Button(tk_calc, button_params, text='abs',
                   command=lambda:button_click('abs(')).grid(row=3, column=3, sticky="nsew")
factorial_button = Button(tk_calc, button_params, text='x!',
                   command=fact_func).grid(row=3, column=4, sticky="nsew")


#Third way

button_7 = Button(tk_calc, button_params_main, text='7',
                  command=lambda:button_click('7')).grid(row=4, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8',
                  command=lambda:button_click('8')).grid(row=4, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9',
                  command=lambda:button_click('9')).grid(row=4, column=2, sticky="nsew")
delete_one = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='DEL', command=button_delete, bg='#db701f').grid(row=4, column=3, sticky="nsew")
delete_all = Button(tk_calc, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
              text='AC', command=button_clear_all, bg='#db701f').grid(row=4, column=4, sticky="nsew")

#fivth way

button_4 = Button(tk_calc, button_params_main, text='4',
                  command=lambda:button_click('4')).grid(row=5, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5',
                  command=lambda:button_click('5')).grid(row=5, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6',
                  command=lambda:button_click('6')).grid(row=5, column=2, sticky="nsew")  

mul = Button(tk_calc, button_params_main, text='*',
             command=lambda:button_click('*')).grid(row=5, column=3, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/',
             command=lambda:button_click('/')).grid(row=5, column=4, sticky="nsew")

#sixth way

button_1 = Button(tk_calc, button_params_main, text='1',
                  command=lambda:button_click('1')).grid(row=6, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2',
                  command=lambda:button_click('2')).grid(row=6, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3',
                  command=lambda:button_click('3')).grid(row=6, column=2, sticky="nsew")
add = Button(tk_calc, button_params_main, text='+',
             command=lambda:button_click('+')).grid(row=6, column=3, sticky="nsew")
sub = Button(tk_calc, button_params_main, text='-',
             command=lambda:button_click('-')).grid(row=6, column=4, sticky="nsew")

#last way

button_0 = Button(tk_calc, button_params_main, text='0',
                  command=lambda:button_click('0')).grid(row=9, column=0, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.',
               command=lambda:button_click('.')).grid(row=9, column=1, sticky="nsew")
equal = Button(tk_calc, button_params_main, text='=',
               command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")

signs = Button(tk_calc, button_params_main, text='\u00B1',
               command=sign_change).grid(row=9, column=2, sticky="nsew")


tk_calc.mainloop()




