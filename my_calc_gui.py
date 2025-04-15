import tkinter as tk

window = tk.Tk()

count = 0
def click():
    global count
    count += 1
    label.config(text=count)




button = tk.Button(window, text="Click Me!!!")
button.config(command=click) #performs the function when the button is clicked
button.config(bg='#ff6200', fg='yellow', font=('Ink Free', 50, 'bold'))
button.config(activebackground='#FF0000', activeforeground='yellow')



label = tk.Label(window, text=count)
label.config(font=('Monospace', 50,))
label.pack()



button.pack()

window.mainloop()