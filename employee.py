from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import time
import sqlite3
import ast
from datetime import datetime

window = Tk()
window.title("Employee")
window.geometry("1191x670")
window.resizable(0, 0)


# Background Image
bg = ImageTk.PhotoImage(file="images/employeeWindow.png")
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


# Storing current date in a variable
current_date = datetime.today().strftime('%Y-%m-%d')


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


bill_list = [[[], [], []]]
product_list = bill_list[0][0]
quantity_list = bill_list[0][1]


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

        price_value = []

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

            bill_list[0][2].append(int(value[1][index_increment]) * int(cp_value[index_of_product]))

            index_increment += 1
            roww += 1

        print(bill_list)


index = 0
# Function that removes product from the bill
def remove():
    global roww
    global index
    global rowww
    global index_increment
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

    myFrame.configure(bg="white")

    remove_product = str(product.get())
    remove_quantity = int(quantityEntry.get())

    bill_list[0][0].remove(remove_product)
    index_of_product = product_value.index(product.get())
    bill_list[0][2].remove(remove_quantity * int(cp_value[index_of_product]))
    bill_list[0][1].remove(remove_quantity)

    print(bill_list)

    product_list = bill_list[0][0]
    quantity_list = bill_list[0][1]

    a = 0
    while i != len(product_list):
        labb1 = Label(myFrame, text=product_list[index_increment_copy], width=20, bg="white")
        labb1.grid(row=rowww, column=1)

        labb2 = Label(myFrame, text=quantity_list[index_increment_copy], width=45, bg="white")
        labb2.grid(row=rowww, column=2)

        index_of_product = product_value.index(product_list[a])
        # print(index_of_product)
        labb3 = Label(myFrame, text=int(quantity_list[index_increment_copy]) * int(cp_value[index_of_product]), width=6, bg="white")
        labb3.grid(row=rowww, column=3)

        # print(int(quantity_list[index_increment_copy]) * int(cp_value[index_of_product]))

        i += 1
        index_increment_copy += 1
        rowww += 1
        a += 1

    roww -= 1
    index += 1
    index_increment = len(bill_list[0][1])



def total():
    # global sum
    global index_increment

    sum = 0

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

    product_list = bill_list[0][0]
    quantity_list = bill_list[0][1]

    i = 0
    while i != len(quantity_list):
        product = bill_list[0][0][i]

        index_of_product = product_value.index(product)
        sum += int(quantity_list[i]) * int(cp_value[index_of_product])
        i += 1

    total_label = Label(myFrame2, text="Total", bg="white", font=("Poppins", 13), width=15)
    total_label.grid(row=0, column=0)

    total_amount = Label(myFrame2, text=f"Rs. {sum}", bg="white", font=("Poppins", 13), width=75)
    total_amount.grid(row=0, column=1)

    index_increment = len(bill_list[0][1])


