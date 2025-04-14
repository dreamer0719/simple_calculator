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

            

main()







#GUI
#root = tk.Tk()
#root.title("Simple Calculator")
#root.geometry('400x375')


#root.mainloop()
