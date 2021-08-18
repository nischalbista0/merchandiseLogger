from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import time

root = Tk()
root.title("Employee")
root.geometry("1191x670")
root.resizable(0, 0)

# Background Image
bg = ImageTk.PhotoImage(file="images/employeeWindow.png")
bg_image = Label(root, image=bg).place(x=0, y=0)

# Displaying clock on screen
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    time_label.config(text=hour + ":" + minute + ":" + second)
    time_label.after(1000, clock)


time_label = Label(root, text="", font=("Comic Sans MS", 14, "bold"), bg="white")
time_label.place(x=1050, y=31)
clock()


# Creating buttons

btn1 = Button(root, text="Search", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn1.place(x=328, y=86)

btn2 = Button(root, text="LOGOUT", font=("Poppins", 12, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn2.place(x=1067, y=604)

btn3 = Button(root, text="Remove", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn3.place(x=235, y=448)

btn4 = Button(root, text="Clear", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn4.place(x=373, y=448)

btn5 = Button(root, text="Add To Cart", font=("Poppins", 11, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn5.place(x=95, y=448)

btn6 = Button(root, text="Total", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn6.place(x=85, y=538)

btn7 = Button(root, text="Generate", font=("Poppins", 12, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn7.place(x=176, y=538)

btn8 = Button(root, text="Clear", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn8.place(x=302, y=538)

btn9 = Button(root, text="Exit", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn9.place(x=416, y=538)


# Creating and placing labels

label1 = Label(root, text="Customer Details", bg="white", fg="brown", font=("Poppins", 16, "bold"))
label1.place(x=520, y=53)

label1 = Label(root, text="Products", bg="white", fg="brown", font=("Poppins", 16, "bold"))
label1.place(x=230, y=135)

label1 = Label(root, text="Bill Options", bg="white", fg="brown", font=("Poppins", 16, "bold"))
label1.place(x=219, y=495)

label1 = Label(root, text="Bill Number", bg="white", fg="black", font=("Poppins", 14))
label1.place(x=65, y=89)

label1 = Label(root, text="Customer Name", bg="white", fg="black", font=("Poppins", 14))
label1.place(x=435, y=89)

label1 = Label(root, text="Contact Number", bg="white", fg="black", font=("Poppins", 14))
label1.place(x=830, y=89)

label1 = Label(root, text="Select Category", bg="white", fg="black", font=("Poppins", 14))
label1.place(x=62, y=165)

label1 = Label(root, text="Sub Category", bg="white", fg="black", font=("Poppins", 14))
label1.place(x=62, y=230)

label1 = Label(root, text="Product", bg="white", fg="black", font=("Poppins", 14))
label1.place(x=62, y=295)

label1 = Label(root, text="Quantity", bg="white", fg="black", font=("Poppins", 14))
label1.place(x=62, y=355)


# Creating and placing entries

billNum = Entry(root, bd=0, width=12 , font=("Franklin Gothic Medium", 13))
billNum.place(x=180, y=92)

customerName = Entry(root, bd=0, width=22 , font=("Franklin Gothic Medium", 13))
customerName.place(x=590, y=92)

contactNum = Entry(root, bd=0, width=16 , font=("Franklin Gothic Medium", 13))
contactNum.place(x=985, y=92)

quantityEntry = Entry(root, width=42, relief='raised', font=("Poppins", 12))
quantityEntry.place(x=65, y=385)


# Creating and placing combo boxes

category = ttk.Combobox(root, value="", width=60)
category.place(x=65, y=195)

subCategory = ttk.Combobox(root, value="", width=60)
subCategory.place(x=65, y=260)

product = ttk.Combobox(root, value="", width=60)
product.place(x=65, y=325)

mainloop()
