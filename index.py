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

        findusername_query = "SELECT * FROM user WHERE USERNAME = ?"
        db_cursor.execute(findusername_query, [self.username.get()])
        if db_cursor.fetchall():
            # checking if the username already exists in the table
            msg.showerror("Error", "Username already taken!!")
        else:
            msg.showinfo("Complete!", "Account Created!!")
            self.login()

        # adding the new username to the database
        addnewuser_query = "INSERT INTO USER(USERNAME, PASSWORD) VALUES(?,?)"
        db_cursor.execute(addnewuser_query, [self.username.get(), self.password.get()])
        db.commit()
        db.close()

    def available_routes(self):
        # create function to show avilable routes
        return


class travel:
    def __init__(self, main):
        self.main = main
        # variables


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x300")
    root.title("Cab Booking System Login")

    application = user(root)
    root.mainloop()
