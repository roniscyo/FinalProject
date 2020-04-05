'''
                     ///                               /////////////////////////////

                    /////        ///// /////          /////        /////
                    /////        /////   /////        /////        /////
                    /////        /////    /////       /////        /////
                    /////        /////      /////     /////        /////
                    /////        /////       /////    /////        /////
                    /////        /////         /////  /////        /////
                    /////        /////           /////             /////

'''


from tkinter import *
from tkinter import messagebox


def signup():
    # ====================signup window====================
    sign = Toplevel()
    sign.geometry("650x370+300+180")
    sign.title("Sign Up")
    sign.configure(bg="#cccccc")
    sign.resizable(0, 0)

    # ====================signup window title====================
    lt = Label(sign, text="Sign Up", bg="#cccccc", font=("Bold", 26))
    lt.place(x=250, y=20)

    # ====================first name label====================
    label_first_name = Label(sign, text="First name", bg="#cccccc", font=("Bold", 16))
    label_first_name.place(x=10, y=100)
    global first_name
    first_name = StringVar()
    first_name = Entry(sign, width=30, textvariable=first_name)
    first_name.place(x=120, y=107)

    # ====================last name label====================
    label_last_name = Label(sign, text="Last name", bg="#cccccc", font=("Bold", 16))
    label_last_name.place(x=340, y=100)
    global last_name
    last_name = StringVar()
    last_name = Entry(sign, width=30, textvariable=last_name)
    last_name.place(x=450, y=107)

    # ====================mail label====================
    label_mail = Label(sign, text="E-mail", bg="#cccccc", font=("Bold", 16))
    label_mail.place(x=10, y=140)
    global mail
    mail = StringVar()
    mail = Entry(sign, width=30, textvariable=mail)
    mail.place(x=120, y=147)

    # ====================phone label====================
    label_phone = Label(sign, text="Phone no.", bg="#cccccc", font=("Bold", 16))
    label_phone.place(x=340, y=140)
    global phone
    phone = StringVar()
    phone = Entry(sign, width=30, textvariable=phone)
    phone.place(x=450, y=147)

    # ====================user name label====================
    label_user_name = Label(sign, text="User name", bg="#cccccc", font=("Bold", 16))
    label_user_name.place(x=10, y=177)
    global user_name
    user_name = StringVar()
    user_name = Entry(sign, width=30, textvariable=user_name)
    user_name.place(x=120, y=184)

    # ====================password label====================
    label_password = Label(sign, text="Password", bg="#cccccc", font=("Bold", 16))
    label_password.place(x=340, y=177)
    global password
    password = StringVar()
    password = Entry(sign, show="*", width=30, textvariable=password)
    password.place(x=450, y=184)

    # ====================birthday label====================
    label_birthday = Label(sign, text="Birthday", bg="#cccccc", font=("Bold", 16))
    label_birthday.place(x=10, y=224)

    list_months = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    global months
    months = StringVar()
    droplist_months = OptionMenu(sign, months, *list_months)
    droplist_months.config(width=8)
    months.set("Month")
    droplist_months.place(x=120, y=223)

    if months == "February":
        list_days = [i for i in range(1, 29)]
    else:
        list_days = [i for i in range(1, 32)]

    global days
    days = StringVar()
    droplist_days = OptionMenu(sign, days, *list_days)
    droplist_days.config(width=2)
    days.set("Day")
    droplist_days.place(x=212, y=223)

    list_years = [i for i in range(1900, 2020)]
    global years
    years = StringVar()
    droplist_years = OptionMenu(sign, years, *list_years)
    droplist_years.config(width=2)
    years.set("Year")
    droplist_years.place(x=270, y=223)

    # ====================gender label====================
    label_gender = Label(sign, text="Gender", bg="#cccccc", font=("Bold", 16))
    label_gender.place(x=340, y=224)
    global gender
    gender = IntVar()
    Radiobutton(sign, text="Male", bg="#cccccc", variable=gender, value=0).place(x=450, y=228)
    Radiobutton(sign, text="Female", bg="#cccccc", variable=gender, value=1).place(x=510, y=228)
    Radiobutton(sign, text="Custom", bg="#cccccc", variable=gender, value=2).place(x=570, y=228)

    # ====================signup button====================
    sign_up_button = Button(sign, text="Click to Sign up", command=register,
                            bg="#3399ff", fg="#ffffff", width=20, font=("Bold", 12))
    sign_up_button.place(x=220, y=300)


