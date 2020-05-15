from tkinter import *
from identity import *
from negative import *
from intensity import *
from powerlaw import *
from logtransformation import *

window = Tk()
window.title("Image Processing")

b1 = Button(window, text="Identity", fg="black",font="Arial",bd="3",command=identity).grid(row=0,column=0) #Create Button
b2 = Button(window, text="Intensity", fg="black", font="Arial", bd="3",command=intensity).grid(row=1,column=0)
b3 = Button(window, text="Power Low", fg="black",font="Arial",bd="3",command=powerlow).grid(row=2,column=0)
b4 = Button(window, text="Negative", fg="black",font="Arial",bd="3",command= negative).grid(row=3,column=0)
b5 = Button(window, text="log", fg="black",font="Arial",bd="3",command= log).grid(row=4,column=0)

photo = PhotoImage(file="tele.png")
label_1 = Label(window, image=photo)
label_1.grid(row=5,column=3,columnspan=3)

window.mainloop()