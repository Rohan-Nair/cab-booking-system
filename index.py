from tkinter import *
from tkinter import messagebox as msg
import mysql.connector


# connecting the database
db = mysql.connector.connect(host="localhost", user="root", password="1234")
db_cursor = db.cursor()
newtablequery = "CREATE TABLE IF NOT EXISTS USER (USERNAME VARCHAR(20) NOT NULL, PASSWORD VARCHAR(10) NOT NULL)"
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
        root.forget()
        newroot = Tk()
        newroot.geometry("700x550")
        newroot.config(bg="black")
        # on clicking the login button
        def clicklogin():
            db = mysql.connector.connect(host="localhost", user="root", password="1234")
            db_cursor = db.cursor()

            query = "SELECT * FROM user WHERE USERNAME = ? AND PASSWORD = ?"
            username = usernameentry.get(),
            password = passwordentry.get()
            db_cursor.execute(query, [username, password])
            result = db_cursor.fetchone()

            if result:
                msg.showinfo("Welcome", "Login Successful Welcome to Cab Booking System")
                # login successful and go to the next window to book the cab
                application = travel(root)
            else:
                # login unsuccessful
                msg.showerror("Error", "Login Unsuccessful")
        
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

        newroot.mainloop()


    def new_user(self):
        db = mysql.connector.connect(host="localhost", user="root", password="1234")
        db_cursor = db.cursor()

        # check if the username entered by the user already exists in the database in that case show and error
        findusername_query = "SELECT * FROM user WHERE USERNAME = ?"
        askusername = self.username.get()
        db_cursor.execute(findusername_query, [askusername])
        if db_cursor.fetchall():
            # checking if the username already exists in the table
            msg.showerror("Error", "Username already taken!!")

        # if the username doesnt already exist show that the account has been created and go to the login page
        else:
            # adding the new user to the database
            addnewuser_query = "INSERT INTO USER(USERNAME, PASSWORD) VALUES(?,?)"
            db_cursor.execute(addnewuser_query, [askusername, self.password.get()])
            db.commit()
            db.close()
            # user added
            msg.showinfo("Complete!", "Account Created!!")
            # go to login
            self.login()

    def available_routes(self):
        root.forget()
        # create a new window
        newroot = Tk()
        newroot.title("Routes")
        newroot.geometry("520x560")
        # list all the available routes
        newroot.config(bg="black")
        Label(
            newroot,
            text="AVAILABLE ROUTES",
            font=("Lato 18 underline"), 
            pady=2, 
            fg="light blue",
            bg="black"
        ).pack(pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> Block 27 (Computing Block)",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).pack(pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> Unipolis",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).pack(pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> Unihospital",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).pack(pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> Block 34",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).pack(pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> BH1",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).pack(pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> BH1",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).pack(pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> BH3",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).pack(pady=10)
        Label(
            newroot,
            text="LPU Main Gate <--> BH6",
            font=("Lato", 15),
            pady=2,
            fg="light blue",
            bg="black",
        ).pack(pady=10)
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
        ).pack(pady=10)
        newroot.mainloop()
        return

    def widgets(self):
        # heading
        self.head = Label(
            self.main,
            text="Welcome to Cab Booking System",
            font=("Lato", 20),
            bg="light blue",
        )
        self.head.pack(pady=10)

        # login button option
        self.optionsframe = Frame(self.main)
        option1login = Button(
            self.optionsframe,
            text="Login",
            command=self.login,
            font=("Lato", 15),
            bg="light blue",
            fg="black",
            activebackground="light blue",
        )
        option1login.pack(padx=10, pady=10)

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
        option2newuser.pack(padx=10, pady=10)

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
        option3routes.pack(padx=10, pady=10)
        self.optionsframe.config(bg="black")
        self.optionsframe.pack()


class travel:
    def __init__(self, main):
        self.main = main
        # variables


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x300")
    root.title("Cab Booking System Login")
    root.config(bg="black")

    application = user(root)
    root.mainloop()
