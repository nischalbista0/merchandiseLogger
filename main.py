from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import ttk
import sqlite3

root = Tk()
root.geometry('1193x671')
root.title('Just checking')
root.resizable(False, False)

fontt = Font(
    family='Poppins',
    size=10,
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


def inven_update():
    global imgg
    inven = Toplevel()
    inven.geometry('1193x671')
    inven.resizable(False, False)

    def clear_all():
        ls = [en1, en2, en3, en4, en5, en6, en7]

        for i in ls:
            i.delete(0, END)

    def upd_product():
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
            'oid' : ddata

        })

        inven.destroy()

        c.execute("SELECT *,oid FROM second")

        records = c.fetchall()
        # print(records)

        for record in records:
            roww = record[10]
            Label(myframe, text=record[10], bg='white', width=10).grid(row=roww, column=0)
            Label(myframe, text=record[0], bg='white', width=30).grid(row=roww, column=1)
            Label(myframe, text=record[1], bg='white', width=13).grid(row=roww, column=2)
            Label(myframe, text=record[2], bg='white', width=10).grid(row=roww, column=3)
            Label(myframe, text=record[3], bg='white', width=10).grid(row=roww, column=4)
            Label(myframe, text=record[8], bg='white', width=10).grid(row=roww, column=5)
            Label(myframe, text=record[9], bg='white', width=10).grid(row=roww, column=6)


        conn.commit()

        conn.close()

    conn = sqlite3.connect('database.db')

    c = conn.cursor()

    imgg = ImageTk.PhotoImage(Image.open('C:/Users/dell/Desktop/illustrato/Update_Product.png'))
    lablo = Label(inven, image=imgg).place(x=0, y=0)
    btn1 = Button(inven, text='Update', bg='#007884', height=1, width=10, activebackground='#007884',
                  command=upd_product, font=fontt, bd=0).place(x=478, y=534)

    btn2 = Button(inven, text='Clear', bg='#007884', height=1, width=10, activebackground='#007884', font=fontt, bd=0,
                  command=clear_all).place(x=602, y=534)

    lab1 = Label(inven, text='Product Name', bd=0, bg='white', font=fontt).place(x=145, y=188)
    lab2 = Label(inven, text='Category', bd=0, bg='white', font=fontt).place(x=145, y=265)
    lab3 = Label(inven, text='Quantity', bd=0, bg='white', font=fontt).place(x=145, y=336)
    lab4 = Label(inven, text='Selling Price(MRP)', bd=0, bg='white', font=fontt).place(x=145, y=400)
    lab5 = Label(inven, text='Sub Category', bd=0, bg='white', font=fontt).place(x=620, y=265)
    lab6 = Label(inven, text='Cost Price', bd=0, bg='white', font=fontt).place(x=620, y=336)
    lab7 = Label(inven, text='Vendor Phone No.', bd=0, bg='white', font=fontt).place(x=620, y=400)

    # Entries for update product

    en1 = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en1.place(x=145, y=217)
    en2 = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en2.place(x=145, y=292)
    en3 = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en3.place(x=145, y=363)
    en4 = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en4.place(x=145, y=426)
    en5 = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en5.place(x=620, y=292)
    en6 = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en6.place(x=620, y=363)
    en7 = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en7.place(x=620, y=426)
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

        for record in records:
            roww = record[10]
            Label(myframe, text=record[10], bg='white', width=10).grid(row=roww, column=0)
            Label(myframe, text=record[0], bg='white', width=30).grid(row=roww, column=1)
            Label(myframe, text=record[1], bg='white', width=13).grid(row=roww, column=2)
            Label(myframe, text=record[2], bg='white', width=10).grid(row=roww, column=3)
            Label(myframe, text=record[3], bg='white', width=10).grid(row=roww, column=4)
            Label(myframe, text=record[8], bg='white', width=10).grid(row=roww, column=5)
            Label(myframe, text=record[9], bg='white', width=10).grid(row=roww, column=6)

        conn.commit()

        conn.close()
        inven.destroy()

    imge = ImageTk.PhotoImage(Image.open('C:/Users/dell/Desktop/illustrato/Add_Product.png'))
    labloo = Label(inven, image=imge).place(x=0, y=0)
    btn1a = Button(inven, text='Add', bg='#007884', height=1, width=10, activebackground='#007884',
                   command=add_product, font=fontt, bd=0).place(x=478, y=534)

    btn2a = Button(inven, text='Clear', bg='#007884', height=1, width=10, activebackground='#007884', font=fontt,
                   bd=0, command=clear_all).place(x=602, y=534)

    lab1a = Label(inven, text='Product Name', bd=0, bg='white', font=fontt).place(x=145, y=188)
    lab2a = Label(inven, text='Category', bd=0, bg='white', font=fontt).place(x=145, y=265)
    lab3a = Label(inven, text='Quantity', bd=0, bg='white', font=fontt).place(x=145, y=336)
    lab4a = Label(inven, text='Selling Price(MRP)', bd=0, bg='white', font=fontt).place(x=145, y=400)
    lab5a = Label(inven, text='Sub Category', bd=0, bg='white', font=fontt).place(x=620, y=265)
    lab6a = Label(inven, text='Cost Price', bd=0, bg='white', font=fontt).place(x=620, y=336)
    lab7a = Label(inven, text='Vendor Phone No.', bd=0, bg='white', font=fontt).place(x=620, y=400)

    # Entries for update product

    en1a = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en1a.place(x=145, y=217)
    en2a = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en2a.place(x=145, y=292)
    en3a = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en3a.place(x=145, y=363)
    en4a = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en4a.place(x=145, y=426)
    en5a = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en5a.place(x=620, y=292)
    en6a = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en6a.place(x=620, y=363)
    en7a = Entry(inven, bd=0, bg='white', fg='black', font=fontt)
    en7a.place(x=620, y=426)


