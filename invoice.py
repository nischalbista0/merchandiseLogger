from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import ast

root = Tk()
root.title("Invoices")
root.geometry("1191x670")
root.resizable(0, 0)

# Background Image setup
bg = ImageTk.PhotoImage(file="images/invoice_window.png")
bg_image = Label(root, image=bg).place(x=0, y=0)


def search():
    for widgets in myFrame.winfo_children():
        widgets.destroy()

    label1 = Label(myFrame, text="Bill Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=13,
                   fg="#0D1C30")
    label1.grid(row=1, column=0)

    label2 = Label(myFrame, text="Customer Name", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20,
                   fg="#0D1C30")
    label2.grid(row=1, column=1)

    label3 = Label(myFrame, text="Contact Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20,
                   fg="#0D1C30")
    label3.grid(row=1, column=2)

    label4 = Label(myFrame, text="Date", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=10, fg="#0D1C30")
    label4.grid(row=1, column=3)

    if billNumber.get() != '':
        conn = sqlite3.connect('billDatabase.db')

        c = conn.cursor()

        c.execute("SELECT * FROM bill")

        records = c.fetchall()

        roww = 0
        rowww = 2
        for record in records:
            if record[2] == int(billNumber.get()):
                Label(myFrame, text=record[2], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"), width=15).grid(row=roww, column=0)
                Label(myFrame, text=record[0], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"), width=22).grid(row=roww, column=1)
                Label(myFrame, text=record[1], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"), width=22).grid(row=roww, column=2)
                Label(myFrame, text=record[3], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"), width=12).grid(row=roww, column=3)


            if record[2] > 0:
                Label(myFrame, text=record[2], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=rowww,
                                                                                                             column=0)
                Label(myFrame, text=record[0], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=rowww,
                                                                                                             column=1)
                Label(myFrame, text=record[1], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=rowww,
                                                                                                             column=2)
                Label(myFrame, text=record[3], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=rowww,
                                                                                                             column=3)
                rowww += 1

            myFrame.config(bg="white")

        conn.commit()
        conn.close()


def open():
    # ------------------------------------------ Testing ------------------------------------------------------------------------

    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM second")

    inventory_records = cursor.fetchall()
    print(inventory_records)

    products_and_cp = {}
    for record in inventory_records:
        products_and_cp[record[0]] = record[7]

    # ------------------------------------------ Testing ------------------------------------------------------------------------

    conn = sqlite3.connect("billDatabase.db")
    c = conn.cursor()

    c.execute("SELECT * FROM bill")

    bill_records = c.fetchall()
    print(bill_records)

    bill_number = int(bill_records[-1][2]) + 1
    if int(billNumber.get()) > 0 and int(billNumber.get()) <= bill_records[-1][2]:
        new = Toplevel(root)
        new.geometry("645x445")
        new.resizable(0, 0)
        new.title("Bill Details")

        # Setting up background image for new window
        image1 = Image.open("images/bill.png")
        img = ImageTk.PhotoImage(image1)

        labell = Label(new, image=img)
        labell.image = img
        labell.place(x=0, y=0)

        # Frame for bill
        wrapper1 = LabelFrame(new, height=800, width=1000, bd=0)

        myCanvas = Canvas(wrapper1, height=236, width=570, bg='white')
        myCanvas.pack(side=LEFT, fill='y', expand='yes')

        myFrame = Frame(myCanvas)
        myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

        wrapper1.place(x=35, y=166)

        # Frame for total
        wrapper2 = LabelFrame(new, height=800, width=1000, bd=0)

        myCanvas2 = Canvas(wrapper2, height=30, width=570, bg='white')
        myCanvas2.pack(side=LEFT, fill='y', expand='yes')

        myFrame2 = Frame(myCanvas2)
        myCanvas2.create_window((0, 0), window=myFrame2, anchor='nw')

        wrapper2.place(x=35, y=405)


        # Placing bill labels
        bill_label_1 = Label(new, text="Product Name", bg="white", font=("Microsoft Sans Serif", 13, "bold"))
        bill_label_1.place(x=50, y=136)

        bill_label_2 = Label(new, text="Quantity", bg="white", font=("Microsoft Sans Serif", 13, "bold"))
        bill_label_2.place(x=290, y=136)

        bill_label_3 = Label(new, text="Price", bg="white", font=("Microsoft Sans Serif", 13, "bold"))
        bill_label_3.place(x=480, y=136)

        bill_label_4 = Label(new, text="Customer Name :", bg="white", font=("Microsoft Sans Serif", 13))
        bill_label_4.place(x=35, y=80)

        bill_label_5 = Label(new, text="Contact Number :", bg="white", font=("Microsoft Sans Serif", 13))
        bill_label_5.place(x=35, y=105)

        bill_label_6 = Label(new, text="Date :", bg="white", font=("Microsoft Sans Serif", 13))
        bill_label_6.place(x=452, y=80)

        bill_label_7 = Label(new, text="Bill Number :", bg="white", font=("Microsoft Sans Serif", 13))
        bill_label_7.place(x=400, y=105)

        # Displaying customer name
        for billNum in bill_records:
            if billNum[2] == int(billNumber.get()):
                customer_name = billNum[0]
                contact_num = billNum[1]
                bill_date = billNum[3]

                bill_label_8 = Label(new, text=customer_name, bg="white", font=("Microsoft Sans Serif", 13))
                bill_label_8.place(x=170, y=80)

                bill_label_9 = Label(new, text=contact_num, bg="white", font=("Microsoft Sans Serif", 13))
                bill_label_9.place(x=170, y=105)

                bill_label_10 = Label(new, text=bill_date, bg="white", font=("Microsoft Sans Serif", 13))
                bill_label_10.place(x=505, y=80)

                bill_label_11 = Label(new, text=billNumber.get(), bg="white", font=("Microsoft Sans Serif", 13))
                bill_label_11.place(x=505, y=105)

                total_label = Label(myFrame2, text="Total", bg="white", font=("Poppins", 13), width=15)
                total_label.grid(row=0, column=0)

                total_amount = Label(myFrame2, text=f"Rs. {billNum[6]}", bg="white", font=("Poppins", 13), width=75)
                total_amount.grid(row=0, column=1)

                # Products
                product_list_string = billNum[4]
                product_list = ast.literal_eval(product_list_string)
                final_product_list = ast.literal_eval(product_list)


                p_row = 0
                for product in final_product_list:
                    lab1 = Label(myFrame, text=product, width=20, bg="white")
                    lab1.grid(row=p_row, column=1)
                    p_row += 1

                # Quantities
                quantity_list_string = billNum[5]
                quantity_list = ast.literal_eval(quantity_list_string)
                final_quantity_list = ast.literal_eval(quantity_list)

                q_row = 0
                for quantity in final_quantity_list:
                    lab2 = Label(myFrame, text=quantity, width=45, bg="white")
                    lab2.grid(row=q_row, column=2)

                    lab3 = Label(myFrame, text=int(quantity) * int(products_and_cp[final_product_list[q_row]]), width=6,
                                 bg="white")
                    lab3.grid(row=q_row, column=3)
                    q_row += 1

    conn.commit()
    conn.close()


# Creating and placing buttons
button1 = Button(root, text="Search", font=("Poppins", 14, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=search)
button1.place(x=300, y=175)

button2 = Button(root, text="Show Invoice", font=("Poppins", 14, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=open)
button2.place(x=160, y=315)

button3 = Button(root, text="Exit", font=("Poppins", 14, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
button3.place(x=205, y=520)

button4 = Button(root, text="LOGOUT", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
button4.place(x=1040, y=610)


# Function for creating and placing label
def createLabel(text, fg, font, x, y):
    labels = Label(root, text=text, bg="white", fg=fg, font=font)
    labels.place(x=x, y=y)


createLabel("Menu", "brown", ("Poppins", 16, "bold"), 84, 90)
createLabel("Invoices", "black", ("Poppins", 25, "bold"), 540, 50)
createLabel("Bill Number", "black", ("Poppins", 14), 60, 150)
createLabel("Bill Options", "black", ("Poppins", 14), 60, 260)

# Frame
wrapper1 = LabelFrame(root, height=800, width=1000, bd=0)

myCanvas = Canvas(wrapper1, height=483, width=725, bg='white')
myCanvas.pack(side=LEFT, fill='y', expand='yes')

myFrame = Frame(myCanvas)
myCanvas.create_window((0, 0), window=myFrame, anchor='nw')

wrapper1.place(x=420, y=107)

# Labels for showing bill details

label1 = Label(myFrame, text="Bill Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=13, fg="#0D1C30")
label1.grid(row=0,column=0)

label2 = Label(myFrame, text="Customer Name", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20, fg="#0D1C30")
label2.grid(row=0,column=1)

label3 = Label(myFrame, text="Contact Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20, fg="#0D1C30")
label3.grid(row=0,column=2)

label4 = Label(myFrame, text="Date", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=10, fg="#0D1C30")
label4.grid(row=0,column=3)


# Showing data

conn = sqlite3.connect("billDatabase.db")
c = conn.cursor()

c.execute("SELECT * FROM bill")
records = c.fetchall()


roww = 1
for record in records:
    if record[2] > 0:
        lab1 = Label(myFrame, text=record[2], bg="white", font=("Microsoft Sans Serif", 11), width=13 )
        lab1.grid(row=roww, column=0)

        Label(myFrame, text=record[0], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=roww, column=1)
        Label(myFrame, text=record[1], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=roww, column=2)
        Label(myFrame, text=record[3], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=roww, column=3)
        roww += 1

    myFrame.config(bg="white")

conn.commit()
conn.close()


# Creating and placing entry
billNumber = Entry(root, bd=0, width=20, font=("Franklin Gothic Medium", 13))
billNumber.place(x=68, y=185)
billNumber.focus()

mainloop()
