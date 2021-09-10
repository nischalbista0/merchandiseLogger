from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox
import time
import ast
import sqlite3



root1 = Tk()

root1.geometry('1191x671')


def inventorryy():
    root = Toplevel()
    root.geometry('1193x671')
    root.title('Just checking')
    root.resizable(False, False)
    '''
    fontt = Font(
        family='Poppins',
        size=10,
        # weight='bold'
    )
    '''
    font1 = Font(
        family='Poppins',
        size=14,
        # weight='bold'
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
                Label(myframe, text=Ent1.get(), bg='blue', width=10).grid(row=1, column=0)
                Label(myframe, text=record[0], bg='blue', width=30).grid(row=1, column=1)
                Label(myframe, text=record[1], bg='blue', width=13).grid(row=1, column=2)
                Label(myframe, text=record[2], bg='blue', width=10).grid(row=1, column=3)
                Label(myframe, text=record[3], bg='blue', width=10).grid(row=1, column=4)
                Label(myframe, text=record[8], bg='blue', width=10).grid(row=1, column=5)
                Label(myframe, text=record[9], bg='blue', width=10).grid(row=1, column=6)

            conn.commit()

            conn.close()
        else:
            messagebox.showwarning('Empty Field', 'Please enter in the search field')

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
            messagebox.showwarning('Empty field', 'Please Enter the number in the field')

    def inven_update():
        if Ent1.get() != '':

            global imgg
            inven = Toplevel()
            inven.geometry('1193x671')
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
                    # print(records)
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
                    messagebox.showwarning('Empty field', 'Please fill all Entries')

            conn = sqlite3.connect('database.db')

            c = conn.cursor()

            imgg = ImageTk.PhotoImage(Image.open('C:/Users/dell/Desktop/Changed_UI/Update_Product.jpg'))
            lablo = Label(inven, image=imgg).place(x=0, y=0)
            btn1 = Button(inven, text='Update', bg='#007884', height=1, width=13, fg='white', cursor='hand2',
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
            messagebox.showwarning('Empty Field', 'Please Enter a number in the field')

    def inven_add():
        global imge
        inven = Toplevel()
        inven.geometry('1193x671')
        inven.resizable(False, False)

        def clear_all():
            ls = [en1a, en2a, en3a, en4a, en5a, en6a, en7a]

            for i in ls:
                i.delete(0, END)

        def add_product():
            if en1a.get() != '' and en2a.get() != '' and en3a.get() != '' and en4a.get() != '' and en5a.get() != '' and en6a.get() != '' and en7a.get() != '':

                conn = sqlite3.connect('database.db')

                c = conn.cursor()

                # only for reference

                # product text,
                # category text,
                # sub_category text,
                # In_stock integer,
                # customer_name text,
                # contact_number text,
                # bill_number text,
                # selling_price integer,
                # cost_price integer,
                # vendor_no text

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
                # print(records)
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
                messagebox.showwarning('Empty Field', 'Please fill all Entries')

        imge = ImageTk.PhotoImage(Image.open('C:/Users/dell/Desktop/Changed_UI/Add_Product.jpg'))
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

    img = ImageTk.PhotoImage(Image.open('C:/Users/dell/Desktop/Changed_UI/Inventory.jpg'))
    lable = Label(root, image=img).place(x=0, y=0)

    lab1 = Label(root, text='Menu', bg='white', font=font1)
    lab1.place(x=66, y=152)

    Ent1 = Entry(root, bd=0, width=16, bg='white', fg='black', font=font1)
    Ent1.place(x=70, y=210)

    btn1 = Button(root, text='Logout', height=1, width=6, bg='#007884', activebackground='#007884', bd=0, font=font1,
                  cursor='hand2',
                  fg='white').place(x=70, y=96)

    btn2 = Button(root, text='Search', height=1, width=7, bg='#007884', activebackground='#007884', bd=0, font=font1,
                  fg='white', cursor='hand2', command=search_it).place(
        x=263, y=213)

    btn3 = Button(root, text='Add Product', height=1, width=19, bg='#007884', activebackground='#007884', fg='white',
                  font=font1, bd=0, cursor='hand2',
                  command=inven_add).place(x=94, y=323)

    btn4 = Button(root, text='Update Product', height=1, width=19, bg='#007884', activebackground='#007884', fg='white',
                  cursor='hand2',
                  command=inven_update, font=font1, bd=0).place(x=92, y=405)

    btn5 = Button(root, text='Delete Product', height=1, width=19, bg='#007884', activebackground='#007884', font=font1,
                  fg='white', cursor='hand2',
                  bd=0, command=deletee).place(x=92, y=485)

    btn6 = Button(root, text='Exit', height=1, width=7, bg='#007884', bd=0, activebackground='#007884', font=font1,
                  cursor='hand2', fg='white').place(
        x=158, y=554)

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
    # print(records)
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

def employeee():
    root = Toplevel()
    root.geometry("1191x670")
    root.title("Employee Management")
    root.resizable(False, False)

    # -------------DATABASE----------------
    # Create a databases or connect to one
    conn = sqlite3.connect("database_employee.db")

    # Create cursor
    c = conn.cursor()

    # query of the database
    #c.execute("SELECT *, oid FROM addresses")


     #Create table
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
            # print(records)
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
            messagebox.showinfo("Great!!", "Employee ID : " + searchbox.get() + " " + "is found.")

            searchbox.delete(0, END)

            conn.commit()
            conn.close()

        else:
            messagebox.showwarning('Empty Field', 'Please enter in the search field')

    # -----------------Update the existing data-----------------
    # Create an update function
    def emp_update():
        if searchbox.get() != '':
            editor = Toplevel()
            editor.title("Update Employee")
            editor.geometry("1191x670")
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

                # print(records)
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
                messagebox.showinfo("Addresses", "Updated Successfully")

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

            # Create clock for the current time
            def clock():
                hour = time.strftime("%I")
                minute = time.strftime("%M")
                second = time.strftime("%S")
                disp_time.config(text=hour + ":" + minute + ":" + second)
                disp_time.after(1000, clock)

            def update():
                disp_time.config(1000, clock)

            disp_time = Label(editor, text="", font=("Arial", 20), bg="white", fg="black")
            disp_time.place(x=985, y=45)

            clock()

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
                l = [namebox_editor, contactbox_editor, citizenbox_editor, designationbox_editor, addressbox_editor,
                     passwordbox_editor]

                for i in l:
                    i.delete(0, END)

            # Create buttons
            update_bt_editor = Button(editor, text="Update", bg="#007884", fg="White", activeforeground="White",
                                      activebackground="#007884", borderwidth=0, pady=0, cursor="hand2", command=edit)
            update_bt_editor.configure(font="-family {Poppins} -size 14")
            update_bt_editor.place(x=480, y=523)

            clear_bt_editor = Button(editor, text="Clear", bg="#007884", fg="White", activeforeground="White",
                                     activebackground="#007884", borderwidth=0, cursor="hand2", command=update_clear)
            clear_bt_editor.configure(font="-family {Poppins} -size 14")
            clear_bt_editor.place(x=655, y=522)

            conn.commit()
            conn.close()

        else:
            messagebox.showwarning('Empty Field', 'Please enter in the search field')

    # -----------------Add new data---------------------
    def add_emp():
        global bg
        top = Toplevel()
        top.title("Add Employee")
        top.geometry("1191x670")
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

                # print(records)
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
                messagebox.showinfo("Addresses", "Inserted Successfully")

                conn.commit()
                conn.close()
                top.destroy()

            else:
                messagebox.showwarning("Warning!", "Fill up Everything")

        # Define image as background in Add Employee window
        bg = ImageTk.PhotoImage(file="images/add_emp.png")
        bg_label = Label(top, image=bg)
        bg_label.place(x=0, y=0)

        # Create clock for the current time
        def clock():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            disp_time.config(text=hour + ":" + minute + ":" + second)
            disp_time.after(1000, clock)

        def update():
            disp_time.config(1000, clock)

        disp_time = Label(top, text="", font=("Arial", 20), bg="white", fg="black")
        disp_time.place(x=985, y=45)

        clock()

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
            print('Deleted Successfully')

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
            messagebox.showwarning('Empty Field', 'Please enter in the search field')

    # Define image as background
    bg1 = ImageTk.PhotoImage(file="images/emp_mngt.png")
    bg_label = Label(root, image=bg1)
    bg_label.place(x=0, y=0)

    # Create clock for the current time
    def clock():
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        disp_time.config(text=hour + ":" + minute + ":" + second)
        disp_time.after(1000, clock)

    def update():
        disp_time.config(1000, clock)

    disp_time = Label(root, text="", font=("Arial", 20), bg="white", fg="black")
    disp_time.place(x=1031, y=45)

    clock()

    # Create Search box
    entry_font = ('Poppins', 12)
    searchbox = Entry(root, borderwidth=0, font=entry_font)
    searchbox.place(x=93, y=160)

    # Create buttons
    search_bt = Button(root, text="Search", bg="#007884", activebackground="#007884",
                       fg="White", activeforeground="White",
                       borderwidth=0, cursor="hand2",
                       command=search)
    search_bt.configure(font="-family {Poppins} -size 14")
    search_bt.place(x=315, y=149)

    add_bt = Button(root, text="Add Employee", bg="#007884", activebackground="#007884",
                    fg="White", activeforeground="White", borderwidth=0, cursor="hand2",
                    command=add_emp)
    add_bt.configure(font="-family {Poppins} -size 14")
    add_bt.place(x=156, y=280)

    update_bt = Button(root, text="Update Employee", bg="#007884", activebackground="#007884",
                       fg="White", activeforeground="White", borderwidth=0, cursor="hand2",
                       command=emp_update)
    update_bt.configure(font="-family {Poppins} -size 14")
    update_bt.place(x=140, y=360)

    delete_bt = Button(root, text="Delete Employee", bg="#007884", activebackground="#007884",
                       fg="White", activeforeground="White", borderwidth=0, cursor="hand2", command=delete)
    delete_bt.configure(font="-family {Poppins} -size 14")
    delete_bt.place(x=140, y=440)

    exit_bt = Button(root, text="Exit", bg="#007884", activebackground="#007884",
                     fg="White", activeforeground="White", borderwidth=0, command=root.quit, cursor="hand2")
    exit_bt.configure(font="-family {Poppins} -size 14")
    exit_bt.place(x=200, y=540)

    logout_bt = Button(root, text="Log Out", fg="White", activeforeground="White",
                       bg="#007884",
                       activebackground="#007884",
                       borderwidth=0, cursor="hand2")
    logout_bt.configure(font="-family {Poppins} -size 14")
    logout_bt.place(x=1046, y=607)

    # -------------Create Frame with scrollbar--------------
    cover = LabelFrame(root, height=800, width=1000, bd=0)
    cover.place(x=457, y=100)

    mycanvas = Canvas(cover, height=495, width=663, bg="white")
    mycanvas.pack(side=LEFT, fill='y', expand='yes')

    myframe = Frame(mycanvas)
    mycanvas.create_window((0, 0), window=myframe, anchor='nw')

    yscrollbar = ttk.Scrollbar(cover, orient='vertical', command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill='y')
    mycanvas.config(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    # -------------------------------------------------------------

    # Create labels
    title = Label(root, text="Employee Management", fg="Black", bg="white", font=('Helvetica', 20, 'bold'))
    title.place(x=450, y=40)

    menu_label = Label(root, text="Menu", bg="white")
    menu_label.configure(font="-family {Poppins} -size 14")
    menu_label.place(x=135, y=85)

    id_label = Label(root, text="Employee ID", bg="white")
    id_label.configure(font="-family {Poppins} -size 14")
    id_label.place(x=90, y=128)

    options_label = Label(root, text="Employee Options", bg="white")
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

    root.mainloop()

def invoiceee():
    root = Toplevel()
    root.title("Invoices")
    root.geometry("1191x670")
    root.resizable(0, 0)

    # Background Image setup
    bg = ImageTk.PhotoImage(file="images/invoice_window.png")
    bg_image = Label(root, image=bg).place(x=0, y=0)

    # Function that searches the bill number and highlights it at the top
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

        label4 = Label(myFrame, text="Date", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=10,
                       fg="#0D1C30")
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
                    Label(myFrame, text=record[2], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"), width=15).grid(
                        row=roww, column=0)
                    Label(myFrame, text=record[0], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"), width=22).grid(
                        row=roww, column=1)
                    Label(myFrame, text=record[1], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"), width=22).grid(
                        row=roww, column=2)
                    Label(myFrame, text=record[3], bg="cyan", font=("Microsoft Sans Serif", 11, "bold"), width=12).grid(
                        row=roww, column=3)

                if record[2] > 0:
                    Label(myFrame, text=record[2], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(
                        row=rowww,
                        column=0)
                    Label(myFrame, text=record[0], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(
                        row=rowww,
                        column=1)
                    Label(myFrame, text=record[1], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(
                        row=rowww,
                        column=2)
                    Label(myFrame, text=record[3], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(
                        row=rowww,
                        column=3)
                    rowww += 1

                myFrame.config(bg="white")

            conn.commit()
            conn.close()

    # Function that displays searched bill in new window
    def open():
        connect = sqlite3.connect("database.db")
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM second")

        inventory_records = cursor.fetchall()
        print(inventory_records)

        products_and_cp = {}
        for record in inventory_records:
            products_and_cp[record[0]] = record[7]

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

                        lab3 = Label(myFrame, text=int(quantity) * int(products_and_cp[final_product_list[q_row]]),
                                     width=6,
                                     bg="white")
                        lab3.grid(row=q_row, column=3)
                        q_row += 1

        conn.commit()
        conn.close()

    # Creating and placing buttons
    button1 = Button(root, text="Search", font=("Poppins", 14, "bold"), border=0, bg="#007884", fg="white",
                     activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=search)
    button1.place(x=300, y=175)

    button2 = Button(root, text="Show Invoice", font=("Poppins", 14, "bold"), border=0, bg="#007884", fg="white",
                     activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2", command=open)
    button2.place(x=160, y=315)

    button3 = Button(root, text="Exit", font=("Poppins", 14, "bold"), border=0, bg="#007884", fg="white",
                     activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
    button3.place(x=205, y=520)

    button4 = Button(root, text="LOGOUT", font=("Poppins", 13, "bold"), border=0, bg="#007884", fg="white",
                     activebackground="#007884", activeforeground="#f1f1e6", cursor="hand2")
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
    label1 = Label(myFrame, text="Bill Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=13,
                   fg="#0D1C30")
    label1.grid(row=0, column=0)

    label2 = Label(myFrame, text="Customer Name", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20,
                   fg="#0D1C30")
    label2.grid(row=0, column=1)

    label3 = Label(myFrame, text="Contact Number", bg="white", font=("Microsoft Sans Serif", 13, "bold"), width=20,
                   fg="#0D1C30")
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

            Label(myFrame, text=record[0], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=roww,
                                                                                                         column=1)
            Label(myFrame, text=record[1], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=roww,
                                                                                                         column=2)
            Label(myFrame, text=record[3], bg="white", font=("Microsoft Sans Serif", 11), width=13).grid(row=roww,
                                                                                                         column=3)
            roww += 1

        myFrame.config(bg="white")

    conn.commit()
    conn.close()

    # Creating and placing entry
    billNumber = Entry(root, bd=0, width=20, font=("Franklin Gothic Medium", 13))
    billNumber.place(x=68, y=185)
    billNumber.focus()

    mainloop()


imgeee = ImageTk.PhotoImage(Image.open('C:/Users/dell/Desktop/finback1-01.png'))
labloooo = Label(root1, image=imgeee).place(x=0, y=0)

btn1 = Button(root1,text= 'click-me', height=2, width=8, bg='#007884', fg='white', bd=0, activebackground='#007884', command=inventorryy).place(x=464, y=286)

btn2 = Button(root1, text='click-here', height=2, width=8, bg='#007884', fg='white',bd=0, activebackground='#007884', command=employeee).place(x=683, y=286)

btn3 = Button(root1, text='Don\'t_._me', height=2, width=8, bg='#007884', fg='white',bd=0, activebackground='#007884', command=invoiceee).place(x=576, y=512)










root1.mainloop()