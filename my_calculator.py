import tkinter as tk
from tkinter import ttk

Calculator = ''

#Handle when button is clicked
def handle_button_click(clicked_button_text):
    current_text = result_var.get()
    #Do the math operation
    if clicked_button_text == '=':
        try:
            #Replace the op inputs into actual math symbol for python
            expression = current_text.replace('x', '*').replace('÷', '/').replace('√', 'sqrt').replace('^', '**')
            result = eval(expression)

            #Check if the outpt is a whoe number
            if result.is_integer():
                result = int(result)  # Convert to integer if it's a whole number
            result_var.set(result)
        except Exception as e:
            result_var.set('Error')
    
    ###
    elif clicked_button_text == 'DEL':
        result_var.set(current_text[:-1])  # Remove the last character from the input
        if current_text == 'Error':
            result_var.set('')

    ###
    elif clicked_button_text == '%':
        result_var.set('')
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set('Error')
    
    ###
    elif clicked_button_text == '+/-':
        try:
            if current_text.startswith('-'):
                result_var.set(current_text[1:])
            else:
                result_var.set('-' + current_text)
        except:
            result_var.set('Error')

    ### Handle the other buttons
    else:
        result_var.set(current_text + clicked_button_text)



#GUI         
root = tk.Tk()
root.geometry("410x481")
root.title('Simple Calulcator')

#Ensure full column expansion
for i in range(5):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=2)

#Display inputs & output 
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var,
                        font=('Arial', 30), relief='ridge', justify='right') 
                        #relief = to create 3d affect (shadow)
                        ##justify = to align the text to the left/right
result_entry.grid(row=0, column=0, columnspan=5,sticky='nsew', 
                  padx=3, pady=3,ipady=15)

#Display operations

##Styles
num_btn_font = ('Arial', 20)
op_btn_font = ('Arial', 16)
btn_pad = {'padx: 5', 'pady: 5'}

##Button frame 
buttonframe = tk.Frame(root)#, bg='ghost white')
buttonframe.grid(row=1, column = 0, sticky ='nsew')
for i in range(5):
    buttonframe.columnconfigure(i, weight=1)
for i in range(5):
    buttonframe.rowconfigure(i, weight=1)

# () Button frame
paren_frame = tk.Frame(buttonframe)
paren_frame.grid(row=0, column=0, sticky='nsew')
# Make sure the parent frame shares column equally
paren_frame.columnconfigure(0, weight=1)
paren_frame.columnconfigure(1, weight=1)

## Row 0
open_btn = tk.Button(paren_frame, text='(', font=op_btn_font, height=3, width=2,bg='#e0e0e0',command=lambda: handle_button_click('('))
open_btn.grid(row=0, column=0,sticky='nsew')
close_btn = tk.Button(paren_frame, text=')', font=op_btn_font, height=3, width=2,bg='#e0e0e0',command=lambda: handle_button_click(')'))
close_btn.grid(row=0, column=1,sticky='nsew')
btn7 = tk.Button(buttonframe, text='7', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('7'))
btn7.grid(row=0, column=1,sticky='nsew')
btn8 = tk.Button(buttonframe, text='8', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('8'))
btn8.grid(row=0, column=2,sticky='nsew')
btn9 = tk.Button(buttonframe, text='9', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('9'))
btn9.grid(row=0, column=3,sticky='nsew')
btn_di = tk.Button(buttonframe, text='÷', font=(op_btn_font, 20), height=2, width=4,bg='#e0e0e0',command=lambda: handle_button_click('÷'))
btn_di.grid(row=0, column=4,sticky='nsew')

## Row 1
btn_percent = tk.Button(buttonframe, text='%', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: handle_button_click('%'))
btn_percent.grid(row=1, column=0,sticky='nsew')
btn4 = tk.Button(buttonframe, text='4', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('4'))
btn4.grid(row=1, column=1,sticky='nsew')
btn5 = tk.Button(buttonframe, text='5', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('5'))
btn5.grid(row=1, column=2,sticky='nsew')
btn6 = tk.Button(buttonframe, text='6', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('6'))
btn6.grid(row=1, column=3,sticky='nsew')
btn_mul = tk.Button(buttonframe, text='x', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: handle_button_click('x'))
btn_mul.grid(row=1, column=4,sticky='nsew')

## Row 2
btn_sr = tk.Button(buttonframe, text='√', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: handle_button_click('√'))
btn_sr.grid(row=2, column=0,sticky='nsew')
btn1 = tk.Button(buttonframe, text='1', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('1'))
btn1.grid(row=2, column=1,sticky='nsew')
btn2 = tk.Button(buttonframe, text='2', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('2'))
btn2.grid(row=2, column=2,sticky='nsew')
btn3 = tk.Button(buttonframe, text='3', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('3'))
btn3.grid(row=2, column=3,sticky='nsew')
btn_minus = tk.Button(buttonframe, text='-', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: handle_button_click('-'))
btn_minus.grid(row=2, column=4,sticky='nsew')

## Row 3
btn_del = tk.Button(buttonframe, text='DEL', font=op_btn_font, height=2, width=4,bg='#f5a250',command=lambda: handle_button_click('DEL'))
btn_del.grid(row=3, column=0,sticky='nsew')
btn_neg = tk.Button(buttonframe, text='+/-', font=num_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: handle_button_click('+/-'))
btn_neg.grid(row=3, column=1,sticky='nsew')
btn0 = tk.Button(buttonframe, text='0', font=num_btn_font, height=2, width=4,bg='#d4d4d4',command=lambda: handle_button_click('0'))
btn0.grid(row=3, column=2,sticky='nsew')
btn_decimal = tk.Button(buttonframe, text='.', font=num_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: handle_button_click('.'))
btn_decimal.grid(row=3, column=3,sticky='nsew')
btn_plus = tk.Button(buttonframe, text='+', font=op_btn_font, height=2, width=4,bg='#e0e0e0',command=lambda: handle_button_click('+'))
btn_plus.grid(row=3, column=4,sticky='nsew')

## Row 4
btn_equals = tk.Button(buttonframe, text='=', font=num_btn_font, height=2, width=25,bg='#f5a250', command=lambda: handle_button_click('='))
btn_equals.grid(row=4, column=0, columnspan=5)

for key in "0123456789+-*/.='":
    root.bind(key, lambda event, key=key: handle_button_click(key))  # Bind number keys to their respective buttons

## keyboard supports
root.bind('^', lambda event: handle_button_click('^'))  # Shift+6 for power
root.bind('(', lambda event: handle_button_click('('))
root.bind(')', lambda event: handle_button_click(')'))
root.bind('<Return>', lambda event: handle_button_click('='))  # Enter key for equals
root.bind('<BackSpace>', lambda event: handle_button_click('DEL'))  # Delete key for clear

root.resizable(False, False)
root.mainloop()