# Function that generates bill and store bill data in database
def generate():
    global product_list
    global quantity_list
    global bill_label_1
    global bill_label_2
    global bill_label_3
    global bill_label_4

    product_list_string = f'"{product_list}"'
    print(product_list_string)
    quantity_list_string = f'"{quantity_list}"'

    if customerName.get() == '' or contactNum.get() == '' or category.get() == '' or subCategory.get() == '' or product.get() == '' or quantityEntry.get() == '':
        messagebox.showerror("Incomplete Information!!", "Please fill up all the details!")

    else:
        # -------------------------------------------------- Testing ---------------------------------------------------------------
        connect = sqlite3.connect('billDatabase.db')
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM bill")
        bill_records = cursor.fetchall()
        bill_number = int(bill_records[-1][2]) + 1

        connect.close()
        # -------------------------------------------------- Testing ---------------------------------------------------------------

        conn = sqlite3.connect('billDatabase.db')
        c = conn.cursor()

        c.execute(
            "INSERT INTO bill VALUES (:customer_name, :contact_num, :bill_num, :date, :product, :quantity, :total)",

            {
                'customer_name': customerName.get(),
                'contact_num': contactNum.get(),
                'bill_num' : bill_number,
                'date': current_date,
                'product': product_list_string,
                'quantity': quantity_list_string,
                'total': sum,
            })
        c.execute("SELECT *,oid FROM bill")

        records = c.fetchall()

        bill_label_1 = Label(window, text=customerName.get(), font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
        bill_label_1.place(x=670, y=230)
        bill_label_2 = Label(window, text=contactNum.get(), font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
        bill_label_2.place(x=670, y=255)
        bill_label_3 = Label(window, text=current_date, font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
        bill_label_3.place(x=995, y=230)
        bill_label_4 = Label(window, text=bill_number, font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
        bill_label_4.place(x=995, y=255)

        conn.commit()
        conn.close()


def search():
    global bill_label1
    global bill_label2
    global bill_label3
    global bill_label4

    # Adding blank label to hide the previous label (if present)
    blank_label1 = Label(window, text="", bg="white", width=28, height=3)
    blank_label1.place(x=673, y=230)

    blank_label2 = Label(window, text="", bg="white", width=16, height=3)
    blank_label2.place(x=995, y=230)

    # ------------------------------------------ Testing ------------------------------------------------------------------------
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM second")

    inventory_records = cursor.fetchall()
    print(inventory_records)

    products_and_cp = {}
    for record in inventory_records:
        products_and_cp[record[0]] = record[7]

    print(products_and_cp)
    # ------------------------------------------ Testing ------------------------------------------------------------------------

    conn = sqlite3.connect("billDatabase.db")
    c = conn.cursor()

    c.execute("SELECT * FROM bill")
    records = c.fetchall()

    # cp_value = []
    # for record in records[:]:
    #     cp_value.append(record[8])

    selected_bill_number = int(billNum.get())

    for record in records:
        if selected_bill_number == record[2]:
            bill_label1 = Label(window, text=record[0], font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
            bill_label1.place(x=670, y=230)
            bill_label2 = Label(window, text=record[1], font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
            bill_label2.place(x=670, y=255)
            bill_label3 = Label(window, text=record[3], font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
            bill_label3.place(x=995, y=230)
            bill_label4 = Label(window, text=record[2], font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
            bill_label4.place(x=995, y=255)
            total_label = Label(myFrame2, text="Total", bg="white", font=("Poppins", 13), width=15)
            total_label.grid(row=0, column=0)
            total_amount = Label(myFrame2, text=f"Rs. {record[6]}", bg="white", font=("Poppins", 13), width=75)
            total_amount.grid(row=0, column=1)

            # Products
            myList1 = record[4]
            products = ast.literal_eval(myList1)
            final_products = ast.literal_eval(products)
            print(final_products)

            # Quantities
            myList2 = record[5]
            quantities = ast.literal_eval(myList2)
            final_quantities = ast.literal_eval(quantities)

    # --------------------------------------------- Testing ---------------------------------------------------------------------------
            roow = 0
            for product in final_products:
                lab1 = Label(myFrame, text=product, width=20, bg="white")
                lab1.grid(row=roow, column=1)
                roow += 1

            rooww = 0
            for quantity in final_quantities:
                lab2 = Label(myFrame, text=quantity, width=45, bg="white")
                lab2.grid(row=rooww, column=2)

                lab3 = Label(myFrame, text=int(quantity) * int(products_and_cp[final_products[rooww]]), width=6, bg="white")
                lab3.grid(row=rooww, column=3)
                rooww += 1

    # --------------------------------------------- Testing ---------------------------------------------------------------------------


# Function that clears 'Customer Details' frame and bill
def clear_bill():
    billNum.delete(0, END)
    customerName.delete(0, END)
    contactNum.delete(0, END)

    for widgets in myFrame.winfo_children():
        widgets.destroy()

    myFrame.configure(bg="white")

    for widgets in myFrame2.winfo_children():
        widgets.destroy()

    myFrame2.configure(bg="white")

    bill_label1.place_forget()
    bill_label2.place_forget()
    bill_label3.place_forget()
    bill_label4.place_forget()


# Creating buttons
btn1 = Button(window, text="Search", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", comman=search)
btn1.place(x=328, y=86)

btn2 = Button(window, text="LOGOUT", font=("Poppins", 12, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
btn2.place(x=1067, y=604)

btn3 = Button(window, text="Remove", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=remove)
btn3.place(x=235, y=448)

btn4 = Button(window, text="Clear", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=clear)
btn4.place(x=373, y=448)

btn5 = Button(window, text="Add To Cart", font=("Poppins", 11, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=addToCart)
btn5.place(x=95, y=448)

btn6 = Button(window, text="Total", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=total)
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
label11 = Label(window, text="Product Name", bg="white", font=("Microsoft Sans Serif", 13, "bold"))
label11.place(x=540, y=288)

label12 = Label(window, text="Quantity", bg="white", font=("Microsoft Sans Serif", 13, "bold"))
label12.place(x=800, y=288)

label13 = Label(window, text="Price", bg="white", font=("Microsoft Sans Serif", 13, "bold"))
label13.place(x=1000, y=288)

label14 = Label(window, text="Customer Name :", bg="white", font=("Microsoft Sans Serif", 13))
label14.place(x=533, y=230)

label15 = Label(window, text="Contact Number :", bg="white", font=("Microsoft Sans Serif", 13))
label15.place(x=533, y=255)

label16 = Label(window, text="Date :", bg="white", font=("Microsoft Sans Serif", 13))
label16.place(x=940, y=230)

label17 = Label(window, text="Bill Number :", bg="white", font=("Microsoft Sans Serif", 13))
label17.place(x=889, y=255)


# Creating and placing entries
billNum = Entry(window, bd=0, width=12 , font=("Franklin Gothic Medium", 13))
billNum.place(x=180, y=92)

customerName = Entry(window, bd=0, width=22 , font=("Franklin Gothic Medium", 13))
customerName.place(x=590, y=92)
customerName.focus()

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

myCanvas = Canvas(wrapper1, height=230, width=590, bg='white')
myCanvas.pack(side=LEFT, fill='y', expand='yes')

myFrame = Frame(myCanvas)
myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

wrapper1.place(x=532, y=320)

# Frame for total
wrapper2 = LabelFrame(window, height=800, width=1000, bd=0)

myCanvas2 = Canvas(wrapper2, height=30, width=590, bg='white')
myCanvas2.pack(side=LEFT, fill='y', expand='yes')

myFrame2 = Frame(myCanvas2)
myCanvas2.create_window((0, 0), window=myFrame2, anchor='nw')

wrapper2.place(x=532, y=550)

conn.commit()
conn.close()

mainloop()
