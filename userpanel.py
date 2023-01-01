from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
import os
import time
db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="phase1")
myCur = db.cursor()

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
	modifyprofile_btn["command"] = modifyprofile

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

def modifyprofile():
	global modifyprofilegui
	modifyprofilegui = Toplevel()
	modifyprofilegui.title("Modify Profile")
	width=400
	height=400
	screenwidth = modifyprofilegui.winfo_screenwidth()
	screenheight = modifyprofilegui.winfo_screenheight()
	alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
	modifyprofilegui.geometry(alignstr)
	modifyprofilegui.resizable(width=False, height=False)

	name_text=tk.Entry(modifyprofilegui)
	name_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	name_text["font"] = ft
	name_text["fg"] = "#333333"
	name_text["justify"] = "center"
	name_text["text"] = "Name"
	name_text.place(x=160,y=60,width=143,height=30)

	age_text=tk.Entry(modifyprofilegui)
	age_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	age_text["font"] = ft
	age_text["fg"] = "#333333"
	age_text["justify"] = "center"
	age_text["text"] = "Age"
	age_text.place(x=160,y=100,width=143,height=30)

	phonenumber_text=tk.Entry(modifyprofilegui)
	phonenumber_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	phonenumber_text["font"] = ft
	phonenumber_text["fg"] = "#333333"
	phonenumber_text["justify"] = "center"
	phonenumber_text["text"] = "Phone number"
	phonenumber_text.place(x=160,y=180,width=142,height=30)

	address_text=tk.Entry(modifyprofilegui)
	address_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	address_text["font"] = ft
	address_text["fg"] = "#333333"
	address_text["justify"] = "center"
	address_text["text"] = "Address"
	address_text.place(x=160,y=140,width=141,height=30)

	modifyprofile_btn=tk.Button(modifyprofilegui)
	modifyprofile_btn["bg"] = "#5fb878"
	ft = tkFont.Font(family='Times',size=10)
	modifyprofile_btn["font"] = ft
	modifyprofile_btn["fg"] = "#000000"
	modifyprofile_btn["justify"] = "center"
	modifyprofile_btn["text"] = "Modify profile"
	modifyprofile_btn.place(x=230,y=280,width=143,height=30)

	emptylabel=tk.Label(modifyprofilegui)
	ft = tkFont.Font(family='Times',size=10)
	emptylabel["font"] = ft
	emptylabel["fg"] = "#ff0b0b"
	emptylabel["justify"] = "center"
	emptylabel["text"] = ""
	emptylabel.place(x=0,y=10,width=399,height=30)

	labelname=tk.Label(modifyprofilegui)
	ft = tkFont.Font(family='Times',size=10)
	labelname["font"] = ft
	labelname["fg"] = "#333333"
	labelname["justify"] = "center"
	labelname["text"] = "Name"
	labelname.place(x=50,y=60,width=70,height=25)

	lableage=tk.Label(modifyprofilegui)
	ft = tkFont.Font(family='Times',size=10)
	lableage["font"] = ft
	lableage["fg"] = "#333333"
	lableage["justify"] = "center"
	lableage["text"] = "Age"
	lableage.place(x=50,y=100,width=70,height=25)

	lablephonenumber=tk.Label(modifyprofilegui)
	ft = tkFont.Font(family='Times',size=10)
	lablephonenumber["font"] = ft
	lablephonenumber["fg"] = "#333333"
	lablephonenumber["justify"] = "center"
	lablephonenumber["text"] = "Phone Number"
	lablephonenumber.place(x=50,y=180,width=97,height=30)

	labeladdress=tk.Label(modifyprofilegui)
	ft = tkFont.Font(family='Times',size=10)
	labeladdress["font"] = ft
	labeladdress["fg"] = "#333333"
	labeladdress["justify"] = "center"
	labeladdress["text"] = "Address"
	labeladdress.place(x=60,y=140,width=70,height=25)

	with open('w.text', 'r') as reader:
		username = reader.readline()
	sql = "select id from USERS where user = %s"
	myCur.execute(sql,[(username)])
	results = myCur.fetchall()
	userid = list(results[0])[0]

	sql = "select * from PATIENT where patient_id = %s"
	myCur.execute(sql,[(userid)])
	results = myCur.fetchall()
	results = list(results[0])
	for result in results:
		if result == "":
			emptylabel["text"] = "Please update your profile!"
			break
	#[1, 'ameer', 20, 1, '6 october', '011551123']
	name, age, address, phone = results[1], results[2], results[4], results[5]
	phonenumber_text.delete(0, END)
	address_text.delete(0, END)
	age_text.delete(0, END)
	name_text.delete(0, END)
	name_text.insert(0, name)
	age_text.insert(0, age)
	address_text.insert(0, address)
	phonenumber_text.insert(0, phone)

	def updateprofile(*args):
		name, age, address, phone = name_text.get(), age_text.get(), address_text.get(), phonenumber_text.get()
		try:
			sql = "update PATIENT SET patient_name=%s,patient_age=%s,patient_address=%s,patient_phone=%s where patient_id = %s"
			myCur.execute(sql,(name, int(age), address, phone, int(userid)))
			db.commit()
			time.sleep(0.50)
			success()
			modifyprofilegui.destroy()
		except:
			failed()
	modifyprofile_btn["command"] = updateprofile

def failed():
	global fail
	fail = Toplevel()
	fail.title("Error")
	fail.geometry("200x100")
	Label(fail, text="Operation failed, please make sure you input the right data!", fg="red", font="bold").pack()
	Label(fail, text="").pack()

def success():
	global err
	err = Toplevel()
	err.title("Success")
	err.geometry("600x100")
	Label(err,text="Profile modified",fg="green",font="bold").pack()
	Label(err,text="").pack()