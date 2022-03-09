import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
# creating the main window widget
root = tk.Tk()

# creating a title for the window
root.title("Roy's Profile")

# creating an icon with ico format
root.iconbitmap("./academytest.ico")

# resizing the window - image for background should be adjusted by these dimensions
root.geometry("700x500")
root.resizable(False, False)

# Add image file
bg = PhotoImage(file="abstract.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# creating a canvas that will be the background for the displays
cnv = tk.Canvas(width=400, height=330)
cnv.place(x=150, y=60)
cnv.configure(background="light grey")

# creating labels for the headline, first name and last name and for the invisible text to be displayed after input
label2 = Label(root, text="Fill My Name", font="bold 30", background="light grey")
label2.place(x=230, y=80)
label3 = Label(root, text="enter my first name :", foreground="black", background="light grey", font=8)
label3.place(x=150, y=170)
label4 = Label(root, text="enter my last name :", foreground="black", background="light grey", font=8)
label4.place(x=150, y=200)
label5 = Label(root, text="", foreground="black", background="light grey", font=8)
label5.place(x=185, y=290)

# creating the entry widgets for the parameters
first_name = Entry(root, borderwidth=0, highlightthickness=0)
first_name.place(x=340, y=179)
last_name = Entry(root, borderwidth=0, highlightthickness=0)
last_name.place(x=340, y=209)

# adding a function that will tell us if a button was pressed then we check answers
button_pressed = StringVar()

# creating a button to submit the inputs
btn = ttk.Button(root, text="submit", width=20, command=lambda: button_pressed.set("button pressed"))
btn.place(x=280, y=250)
btn.wait_variable(button_pressed)  # this function will wait until a change has been made to button pressed variable

#links to git and lkedin


def callback_git():
    webbrowser.open_new(r"https://github.com/MopyKing")


def callback_linkedin():
    webbrowser.open_new(r"https://www.linkedin.com/in/roy-edri")


if first_name.get() != "roy" and first_name.get() != "Roy":
    label5.configure(text="This Is Not My Name, Try Again.", foreground="red")


elif last_name.get() != "edri" and last_name.get() != "Edri":
    label5.configure(text="This Is Not My Name, Try Again.", foreground="red")


else:  # creating button for the links of github and linked in
    label5.configure(text="You May Proceed To The Links Below!", foreground="green")
    git_btn_img = PhotoImage(file="gittest.png")
    git_btn = Button(root, image=git_btn_img, border=0, command=callback_git)
    git_btn.place(x=290, y=340)
    link_btn_img = PhotoImage(file="linktest.png")
    link_btn = Button(root, image=link_btn_img, border=0, command=callback_linkedin)
    link_btn.place(x=360, y=340)

root.mainloop()

