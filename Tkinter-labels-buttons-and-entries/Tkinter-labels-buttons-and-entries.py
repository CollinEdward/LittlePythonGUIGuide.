
from tkinter import * # Here we import everything (*) from tkinter


 # Defining the GUI window. This is a veriable and can be named anything you like
root = Tk()
root.geometry("500x200")

 # creating a Label is as simple as writing

label_name_here = Label(root, text="Hello World!").pack()

 # Labels can also be resied, and font changed.

label_2 = Label(root, text="Differnt font and size", font=("Helvica", 10)).pack()

 # Creating a buttond and entry is the same.

button_name = Button(root, text="Click!").pack()

 # buttons can also be resized with height= and width=
button_2 = Button(root, text="Resized!!", height=2, width=20).pack()

 # Entries are input fields for the user to input anything, this can be used to input number, letters etc, and use those things fx for a calculator.
entry_name = Entry(root).pack()


 # The mainloop is so the window keep running until you press on x or exit the script from terminal
root.mainloop() 


