 # In the Tkinter configuratin showcasem, we changed the background colour of the window. 
 # But we can chagne much more then just the GUI colour.
 # Using the knoledge from TkinterLabels, we create a label and is able to change that colour.

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
           
            
            # root, is the veriable we created to define the GUI window, we use that to tell the Label where to display (Because we are able to create multiple windows in one python script)
                    # text= is the text we want to display
Label_1 = Label(root, text="Lorem Ipsum. .", fg="White", bg="Orange").pack()
                                            # fg= means Foreground colour of text 
                                                        # bg= means Background colour of text

                                                            # fg= is for setting the text colour inside the button
Button_1 = Button(root, text="Button! ", height=2, width=20, fg="Orange", borderwidth=0).pack()

 # The mainloop is so the window keep running until you press on x or exit the script from terminal
root.mainloop() 


