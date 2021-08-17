from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

root = Tk()

root.geometry("1191x670")

# Create a databases or connect to one
conn = sqlite3.connect("employee.db")

#create a cursor
c = conn.cursor()
'''
# Create table
c.execute(""" CREATE TABLE addresses(
      emp_id integer,
      emp_name text,
      contact_no integer,
      address text,
      citizen_no integer,
      password text,
      designation text
) """)'''
'''
# Create submit button for databases
def submit():
    # Create a databases or connect to one
    conn = sqlite3.connect('employee.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:emp_id, :emp_name, :contact_no, :address, :citizen_no, :password, :designation)",{
        'emp_id':emp_id.get(),
        'emp_name':emp_name.get(),
        'contact_no':contact_no.get(),
        'address':address.get(),
        'citizen_no': citizen_no.get(),
        'password':password.get(),
        "designation" : designation.get()
    })
    # showinfo messagebox
    messagebox.showinfo("Addresses", "Inserted Successfully")

    conn.commit()

    conn.close()

    # clear the text boxes
    emp_id.delete(0,END)
    emp_name.delete(0,END)
    contact_no.delete(0,END)
    address.delete(0, END)
    citizen_no.delete(0, END)
    password.delete(0, END)
    designation.delete(0, END)

# Create a databases or connect to one
conn = sqlite3.connect('employee.db')

# Create cursor
c = conn.cursor()

# query of the database
c.execute("SELECT *, oid FROM addresses")

records = c.fetchall()
# print(records)

# Loop through the results
print_record=''
for record in records:
        #str(record[6]) added for displaying the id
    print_record += str(record[0]) + '\t' + str(record[1]) + ' \t'+ str(record[2]) + '\t ' + str(record[3]) + '\t' + str(record[4] + '\t' + str(record[5}) + "\n"

query_label = Label(root, text=print_record)
query_label.grid(row=1, column= 5000, rowspan = 5)'''

def add_emp():
    global bg
    top = Toplevel()  # using top to call instead of Tk()
    top.title("Add Employee")
    top.geometry("1191x670")

    # Define image as background
    bg = ImageTk.PhotoImage(file="add_emp.png")
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

    # clearing everything from the add's textbox
    def add_clear():
        namebox.delete(0, END)
        contactbox.delete(0, END)
        citizenbox.delete(0, END)
        designationbox.delete(0, END)
        addressbox.delete(0, END)
        passwordbox.delete(0, END)

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
            messagebox.showinfo("Warning!", "Fill up Everything")

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
                    activebackground="#007884", borderwidth=0, cursor = "hand2", command = empty_add)
    add_bt.configure(font="-family {Poppins} -size 14")
    add_bt.place(x=490, y=522)

    clear_bt = Button(top, text="Clear", bg="#007884", fg="White", activeforeground = "White",
                      activebackground="#007884", borderwidth=0, cursor = "hand2", command = add_clear)
    clear_bt.configure(font="-family {Poppins} -size 14")
    clear_bt.place(x=655, y=522)


'''
def delete():
    # create database
    conn = sqlite3.connect('employee.db')

    #create cursor
    c = conn.cursor()

    #delete a record
    c.execute("DELETE from addresses WHERE oid = " + searchbox.get())
    print('Deleted Successfully')

    # query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    # print(records)

    # Loop through the results
    print_record = ''
    for record in records:
        # str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()

    conn.close()

#Creating an update function
def update():
    # Create a databases or connect to one
    conn = sqlite3.connect('add_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = searchbox.get()

    c.execute(""" UPDATE addresses SET
         first_name = :first,
         last_name = :last,
         address = :address,
         city = :city,
         state = :state,
         zipcode = :zipcode
         WHERE oid = :oid""",
         {'first': f_name_editor.get(),
          'last': l_name_editor.get(),
          'address': address_editor.get(),
          'city': city_editor.get(),
          'state': state_editor.get(),
          'zipcode': zipcode_editor.get(),
          'oid': record_id

               }
    )
    conn.commit()
    conn.close()
    #Destroying all the data and closing window
    editor.destroy()'''

