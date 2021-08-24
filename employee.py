from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("1191x670")
root.resizable(False, False)

#DATABASE
# Create a databases or connect to one
conn = sqlite3.connect("database_employee.db")

#Create cursor
c = conn.cursor()

# query of the database
c.execute("SELECT *, oid FROM addresses")

'''
# Create table
c.execute(""" CREATE TABLE addresses(
      emp_name text,
      contact_no integer,
      citizen_no integer,
      designation text,
      address text,
      password text
) """)'''

def search_it():
    conn = sqlite3.connect("database_employee.db")

    c = conn.cursor()

    # query of the database
    c.execute("SELECT * FROM addresses WHERE oid=" + searchbox.get())

    records = c.fetchall()
    # print(records)

    # Loop through the results
    for record in records:
        Label(myframe, text = searchbox.get(), bg = "green" ,width = 10).grid(row = 1, column = 0)
        Label(myframe, text=record[0], bg='green', width=30).grid(row=1, column=1)
        Label(myframe, text=record[1], bg='green', width=13).grid(row=1, column=2)
        Label(myframe, text=record[2], bg='green', width=10).grid(row=1, column=3)
        Label(myframe, text=record[3], bg='green', width=10).grid(row=1, column=4)
        Label(myframe, text=record[4], bg='green', width=10).grid(row=1, column=5)
        Label(myframe, text=record[5], bg='green', width=10).grid(row=1, column=6)

    # showinfo messagebox
    messagebox.showinfo("Great!!", "Employee ID : " + searchbox.get() +" "+ "is found.")

    searchbox.delete(0, END)

    conn.commit()
    conn.close()