img = ImageTk.PhotoImage(Image.open('C:/Users/dell/Desktop/illustrato/Inventory.png'))
lable = Label(root, image=img).place(x=0, y=0)

lab1 = Label(root, text='Menu', bg='white', font=fontt)
lab1.place(x=70, y=155)

Ent1 = Entry(root, bd=0, bg='white', fg='black', font=fontt)
Ent1.place(x=70, y=210)

btn1 = Button(root, text='Logout', height=1, width=7, bg='#007884', activebackground='#007884', font=fontt, bd=0,
              fg='white').place(x=65, y=96)

btn2 = Button(root, text='Search', height=1, width=9, bg='#007884', activebackground='#007884', font=fontt, bd=0).place(
    x=262, y=215)

btn3 = Button(root, text='Add Product', height=1, width=26, bg='#007884', activebackground='#007884', font=fontt, bd=0,
              command=inven_add).place(x=76, y=316)

btn4 = Button(root, text='Update Product', height=1, width=26, bg='#007884', activebackground='#007884',
              command=inven_update, font=fontt, bd=0).place(x=76, y=392)

btn5 = Button(root, text='Delete Product', height=1, width=26, bg='#007884', activebackground='#007884', font=fontt,
              bd=0).place(x=76, y=469)

btn6 = Button(root, text='Exit', height=1, width=7, bg='#007884', activebackground='#007884', font=fontt, bd=0).place(
    x=148, y=560)

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


for record in records:
    roww = record[10]
    Label(myframe, text=record[10], bg='white', width=10).grid(row=roww, column=0)
    Label(myframe, text=record[0], bg='white', width=30).grid(row=roww, column=1)
    Label(myframe, text=record[1], bg='white', width=13).grid(row=roww, column=2)
    Label(myframe, text=record[2], bg='white', width=10).grid(row=roww, column=3)
    Label(myframe, text=record[3], bg='white', width=10).grid(row=roww, column=4)
    Label(myframe, text=record[8], bg='white', width=10).grid(row=roww, column=5)
    Label(myframe, text=record[9], bg='white', width=10).grid(row=roww, column=6)

conn.commit()

conn.close()

root.mainloop()