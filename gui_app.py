from tkinter import *

def button_action(*args):
	print(len(args), args)

root = Tk()
button1 = Button(root, text = "what do i do?", command = button_action)
button1.pack()
root.mainloop()