def update_emp():
    global bgg
    top = Toplevel()  # using top to call instead of Tk()
    top.title("Update Employee")
    top.geometry("1191x670")

    # Define image as background
    bgg = ImageTk.PhotoImage(file="update_emp.png")
    bg_label = Label(top, image=bgg)
    bg_label.place(x=0, y=0)

    # creating labels
    title = Label(top, text="Update Employee", fg="Black", bg = "White", font=('Helvetica', 20, 'bold'))
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

    # creating entryboxes
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

    # clearing everything from the update's textbox
    def update_clear():
        namebox.delete(0, END)
        contactbox.delete(0, END)
        citizenbox.delete(0, END)
        designationbox.delete(0, END)
        addressbox.delete(0, END)
        passwordbox.delete(0, END)

    # creating buttons
    update_bt = Button(top, text="Update", bg="#007884", fg="White", activeforeground = "White",
                       activebackground="#007884", borderwidth=0, pady=0,cursor = "hand2")
    update_bt.configure(font="-family {Poppins} -size 14")
    update_bt.place(x=480, y=523)

    clear_bt = Button(top, text="Clear", bg="#007884", fg="White", activeforeground = "White",
                      activebackground="#007884", borderwidth=0, cursor = "hand2", command= update_clear)
    clear_bt.configure(font="-family {Poppins} -size 14")
    clear_bt.place(x=655, y=522)


#Define image as background
bg1 =ImageTk.PhotoImage(file = "Employee_mgt.png")
bg_label = Label(root, image = bg1)
bg_label.place(x = 0, y = 0)

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

emp_id = Label(root, text = "Employee ID", bg = "#F2F2F2")
emp_id.configure(font = "-family {Poppins} -size 10")
emp_id.place(x = 460, y = 100)

emp_name = Label(root, text = "Employee Name", bg = "#F2F2F2")
emp_name.configure(font = "-family {Poppins} -size 10")
emp_name.place(x = 545, y = 100)

contact_no = Label(root, text = "Contact No.", bg = "#F2F2F2")
contact_no.configure(font = "-family {Poppins} -size 10")
contact_no.place(x = 700 ,y = 100)

contact_no = Label(root, text = "Address", bg = "#F2F2F2")
contact_no.configure(font = "-family {Poppins} -size 10")
contact_no.place(x = 800 ,y = 100)

citizen_no = Label(root, text = "Citizenship No.", bg = "#F2F2F2")
citizen_no.configure(font = "-family {Poppins} -size 10")
citizen_no.place(x = 885, y = 100)

password = Label(root, text = "Password", bg = "#F2F2F2")
password.configure(font = "-family {Poppins} -size 10")
password.place(x = 990, y = 100)

designation = Label(root, text = "Designation", bg = "#F2F2F2")
designation.configure(font = "-family {Poppins} -size 10")
designation.place(x = 1060, y = 100)


#creating buttons
logout_bt = Button(root, text = "Log Out", fg = "White", activeforeground = "White",
                   bg = "#007884",
                   activebackground="#007884",
                   borderwidth = 0, cursor = "hand2")
logout_bt.configure(font = "-family {Poppins} -size 14")
logout_bt.place(x = 1046, y = 607)

#popping up messsage if the entry widget is empty
def emp_search():
    if len(searchbox.get()) == 0:
        messagebox.showinfo("Warning!", "Its empty! Write something")

search_bt = Button(root, text = "Search", bg = "#007884", activebackground = "#007884",
                   fg = "White", activeforeground = "White",
                   borderwidth = 0, cursor = "hand2",
                   command = emp_search)
search_bt.configure(font = "-family {Poppins} -size 14")
search_bt.place(x = 315, y = 138)

add_bt = Button(root, text = "Add Employee", bg = "#007884", activebackground = "#007884",
                fg = "White", activeforeground = "White",borderwidth = 0, cursor = "hand2",
                command = add_emp)
add_bt.configure(font = "-family {Poppins} -size 14")
add_bt.place(x = 156, y = 280)

update_bt = Button(root, text = "Update Employee", bg = "#007884", activebackground = "#007884",
                   fg = "White", activeforeground = "White", borderwidth = 0, cursor = "hand2",
                   command = update_emp)
update_bt.configure(font = "-family {Poppins} -size 14")
update_bt.place(x = 140, y = 360)

delete_bt = Button(root, text = "Delete Employee", bg = "#007884", activebackground = "#007884",
                   fg = "White", activeforeground = "White", borderwidth = 0, cursor = "hand2")
delete_bt.configure(font = "-family {Poppins} -size 14")
delete_bt.place(x = 140, y = 440)

exit_bt = Button(root, text = "Exit", bg = "#007884", activebackground = "#007884",
                 fg = "White", activeforeground = "White", borderwidth = 0, command = root.quit, cursor = "hand2")
exit_bt.configure(font = "-family {Poppins} -size 14")
exit_bt.place(x = 200, y = 540)

#creating entry box
entry_font = ('Poppins', 12)
searchbox = Entry(root, borderwidth = 0, bg = "#f2f2f2", font = entry_font)
searchbox.place(x = 105, y = 160)

root.mainloop()
