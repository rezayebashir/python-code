from tkinter import *
def click():
    print('hello')
window = Tk()
button = Button(window, text='Click')
button.config(command=click)
button.config(font=('INK free',50, 'bold'))
button.config(background='red')
button.config(fg='#ffff11')
button.config(activebackground='white')
button.config(activeforeground='black')
button.pack()
window.mainloop()
