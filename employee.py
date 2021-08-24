from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import time
import sqlite3

window = Tk()
window.title("Employee")
window.geometry("1191x670")
window.resizable(0, 0)


# Background Image
bg = ImageTk.PhotoImage(file="Images/employeeWindow.png")
bg_image = Label(window, image=bg).place(x=0, y=0)


# Displaying clock on screen
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    time_label.config(text=hour + ":" + minute + ":" + second)
    time_label.after(1000, clock)


time_label = Label(window, text="", font=("Comic Sans MS", 14, "bold"), bg="white")
time_label.place(x=1050, y=31)
clock()


# Working with database
conn = sqlite3.connect('billDatabase.db')
c = conn.cursor()

# c.execute('''CREATE TABLE bill (
# customer_name text,
# contact_num integer,
# bill_num integer,
# date integer,
# product text,
# quantity integer,
# total integer )
# ''')


# Function that shows category values in 'Category' combobox
def category_input():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM second")
    records = c.fetchall()

    category_value = []
    for record in records:
        category_value.append(record[1])

    return category_value


# Function that shows sub category values in 'Sub Category' combobox
def sub_category_input():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM second")
    records = c.fetchall()

    sub_category_value = []
    for record in records:
        sub_category_value.append(record[2])

    return sub_category_value


# Function that shows products values in 'Product' combobox
def product_input():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM second")
    records = c.fetchall()

    product_value = []
    for record in records:
        product_value.append(record[0])

    return product_value


# Function that clears 'Products' frame
def clear():
    quantityEntry.delete(0, END)
    category.delete(0, END)
    subCategory.delete(0, END)
    product.delete(0, END)


# Function that clears 'Customer Details' frame and bill
def clear_bill():
    billNum.delete(0, END)
    customerName.delete(0, END)
    contactNum.delete(0, END)


bill_list = [[[], []]]
roww = 0
index_increment = 0
# Function that adds product to the bill
def addToCart():
    global roww
    global index_increment
    global lab1
    global lab2
    global lab3


    if category.get() == '' or subCategory.get() == '' or product.get() == '' or quantityEntry.get() == '':
        messagebox.showerror("Incomplete Information!!", "Please fill up all the details!")

    else:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT *, oid FROM second")
        records = c.fetchall()

        cp_value = []
        for record in records[:]:
            cp_value.append(record[8])

        product_value = []
        for record in records:
            product_value.append(record[0])

        bill_list[0][0].append(product.get())
        bill_list[0][1].append(int(quantityEntry.get()))


        for value in bill_list:
            lab1 = Label(myFrame, text=value[0][index_increment], width=20, bg="white")
            lab1.grid(row=roww, column=1)

            lab2 = Label(myFrame, text=value[1][index_increment], width=45, bg="white")
            lab2.grid(row=roww, column=2)

            index_of_product = product_value.index(product.get())
            lab3 = Label(myFrame, text=int(value[1][index_increment]) * int(cp_value[index_of_product]), width=6, bg="white")
            lab3.grid(row=roww, column=3)

            index_increment += 1
            roww += 1



# Function that removes product from the bill
def remove():
    global rowww
    global index_increment_copy
    global i

    index_increment_copy = 0
    i = 0
    rowww = 0

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM second")
    records = c.fetchall()

    cp_value = []
    for record in records[:]:
        cp_value.append(record[8])

    product_value = []
    for record in records:
        product_value.append(record[0])

    for widgets in myFrame.winfo_children():
        widgets.destroy()

    remove_product = str(product.get())
    remove_quantity = int(quantityEntry.get())

    bill_list[0][0].remove(remove_product)
    bill_list[0][1].remove(remove_quantity)
    print(bill_list)


    product_list = bill_list[0][0]
    quantity_list = bill_list[0][1]

    while i != len(product_list):
        labb1 = Label(myFrame, text=product_list[index_increment_copy], width=20, bg="white")
        labb1.grid(row=rowww, column=1)

        labb2 = Label(myFrame, text=quantity_list[index_increment_copy], width=45, bg="white")
        labb2.grid(row=rowww, column=2)

        index_of_product = product_value.index(product.get())
        labb3 = Label(myFrame, text=int(quantity_list[index_increment_copy]) * int(cp_value[index_of_product]), width=6, bg="white")
        labb3.grid(row=rowww, column=3)

        i += 1
        index_increment_copy += 1
        rowww += 1





