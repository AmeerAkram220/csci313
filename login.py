from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
from adminpanel import *
from userpanel import *

db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="phase1")
myCur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("600x100")
    Label(err,text="All fields are required or username already registered.",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()
    myCur.execute("select * from USERS")
    results = myCur.fetchall()
    userid = len(results)+1
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
    	if check_duplicates(username_info):
    		error()
    	else:
        	sql = "insert into USERS values(%s,%s,%s, false)"
        	t = (userid, username_info, password_info)
        	myCur.execute(sql, t)
        	db.commit()
        	Label(root1, text="").pack()
        	time.sleep(0.50)
        	success()



def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration")
    root1.geometry("600x500")
    global username
    global password
    Label(root1,text="Register your account",bg="grey",fg="black",font="bold",width=300).pack()
    username = StringVar()
    password = StringVar()
    Label(root1,text="").pack()
    Label(root1,text="Username :",font="bold").pack()
    Entry(root1,textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Password :").pack()
    Entry(root1, textvariable=password,show="*").pack()
    Label(root1, text="").pack()
    Button(root1,text="Register",bg="green",command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Hospital reservation system")
    root2.geometry("600x600")
    global username_verify
    global password_verify
    Label(root2, text="Hospital reservation system", bg="grey", fg="black", font="bold",width=300).pack()
    username_verify = StringVar()
    password_verify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font="bold").pack()
    Entry(root2, textvariable=username_verify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_verify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="green",command=login_verify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged():
	view_userpanel()
	with open('w.text', 'w') as write:
		write.write(username_verify.get())
	root2.destroy()
    # global logg
    # logg = Toplevel(root)
    # root2.destroy()
    # logg.title("Welcome")
    # logg.geometry("200x100")
    # Label(logg, text="Welcome {} ".format(username_verify.get()), fg="green", font="bold").pack()
    # Label(logg, text="").pack()
    # Button(logg, text="Log out", bg="green", width=8, height=1, command=logg_destroy).pack()

def logged_admin():
	view_adminpanel()
	root2.destroy()
    # global logg
    # logg = Toplevel(root2)
    # logg.title("Admin Panel")
    # logg.geometry("200x100")
    # Label(logg, text="Welcome {} ".format(username_verify.get()), fg="green", font="bold").pack()
    # Label(logg, text="").pack()
    # Button(logg, text="Log out", bg="green", width=8, height=1, command=logg_destroy).pack()


def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="green", width=8, height=1, command=fail_destroy).pack()

def check_duplicates(username_info):
    sql = "select * from USERS where user = %s"
    myCur.execute(sql,[(username_info)])
    results = myCur.fetchall()
    if results:
        for i in results:
            return True
    else:
        return False


def login_verify():
    user_verify = username_verify.get()
    pas_verify = password_verify.get()
    sql = "select * from USERS where user = %s and password = %s"
    myCur.execute(sql,[(user_verify),(pas_verify)])
    results = myCur.fetchall()
    if results:
    	for i in results:
    		if isadmin():
    			logged_admin()
    			break
    		else:
    			logged()
    			break
    else:
    	failed()

def isadmin():
	user_verify = username_verify.get()
	sql = "select * from USERS where user = %s"
	myCur.execute(sql, [(user_verify)])
	results = myCur.fetchall()
	results = list(results[0]) if results else None
	if results[3] == 0:
		return False
	else:
		return True


def main_screen():
    global root
    root = Tk()
    root.title("Hospital reservation system")
    root.geometry("600x600")
    Label(root,text="Welcome, Please login or register",font="bold",bg="grey",fg="black",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Login",width="8",height="3",bg="green",font="bold",command=login).place(x=250, y=220)
    Button(root, text="Register",height="3",width="15",bg="green",font="bold",command=registration).place(x=215, y=320)

main_screen()
root.mainloop()
