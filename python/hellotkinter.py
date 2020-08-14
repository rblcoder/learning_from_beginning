# https://github.com/PacktPublishing/Python-GUI-Programming-with-Tkinter
"""Hello Developer from Tkinter!"""


from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("800x600")
label = Label(root, text="Welcome Python Developer!", font=("TkDefaultFont", 64), wraplength=600)
label.pack()
root.mainloop()