# Function that generates bill and store bill data in database
def generate():
    if billNum.get() == '' or customerName.get() == '' or contactNum.get() == '' or category.get() == '' or subCategory.get() == '' or product.get() == '' or quantityEntry.get() == '':
        messagebox.showerror("Incomplete Information!!", "Please fill up all the details!")


# Creating buttons
btn1 = Button(window, text="Search", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn1.place(x=328, y=86)

btn2 = Button(window, text="LOGOUT", font=("Poppins", 12, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn2.place(x=1067, y=604)

btn3 = Button(window, text="Remove", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=remove)
btn3.place(x=235, y=448)

btn4 = Button(window, text="Clear", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=clear)
btn4.place(x=373, y=448)

btn5 = Button(window, text="Add To Cart", font=("Poppins", 11, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=addToCart)
btn5.place(x=95, y=448)

btn6 = Button(window, text="Total", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn6.place(x=85, y=538)

btn7 = Button(window, text="Generate", font=("Poppins", 12, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=generate)
btn7.place(x=176, y=538)

btn8 = Button(window, text="Clear", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=clear_bill)
btn8.place(x=302, y=538)

btn9 = Button(window, text="Exit", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn9.place(x=416, y=538)


# Creating and placing labels
label1 = Label(window, text="Customer Details", bg="white", fg="brown", font=("Poppins", 16, "bold"))
label1.place(x=520, y=53)

label2 = Label(window, text="Products", bg="white", fg="brown", font=("Poppins", 16, "bold"))
label2.place(x=230, y=135)

label3 = Label(window, text="Bill Options", bg="white", fg="brown", font=("Poppins", 16, "bold"))
label3.place(x=219, y=495)

label4 = Label(window, text="Bill Number", bg="white", fg="black", font=("Poppins", 14))
label4.place(x=65, y=89)

label5 = Label(window, text="Customer Name", bg="white", fg="black", font=("Poppins", 14))
label5.place(x=435, y=89)

label6 = Label(window, text="Contact Number", bg="white", fg="black", font=("Poppins", 14))
label6.place(x=830, y=89)

label7 = Label(window, text="Category", bg="white", fg="black", font=("Poppins", 14))
label7.place(x=62, y=165)

label8 = Label(window, text="Sub Category", bg="white", fg="black", font=("Poppins", 14))
label8.place(x=62, y=230)

label9 = Label(window, text="Product", bg="white", fg="black", font=("Poppins", 14))
label9.place(x=62, y=295)

label10 = Label(window, text="Quantity", bg="white", fg="black", font=("Poppins", 14))
label10.place(x=62, y=355)


# Bill labels
label11 = Label(window, text="Product Name", bg="white", font=("Poppins", 12, "bold"))
label11.place(x=540, y=288)

label12 = Label(window, text="Quantity", bg="white", font=("Poppins", 12, "bold"))
label12.place(x=800, y=288)

label13 = Label(window, text="Price", bg="white", font=("Poppins", 12, "bold"))
label13.place(x=1000, y=288)


# Creating and placing entries
billNum = Entry(window, bd=0, width=12 , font=("Franklin Gothic Medium", 13))
billNum.place(x=180, y=92)

customerName = Entry(window, bd=0, width=22 , font=("Franklin Gothic Medium", 13))
customerName.place(x=590, y=92)

contactNum = Entry(window, bd=0, width=16 , font=("Franklin Gothic Medium", 13))
contactNum.place(x=985, y=92)

quantityEntry = Entry(window, width=42, relief='raised', font=("Poppins", 12))
quantityEntry.place(x=65, y=385)


# Creating and placing combo boxes
category = ttk.Combobox(window, width=60)
category.place(x=65, y=195)
category['values'] = category_input()

subCategory = ttk.Combobox(window, width=60)
subCategory.place(x=65, y=260)
subCategory['values'] = sub_category_input()

product = ttk.Combobox(window, width=60)
product.place(x=65, y=325)
product['values'] = product_input()


# Frame for bill
wrapper1 = LabelFrame(window, height=800, width=1000, bd=0)

myCanvas = Canvas(wrapper1, height=265, width=590, bg='white')
myCanvas.pack(side=LEFT, fill='y', expand='yes')

myFrame = Frame(myCanvas)
myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

wrapper1.place(x=532, y=320)

conn.commit()
conn.close()

mainloop()
