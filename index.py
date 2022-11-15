from tkinter import *
from tkinter import messagebox as msg
import mysql.connector


# connecting the database
db = mysql.connector.connect(host="localhost", user="root", password="1234", database="CABMS")
db_cursor = db.cursor()
newtablequery = "CREATE TABLE IF NOT EXISTS USER (UID INT PRIMARY KEY NOT NULL AUTO_INCREMENT, USERNAME VARCHAR(20) NOT NULL, PASSWORD VARCHAR(10) NOT NULL)"
db_cursor.execute(newtablequery)
db.commit()  # saving the changes
db.close()  # closing the connection


class user:
    # creating the variables
    def __init__(self, main):
        # window
        self.main = main
        # variables
        # self.username = StringVar()
        # self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        # widgets
        self.widgets()


    def login(self):
        newroot = Tk()
        newroot.geometry("400x340")
        newroot.config(bg="black")
        newroot.title("Login")
        # on clicking the login button
        # --------------------------------------------
        # def clicklogin():
        #     username=StringVar()
        #     password=StringVar()
        #     db = mysql.connector.connect(host="localhost", user="root", password="1234")
        #     db_cursor = db.cursor()

        #     query = "SELECT * FROM user WHERE USERNAME = ? AND PASSWORD = ?"
        #     print(usernameentry.get())
        #     print(passwordentry.get())
        #     db_cursor.execute(query, [usernameentry.get(), passwordentry.get()])
        #     result = db_cursor.fetchall()

        #     if result is not None:
        #         msg.showinfo("Welcome", "Login Successful Welcome to Cab Booking System")
        #         # login successful and go to the next window to book the cab
        #         application = travel(root)
        #     else:
        #         # login unsuccessful
        #         msg.showerror("Error", "Login Unsuccessful")
        # --------------------------------------------

        def clicklogin():
            #init
            username = StringVar()
            passwrd = StringVar()
            #getting
            username = usernameentry.get()
            passwrd = passwordentry.get()

            if username=="" or passwrd=="":
                msg.showerror("Error", "Enter username and password")

            # connecting to the database
            else: 
                db = mysql.connector.connect(host="localhost", user="root", password="1234", database="CABMS")
                db_cursor = db.cursor()
                db_cursor.execute("SELECT * FROM USER WHERE USERNAME = %s AND PASSWORD = %s", (username, passwrd))
                result = db_cursor.fetchone()
                
                if result == None:
                    msg.showerror("Error", "Invalid username or password")
                else: 
                    msg.showinfo("Success", "Login complete!")
                    newroot.destroy()
                    application = travel(root)
                    # root shouldnt be destroyed else cant pass to travel class 

        # go back to main 
        def gobacktomain():
            newroot.destroy()      
            return  
        # to clear text on clicking 
        def cleartextonclick1(e): # for username
            usernameentry.delete(0, "end")
        
        def cleartextonclick2(e): # for password   
            passwordentry.delete(0,"end")

        # login page heading 
        Label(
            newroot,
            text="LOGIN",
            font=("Lato", 15), 
            pady=2,
            fg="light blue", 
            bg="black",
            width=32
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # username label and entry space
        Label(
            newroot,
            text="Username: ", 
            font=("Lato", 12),
            pady=2,
            fg="light blue",
            bg="black"
        ).grid(row=1, column=0, pady=37)
        usernameentry = Entry(newroot, width=30, font=("Lato", 13), background="light blue")
        usernameentry.insert(0, "enter your username...")
        usernameentry.bind("<FocusIn>", cleartextonclick1) # to delete the existing text when the username entry space is clicked
        usernameentry.grid(row=1,column=1, pady=37)

        # password space
        Label(
            newroot,
            text="Password: ",
            font=("Lato", 12),
            pady=2,
            fg="light blue",
            bg="black"
        ).grid(row=2, column=0,pady=10)
        passwordentry = Entry(newroot, width=30, font=("Lato", 13),background="light blue")
        passwordentry.insert(0, "Enter your password...")
        passwordentry.bind("<FocusIn>", cleartextonclick2) #to delete the existing text when the password entry space is clicked
        passwordentry.grid(row=2, column=1, pady=10)

        # login button 
        Button(
            newroot,
            text="Login", 
            font=("Lato", 13),
            padx=5, 
            pady=2,
            fg="light blue", 
            bg="black",
            command=clicklogin
        ).grid(row=3, column=0, columnspan=2, pady=20)

        Button(
            newroot, 
            text="Back", 
            font=("Lato", 10),
            padx=5,
            pady=2,
            fg="light blue", 
            bg="black", 
            command=gobacktomain
        ).grid(row=4, column=1, pady=10, sticky="e")

        newroot.mainloop()


    def new_user(self):
        # db = mysql.connector.connect(host="localhost", user="root", password="1234")
        # db_cursor = db.cursor()

        # # check if the username entered by the user already exists in the database in that case show and error
        # findusername_query = "SELECT * FROM user WHERE USERNAME = ?"
        # askusername = self.username.get()
        # db_cursor.execute(findusername_query, [askusername])
        # if db_cursor.fetchall():
        #     # checking if the username already exists in the table
        #     msg.showerror("Error", "Username already taken!!")

        # # if the username doesnt already exist show that the account has been created and go to the login page
        # else:
        #     # adding the new user to the database
        #     addnewuser_query = "INSERT INTO USER(USERNAME, PASSWORD) VALUES(?,?)"
        #     db_cursor.execute(addnewuser_query, [askusername, self.password.get()])
        #     db.commit()
        #     db.close()
        #     # user added
        #     msg.showinfo("Complete!", "Account Created!!")
        #     # go to login
        #     user(root)

        def clicksubmit():
            #init
            newusername = StringVar()
            newpwd = StringVar()
            # getting
            newusername = usernameentry.get()
            newpwd = passwordentry.get()

            if newusername=="" or newpwd=="":
                msg.showerror("Error", "Enter username and password")
            else:
                db = mysql.connector.connect(host="localhost", user="root", password="1234", database="CABMS")
                db_cursor = db.cursor()
                db_cursor.execute("INSERT INTO USER(USERNAME, PASSWORD) VALUES(%s, %s)", (newusername, newpwd))
                db.commit()
                msg.showinfo("Success", "Successfully Registered! You can now login")
                newroot.destroy()
            return       


        newroot = Tk()
        newroot.title("Register User")
        # root.forget()
        newroot.config(bg="black")

        def clearonclick1(e): #to clear existing text in username section
            usernameentry.delete(0, "end")
        def clearonclick2(e): #to clear existing text in password section
            passwordentry.delete(0, "end")
        def clearonclick3(e): #to clear existing text in mobile number section
            mobileentry.delete(0,"end")
        def clearonclick4(e): #to clear existing text in email section
            emailentry.delete(0,"end")

        # new user heading 
        Label(
            newroot,
            text="Welcome to Cab Booking System",
            font=("Lato 18 underline"),
            pady=2,  
            fg="light blue", 
            bg="black", 
            width=35,
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # username
        Label(
            newroot, 
            text="Username: ", 
            font = ("Lato", 15), 
            pady=2, 
            fg="light blue", 
            bg="black"
        ).grid(row=1, column=0, pady=10, sticky="w", padx=2)
        usernameentry = Entry(newroot, width=30, font=("Lato", 15), background="light blue")
        usernameentry.insert(0, "Enter your username...")
        usernameentry.bind("<FocusIn>", clearonclick1)
        usernameentry.grid(row=1, column=1, pady=10, padx=2)

        # password 
        Label(
            newroot, 
            text="Password: ",
            font=("Lato", 15), 
            pady=2, 
            fg="light blue", 
            bg="black",
        ).grid(row=2, column=0, pady=10, padx=2, sticky="w")
        passwordentry = Entry(newroot, width=30, font=("Lato", 15), background="light blue")
        passwordentry.insert(0, "Enter your password...")
        passwordentry.bind("<FocusIn>", clearonclick2)
        passwordentry.grid(row=2, column=1, pady=10, padx=2)

        # gender drop down 
        # Label(
        #     newroot,
        #     text="Gender: ",
        #     font=("Lato", 15),
        #     pady=2,
        #     fg="light blue", 
        #     bg="black", 
        #     activeforeground="light blue",
        #     activebackground="black", 
        # ).grid(row=3, column=0, sticky="w", padx=2)
        # gender=StringVar()
        # gender.set("--Select--")
        # genderdrop = OptionMenu(newroot, gender, "Male", "Female", "Other")
        # genderdrop.config(fg="light blue", bg="black", font=("Lato", 13))
        # genderdrop.grid(row=3, column=1, pady=10, sticky="w", padx=5)

        # mobile number 
        Label(
            newroot, 
            text="Mobile: ", 
            font=("Lato", 15), 
            pady=2, 
            fg="light blue", 
            bg="black"
        ).grid(row=4, column=0, pady=10, padx=2, sticky="w")
        mobileentry=Entry(newroot, width=30, font=("Lato", 15), background="light blue")
        mobileentry.insert(0, "Enter your mobile number...")
        mobileentry.bind("<FocusIn>", clearonclick3)
        mobileentry.grid(row=4, column=1,pady=10, padx=2)

        # email id 
        Label(
            newroot, 
            text="Email ID: ",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black", 
        ).grid(row=5, column=0, pady=10, padx=2, sticky="w")
        emailentry=Entry(newroot,width=30, font=("Lato", 15), background="light blue")
        emailentry.insert(0,"Enter your Email ID...")
        emailentry.bind("<FocusIn>", clearonclick4)
        emailentry.grid(row=5, column=1, pady=10, padx=2)

        # Register button 
        Button(
            newroot,
            text="Submit",
            font=("Lato", 16),
            pady=2, 
            fg="light blue", 
            bg="black", 
            command=clicksubmit
        ).grid(row=6, column=0, columnspan=2, pady=10)

        newroot.mainloop()


    def available_routes(self):
        # root.forget()
        # create a new window
        newroot = Tk()
        newroot.title("Routes")
        newroot.geometry("520x500")
        # list all the available routes
        newroot.config(bg="black")
        Label(
            newroot,
            text="AVAILABLE ROUTES",
            font=("Lato 18 underline"), 
            pady=2, 
            fg="light blue",
            bg="black"
        ).grid(row=0, column=0,pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> Block 27 (Computing Block)",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).grid(row=1, column=0,pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> Unipolis",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).grid(row=2, column=0,pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> Unihospital",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).grid(row=3, column=0,pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> Admission Block",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).grid(row=4, column=0,pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> BH1",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).grid(row=5, column=0,pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> BH3",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).grid(row=6, column=0,pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> BH6",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).grid(row=7, column=0,pady=10)
        # button to close the window and go back to the main page
        Button(
            newroot,
            text="Close",
            command=newroot.destroy,
            font=("Lato", 15),
            fg="light blue",
            bg="black",
            activeforeground="light blue",
            activebackground="black"
        ).grid(row=8, column=0,pady=10)
        newroot.mainloop()
        return

    def widgets(self):
        # heading
        self.optionsframe = Frame(self.main, padx=5)
        self.head = Label(
            self.optionsframe,
            text="Welcome to Cab Booking System",
            font=("Lato", 20),
            bg="light blue",
        )
        self.head.grid(row= 0, column=0, pady=10)

        # login button option
        option1login = Button(
            self.optionsframe,
            text="Login",
            command=self.login,
            font=("Lato", 15),
            bg="light blue",
            fg="black",
            activebackground="light blue",
        )
        option1login.grid(row=1, column = 0, padx=10, pady=10)

        # register new user option
        option2newuser = Button(
            self.optionsframe,
            text="New User",
            command=self.new_user,
            font=("Lato", 15),
            bg="light blue",
            fg="black",
            activebackground="light blue",
        )
        option2newuser.grid(row=2, column = 0, padx=10, pady=10)

        # show all available routes option
        option3routes = Button(
            self.optionsframe,
            text="View Routes",
            command=self.available_routes,
            font=("Lato", 15),
            bg="light blue",
            fg="black",
            activebackground="light blue",
        )
        option3routes.grid(row= 3, column = 0, padx=10, pady=10)
        self.optionsframe.config(bg="black")
        self.optionsframe.grid(row=0, column=0)


class travel:
    def __init__(self, main):
        self.main = main
        self.bookingfunction()

    def bookingfunction(e):
        newroot = Tk()
        newroot.geometry("580x400")
        newroot.title("Booking")
        newroot.config(bg="black")

        # init
        mobilevalue = StringVar()
        Fromvalue = StringVar()
        Tovalue = StringVar()
        Farevalue = StringVar()
        dayvalue = StringVar()
        timevalue = StringVar()
        paymentmodevalue = StringVar()

        # clear on click for mobile number 
        def clearonclick(e):
            mobileentry.delete(0,"end")
        # heading
        Label(
            newroot,
            text="Booking Details",
            font="Lato 15 underline",
            pady=10,
            width=45,
            fg="light blue", 
            bg="black",
        ).grid(row=0, column=2, columnspan=3)

        # mobile entry
        Label(
            newroot,
            text="Mobile No.",
            padx=80,
            pady=5,
            font =("Lato", 15),
            fg="light blue", 
            bg="black",
        ).grid(row=1, column=2)
        mobileentry = Entry(newroot, textvariable=mobilevalue,bg="light blue", fg="black", font=("Lato", 15))
        mobileentry.insert(0, "Enter your mobile number...")
        mobileentry.bind("<FocusIn>", clearonclick)
        mobileentry.grid(row=1, column=3)

        # From entry
        Label(
            newroot, 
            text="FROM", 
            padx=80, 
            pady=5,
            font =("Lato", 15),
            fg="light blue", 
            bg="black",
        ).grid(row=2, column=2)
        clicked = StringVar()
        clicked.set("Pickup")
        drop = OptionMenu(
            newroot,
            clicked,
            "Main Gate ",
            "Computing Block",
            "BH-1",
            "BH-3",
            "BH-6",
            "Admission Block",
            "Unihospital",
            "UniMall",
        )
        drop.config(font=("Lato", 15), fg="light blue", bg="black")
        drop.grid(row=2, column=3, sticky=E)
        

        # To entry 
        Label(
            newroot, 
            text="TO", 
            pady=5,
            font =("Lato", 15),
            fg="light blue", 
            bg="black",
        ).grid(row=3, column=2)
        clicked2 = StringVar()
        clicked2.set("Drop")
        drop1 = OptionMenu(
            newroot,
            clicked2,
            "Main Gate ",
            "Computing Block",
            "BH-1",
            "BH-3",
            "BH-6",
            "Admission Block",
            "Unihospital",
            "UniMall",
        )
        drop1.config(font=("Lato", 15), fg="light blue", bg="black", activebackground="black", activeforeground="light blue")
        drop1.grid(row=3, column=3, sticky=E)

        # Fare entry 
        Label(
            newroot,
            text="Fare", 
            pady=5,
            font =("Lato", 15),
            fg="light blue", 
            bg="black",
        ).grid(row=4, column=2)
        Fareentry = Entry(newroot, textvariable=Farevalue, state=DISABLED, fg="light blue", bg="black", font=("Lato", 15), background="light blue", foreground="black")
        Fareentry.grid(row=4, column=3)

        # calculating fare
        def calcfare():
            fromdisplay = Entry(newroot, font=("Lato", 15), bg="light blue", fg="black", width=17)
            fromdisplay.insert(0, clicked.get())
            fromdisplay.grid(row=2, column=3,padx=2, sticky=W)

            todisplay = Entry(newroot, font=("Lato", 15), bg="light blue", fg="black", width=17)
            todisplay.insert(0, clicked2.get())
            todisplay.grid(row=3, column=3, padx=2, sticky=W)

            modedisplay = Entry(newroot, font=("Lato", 15), bg="light blue", fg="black",width=17)
            modedisplay.insert(0, clicked3.get())
            modedisplay.grid(row=7, column=3, padx=2, sticky=W)

            startplace = clicked.get()
            reachplace = clicked2.get()


            if (startplace == "Pickup" or reachplace == "Drop"):
                Fareentry.config(state=NORMAL)
                Fareentry.delete(0,"end")
                Fareentry.insert(0,"0")
            elif(startplace == reachplace):
                Fareentry.config(state=NORMAL)
                Fareentry.delete(0,"end")
                Fareentry.insert(0,"0")
            elif(reachplace == "Unihospital"):
                Fareentry.config(state=NORMAL)
                Fareentry.delete(0,"end")
                Fareentry.insert(0,"0")
            elif(reachplace == "Main Gate"):
                Fareentry.config(state=NORMAL)
                Fareentry.delete(0,"end")
                Fareentry.insert(0,"30")
            elif(reachplace == "Computing Block" or reachplace == "Admission Block"):
                Fareentry.config(state=NORMAL)
                Fareentry.delete(0,"end")
                Fareentry.insert(0,"20")
            elif(reachplace == "BH-1" or reachplace == "BH-3" or reachplace == "BH-6"):
                Fareentry.config(state=NORMAL)
                Fareentry.delete(0,"end")
                Fareentry.insert(0,"10")
            elif(reachplace == "UniMall"):
                Fareentry.config(state=NORMAL)
                Fareentry.delete(0,"end")
                Fareentry.insert(0,"40")
        # calc fare button 
        calcbutton = Button(newroot,text="Calc Fare", font=("Lato", 15), bg="light blue", fg="black", command=calcfare)
        calcbutton.grid(row=8, column=2, pady=8, padx=16, sticky=E)


        # Day entry 
        Label(
            newroot,
            text="Day", 
            pady=5,
            font =("Lato", 15),
            fg="light blue", 
            bg="black",
        ).grid(row=5, column=2)
        dayentry = Entry(newroot, textvariable=dayvalue, bg="light blue", fg="black", font=("Lato", 15))
        dayentry.grid(row=5, column=3)


        # Time entry 
        Label(
            newroot, 
            text="Time", 
            pady=5,
            font =("Lato", 15),
            fg="light blue", 
            bg="black",
        ).grid(row=6, column=2)
        timeentry = Entry(newroot, textvariable=timevalue, font=("Lato", 15), fg="black", bg="light blue")
        timeentry.grid(row=6, column=3)


        # payment 
        Label(
            newroot, 
            text="Payment Mode", 
            pady=5,
            font =("Lato", 15),
            fg="light blue", 
            bg="black",
        ).grid(row=7, column=2)
        clicked3 = StringVar()
        clicked3.set("choose payment option")
        drop2 = OptionMenu(
            newroot, 
            clicked3, 
            "Cash", 
            "Onine payment"
        )
        drop2.config(font=("Lato", 15), fg="light blue", bg="black", activebackground="black", activeforeground="light blue")
        drop2.grid(row=7, column=3,sticky=E)


        # book button
        def confirm():
            msg.showinfo(title="Booking status", message="Booking successful.")

        bookbutton = Button(newroot, command=confirm, text="Confirm Booking", font=("Lato", 15), fg="black", bg="light blue")
        bookbutton.grid(row=8, column=3,pady=8, sticky=W)

        # cancel button 
        def cancel():
            status = msg.askyesno(
                title="Question", message="Do you want to cancel the booking?"
            )
            if status == True:
                newroot.destroy()

        cancelbutton = Button(newroot, command=cancel, text="Cancel", font=("Lato", 15), fg="black", bg="light blue")
        cancelbutton.grid(row=8, column=3, pady=8, sticky=E)

        newroot.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.geometry("410x300")
    root.title("Cab Booking System Login")
    root.config(bg="black")

    application = user(root)
    root.mainloop()
