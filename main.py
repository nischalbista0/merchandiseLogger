import sqlite3
from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import time
import ast
from tkinter.font import Font
from datetime import datetime

splash=Tk()
splash.title("Merchandise")
splash.geometry("1193x671+145+50")
splash.overrideredirect(True)
bg = PhotoImage(file ="images/Untitledd.png")
splash_label = Label(splash, image= bg)
splash_label.pack()


def main_window():
    global fg
    splash.destroy()
    root = Tk()
    root.title("Login")
    root.geometry("1193x671+145+50")
    root.resizable(0,0)
    root.iconbitmap('images/Icon.ico')


    def login_window():
        global roww
        global index_increment
        global index

        if entry1.get() == 'Admin' and entry2.get() == '123':
            root1 = Toplevel()

            root1.geometry('1191x671+145+50')
            root1.title('Dashboard')
            root1.resizable(0,0)
            root1.iconbitmap('images/Icon.ico')

            # ------------------------------------- Inventory ----------------------------------------------------------
            def inventorryy():
                root = Toplevel()
                root.geometry('1193x671+145+50')
                root.title('Inventory')
                root.iconbitmap('images/Icon.ico')
                root.resizable(False, False)

                font1 = Font(
                    family='Poppins',
                    size=14,
                )

                conn = sqlite3.connect('database.db')

                c = conn.cursor()

                #c.execute('''CREATE TABLE second(
                #product text,
                #category text,
                #sub_category text,
                #In_stock integer,
                #customer_name text,
                #contact_number text,
                #bill_number text,
                #selling_price integer,
                #cost_price integer,
                #vendor_no text
                #)''')

                def search_it():
                    if Ent1.get() != '':
                        conn = sqlite3.connect('database.db')

                        c = conn.cursor()

                        c.execute("SELECT * FROM second WHERE oid=" + Ent1.get())

                        records = c.fetchall()

                        for record in records:
                            Label(myframe, text=Ent1.get(), bg='#16EEE9', width=10).grid(row=1, column=0)
                            Label(myframe, text=record[0], bg='#16EEE9', width=30).grid(row=1, column=1)
                            Label(myframe, text=record[1], bg='#16EEE9', width=13).grid(row=1, column=2)
                            Label(myframe, text=record[2], bg='#16EEE9', width=10).grid(row=1, column=3)
                            Label(myframe, text=record[3], bg='#16EEE9', width=10).grid(row=1, column=4)
                            Label(myframe, text=record[8], bg='#16EEE9', width=10).grid(row=1, column=5)
                            Label(myframe, text=record[9], bg='#16EEE9', width=10).grid(row=1, column=6)

                        conn.commit()

                        conn.close()

                    else:
                        messagebox.showwarning('Empty Field', 'Please enter in the search field', parent=root)


                def deletee():
                    if Ent1.get() != '':
                        conn = sqlite3.connect('database.db')

                        c = conn.cursor()

                        c.execute('DELETE FROM second WHERE oid=' + Ent1.get())

                        c.execute("SELECT *,oid FROM second")

                        records = c.fetchall()

                        number = Ent1.get()
                        roww = 1
                        for record in records:
                            Label(myframe, text=record[10], bg='white', width=10).grid(row=roww, column=0)
                            Label(myframe, text=record[0], bg='white', width=30).grid(row=roww, column=1)
                            Label(myframe, text=record[1], bg='white', width=13).grid(row=roww, column=2)
                            Label(myframe, text=record[2], bg='white', width=10).grid(row=roww, column=3)
                            Label(myframe, text=record[3], bg='white', width=10).grid(row=roww, column=4)
                            Label(myframe, text=record[8], bg='white', width=10).grid(row=roww, column=5)
                            Label(myframe, text=record[9], bg='white', width=10).grid(row=roww, column=6)
                            roww += 1

                        Label(myframe, text='', bg='white', width=10).grid(row=roww, column=0)
                        Label(myframe, text='', bg='white', width=10).grid(row=roww, column=1)
                        Label(myframe, text='', bg='white', width=10).grid(row=roww, column=2)
                        Label(myframe, text='', bg='white', width=10).grid(row=roww, column=3)
                        Label(myframe, text='', bg='white', width=10).grid(row=roww, column=4)
                        Label(myframe, text='', bg='white', width=10).grid(row=roww, column=5)
                        Label(myframe, text='', bg='white', width=10).grid(row=roww, column=6)

                        Ent1.delete(0, END)

                        conn.commit()

                        conn.close()
                    else:
                        messagebox.showwarning('Empty field', 'Please Enter the number in the field', parent=root)

                def inven_update():
                    if Ent1.get() != '':

                        global imgg
                        inven = Toplevel()
                        inven.geometry('1193x671+145+50')
                        inven.iconbitmap('images/Icon.ico')
                        inven.resizable(False, False)

                        def clear_all():
                            ls = [en1, en2, en3, en4, en5, en6, en7]

                            for i in ls:
                                i.delete(0, END)

                        def upd_product():
                            if en1.get() != '' and en2.get() != '' and en3.get() != '' and en4.get() != '' and en5.get() != '' and en6.get() != '' and en7.get() != '':

                                conn = sqlite3.connect('database.db')

                                c = conn.cursor()

                                ddata = Ent1.get()

                                c.execute('''UPDATE second SET
                                product = :pd,
                                category = :cate,
                                sub_category= :s_cate,
                                In_stock = :stock,
                                customer_name= :c_n,
                                contact_number= :c_num,
                                bill_number= :bill,
                                selling_price = :s_p,
                                cost_price = :c_p,
                                vendor_no = :vendor
                                WHERE oid = :oid
                                ''', {

                                    'pd': en1.get(),
                                    'cate': en2.get(),
                                    's_cate': en5.get(),
                                    'stock': en3.get(),
                                    'c_n': '',
                                    'c_num': '',
                                    'bill': '',
                                    's_p': en4.get(),
                                    'c_p': en6.get(),
                                    'vendor': en7.get(),
                                    'oid': ddata
                                })

                                inven.destroy()

                                c.execute("SELECT *,oid FROM second")

                                records = c.fetchall()

                                roww = 1
                                for record in records:
                                    Label(myframe, text=record[10], bg='white', width=10).grid(row=roww, column=0)
                                    Label(myframe, text=record[0], bg='white', width=30).grid(row=roww, column=1)
                                    Label(myframe, text=record[1], bg='white', width=13).grid(row=roww, column=2)
                                    Label(myframe, text=record[2], bg='white', width=10).grid(row=roww, column=3)
                                    Label(myframe, text=record[3], bg='white', width=10).grid(row=roww, column=4)
                                    Label(myframe, text=record[8], bg='white', width=10).grid(row=roww, column=5)
                                    Label(myframe, text=record[9], bg='white', width=10).grid(row=roww, column=6)
                                    roww += 1

                                conn.commit()

                                conn.close()

                            else:
                                messagebox.showwarning('Empty field', 'Please fill all Entries', parent=inven)

                        conn = sqlite3.connect('database.db')

                        c = conn.cursor()

                        imgg = ImageTk.PhotoImage(Image.open('images/Update_Product.jpg'))
                        lablo = Label(inven, image=imgg).place(x=0, y=0)
                        btn1 = Button(inven, text='Update', bg='#007884', height=1, width=13, fg='white',
                                      cursor='hand2',
                                      activebackground='#007884',
                                      bd=0, command=upd_product, font=font1).place(x=410, y=518)

                        btn2 = Button(inven, text='Clear', bg='#007884', height=1, fg='white', width=13, cursor='hand2',
                                      activebackground='#007884', font=font1,
                                      bd=0, command=clear_all).place(x=618, y=518)

                        lab1 = Label(inven, text='Product Name', bd=0, bg='white', font=font1).place(x=145, y=188)
                        lab2 = Label(inven, text='Category', bd=0, bg='white', font=font1).place(x=145, y=255)
                        lab3 = Label(inven, text='Quantity', bd=0, bg='white', font=font1).place(x=145, y=328)
                        lab4 = Label(inven, text='Selling Price(MRP)', bd=0, bg='white', font=font1).place(x=145, y=392)
                        lab5 = Label(inven, text='Sub Category', bd=0, bg='white', font=font1).place(x=620, y=255)
                        lab6 = Label(inven, text='Cost Price', bd=0, bg='white', font=font1).place(x=620, y=328)
                        lab7 = Label(inven, text='Vendor Phone No.', bd=0, bg='white', font=font1).place(x=620, y=392)

                        # Entries for update product
                        en1 = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=50)
                        en1.place(x=145, y=217)
                        en2 = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=36)
                        en2.place(x=145, y=285)
                        en3 = Entry(inven, bd=0, bg='white', fg='black', font=font1, width=36)
                        en3.place(x=145, y=358)
                        en4 = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=36)
                        en4.place(x=145, y=422)
                        en5 = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=34)
                        en5.place(x=620, y=285)
                        en6 = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=34)
                        en6.place(x=620, y=358)
                        en7 = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=34)
                        en7.place(x=620, y=422)

                        global ddata
                        ddata = Ent1.get()

                        c.execute("SELECT * FROM second WHERE oid=" + ddata)
                        records = c.fetchall()

                        for record in records:
                            en1.insert(0, record[0])
                            en2.insert(0, record[1])
                            en3.insert(0, record[3])
                            en4.insert(0, record[7])
                            en5.insert(0, record[2])
                            en6.insert(0, record[8])
                            en7.insert(0, record[9])

                        conn.commit()

                        conn.close()

                    else:
                        messagebox.showwarning('Empty Field', 'Please Enter a number in the field', parent=root)

                def inven_add():
                    global inven
                    global imge
                    inven = Toplevel()
                    inven.geometry('1193x671+145+50')
                    inven.iconbitmap('images/Icon.ico')
                    inven.resizable(False, False)

                    def clear_all():
                        ls = [en1a, en2a, en3a, en4a, en5a, en6a, en7a]

                        for i in ls:
                            i.delete(0, END)

                    def add_product():
                        if en1a.get() != '' and en2a.get() != '' and en3a.get() != '' and en4a.get() != '' and en5a.get() != '' and en6a.get() != '' and en7a.get() != '':

                            conn = sqlite3.connect('database.db')

                            c = conn.cursor()

                            c.execute(
                                "INSERT INTO second VALUES (:product, :category, :sub_category, :In_stock, :customer_name, :contact_number, :bill_number,:selling_price, :cost_price, :vendor_no)",

                                {
                                    'product': en1a.get(),
                                    'category': en2a.get(),
                                    'sub_category': en5a.get(),
                                    'In_stock': en3a.get(),
                                    'customer_name': '',
                                    'contact_number': '',
                                    'bill_number': '',
                                    'selling_price': en4a.get(),
                                    'cost_price': en6a.get(),
                                    'vendor_no': en7a.get()
                                })

                            c.execute("SELECT *,oid FROM second")

                            records = c.fetchall()

                            roww = 1
                            for record in records:
                                Label(myframe, text=record[10], bg='white', width=10).grid(row=roww, column=0)
                                Label(myframe, text=record[0], bg='white', width=30).grid(row=roww, column=1)
                                Label(myframe, text=record[1], bg='white', width=13).grid(row=roww, column=2)
                                Label(myframe, text=record[2], bg='white', width=10).grid(row=roww, column=3)
                                Label(myframe, text=record[3], bg='white', width=10).grid(row=roww, column=4)
                                Label(myframe, text=record[8], bg='white', width=10).grid(row=roww, column=5)
                                Label(myframe, text=record[9], bg='white', width=10).grid(row=roww, column=6)
                                roww += 1

                            conn.commit()

                            conn.close()
                            inven.destroy()

                        else:
                            messagebox.showwarning('Empty Field', 'Please fill all Entries', parent=inven)

                    imge = ImageTk.PhotoImage(Image.open('images/Add_Product.jpg'))
                    labloo = Label(inven, image=imge).place(x=0, y=0)
                    btn1a = Button(inven, text='Add', bg='#007884', height=1, width=12, cursor='hand2', fg='white',
                                   activebackground='#007884',
                                   command=add_product, font=font1, bd=0).place(x=410, y=520)

                    btn2a = Button(inven, text='Clear', bg='#007884', height=1, fg='white', cursor='hand2', width=12,
                                   activebackground='#007884', font=font1,
                                   bd=0, command=clear_all).place(x=620, y=520)

                    lab1a = Label(inven, text='Product Name', bd=0, bg='white', font=font1).place(x=145, y=188)
                    lab2a = Label(inven, text='Category', bd=0, bg='white', font=font1).place(x=145, y=255)
                    lab3a = Label(inven, text='Quantity', bd=0, bg='white', font=font1).place(x=145, y=328)
                    lab4a = Label(inven, text='Selling Price(MRP)', bd=0, bg='white', font=font1).place(x=145, y=392)
                    lab5a = Label(inven, text='Sub Category', bd=0, bg='white', font=font1).place(x=620, y=255)
                    lab6a = Label(inven, text='Cost Price', bd=0, bg='white', font=font1).place(x=620, y=328)
                    lab7a = Label(inven, text='Vendor Phone No.', bd=0, bg='white', font=font1).place(x=620, y=392)

                    # Entries for update product

                    en1a = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=50)
                    en1a.place(x=145, y=217)
                    en2a = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=36)
                    en2a.place(x=145, y=285)
                    en3a = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=36)
                    en3a.place(x=145, y=358)
                    en4a = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=36)
                    en4a.place(x=145, y=422)
                    en5a = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=34)
                    en5a.place(x=620, y=285)
                    en6a = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=34)
                    en6a.place(x=620, y=358)
                    en7a = Entry(inven, bg='white', bd=0, fg='black', font=font1, width=34)
                    en7a.place(x=620, y=422)

                def exito():
                    ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=root)
                    if ans:
                        root.destroy()
                        root1.destroy()

                        global entry1, entry2
                        entry1.delete(0,END)
                        entry2.delete(0, END)
                        entry1.focus()

                img = ImageTk.PhotoImage(Image.open('images/Inventory.jpg'))
                lable = Label(root, image=img).place(x=0, y=0)

                lab1 = Label(root, text='Menu', bg='white', font=font1)
                lab1.place(x=66, y=152)

                Ent1 = Entry(root, bd=0, width=16, bg='white', fg='black', font=font1)
                Ent1.place(x=70, y=210)
                btn1 = Button(root, text='Logout', height=1, width=6, bg='#007884', activebackground='#007884', bd=0, font=font1, cursor='hand2', fg='white', command=exito).place(x=70, y=96)
                btn2 = Button(root, text='Search', height=1, width=7, bg='#007884', activebackground='#007884', bd=0, font=font1, fg='white', cursor='hand2', command=search_it).place(x=263, y=213)
                btn3 = Button(root, text='Add Product', height=1, width=19, bg='#007884', activebackground='#007884', fg='white', font=font1, bd=0, cursor='hand2', command=inven_add).place(x=94, y=323)
                btn4 = Button(root, text='Update Product', height=1, width=19, bg='#007884', activebackground='#007884', fg='white', cursor='hand2', command=inven_update, font=font1, bd=0).place(x=92, y=405)
                btn5 = Button(root, text='Delete Product', height=1, width=19, bg='#007884', activebackground='#007884', font=font1, fg='white', cursor='hand2', bd=0, command=deletee).place(x=92, y=485)
                btn6 = Button(root, text='Exit', height=1, width=7, bg='#007884', bd=0, activebackground='#007884', font=font1, cursor='hand2', fg='white', command=root.destroy).place(x=158, y=554)


                wrapper1 = LabelFrame(root, height=800, width=1000, bd=0)

                mycanvas = Canvas(wrapper1, height=412, width=710, bg='white')

                mycanvas.pack(side=LEFT, fill='y', expand='yes')

                myframe = Frame(mycanvas)
                mycanvas.create_window((0, 0), window=myframe, anchor='nw')

                yscrollbar = ttk.Scrollbar(wrapper1, orient='vertical', command=mycanvas.yview)
                yscrollbar.pack(side=RIGHT, fill='y')

                mycanvas.config(yscrollcommand=yscrollbar.set)

                mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

                lb_t1 = Label(myframe, text='Product ID', bg='white', width=10).grid(row=0, column=0)
                lb_t2 = Label(myframe, text='Name', bg='white', width=30).grid(row=0, column=1)
                lb_t3 = Label(myframe, text='Category', bg='white', width=13).grid(row=0, column=2)
                lb_t4 = Label(myframe, text='Sub-category', bg='white', width=10).grid(row=0, column=3)
                lb_t5 = Label(myframe, text='In stock', bg='white', width=10).grid(row=0, column=4)
                lb_t6 = Label(myframe, text='Cost price', bg='white', width=10).grid(row=0, column=5)
                lb_t7 = Label(myframe, text='Vendor no.', bg='white', width=10).grid(row=0, column=6)

                # for i in range(50):
                # Button(myframe, text='My button-'+str(i)).pack()

                wrapper1.place(x=380, y=170)

                c.execute("SELECT *,oid FROM second")

                records = c.fetchall()

                roww = 1

                for record in records:
                    Label(myframe, text=record[10], bg='white', width=10).grid(row=roww, column=0)
                    Label(myframe, text=record[0], bg='white', width=30).grid(row=roww, column=1)
                    Label(myframe, text=record[1], bg='white', width=13).grid(row=roww, column=2)
                    Label(myframe, text=record[2], bg='white', width=10).grid(row=roww, column=3)
                    Label(myframe, text=record[3], bg='white', width=10).grid(row=roww, column=4)
                    Label(myframe, text=record[8], bg='white', width=10).grid(row=roww, column=5)
                    Label(myframe, text=record[9], bg='white', width=10).grid(row=roww, column=6)
                    roww += 1
                conn.commit()

                conn.close()
                root.mainloop()

            # ------------------------------------- Employee ----------------------------------------------------------
            def employeee():
                employee = Toplevel()
                employee.geometry("1191x670+145+50")
                employee.title("Employee Management")
                employee.iconbitmap('images/Icon.ico')
                employee.resizable(False, False)

                # -------------DATABASE----------------
                # Create a databases or connect to one
                conn = sqlite3.connect("database_employee.db")

                # Create cursor
                c = conn.cursor()

                # query of the database
                # c.execute("SELECT *, oid FROM addresses")

                # Create table
                '''c.execute(""" CREATE TABLE addresses(
                      emp_name text,
                      contact_no integer,
                      citizen_no integer,
                      designation text,
                      address text,
                      password text
                ) """)'''

                # ----------------Search the existing data----------------
                # Create search function
                def search():
                    if searchbox.get() != '':
                        # Connect to the existing database
                        conn = sqlite3.connect('database_employee.db')
                        c = conn.cursor()
                        # query of the database
                        c.execute("SELECT * FROM addresses WHERE oid=" + searchbox.get())

                        records = c.fetchall()

                        # Loop through the results
                        for record in records:
                            Label(myframe, text=searchbox.get(), bg="#16EEE9", width=10).grid(row=1, column=0)
                            Label(myframe, text=record[0], bg='#16EEE9', width=24).grid(row=1, column=1)
                            Label(myframe, text=record[1], bg='#16EEE9', width=13).grid(row=1, column=2)
                            Label(myframe, text=record[2], bg='#16EEE9', width=11).grid(row=1, column=3)
                            Label(myframe, text=record[3], bg='#16EEE9', width=10).grid(row=1, column=4)
                            Label(myframe, text=record[4], bg='#16EEE9', width=10).grid(row=1, column=5)
                            Label(myframe, text=record[5], bg='#16EEE9', width=10).grid(row=1, column=6)

                        # showinfo messagebox
                        messagebox.showinfo("Great!!", "Employee ID : " + searchbox.get() + " " + "is found.", parent=employee)

                        searchbox.delete(0, END)

                        conn.commit()
                        conn.close()

                    else:
                        messagebox.showwarning('Empty Field', 'Please enter in the search field', parent=employee)

                # -----------------Update the existing data-----------------
                # Create an update function
                def emp_update():
                    if searchbox.get() != '':
                        editor = Toplevel()
                        editor.title("Update Employee")
                        editor.geometry("1191x670+145+50")
                        editor.iconbitmap('images/Icon.ico')
                        editor.resizable(False, False)

                        def edit():
                            # Create a databases or connect to one
                            conn = sqlite3.connect("database_employee.db")
                            # Create cursor
                            c = conn.cursor()
                            record_id = searchbox.get()

                            c.execute(""" UPDATE addresses SET
                            emp_name = :name,
                            contact_no = :contact,
                            address = :address,
                            citizen_no = :citizen,
                            designation = :designation,
                            address = :address,
                            password = :password
                            WHERE oid = :oid""",
                                      {'name': namebox_editor.get(),
                                       'contact': contactbox_editor.get(),
                                       'citizen': citizenbox_editor.get(),
                                       'designation': designationbox_editor.get(),
                                       'address': addressbox_editor.get(),
                                       'password': passwordbox_editor.get(),
                                       'oid': record_id

                                       }
                                      )

                            editor.destroy()

                            # query of the database
                            c.execute("SELECT *, oid FROM addresses")

                            records = c.fetchall()

                            # Loop through the results
                            place = 1
                            for record in records:
                                Label(myframe, text=record[6], bg="white", width=10).grid(row=place, column=0)
                                Label(myframe, text=record[0], bg="white", width=24).grid(row=place, column=1)
                                Label(myframe, text=record[1], bg="white", width=13).grid(row=place, column=2)
                                Label(myframe, text=record[2], bg="white", width=11).grid(row=place, column=3)
                                Label(myframe, text=record[3], bg="white", width=10).grid(row=place, column=4)
                                Label(myframe, text=record[4], bg="white", width=10).grid(row=place, column=5)
                                Label(myframe, text=record[5], bg="white", width=10).grid(row=place, column=6)
                                place += 1

                            # showinfo messagebox
                            messagebox.showinfo("Addresses", "Updated Successfully", parent=employee)

                            conn.commit()
                            conn.close()

                        # Create a databases or connect to one
                        conn = sqlite3.connect("database_employee.db")

                        # Create cursor
                        c = conn.cursor()

                        global bgg
                        # Define image as background in Update Employee window
                        bgg = ImageTk.PhotoImage(file="images/update_emp.png")
                        bg_label = Label(editor, image=bgg)
                        bg_label.place(x=0, y=0)


                        # Create labels
                        title = Label(editor, text="Update Employee", fg="Black", bg="White", font=('Helvetica', 20, 'bold'))
                        title.place(x=480, y=40)

                        name_label_editor = Label(editor, text="Employee Name", bg="#FFFFFF")
                        name_label_editor.configure(font="-family {Poppins} -size 14")
                        name_label_editor.place(x=160, y=185)

                        contact_label_editor = Label(editor, text="Contact No.", bg="#FFFFFF")
                        contact_label_editor.configure(font="-family {Poppins} -size 14")
                        contact_label_editor.place(x=160, y=265)

                        citizen_label_editor = Label(editor, text="Citizenship No.", bg="#FFFFFF")
                        citizen_label_editor.configure(font="-family {Poppins} -size 14")
                        citizen_label_editor.place(x=160, y=338)

                        designation_label_editor = Label(editor, text="Designation", bg="#FFFFFF")
                        designation_label_editor.configure(font="-family {Poppins} -size 14")
                        designation_label_editor.place(x=625, y=185)

                        address_label_editor = Label(editor, text="Address", bg="#FFFFFF")
                        address_label_editor.configure(font="-family {Poppins} -size 14")
                        address_label_editor.place(x=625, y=265)

                        password_label_editor = Label(editor, text="Passsword", bg="#FFFFFF")
                        password_label_editor.configure(font="-family {Poppins} -size 14")
                        password_label_editor.place(x=625, y=338)

                        # Create entryboxes
                        entry_font = ('Poppins', 12)
                        namebox_editor = Entry(editor, borderwidth=0, font=entry_font, width=40)
                        namebox_editor.place(x=165, y=220)
                        entry_font = ('Poppins', 12)
                        contactbox_editor = Entry(editor, borderwidth=0, font=entry_font, width=40)
                        contactbox_editor.place(x=165, y=295)
                        entry_font = ('Poppins', 12)
                        citizenbox_editor = Entry(editor, borderwidth=0, font=entry_font, width=40)
                        citizenbox_editor.place(x=165, y=368)
                        entry_font = ('Poppins', 12)
                        designationbox_editor = Entry(editor, borderwidth=0, font=entry_font, width=40)
                        designationbox_editor.place(x=630, y=220)
                        entry_font = ('Poppins', 12)
                        addressbox_editor = Entry(editor, borderwidth=0, font=entry_font, width=40)
                        addressbox_editor.place(x=630, y=295)
                        entry_font = ('Poppins', 12)
                        passwordbox_editor = Entry(editor, borderwidth=0, font=entry_font, width=40)
                        passwordbox_editor.place(x=630, y=368)

                        global record_id
                        record_id = searchbox.get()
                        c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
                        records = c.fetchall()

                        # loop through the results
                        for record in records:
                            namebox_editor.insert(0, record[0])
                            contactbox_editor.insert(0, record[1])
                            citizenbox_editor.insert(0, record[2])
                            designationbox_editor.insert(0, record[3])
                            addressbox_editor.insert(0, record[4])
                            passwordbox_editor.insert(0, record[5])

                        # Clear everything from the update's textbox
                        def update_clear():
                            l = [namebox_editor, contactbox_editor, citizenbox_editor, designationbox_editor,
                                 addressbox_editor,
                                 passwordbox_editor]

                            for i in l:
                                i.delete(0, END)

                        # Create buttons
                        update_bt_editor = Button(editor, text="Update", bg="#007884", fg="White",
                                                  activeforeground="White",
                                                  activebackground="#007884", borderwidth=0, pady=0, cursor="hand2",
                                                  command=edit)
                        update_bt_editor.configure(font="-family {Poppins} -size 14")
                        update_bt_editor.place(x=480, y=523)

                        clear_bt_editor = Button(editor, text="Clear", bg="#007884", fg="White",
                                                 activeforeground="White",
                                                 activebackground="#007884", borderwidth=0, cursor="hand2",
                                                 command=update_clear)
                        clear_bt_editor.configure(font="-family {Poppins} -size 14")
                        clear_bt_editor.place(x=655, y=522)

                        conn.commit()
                        conn.close()

                    else:
                        messagebox.showwarning('Empty Field', 'Please enter in the search field', parent=employee)

                # -----------------Add new data---------------------
                def add_emp():
                    global bg
                    top = Toplevel()
                    top.title("Add Employee")
                    top.geometry("1191x670+145+50")
                    top.iconbitmap('images/Icon.ico')
                    top.resizable(False, False)

                    # Create submit button for databases
                    def submit():
                        if namebox.get() != '' and contactbox.get() != '' and citizenbox.get() != '' and designationbox.get() != '' and \
                                addressbox.get() != '' and passwordbox.get() != 0:
                            # Create a databases or connect to one
                            conn = sqlite3.connect("database_employee.db")

                            # Create cursor
                            c = conn.cursor()

                            # Insert into table
                            c.execute(
                                "INSERT INTO addresses VALUES (:emp_name, :contact_no, :citizen_no, :designation, :address, :password)",
                                {
                                    'emp_name': namebox.get(),
                                    'contact_no': contactbox.get(),
                                    'citizen_no': citizenbox.get(),
                                    'designation': designationbox.get(),
                                    'address': addressbox.get(),
                                    'password': passwordbox.get(),

                                })

                            # query of the database
                            c.execute("SELECT *, oid FROM addresses")

                            records = c.fetchall()

                            # Loop through the results
                            place = 1
                            for record in records:
                                Label(myframe, text=record[6], bg="white", width=10).grid(row=place, column=0)
                                Label(myframe, text=record[0], bg="white", width=24).grid(row=place, column=1)
                                Label(myframe, text=record[1], bg="white", width=13).grid(row=place, column=2)
                                Label(myframe, text=record[2], bg="white", width=11).grid(row=place, column=3)
                                Label(myframe, text=record[3], bg="white", width=10).grid(row=place, column=4)
                                Label(myframe, text=record[4], bg="white", width=10).grid(row=place, column=5)
                                Label(myframe, text=record[5], bg="white", width=10).grid(row=place, column=6)
                                place += 1

                            # showinfo messagebox
                            messagebox.showinfo("Addresses", "Inserted Successfully", parent=top)

                            conn.commit()
                            conn.close()
                            top.destroy()

                        else:
                            messagebox.showwarning("Warning!", "Fill up Everything", parent=top)

                    #Define image as background in Add Employee window
                    bg = ImageTk.PhotoImage(file="images/add_emp.png")
                    bg_label = Label(top, image=bg)
                    bg_label.place(x=0, y=0)

                    # Create labels
                    title = Label(top, text="Add Employee", fg="Black", bg="White", font=('Helvetica', 20, 'bold'))
                    title.place(x=480, y=40)

                    name_label = Label(top, text="Employee Name", bg="#FFFFFF")
                    name_label.configure(font="-family {Poppins} -size 14")
                    name_label.place(x=160, y=185)

                    contact_label = Label(top, text="Contact No.", bg="#FFFFFF")
                    contact_label.configure(font="-family {Poppins} -size 14")
                    contact_label.place(x=160, y=265)

                    citizen_label = Label(top, text="Citizenship No.", bg="#FFFFFF")
                    citizen_label.configure(font="-family {Poppins} -size 14")
                    citizen_label.place(x=160, y=338)

                    designation_label = Label(top, text="Designation", bg="#FFFFFF")
                    designation_label.configure(font="-family {Poppins} -size 14")
                    designation_label.place(x=625, y=185)

                    address_label = Label(top, text="Address", bg="#FFFFFF")
                    address_label.configure(font="-family {Poppins} -size 14")
                    address_label.place(x=625, y=265)

                    password_label = Label(top, text="Password", bg="#FFFFFF")
                    password_label.configure(font="-family {Poppins} -size 14")
                    password_label.place(x=625, y=338)

                    # Remove every entry from the entry boxes
                    def add_clear():
                        l = [namebox, contactbox, citizenbox, designationbox, addressbox, passwordbox]

                        for i in l:
                            i.delete(0, END)

                    # Create entry boxes
                    entry_font = ('Poppins', 12)
                    namebox = Entry(top, borderwidth=0, font=entry_font, width=40)
                    namebox.place(x=165, y=220)

                    entry_font = ('Poppins', 12)
                    contactbox = Entry(top, borderwidth=0, font=entry_font, width=40)
                    contactbox.place(x=165, y=295)

                    entry_font = ('Poppins', 12)
                    citizenbox = Entry(top, borderwidth=0, font=entry_font, width=40)
                    citizenbox.place(x=165, y=368)

                    entry_font = ('Poppins', 12)
                    designationbox = Entry(top, borderwidth=0, font=entry_font, width=40)
                    designationbox.place(x=630, y=220)

                    entry_font = ('Poppins', 12)
                    addressbox = Entry(top, borderwidth=0, font=entry_font, width=40)
                    addressbox.place(x=630, y=295)

                    entry_font = ('Poppins', 12)
                    passwordbox = Entry(top, borderwidth=0, font=entry_font, width=40)
                    passwordbox.place(x=630, y=368)

                    # creating buttons
                    add_bt = Button(top, text="Add", bg="#007884", fg="White", activeforeground="White",
                                    activebackground="#007884", borderwidth=0, cursor="hand2", command=submit)
                    add_bt.configure(font="-family {Poppins} -size 14")
                    add_bt.place(x=490, y=522)

                    clear_bt = Button(top, text="Clear", bg="#007884", fg="White", activeforeground="White",
                                      activebackground="#007884", borderwidth=0, cursor="hand2", command=add_clear)
                    clear_bt.configure(font="-family {Poppins} -size 14")
                    clear_bt.place(x=655, y=522)

                # Create function to delete a data
                def delete():
                    if searchbox.get() != '':
                        # create database
                        conn = sqlite3.connect("database_employee.db")

                        # create cursor
                        c = conn.cursor()

                        # delete a record
                        c.execute("DELETE from addresses WHERE oid = " + searchbox.get())

                        # query of the database
                        c.execute("SELECT *, oid FROM addresses")

                        records = c.fetchall()

                        # Loop through the results
                        place = 1
                        for record in records:
                            Label(myframe, text=record[6], bg="white", width=10).grid(row=place, column=0)
                            Label(myframe, text=record[0], bg="white", width=24).grid(row=place, column=1)
                            Label(myframe, text=record[1], bg="white", width=13).grid(row=place, column=2)
                            Label(myframe, text=record[2], bg="white", width=11).grid(row=place, column=3)
                            Label(myframe, text=record[3], bg="white", width=10).grid(row=place, column=4)
                            Label(myframe, text=record[4], bg="white", width=10).grid(row=place, column=5)
                            Label(myframe, text=record[5], bg="white", width=10).grid(row=place, column=6)
                            place += 1

                        Label(myframe, text='', bg="white", width=10).grid(row=place, column=0)
                        Label(myframe, text='', bg="white", width=24).grid(row=place, column=1)
                        Label(myframe, text='', bg="white", width=13).grid(row=place, column=2)
                        Label(myframe, text='', bg="white", width=11).grid(row=place, column=3)
                        Label(myframe, text='', bg="white", width=10).grid(row=place, column=4)
                        Label(myframe, text='', bg="white", width=10).grid(row=place, column=5)
                        Label(myframe, text='', bg="white", width=10).grid(row=place, column=6)

                        searchbox.delete(0, END)
                        conn.commit()

                        conn.close()

                    else:
                        messagebox.showwarning('Empty Field', 'Please enter in the search field', parent=employee)

                # Define image as background
                bg1 = ImageTk.PhotoImage(file="images/emp_mngt.png")
                bg_label = Label(employee, image=bg1)
                bg_label.place(x=0, y=0)

                # Create Search box
                entry_font = ('Poppins', 12)
                searchbox = Entry(employee, borderwidth=0, font=entry_font)
                searchbox.place(x=93, y=160)


                def exitt3():
                    ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=employee)
                    if ans:
                        employee.destroy()
                        root1.destroy()
                        global entry1, entry2
                        entry1.delete(0, END)
                        entry2.delete(0, END)
                        entry1.focus()

                # Create buttons
                search_bt = Button(employee, text="Search", bg="#007884", activebackground="#007884", fg="White", activeforeground="White", borderwidth=0, cursor="hand2", command=search)
                search_bt.configure(font="-family {Poppins} -size 14")
                search_bt.place(x=315, y=149)

                add_bt = Button(employee, text="Add Employee", bg="#007884", activebackground="#007884", fg="White", activeforeground="White", borderwidth=0, cursor="hand2", command=add_emp)
                add_bt.configure(font="-family {Poppins} -size 14")
                add_bt.place(x=156, y=280)

                update_bt = Button(employee, text="Update Employee", bg="#007884", activebackground="#007884", fg="White", activeforeground="White", borderwidth=0, cursor="hand2", command=emp_update)
                update_bt.configure(font="-family {Poppins} -size 14")
                update_bt.place(x=140, y=360)

                delete_bt = Button(employee, text="Delete Employee", bg="#007884", activebackground="#007884", fg="White", activeforeground="White", borderwidth=0, cursor="hand2", command=delete)
                delete_bt.configure(font="-family {Poppins} -size 14")
                delete_bt.place(x=140, y=440)

                exit_bt = Button(employee, text="Exit", bg="#007884", activebackground="#007884", fg="White", activeforeground="White", borderwidth=0, command=employee.destroy, cursor="hand2")
                exit_bt.configure(font="-family {Poppins} -size 14")
                exit_bt.place(x=200, y=540)

                logout_bt = Button(employee, text="Log Out", fg="White", activeforeground="White", bg="#007884", activebackground="#007884", borderwidth=0, cursor="hand2", command=exitt3)
                logout_bt.configure(font="-family {Poppins} -size 14")
                logout_bt.place(x=1046, y=607)

                # -------------Create Frame with scrollbar--------------
                cover = LabelFrame(employee, height=800, width=1000, bd=0)
                cover.place(x=457, y=100)

                mycanvas = Canvas(cover, height=495, width=663, bg="white")
                mycanvas.pack(side=LEFT, fill='y', expand='yes')

                myframe = Frame(mycanvas)
                mycanvas.create_window((0, 0), window=myframe, anchor='nw')

                yscrollbar = ttk.Scrollbar(cover, orient='vertical', command=mycanvas.yview)
                yscrollbar.pack(side=RIGHT, fill='y')
                mycanvas.config(yscrollcommand=yscrollbar.set)
                mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

                # Create labels
                title = Label(employee, text="Employee Management", fg="Black", bg="white", font=('Helvetica', 20, 'bold'))
                title.place(x=450, y=40)

                menu_label = Label(employee, text="Menu", bg="white")
                menu_label.configure(font="-family {Poppins} -size 14")
                menu_label.place(x=135, y=85)

                id_label = Label(employee, text="Employee ID", bg="white")
                id_label.configure(font="-family {Poppins} -size 14")
                id_label.place(x=90, y=128)

                options_label = Label(employee, text="Employee Options", bg="white")
                options_label.configure(font="-family {Poppins} -size 14")
                options_label.place(x=90, y=220)

                emp_id = Label(myframe, text='Employee ID', bg="white", width=10).grid(row=0, column=0)
                emp_name = Label(myframe, text='Employee Name', bg="white", width=24).grid(row=0, column=1)
                contact_no = Label(myframe, text='Contact No.', bg="white", width=13).grid(row=0, column=2)
                citizen_no = Label(myframe, text='Citizenship No.', bg="white", width=11).grid(row=0, column=3)
                designation = Label(myframe, text='Designation', bg="white", width=10).grid(row=0, column=4)
                address = Label(myframe, text='Address', bg="white", width=10).grid(row=0, column=5)
                password = Label(myframe, text='Password', bg="white", width=10).grid(row=0, column=6)

                c.execute("SELECT *,oid FROM addresses")

                records = c.fetchall()

                # Loop through the results
                place = 1
                for record in records:
                    Label(myframe, text=record[6], bg="white", width=10).grid(row=place, column=0)
                    Label(myframe, text=record[0], bg="white", width=24).grid(row=place, column=1)
                    Label(myframe, text=record[1], bg="white", width=13).grid(row=place, column=2)
                    Label(myframe, text=record[2], bg="white", width=11).grid(row=place, column=3)
                    Label(myframe, text=record[3], bg="white", width=10).grid(row=place, column=4)
                    Label(myframe, text=record[4], bg="white", width=10).grid(row=place, column=5)
                    Label(myframe, text=record[5], bg="white", width=10).grid(row=place, column=6)
                    place += 1

                # close commit
                conn.commit()

                # close connection
                conn.close()

                employee.mainloop()

            # ------------------------------------- Invoices ----------------------------------------------------------
            def invoiceee():
                root = Toplevel()
                root.title("Invoices")
                root.geometry("1191x670+145+50")
                root.iconbitmap('images/Icon.ico')
                root.resizable(0, 0)

                # Background Image setup
                bg = ImageTk.PhotoImage(file="images/invoice_window.png")
                bg_image = Label(root, image=bg).place(x=0, y=0)

                # Function that searches the bill number and highlights it at the top
                def search():
                    for widgets in myFrame.winfo_children():
                        widgets.destroy()

                    label1 = Label(myFrame, text="Bill Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=13, fg="#0D1C30")
                    label1.grid(row=1, column=0)

                    label2 = Label(myFrame, text="Customer Name", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20, fg="#0D1C30")
                    label2.grid(row=1, column=1)

                    label3 = Label(myFrame, text="Contact Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20, fg="#0D1C30")
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
                                Label(myFrame, text=record[2], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"),
                                      width=15).grid(
                                    row=roww, column=0)
                                Label(myFrame, text=record[0], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"),
                                      width=22).grid(
                                    row=roww, column=1)
                                Label(myFrame, text=record[1], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"),
                                      width=22).grid(
                                    row=roww, column=2)
                                Label(myFrame, text=record[3], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"),
                                      width=12).grid(
                                    row=roww, column=3)

                            if record[2] > 0:
                                Label(myFrame, text=record[2], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=rowww, column=0)
                                Label(myFrame, text=record[0], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=rowww, column=1)
                                Label(myFrame, text=record[1], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=rowww, column=2)
                                Label(myFrame, text=record[3], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=rowww, column=3)

                                rowww += 1

                            myFrame.config(bg="white")

                        conn.commit()
                        conn.close()

                    else:
                        messagebox.showinfo("Bill number not found", "Please enter valid bill number!", parent=root)

                # Function that displays searched bill in new window
                def open():
                    connect = sqlite3.connect("database.db")
                    cursor = connect.cursor()

                    cursor.execute("SELECT * FROM second")

                    inventory_records = cursor.fetchall()

                    products_and_cp = {}
                    for record in inventory_records:
                        products_and_cp[record[0]] = record[7]

                    conn = sqlite3.connect("billDatabase.db")
                    c = conn.cursor()

                    c.execute("SELECT * FROM bill")

                    bill_records = c.fetchall()

                    bill_number = int(bill_records[-1][2]) + 1
                    if int(billNumber.get()) > 0 and int(billNumber.get()) <= bill_records[-1][2]:
                        new = Toplevel(root)
                        new.geometry("645x445")
                        new.resizable(0, 0)
                        new.iconbitmap('images/Icon.ico')
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

                        bill_label_8 = Label(new, text="The Slytherin Store", bg="white", font=("Microsoft Sans Serif", 15))
                        bill_label_8.place(x=255, y=5)

                        bill_label_9 = Label(new, text="Kirtipur-4, Kathmandu, Nepal", bg="white", font=("Microsoft Sans Serif", 13))
                        bill_label_9.place(x=235, y=33)

                        bill_label_10 = Label(new, text="Ph: 01-43344990", bg="white", font=("Microsoft Sans Serif", 13))
                        bill_label_10.place(x=280, y=55)

                        # Displaying customer name
                        for billNum in bill_records:
                            if billNum[2] == int(billNumber.get()):
                                customer_name = billNum[0]
                                contact_num = billNum[1]
                                bill_date = billNum[3]

                                bill_label_8 = Label(new, text=customer_name, bg="white",
                                                     font=("Microsoft Sans Serif", 13))
                                bill_label_8.place(x=170, y=80)

                                bill_label_9 = Label(new, text=contact_num, bg="white",
                                                     font=("Microsoft Sans Serif", 13))
                                bill_label_9.place(x=170, y=105)

                                bill_label_10 = Label(new, text=bill_date, bg="white",
                                                      font=("Microsoft Sans Serif", 13))
                                bill_label_10.place(x=505, y=80)

                                bill_label_11 = Label(new, text=billNumber.get(), bg="white",
                                                      font=("Microsoft Sans Serif", 13))
                                bill_label_11.place(x=505, y=105)

                                total_label = Label(myFrame2, text="Total", bg="white", font=("Poppins", 13), width=15)
                                total_label.grid(row=0, column=0)

                                total_amount = Label(myFrame2, text=f"Rs. {billNum[6]}", bg="white",
                                                     font=("Poppins", 13), width=75)
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

                                    lab3 = Label(myFrame,
                                                 text=int(quantity) * int(products_and_cp[final_product_list[q_row]]),
                                                 width=6,
                                                 bg="white")
                                    lab3.grid(row=q_row, column=3)
                                    q_row += 1

                    conn.commit()
                    conn.close()

                def exitt1():
                    ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=root)
                    if ans:
                        root.destroy()
                        root1.destroy()

                        global entry1, entry2
                        entry1.delete(0, END)
                        entry2.delete(0, END)
                        entry1.focus()


                # Creating and placing buttons
                button1 = Button(root, text="Search", font=("Poppins", 14, "bold"), border=0, bg="#007884", fg="white",
                                 activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=search)
                button1.place(x=300, y=175)

                button2 = Button(root, text="Show Invoice", font=("Poppins", 14, "bold"), border=0, bg="#007884",
                                 fg="white",
                                 activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=open)
                button2.place(x=160, y=315)

                button3 = Button(root, text="Exit", font=("Poppins", 14, "bold"), border=0, bg="#007884", fg="white",
                                 activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2",command=root.destroy)
                button3.place(x=205, y=520)

                button4 = Button(root, text="LOGOUT", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white",
                                 activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2",command= exitt1)
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

                yscrollbar = ttk.Scrollbar(wrapper1, orient='vertical', command=myCanvas.yview)
                yscrollbar.pack(side=RIGHT, fill='y')
                myCanvas.config(yscrollcommand=yscrollbar.set)
                myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox('all')))

                # Labels for showing bill details
                label1 = Label(myFrame, text="Bill Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=13, fg="#0D1C30")
                label1.grid(row=0, column=0)

                label2 = Label(myFrame, text="Customer Name", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20, fg="#0D1C30")
                label2.grid(row=0, column=1)

                label3 = Label(myFrame, text="Contact Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20, fg="#0D1C30")
                label3.grid(row=0, column=2)

                label4 = Label(myFrame, text="Date", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=10, fg="#0D1C30")
                label4.grid(row=0, column=3)

                # Showing all the bill created in listed view
                conn = sqlite3.connect("billDatabase.db")
                c = conn.cursor()

                c.execute("SELECT * FROM bill")
                records = c.fetchall()

                roww = 1
                for record in records:
                    if record[2] > 0:
                        lab1 = Label(myFrame, text=record[2], bg="white", font=("Microsoft Sans Serif", 11), width=13)
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

            def exxit():
                ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=root1)
                if ans:
                    root1.destroy()
                    global entry1, entry2
                    entry1.delete(0, END)
                    entry2.delete(0, END)
                    entry1.focus()

            imgeee = ImageTk.PhotoImage(Image.open('images/dashboard.png'))
            labloooo = Label(root1, image=imgeee).place(x=0, y=0)

            btn1 = Button(root1, text='Inventory', width=8, bg='#007884', fg='white', bd=0, font=("Poppins", 15),
                          activebackground='#007884', cursor="hand2", command=inventorryy).place(x=450, y=280)
            btn2 = Button(root1, text='Employee', width=8, bg='#007884', fg='white', bd=0, font=("Poppins", 15),
                          activebackground='#007884', cursor="hand2", command=employeee).place(x=677, y=280)
            btn3 = Button(root1, text='Invoices', width=8, bg='#007884', fg='white', bd=0, font=("Poppins", 15),
                          activebackground='#007884', cursor="hand2", command=invoiceee).place(x=566, y=510)

            btn4 = Button(root1, text='Log-Out', width=8, bg='#007884', fg='white',activebackground='#007884',
                          command= exxit, bd=0, font=("Poppins", 15), cursor="hand2").place(x=1056, y=610)


            root1.mainloop()

        else:
            conn = sqlite3.connect('database_employee.db')

            c = conn.cursor()

            c.execute('SELECT *,oid FROM addresses')

            records = c.fetchall()
            In = False

            for record in records:
                global window
                if record[0] == entry1.get() and record[5] == entry2.get():
                    In = True
                    window = Toplevel()
                    window.title("Billing")
                    window.geometry("1191x670+145+50")
                    window.iconbitmap('images/Icon.ico')
                    window.resizable(0, 0)

                    # Background Image
                    bg = ImageTk.PhotoImage(file="images/employeeWindow.png")
                    bg_image = Label(window, image=bg).place(x=0, y=0)

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
                        records = c.fetchall()  # Storing all the data of database in 'records' variable

                        category_value = []
                        for record in records:  # Looping through records to store category values in list
                            category_value.append(record[1])

                        return category_value

                    # Function that shows sub category values in 'Sub Category' combobox
                    def sub_category_input():
                        conn = sqlite3.connect('database.db')
                        c = conn.cursor()

                        c.execute("SELECT *, oid FROM second")
                        records = c.fetchall()

                        sub_category_value = []
                        for record in records:  # Looping through records to store sub category values in list
                            sub_category_value.append(record[2])

                        return sub_category_value

                    # Function that shows products values in 'Product' combobox
                    def product_input():
                        conn = sqlite3.connect('database.db')
                        c = conn.cursor()

                        c.execute("SELECT *, oid FROM second")
                        records = c.fetchall()

                        product_value = []
                        for record in records:  # Looping through records to store products values in list
                            product_value.append(record[0])

                        return product_value

                    bill_list = [[[], [], []]]  # Empty list to store all data before adding to database
                    product_list = bill_list[0][0]
                    quantity_list = bill_list[0][1]

                    # Function that adds product to the bill
                    roww = 0
                    index_increment = 0

                    def addToCart():
                        global roww
                        global index_increment
                        global lab1
                        global lab2
                        global lab3

                        # Showing messagebox if given condition occurs
                        if category.get() == '' or subCategory.get() == '' or product.get() == '' or quantityEntry.get() == '':
                            messagebox.showerror("Incomplete Information!!", "Please fill up all the product details!")

                        else:
                            conn = sqlite3.connect('database.db')
                            c = conn.cursor()

                            c.execute("SELECT *, oid FROM second")
                            records = c.fetchall()

                            # Looping through records and appending all cost price in empty list
                            sp_value = []
                            for record in records[:]:
                                sp_value.append(record[7])

                            # Looping through records and appending all products in empty list
                            product_value = []
                            for record in records:
                                product_value.append(record[0])

                            # Appending to all products and quantities in empty list 'bill_list'
                            bill_list[0][0].append(product.get())
                            bill_list[0][1].append(int(quantityEntry.get()))

                            # Looping through list to display added products in bill
                            for value in bill_list:
                                lab1 = Label(myFrame, text=value[0][index_increment], width=20, bg="white")
                                lab1.grid(row=roww, column=1)

                                lab2 = Label(myFrame, text=value[1][index_increment], width=45, bg="white")
                                lab2.grid(row=roww, column=2)

                                index_of_product = product_value.index(product.get())
                                lab3 = Label(myFrame,
                                             text=int(value[1][index_increment]) * int(sp_value[index_of_product]),
                                             width=6, bg="white")
                                lab3.grid(row=roww, column=3)

                                bill_list[0][2].append(int(value[1][index_increment]) * int(sp_value[index_of_product]))

                                index_increment += 1
                                roww += 1

                    # Function that removes product from the bill
                    index = 0

                    def remove():
                        global roww
                        global index
                        global rowww
                        global index_increment
                        global index_increment_copy
                        global product_list
                        global quantity_list
                        global i

                        index_increment_copy = 0
                        i = 0
                        rowww = 0

                        conn = sqlite3.connect('database.db')
                        c = conn.cursor()

                        c.execute("SELECT *, oid FROM second")
                        records = c.fetchall()

                        sp_value = []
                        for record in records[:]:
                            sp_value.append(record[7])

                        product_value = []
                        for record in records:
                            product_value.append(record[0])

                        # Destroying all the widgets of 'myFrame' frame
                        for widgets in myFrame.winfo_children():
                            widgets.destroy()
                        myFrame.configure(bg="white")

                        remove_product = str(product.get())
                        remove_quantity = int(quantityEntry.get())

                        # Removing selected product's data from the list
                        bill_list[0][0].remove(remove_product)
                        index_of_product = product_value.index(product.get())
                        bill_list[0][2].remove(remove_quantity * int(sp_value[index_of_product]))
                        bill_list[0][1].remove(remove_quantity)

                        product_list = bill_list[0][0]
                        quantity_list = bill_list[0][1]

                        # Displaying all the data in bill after removing selected product's data
                        a = 0
                        while i != len(product_list):
                            labb1 = Label(myFrame, text=product_list[index_increment_copy], width=20, bg="white")
                            labb1.grid(row=rowww, column=1)

                            labb2 = Label(myFrame, text=quantity_list[index_increment_copy], width=45, bg="white")
                            labb2.grid(row=rowww, column=2)

                            index_of_product = product_value.index(product_list[a])

                            labb3 = Label(myFrame, text=int(quantity_list[index_increment_copy]) * int(sp_value[index_of_product]), width=6, bg="white")
                            labb3.grid(row=rowww, column=3)

                            i += 1
                            index_increment_copy += 1
                            rowww += 1
                            a += 1

                        roww -= 1
                        index += 1
                        index_increment = len(bill_list[0][1])

                    # Function that calculates and shows total price
                    def total():
                        global sum

                        conn = sqlite3.connect('database.db')
                        c = conn.cursor()

                        c.execute("SELECT *, oid FROM second")
                        records = c.fetchall()

                        sum = 0

                        sp_value = []
                        for record in records[:]:
                            sp_value.append(record[7])

                        product_value = []
                        for record in records:
                            product_value.append(record[0])

                        product_list = bill_list[0][0]
                        quantity_list = bill_list[0][1]

                        i = 0
                        while i != len(quantity_list):
                            product = bill_list[0][0][i]

                            index_of_product = product_value.index(product)
                            sum += int(quantity_list[i]) * int(sp_value[index_of_product])
                            i += 1

                        total_label = Label(myFrame2, text="Total", bg="white", font=("Poppins", 13), width=15)
                        total_label.grid(row=0, column=0)

                        total_amount = Label(myFrame2, text=f"Rs. {sum}", bg="white", font=("Poppins", 13), width=75)
                        total_amount.grid(row=0, column=1)

                        index_increment = len(bill_list[0][1])

                    # Function that generates bill and store bill data in database
                    def generate():
                        global bill_label_1
                        global bill_label_2
                        global bill_label_3
                        global bill_label_4
                        global sum

                        product_list_string = f'"{product_list}"'
                        quantity_list_string = f'"{quantity_list}"'

                        # Displaying messagebox if below conditions occur
                        if customerName.get() == '' or contactNum.get() == '' or category.get() == '' or subCategory.get() == '' or product.get() == '' or quantityEntry.get() == '':
                            messagebox.showerror("Incomplete Information!!", "Please fill up all the details!", parent=window)

                        else:
                            connect = sqlite3.connect('billDatabase.db')
                            cursor = connect.cursor()

                            cursor.execute("SELECT * FROM bill")
                            bill_records = cursor.fetchall()
                            bill_number = int(bill_records[-1][2]) + 1

                            connect.close()

                            conn = sqlite3.connect('billDatabase.db')
                            c = conn.cursor()

                            c.execute(
                                "INSERT INTO bill VALUES (:customer_name, :contact_num, :bill_num, :date, :product, :quantity, :total)",

                                {
                                    'customer_name': customerName.get(),
                                    'contact_num': contactNum.get(),
                                    'bill_num': bill_number,
                                    'date': current_date,
                                    'product': product_list_string,
                                    'quantity': quantity_list_string,
                                    'total': sum,
                                })
                            c.execute("SELECT *,oid FROM bill")

                            records = c.fetchall()

                            # Displaying customer information on bill
                            bill_label_1 = Label(window, text=customerName.get(), font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
                            bill_label_1.place(x=670, y=230)

                            bill_label_2 = Label(window, text=contactNum.get(), font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
                            bill_label_2.place(x=670, y=255)

                            bill_label_3 = Label(window, text=current_date, font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
                            bill_label_3.place(x=995, y=230)

                            bill_label_4 = Label(window, text=bill_number, font=("Microsoft Sans Serif", 13), bg="white", fg="#0D1C30")
                            bill_label_4.place(x=995, y=255)

                            messagebox.showinfo("Bill Generated Successfully!", "Bill has been added to the database successfully.", parent=window)

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

                        # --------------------------------------------------------------
                        connect = sqlite3.connect("database.db")
                        cursor = connect.cursor()

                        cursor.execute("SELECT * FROM second")

                        inventory_records = cursor.fetchall()

                        products_and_cp = {}
                        for record in inventory_records:
                            products_and_cp[record[0]] = record[7]
                        # ----------------------------------------------------------------

                        conn = sqlite3.connect("billDatabase.db")
                        c = conn.cursor()

                        c.execute("SELECT * FROM bill")
                        records = c.fetchall()

                        selected_bill_number = int(billNum.get())

                        # Looping through records to display all the data of searched bill number
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

                                # Quantities
                                myList2 = record[5]
                                # Converting string list into actual list
                                quantities = ast.literal_eval(myList2)  #
                                final_quantities = ast.literal_eval(quantities)

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


                    def exittt():
                        ans = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?", parent=window)
                        if ans:
                            window.destroy()
                            global entry1, entry2
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry1.focus()

                    # Creating and placing buttons
                    btn1 = Button(window, text="Search", font=("Poppins", 13, "bold"), border=0, bg="#007884",
                                  fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=search)
                    btn1.place(x=328, y=86)

                    btn2 = Button(window, text="LOGOUT", font=("Poppins", 12, "bold"), border=0, bg="#007884",
                                  fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=exittt)
                    btn2.place(x=1067, y=604)

                    btn3 = Button(window, text="Remove", font=("Poppins", 13, "bold"), border=0, bg="#007884",
                                  fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=remove)
                    btn3.place(x=235, y=448)

                    btn4 = Button(window, text="Clear", font=("Poppins", 13, "bold"), border=0, bg="#007884",
                                  fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=clear)
                    btn4.place(x=373, y=448)

                    btn5 = Button(window, text="Add", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white",
                                  activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=addToCart)
                    btn5.place(x=120, y=448)

                    btn6 = Button(window, text="Total", font=("Poppins", 13, "bold"), border=0, bg="#007884",
                                  fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=total)
                    btn6.place(x=85, y=538)

                    btn7 = Button(window, text="Generate", font=("Poppins", 12, "bold"), border=0, bg="#007884",
                                  fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=generate)
                    btn7.place(x=176, y=538)

                    btn8 = Button(window, text="Clear", font=("Poppins", 13, "bold"), border=0, bg="#007884",
                                  fg="white", activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=clear_bill)
                    btn8.place(x=302, y=538)

                    btn9 = Button(window, text="Exit", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white",
                                  activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=exittt)
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

                    label18 = Label(window, text="The Slytherin Store", bg="white", font=("Microsoft Sans Serif", 15))
                    label18.place(x=740, y=152)

                    label19 = Label(window, text="Kirtipur-4, Kathmandu, Nepal", bg="white", font=("Microsoft Sans Serif", 13))
                    label19.place(x=720, y=180)

                    label20 = Label(window, text="Ph: 01-43344990", bg="white", font=("Microsoft Sans Serif", 13))
                    label20.place(x=760, y=205)

                    # Creating and placing entries
                    billNum = Entry(window, bd=0, width=12, font=("Franklin Gothic Medium", 13))
                    billNum.place(x=180, y=92)
                    billNum.focus()

                    customerName = Entry(window, bd=0, width=22, font=("Franklin Gothic Medium", 13))
                    customerName.place(x=590, y=92)

                    contactNum = Entry(window, bd=0, width=16, font=("Franklin Gothic Medium", 13))
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

                    # Creating frame for displaying bill
                    wrapper1 = LabelFrame(window, height=800, width=1000, bd=0)
                    myCanvas = Canvas(wrapper1, height=230, width=590, bg='white')
                    myCanvas.pack(side=LEFT, fill='y', expand='yes')
                    myFrame = Frame(myCanvas)
                    myCanvas.create_window((0, 0), window=myFrame, anchor='nw')
                    wrapper1.place(x=532, y=320)

                    # Creating frame for displaying total price
                    wrapper2 = LabelFrame(window, height=800, width=1000, bd=0)
                    myCanvas2 = Canvas(wrapper2, height=30, width=590, bg='white')
                    myCanvas2.pack(side=LEFT, fill='y', expand='yes')
                    myFrame2 = Frame(myCanvas2)
                    myCanvas2.create_window((0, 0), window=myFrame2, anchor='nw')
                    wrapper2.place(x=532, y=550)

                    conn.commit()
                    conn.close()

                    mainloop()

            if In== False:
                messagebox.showinfo('Invalid','Enter the right combination')

            conn.close()

    fg = PhotoImage(file="images/login.png")
    main_label = Label(root,image=fg)
    main_label.pack()
    global entry1, entry2

    entry1 = Entry(root, font=("Poppins", 13), width=30, border=0, bg="#30355A", fg="White")
    entry1.place(x=525, y=280, height=35)

    entry2 = Entry(root, font=("Poppins", 13), width=30, border=0, show='*', bg="#30355A", fg="white")
    entry2.place(x=525, y=355, height=35)

    Frame(root, width=278, height=2, bg='#141414').place(x=520, y=393)
    Frame(root, width=278, height=2, bg='#141414').place(x=520, y=320)

    button_log = Button(root, text="Login", width=28, border=0, fg="white", bg="#051C36", activebackground="#051C36", activeforeground="white", cursor="hand2", command=login_window)
    button_log.configure(font="-family {Poppins} -size 14")
    button_log.place(x=490, y=511, height=49)


splash.after(800, main_window)
splash.mainloop()