def login():
    # ====================login window====================
    log = Toplevel()
    log.geometry("650x350+300+180")
    log.title("Login")
    log.configure(bg="#cccccc")
    log.resizable(0, 0)

    # ====================login menu====================
    menu = Menu(log)
    log.config(menu=menu)
    file_menu = Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=log.quit)

    # ====================login window title====================
    lt = Label(log, text="Login", bg="#cccccc", font=("Bold", 48))
    lt.place(x=240, y=20)

    # ====================verify username====================
    label_user = Label(log, text="User name", bg="#cccccc", font=("Bold", 16))
    label_user.place(x=30, y=130)
    global verify_user
    verify_user = Entry(log, width=40)
    verify_user.place(x=200, y=140)

    # ====================verify password====================
    label_psswprd = Label(log, text="Password", bg="#cccccc", font=("Bold", 16))
    label_psswprd.place(x=30, y=180)
    global verify_psswprd
    verify_psswprd = Entry(log, show="*", width=40)
    verify_psswprd.place(x=200, y=190)

    button_log = Button(log, text="Click to Login",
                        bg="#3399ff", fg="#ffffff",
                        command=verify, width=20, font=("Bold", 12))

    button_log.place(x=230, y=280)


def verify():
    # ====================verify user/password====================
    user_v = verify_user.get()
    passw_v = verify_psswprd.get()
    verify_user.delete(0, END)
    verify_psswprd.delete(0, END)
    if user_v == "" or passw_v == "":
        messagebox.showinfo("Error", "All fields are required !")
    else:
        file = open("members.csv", "r")
        if file.mode == 'r':
            list_of_files = file.read()
            if user_v in list_of_files:
                if passw_v in list_of_files:
                    messagebox.showinfo("Message","login success")
                else:
                    messagebox.showinfo("Message", "password not correct")
            else:
                messagebox.showinfo("Message", "user not correct")


def register():
    # ====================registertion file====================
    first = first_name.get()
    last = last_name.get()
    email = mail.get()
    tel = phone.get()
    user = user_name.get()
    passw = password.get()
    month = months.get()
    day = days.get()
    year = years.get()
    sex = gender.get()
    # ====================check details====================
    if first == "" or last == "" or email == "" or tel == "" or user == "" or passw == ""\
            or month == "Month" or day == "Day" or year == "Year":
        messagebox.showerror("Signup Error", "Please field the details")
    elif len(passw) <= 7:
        messagebox.showerror("Password", "Your password must be at least 8 charecter")
    else:
        with open("members.csv", "a") as file:
            file.write(f'{first},{last},{email},{tel},{user},{passw},{month},{day},{year},{sex}\n')
        file.close()

        first_name.delete(0, END)
        last_name.delete(0, END)
        mail.delete(0, END)
        phone.delete(0, END)
        user_name.delete(0, END)
        password.delete(0, END)


def about():
    messagebox.showinfo("about", "My last Project")


root = Tk()

# ====================welcome window====================
root.geometry("650x350+300+180")
root.title("Welcome")
root.configure(bg="#cccccc")
root.resizable(0, 0)

# ====================main menu====================
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_cascade(label="About", command=about)

# ====================welcome window title====================
lm = Label(root, text="Welcome", bg="#cccccc", font=("Bold", 48))
lm.place(x=190, y=20)

button_login = Button(root, text="Login", bg="#3399ff", fg="#ffffff", width=20, command=login, font=("Bold", 12))
button_login.place(x=230, y=150)

label_or = Label(root, text="_______________or_______________", bg="#cccccc", font=("Bold", 12))
label_or.place(x=180, y=210)

button_signup = Button(root, text="Sign Up", bg="#3399ff", fg="#ffffff", width=20, command=signup, font=("Bold", 12))
button_signup.place(x=230, y=280)


root.mainloop()
