
 # Simple interaction with functions in tkinter

from tkinter import * # Here we import everything (*) from tkinter


 # Defining the GUI window. This is a veriable and can be named anything you like
root = Tk()
root.geometry("200x200")

 # This is a normal python function, that we call with the button.
 # In this function you can put any code and call it with the button, in this case, the button opens a second GUI window, called root2
def SecondScreen():
    root2 = Tk()
    root2.title("This window opened via a button")
    # When we want to configure the second window, now we have to use root2 for everything in this function.
    Label_1 = Label(root2, text="This GUI window was opened via a button").pack()


 # In buttons you are able to set "commands" which is where you can call functions etc.
 # In this example, I call the SecondScreen function, but without the () at the end.
 # If I was to use the () at the end, it would call the function before the buttons gets pressed.
Button_window2 = Button(root, text="Open second screen", bg="grey",command=SecondScreen).pack(pady=40)


# Like with this exit button, we can still use built in function in python, and call them with the button command
button_exit = Button(root, text="EXIT", command=exit).pack()

 # The mainloop is so the window keep running until you press on x or exit the script from terminal
root.mainloop() 


