from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
import os
import time

def view_userpanel():
	global userpanel
	userpanel = Toplevel()
	userpanel.title("User panel")
	width=400
	height=400
	screenwidth = userpanel.winfo_screenwidth()
	screenheight = userpanel.winfo_screenheight()
	alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
	userpanel.geometry(alignstr)
	userpanel.resizable(width=False, height=False)

	viewdoctors_btn=tk.Button(userpanel)
	viewdoctors_btn["bg"] = "#efefef"
	ft = tkFont.Font(family='Times',size=10)
	viewdoctors_btn["font"] = ft
	viewdoctors_btn["fg"] = "#000000"
	viewdoctors_btn["justify"] = "center"
	viewdoctors_btn["text"] = "View doctors"
	viewdoctors_btn.place(x=30,y=320,width=110,height=30)
	#viewdoctors_btn["command"] = self.viewdoctors_btn_command

	modifyprofile_btn=tk.Button(userpanel)
	modifyprofile_btn["bg"] = "#efefef"
	ft = tkFont.Font(family='Times',size=10)
	modifyprofile_btn["font"] = ft
	modifyprofile_btn["fg"] = "#000000"
	modifyprofile_btn["justify"] = "center"
	modifyprofile_btn["text"] = "Modify profile"
	modifyprofile_btn.place(x=240,y=320,width=110,height=30)
	#modifyprofile_btn["command"] = self.modifyprofile_btn_command

	bookappointment_btn=tk.Button(userpanel)
	bookappointment_btn["bg"] = "#efefef"
	ft = tkFont.Font(family='Times',size=10)
	bookappointment_btn["font"] = ft
	bookappointment_btn["fg"] = "#000000"
	bookappointment_btn["justify"] = "center"
	bookappointment_btn["text"] = "Book appointment"
	bookappointment_btn.place(x=30,y=70,width=110,height=30)
	#bookappointment_btn["command"] = self.bookappointment_btn_command

	viewappointments_btn=tk.Button(userpanel)
	viewappointments_btn["bg"] = "#efefef"
	ft = tkFont.Font(family='Times',size=10)
	viewappointments_btn["font"] = ft
	viewappointments_btn["fg"] = "#000000"
	viewappointments_btn["justify"] = "center"
	viewappointments_btn["text"] = "View appointments"
	viewappointments_btn.place(x=240,y=70,width=110,height=30)
	#viewappointments_btn["command"] = self.viewappointments_btn_command