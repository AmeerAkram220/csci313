from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
import os
import time

def view_adminpanel():
	global adminpanel
	adminpanel = Toplevel()
	adminpanel.title("Admin panel")
	width=400
	height=400
	screenwidth = adminpanel.winfo_screenwidth()
	screenheight = adminpanel.winfo_screenheight()
	alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
	adminpanel.geometry(alignstr)
	adminpanel.resizable(width=False, height=False)	
	managedoctors_btn=tk.Button(adminpanel)
	managedoctors_btn["bg"] = "#efefef"
	ft = tkFont.Font(family='Times',size=10)
	managedoctors_btn["font"] = ft
	managedoctors_btn["fg"] = "#000000"
	managedoctors_btn["justify"] = "center"
	managedoctors_btn["text"] = "Manage doctors"
	managedoctors_btn.place(x=30,y=320,width=110,height=30)
	#managedoctors_btn["command"] = self.managedoctors_btn_command	
	manageusers_btn=tk.Button(adminpanel)
	manageusers_btn["bg"] = "#efefef"
	ft = tkFont.Font(family='Times',size=10)
	manageusers_btn["font"] = ft
	manageusers_btn["fg"] = "#000000"
	manageusers_btn["justify"] = "center"
	manageusers_btn["text"] = "Manage users"
	manageusers_btn.place(x=240,y=320,width=110,height=30)
	#manageusers_btn["command"] = self.manageusers_btn_command