

 # The comments from "Creating GUI" will stay in all the examples and showcases.

from tkinter import * # Here we import everything (*) from tkinter


 # Defining the GUI window. This is a veriable and can be named anything you like
root = Tk()

 # Now that we have defined Tk() to a veriable, we can use that veriable with the tkinter attributes, and configure the GUI window.
root.title("Put GUI name here")

 # Creating the GUI we also want a set width and hight, to do that we use the geometry attribute.
root.geometry("400x400") # x and y 
 # You can set x and y to any number you want

 # With configure we can do a lot, fx: Change background colour 
root.configure(bg="Orange")

 # If we don't want the User of the program to be able to resize our program, and have it only set to the x and y value, we can do that with .resizable().
root.resizable(height=False, width=False)
 # We can also set one of them to true, and then fx the hight would be resizable but not the width


 # The mainloop is so the window keep running until you press on x or exit the script from terminal
root.mainloop() 


