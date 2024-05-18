from tkinter import*
from tkinter.ttk import*

from time import strftime

root=Tk()
root.title("Digital Clock")
def time():
    st = strftime('%a %d %b %H:%M:%S %Y')
    Lab.config(text=st)
    Lab.after(1000,time)

Lab = Label(root, font=("ds-digital",70), background="black",foreground="red")
Lab.pack(anchor="center")
time()

mainloop()