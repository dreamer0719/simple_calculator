import tkinter as tk

Calculator = ''

#Function
def main():
    valid_functions = ['+', '-', '*','/']
    while True:
        try: 
            user_input = input().split()
            x, functions, y = user_input
            x = float(x)
            y = float(y)

            if functions not in valid_functions:
                raise ValueError
            
            elif '+' in functions:
                z = print('Result:',x+y)
                z
                break

            elif '-' in functions:
                z = print('Result:',x-y)
                z
                break

            elif '*' in functions:
                z = print('Result:',x*y)
                z
                break


        except ValueError and TypeError:
            print("Error")
            pass
        except KeyboardInterrupt:
            print("Keyboard") 
            break 


#Function to add value to input display
def add_to_input(value):
    current = user_input.get()
    user_input.set(current + str(value))


#GUI         
root = tk.Tk()
root.geometry("400x500")
root.title('Simple Calulcator')

#Display inputs
user_input = tk.StringVar()
user_input.set("") 
input_display = tk.Entry(root, textvariable=user_input, font=('Arial', 30), bd=10, relief='ridge', justify='right')
input_display.pack(fill='both', padx=10, pady=10)

#Display result 
...


#Display operations

##Styles
num_btn_font = ('Arial', 20)
op_btn_font = ('Arial', 16)
btn_pad = {'padx: 5', 'pady: 5'}

##Button frame 
buttonframe = tk.Frame(root)#, bg='ghost white')
buttonframe.pack(anchor='center')

## Row 0
btn_percent = tk.Button(buttonframe, text='%', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input('%'))
btn_percent.grid(row=0, column=0,sticky='nsew')
#btn_percent.bind("<KeyPress-1>", lambda event: add_to_input('%'))
btn7 = tk.Button(buttonframe, text='7', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('7'))
btn7.grid(row=0, column=1,sticky='nsew')
btn7.bind("<KeyPress-1>", lambda event: add_to_input('7'))
btn8 = tk.Button(buttonframe, text='8', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('8'))
btn8.grid(row=0, column=2,sticky='nsew')
btn8.bind("<KeyPress-1>", lambda event: add_to_input('8'))
btn9 = tk.Button(buttonframe, text='9', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('9'))
btn9.grid(row=0, column=3,sticky='nsew')
btn9.bind("<KeyPress-1>", lambda event: add_to_input('9'))
btn_di = tk.Button(buttonframe, text='÷', font=(op_btn_font, 20), height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input('÷'))
btn_di.grid(row=0, column=4,sticky='nsew')
btn_di.bind("<KeyPress-\>", lambda event: add_to_input('÷'))

## Row 1
btn_sr = tk.Button(buttonframe, text='√', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input(f'√({user_input.get()})'))
btn_sr.grid(row=1, column=0,sticky='nsew')
#btn_sr.bind("<KeyPress-1>", lambda event: add_to_input('1'))
btn4 = tk.Button(buttonframe, text='4', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('4'))
btn4.grid(row=1, column=1,sticky='nsew')
btn4.bind("<KeyPress-1>", lambda event: add_to_input('4'))
btn5 = tk.Button(buttonframe, text='5', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('5'))
btn5.grid(row=1, column=2,sticky='nsew')
btn5.bind("<KeyPress-1>", lambda event: add_to_input('5'))
btn6 = tk.Button(buttonframe, text='6', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('6'))
btn6.grid(row=1, column=3,sticky='nsew')
btn6.bind("<KeyPress-1>", lambda event: add_to_input('6'))
btn_mul = tk.Button(buttonframe, text='x', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input('x'))
btn_mul.grid(row=1, column=4,sticky='nsew')
#btn_mul.bind("<...>", lambda event: add_to_input('x'))

## Row 2
btn_power = tk.Button(buttonframe, text='xⁿ',font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input(f'({user_input.get()})^({user_input.get()})'))
btn_power.grid(row=2, column=0,sticky='nsew')
#btn_power.bind("<KeyPress-1>", lambda event: add_to_input('1'))
btn1 = tk.Button(buttonframe, text='1', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('1'))
btn1.grid(row=2, column=1,sticky='nsew')
btn1.bind("<KeyPress-1>", lambda event: add_to_input('1'))
btn2 = tk.Button(buttonframe, text='2', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('2'))
btn2.grid(row=2, column=2,sticky='nsew')
btn2.bind("<KeyPress-1>", lambda event: add_to_input('2'))
btn3 = tk.Button(buttonframe, text='3', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('3'))
btn3.grid(row=2, column=3,sticky='nsew')
btn3.bind("<KeyPress-1>", lambda event: add_to_input('3'))
btn_minus = tk.Button(buttonframe, text='-', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input('-'))
btn_minus.grid(row=2, column=4,sticky='nsew')
btn_minus.bind("<KeyPress-->", lambda event: add_to_input('-'))

## Row 3
btn_del = tk.Button(buttonframe, text='DEL', font=op_btn_font, height=2, width=4,bg='#f5a250',command=lambda: ...)
btn_del.grid(row=3, column=0,sticky='nsew')
btn_del.bind("<KeyPress-.>", lambda event: ...)
btn_neg = tk.Button(buttonframe, text='+/-', font=num_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input('...'))
btn_neg.grid(row=3, column=1,sticky='nsew')
btn_neg.bind("<KeyPress-1>", lambda event: add_to_input('...'))
btn0 = tk.Button(buttonframe, text='0', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: add_to_input('0'))
btn0.grid(row=3, column=2,sticky='nsew')
btn0.bind("<KeyPress-0>", lambda event: add_to_input('0'))
btn_decimal = tk.Button(buttonframe, text='.', font=num_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input('.'))
btn_decimal.grid(row=3, column=3,sticky='nsew')
btn_decimal.bind("<KeyPress-.>", lambda event: add_to_input('.'))
btn_plus = tk.Button(buttonframe, text='+', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: add_to_input('+'))
btn_plus.grid(row=3, column=4,sticky='nsew')
btn_plus.bind("<KeyPress-=>", lambda event: add_to_input('+'))

## Row 4
btn_equals = tk.Button(buttonframe, text='=', font=num_btn_font, height=2, width=24,bg='#f5a250')
btn_equals.grid(row=4, column=0, columnspan=5)
btn_equals.bind("<KeyPress-Return>", lambda event: ...)




root.mainloop()