#Creating an update function
def emp_update():
    editor = Toplevel()  # using top to call instead of Tk()
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
         password = :password,
         address = :address
         WHERE oid = :oid""",
         {'name': namebox_editor.get(),
          'contact': contactbox_editor.get(),
          'citizen': citizenbox_editor.get(),
          'password': designationbox_editor.get(),
          'address': addressbox_editor.get(),
          'designation': passwordbox_editor.get(),
          'oid': record_id

          }
        )

        editor.destroy()

        # query of the database
        c.execute("SELECT *, oid FROM addresses")

        records = c.fetchall()
        # print(records)

        # Loop through the results
        place = 1
        for record in records:
            Label(myframe, text=record[6], bg="#F2F2F2", width=10).grid(row=place, column=0)
            Label(myframe, text=record[0], bg="#F2F2F2", width=30).grid(row=place, column=1)
            Label(myframe, text=record[1], bg="#F2F2F2", width=13).grid(row=place, column=2)
            Label(myframe, text=record[2], bg="#F2F2F2", width=10).grid(row=place, column=3)
            Label(myframe, text=record[3], bg="#F2F2F2", width=10).grid(row=place, column=4)
            Label(myframe, text=record[4], bg="#F2F2F2", width=10).grid(row=place, column=5)
            Label(myframe, text=record[5], bg="#F2F2F2", width=10).grid(row=place, column=6)
            place +=1

        conn.commit()
        conn.close()

    # Create a databases or connect to one
    conn = sqlite3.connect("database_employee.db")

    # Create cursor
    c = conn.cursor()

    global bgg
    # Define image as background
    bgg = ImageTk.PhotoImage(file="images/update_emp.png")
    bg_label = Label(editor, image=bgg)
    bg_label.place(x=0, y=0)

    # Create a databases or connect to one
    conn = sqlite3.connect("database_employee.db")

    # Create cursor
    c = conn.cursor()

    # creating labels
    title = Label(editor, text="Update Employee", fg="Black", bg = "White", font=('Helvetica', 20, 'bold'))
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

    # creating entryboxes
    entry_font = ('Poppins', 12)
    namebox_editor = Entry(editor, borderwidth=0, font=entry_font)
    namebox_editor.place(x=165, y=220)

    entry_font = ('Poppins', 12)
    contactbox_editor = Entry(editor, borderwidth=0, font=entry_font)
    contactbox_editor.place(x=165, y=295)

    entry_font = ('Poppins', 12)
    citizenbox_editor = Entry(editor, borderwidth=0, font=entry_font)
    citizenbox_editor.place(x=165, y=368)

    entry_font = ('Poppins', 12)
    designationbox_editor = Entry(editor, borderwidth=0, font=entry_font)
    designationbox_editor.place(x=630, y=220)

    entry_font = ('Poppins', 12)
    addressbox_editor = Entry(editor, borderwidth=0, font=entry_font)
    addressbox_editor.place(x=630, y=295)

    entry_font = ('Poppins', 12)
    passwordbox_editor = Entry(editor, borderwidth=0, font=entry_font)
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

    # clearing everything from the update's textbox
    def update_clear():
        l = [namebox_editor, contactbox_editor, citizenbox_editor, designationbox_editor, addressbox_editor, passwordbox_editor]

        for i in l:
            i.delete(0, END)

    # creating buttons
    update_bt_editor = Button(editor, text="Update", bg="#007884", fg="White", activeforeground = "White",
                       activebackground="#007884", borderwidth=0, pady=0,cursor = "hand2", command = edit)
    update_bt_editor.configure(font="-family {Poppins} -size 14")
    update_bt_editor.place(x=480, y=523)

    clear_bt_editor = Button(editor, text="Clear", bg="#007884", fg="White", activeforeground = "White",
                      activebackground="#007884", borderwidth=0, cursor = "hand2", command= update_clear)
    clear_bt_editor.configure(font="-family {Poppins} -size 14")
    clear_bt_editor.place(x=655, y=522)

    searchbox.delete(0, END)
    conn.commit()
    conn.close()

def add_emp():
    global bg
    top = Toplevel()  # using top to call instead of Tk()
    top.title("Add Employee")
    top.geometry("1191x670")
    top.resizable(False, False)

    # Create submit button for databases
    def submit():
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
        # print(records)

        # Loop through the results
        place = 1
        for record in records:
            Label(myframe, text=record[6], bg="#F2F2F2", width=10).grid(row=place, column=0)
            Label(myframe, text=record[0], bg="#F2F2F2", width=30).grid(row=place, column=1)
            Label(myframe, text=record[1], bg="#F2F2F2", width=13).grid(row=place, column=2)
            Label(myframe, text=record[2], bg="#F2F2F2", width=10).grid(row=place, column=3)
            Label(myframe, text=record[3], bg="#F2F2F2", width=10).grid(row=place, column=4)
            Label(myframe, text=record[4], bg="#F2F2F2", width=10).grid(row=place, column=5)
            Label(myframe, text=record[5], bg="#F2F2F2", width=10).grid(row=place, column=6)
            place += 1

        # showinfo messagebox
        messagebox.showinfo("Addresses", "Inserted Successfully")

        conn.commit()
        conn.close()
        top.destroy()

    # Define image as background
    bg = ImageTk.PhotoImage(file="images/add_emp.png")
    bg_label = Label(top, image=bg)
    bg_label.place(x=0, y=0)

    # creating labels
    title = Label(top, text="Add Employee", fg="Black", bg = "White", font=('Helvetica', 20, 'bold'))
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

    def add_clear():
        l = [namebox, contactbox, citizenbox, designationbox, addressbox, passwordbox]

        for i in l:
            i.delete(0, END)

    '''
    # popping up messsage if the entry widget is empty
    def empty_add():
        if len(namebox.get()) == 0:
            messagebox.showinfo("Warning!", "Fill up Everything")
        elif len(contactbox.get()) == 0:
            messagebox.showinfo("Warning!", "Fill up Everything")
        elif len(citizenbox.get()) == 0:
            messagebox.showinfo("Warning!", "Fill up Everything")
        elif len(designationbox.get()) == 0:
            messagebox.showinfo("Warning!", "Fill up Everything")
        elif len(addressbox.get()) == 0:
            messagebox.showinfo("Warning!", "Fill up Everything")
        elif len(passwordbox.get()) == 0:
            messagebox.showinfo("Warning!", "Fill up Everything")'''

    # creating entry boxes
    entry_font = ('Poppins', 12)
    namebox = Entry(top, borderwidth=0, font=entry_font)
    namebox.place(x=165, y=220)

    entry_font = ('Poppins', 12)
    contactbox = Entry(top, borderwidth=0, font=entry_font)
    contactbox.place(x=165, y=295)

    entry_font = ('Poppins', 12)
    citizenbox = Entry(top, borderwidth=0, font=entry_font)
    citizenbox.place(x=165, y=368)

    entry_font = ('Poppins', 12)
    designationbox = Entry(top, borderwidth=0, font=entry_font)
    designationbox.place(x=630, y=220)

    entry_font = ('Poppins', 12)
    addressbox = Entry(top, borderwidth=0, font=entry_font)
    addressbox.place(x=630, y=295)

    entry_font = ('Poppins', 12)
    passwordbox = Entry(top, borderwidth=0, font=entry_font)
    passwordbox.place(x=630, y=368)

    # creating buttons
    add_bt = Button(top, text="Add", bg="#007884", fg="White", activeforeground = "White",
                    activebackground="#007884", borderwidth=0, cursor = "hand2", command = submit)
    add_bt.configure(font="-family {Poppins} -size 14")
    add_bt.place(x=490, y=522)

    clear_bt = Button(top, text="Clear", bg="#007884", fg="White", activeforeground = "White",
                      activebackground="#007884", borderwidth=0, cursor = "hand2", command = add_clear)
    clear_bt.configure(font="-family {Poppins} -size 14")
    clear_bt.place(x=655, y=522)



#function to delete a data
def delete():
    # create database
    conn = sqlite3.connect("database_employee.db")

    #create cursor
    c = conn.cursor()

    #delete a record
    c.execute("DELETE from addresses WHERE oid = " + searchbox.get())
    print('Deleted Successfully')

    # query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()

    # Loop through the results
    place = 1
    for record in records:
        Label(myframe, text=record[6], bg="#F2F2F2", width=10).grid(row=place, column=0)
        Label(myframe, text=record[0], bg="#F2F2F2", width=30).grid(row=place, column=1)
        Label(myframe, text=record[1], bg="#F2F2F2", width=13).grid(row=place, column=2)
        Label(myframe, text=record[2], bg="#F2F2F2", width=10).grid(row=place, column=3)
        Label(myframe, text=record[3], bg="#F2F2F2", width=10).grid(row=place, column=4)
        Label(myframe, text=record[4], bg="#F2F2F2", width=10).grid(row=place, column=5)
        Label(myframe, text=record[5], bg="#F2F2F2", width=10).grid(row=place, column=6)
        place += 1

    Label(myframe, text='', bg="#F2F2F2", width=10).grid(row=place, column=0)
    Label(myframe, text='', bg="#F2F2F2", width=30).grid(row=place, column=1)
    Label(myframe, text='', bg="#F2F2F2", width=13).grid(row=place, column=2)
    Label(myframe, text='', bg="#F2F2F2", width=10).grid(row=place, column=3)
    Label(myframe, text='', bg="#F2F2F2", width=10).grid(row=place, column=4)
    Label(myframe, text='', bg="#F2F2F2", width=10).grid(row=place, column=5)
    Label(myframe, text='', bg="#F2F2F2", width=10).grid(row=place, column=6)

    searchbox.delete(0, END)
    conn.commit()

    conn.close()


#Define image as background
bg1 =ImageTk.PhotoImage(file = "images/Employee_mgt.png")
bg_label = Label(root, image = bg1)
bg_label.place(x = 0, y = 0)


#creating buttons
logout_bt = Button(root, text = "Log Out", fg = "White", activeforeground = "White",
                   bg = "#007884",
                   activebackground="#007884",
                   borderwidth = 0, cursor = "hand2")
logout_bt.configure(font = "-family {Poppins} -size 14")
logout_bt.place(x = 1046, y = 607)

#creating entry box
entry_font = ('Poppins', 12)
searchbox = Entry(root, borderwidth = 0, bg = "#f2f2f2", font = entry_font)
searchbox.place(x = 105, y = 160)

#popping up messsage if the entry widget is empty
def emp_search():
    if len(searchbox.get()) == 0:
        messagebox.showinfo("Warning!", "Its empty! Write something")

search_bt = Button(root, text = "Search", bg = "#007884", activebackground = "#007884",
                   fg = "White", activeforeground = "White",
                   borderwidth = 0, cursor = "hand2",
                   command = search_it)
search_bt.configure(font = "-family {Poppins} -size 14")
search_bt.place(x = 315, y = 138)

add_bt = Button(root, text = "Add Employee", bg = "#007884", activebackground = "#007884",
                fg = "White", activeforeground = "White",borderwidth = 0, cursor = "hand2",
                command = add_emp)
add_bt.configure(font = "-family {Poppins} -size 14")
add_bt.place(x = 156, y = 280)

update_bt = Button(root, text = "Update Employee", bg = "#007884", activebackground = "#007884",
                   fg = "White", activeforeground = "White", borderwidth = 0, cursor = "hand2",
                   command = emp_update)
update_bt.configure(font = "-family {Poppins} -size 14")
update_bt.place(x = 140, y = 360)

delete_bt = Button(root, text = "Delete Employee", bg = "#007884", activebackground = "#007884",
                   fg = "White", activeforeground = "White", borderwidth = 0, cursor = "hand2", command = delete)
delete_bt.configure(font = "-family {Poppins} -size 14")
delete_bt.place(x = 140, y = 440)

exit_bt = Button(root, text = "Exit", bg = "#007884", activebackground = "#007884",
                 fg = "White", activeforeground = "White", borderwidth = 0, command = root.quit, cursor = "hand2")
exit_bt.configure(font = "-family {Poppins} -size 14")
exit_bt.place(x = 200, y = 540)

#creating frame
cover = LabelFrame(root, height=800, width=1000, bd=0)
cover.place(x = 460, y = 100)

mycanvas = Canvas(cover, height=490, width=675, bg="#F2F2F2")
mycanvas.pack(side=LEFT, fill='y', expand='yes')

myframe = Frame(mycanvas)
mycanvas.create_window((0, 0), window=myframe, anchor='nw')

#yscrollbar = ttk.Scrollbar(wrapper1, orient='vertical', command=mycanvas.yview)
#yscrollbar.pack(side=RIGHT, fill='y')

#mycanvas.config(yscrollcommand=yscrollbar.set)

#mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))


#creating labels
title = Label(root, text = "Employee Management", fg = "Black", font=('Helvetica', 20, 'bold'))
title.place(x = 450, y = 40)

menu_label = Label(root, text = "Menu", bg = "#F2F2F2")
menu_label.configure(font = "-family {Poppins} -size 14")
menu_label.place(x = 135, y = 85)

id_label = Label(root, text = "Employee ID", bg = "#F2F2F2")
id_label.configure(font = "-family {Poppins} -size 14")
id_label.place(x = 90, y = 128)

options_label = Label(root, text = "Employee Options", bg = "#F2F2F2")
options_label.configure(font = "-family {Poppins} -size 14")
options_label.place(x = 90, y = 220)

emp_id = Label(myframe, text='Employee ID', bg="#F2F2F2", width=10).grid(row=0, column=0)
emp_name = Label(myframe, text='Employee Name', bg="#F2F2F2", width=24).grid(row=0, column=1)
contact_no = Label(myframe, text='Contact No.', bg="#F2F2F2", width=13).grid(row=0, column=2)
citizen_no = Label(myframe, text='Citizenship No.', bg="#F2F2F2", width=11).grid(row=0, column=3)
designation = Label(myframe, text='Designation', bg="#F2F2F2", width=10).grid(row=0, column=4)
address = Label(myframe, text='Address', bg="#F2F2F2", width=10).grid(row=0, column=5)
password = Label(myframe, text='Password', bg="#F2F2F2", width=10).grid(row=0, column=6)

c.execute("SELECT *,oid FROM addresses")

records = c.fetchall()
# print(records)

# Loop through the results
place = 1
for record in records:
    Label(myframe, text=record[6], bg="#F2F2F2", width=10).grid(row=place, column=0)
    Label(myframe, text=record[0], bg="#F2F2F2", width=24).grid(row=place, column=1)
    Label(myframe, text=record[1], bg="#F2F2F2", width=13).grid(row=place, column=2)
    Label(myframe, text=record[2], bg="#F2F2F2", width=11).grid(row=place, column=3)
    Label(myframe, text=record[3], bg="#F2F2F2", width=10).grid(row=place, column=4)
    Label(myframe, text=record[4], bg="#F2F2F2", width=10).grid(row=place, column=5)
    Label(myframe, text=record[5], bg="#F2F2F2", width=10).grid(row=place, column=6)
    place += 1


#close commit
conn.commit()

#close connection
conn.close()

root.mainloop()
