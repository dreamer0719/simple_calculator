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


#GUI         
root = tk.Tk()
root.geometry("400x500")
root.title('Simple Calulcator')

#Display problem
...

#Display result 
...


#Display operations

##Styles
num_btn_font = ('Arial', 20)
op_btn_font = ('Arial', 14)
btn_pad = {'padx: 5', 'pady: 5'}

##Button frame 
buttonframe = tk.Frame(root)
buttonframe.pack(anchor='center')

##Row 0
btn_percent = tk.Button(buttonframe, text='%', font=op_btn_font,height=2, width=4,).grid(row=0, column=0)
btn1 = tk.Button(buttonframe, text='1', font=num_btn_font, height=2, width=4).grid(row=0, column=1)
btn2 = tk.Button(buttonframe, text='2', font=num_btn_font, height=2, width=4).grid(row=0, column=2)
btn3 = tk.Button(buttonframe, text='3', font=num_btn_font, height=2, width=4).grid(row=0, column=3) 
btn_di = tk.Button(buttonframe, text='÷', font=op_btn_font, height=2, width=4).grid(row=0, column=4)

##Row 1
btn_sr = tk.Button(buttonframe, text='√', font=('Arial', 18))
btn_sr.grid(row=2, column=0)
btn4 = tk.Button(buttonframe, text='4', font=('Arial', 18))
btn4.grid(row=2, column=1)
btn5 = tk.Button(buttonframe, text='5', font=('Arial', 18))
btn5.grid(row=2, column=2)
btn6 = tk.Button(buttonframe, text='6', font=('Arial', 18))
btn6.grid(row=2, column=3)
btn_mul = tk.Button(buttonframe, text='x', font=('Arial', 18))
btn_mul.grid(row=2, column=4)

##Row 2
btn_power = tk.Button(buttonframe, text='xⁿ', font=('Arial', 18))
btn_power.grid(row=3, column=0)
btn7 = tk.Button(buttonframe, text='7', font=('Arial', 18))
btn7.grid(row=3, column=1)
btn8 = tk.Button(buttonframe, text='8', font=('Arial', 18))
btn8.grid(row=3, column=2)
btn9 = tk.Button(buttonframe, text='9', font=('Arial', 18))
btn9.grid(row=3, column=3)
btn_minus = tk.Button(buttonframe, text='-', font=('Arial', 18))
btn_minus.grid(row=3, column=4)

##Row 3
...
btn_neg = tk.Button(buttonframe, text='+/-', font=('Arial', 18))
btn_neg.grid(row=4, column=1)






root.mainloop()







#GUI
#root = tk.Tk()
#root.title("Simple Calculator")
#root.geometry('400x375')


#root.mainloop()
