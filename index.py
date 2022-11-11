from tkinter import *
from tkinter.ttk import *
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
        self.username = StringVar()
        self.password = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        # widgets
        self.widgets()

    def login(self):
        db = mysql.connector.connect(host="localhost", user="root", password="1234")
        db_cursor = db.cursor()

        query = "SELECT * FROM user WHERE USERNAME = ? AND PASSWORD = ?"
        db_cursor.execute(query, [self.username.get(), self.password.get()])
        result = db_cursor.fetchone()

        if result:
            msg.showinfo("Welcome", "Login Successful Welcome to Cab Booking System")
            # login successful and go to the next window to book the cab
            application = travel(root)
        else:
            # login unsuccessful
            msg.showerror("Error", "Login Unsuccessful")

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
        # create a new window
        newroot = Tk()
        newroot.title("Routes")
        newroot.geometry("550x300")
        # list all the available routes
        newroot.config(bg="black")
        Label(
            newroot,
            text="LPU Main Gate <--> Block 27 (Computing Block)",
            font=("Lato", 15),
            pady=2,
            fg="red",
            bg="black",
        ).pack()
        Label(
            newroot,
            text="LPU Main Gate <--> Unipolis",
            font=("Lato", 15),
            pady=2,
            fg="red",
            bg="black",
        ).pack()
        Label(
            newroot,
            text="LPU Main Gate <--> Unihospital",
            font=("Lato", 15),
            pady=2,
            fg="red",
            bg="black",
        ).pack()
        Label(
            newroot,
            text="LPU Main Gate <--> Block 34",
            font=("Lato", 15),
            pady=2,
            fg="red",
            bg="black",
        ).pack()
        Label(
            newroot,
            text="LPU Main Gate <--> BH1",
            font=("Lato", 15),
            pady=2,
            fg="red",
            bg="black",
        ).pack()
        Label(
            newroot,
            text="LPU Main Gate <--> BH1",
            font=("Lato", 15),
            pady=2,
            fg="red",
            bg="black",
        ).pack()
        Label(
            newroot,
            text="LPU Main Gate <--> BH3",
            font=("Lato", 15),
            pady=2,
            fg="red",
            bg="black",
        ).pack()
        Label(
            newroot,
            text="LPU Main Gate <--> BH6",
            font=("Lato", 15),
            pady=2,
            fg="red",
            bg="black",
        ).pack()
        # button to close the window and go back to the main page
        Button(
            newroot,
            text="Close",
            command=newroot.destroy,
            font=("Lato", 15),
            fg="red",
            bg="black",
        ).pack()
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
