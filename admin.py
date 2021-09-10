from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox

splash=Tk()
splash.title("Merchandise")
splash.geometry("1193x671")
splash.overrideredirect(True)
bg = PhotoImage(file ="C:/Users/ACER/Desktop/Untitledd.png")
splash_label = Label(splash, image= bg)
splash_label.pack()


def main_window():

    global fg
    global entry1
    global entry2

    splash.destroy()
    root = Tk()
    root.title("merchandise")
    root.geometry("1193x671")

    fg = PhotoImage(file="C:/Users/ACER/Desktop/login.png")
    main_label = Label(root,image=fg)
    main_label.pack()

    entry1 = Entry(root, width=46, border=0 ,bg="#30355A")
    #e1.config(font=l)
    entry1.place(x=520,y=280, height=35)


    entry2 = Entry(root, width=46, border=0 ,show='*',bg="#30355A")
    #e2.config(font=l)
    entry2.place(x=520,y=355, height=35)


    Frame(root, width=278, height=2, bg='#141414').place(x=520, y=393)
    Frame(root, width=278, height=2, bg='#141414').place(x=520, y=320)

    button_log = Button(root, text="login", width= 28,border=0, bg="#051C36", command=hi)
    button_log.place(x=540, y=511, height=49)



splash.after(1000, main_window)


def hi():
    global entry1
    global entry2
    global root
    uname= entry1.get()
    password=entry2.get()
    if (uname == "" and password == ""):
        messagebox.showinfo("", "Blank Not allowed")


    elif (uname == "Admin" and password == "123"):

        messagebox.showinfo("", "Login Success")
        root.destroy()

    else:
        messagebox.showinfo("", "Incorrect Username and Password")

splash.mainloop()

