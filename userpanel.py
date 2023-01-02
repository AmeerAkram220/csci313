from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
import os
import time
from helper import *

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
	bookappointment_btn["command"] = bookappointment

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

	username = get_username()
	sql = "select id from USERS where user = %s"
	myCur.execute(sql,[(username)])
	results = myCur.fetchall()
	userid = list(results[0])[0]

	sql = "select * from PATIENT where patient_id = %s"
	myCur.execute(sql,[(userid)])
	results = myCur.fetchall()
	results = list(results[0]) if len(results) > 0 else None
	if not results:
		emptylabel["text"] = "Please update your profile!"
		sql = "insert into PATIENT values(%s,%s,NULL, NULL, NULL, NULL)"
		t = (get_userid(get_username()), get_username())
		myCur.execute(sql, t)
		db.commit()
	else:
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
		for result in results:
			if result == "":
				emptylabel["text"] = "Please update your profile!"
				break

	def updateprofile(*args):
		name, age, address, phone = name_text.get(), age_text.get(), address_text.get(), phonenumber_text.get()
		try:
			sql = "update PATIENT SET patient_name=%s,patient_age=%s,patient_address=%s,patient_phone=%s where patient_id = %s"
			myCur.execute(sql,(name, int(age), address, phone, int(userid)))
			db.commit()
			time.sleep(0.50)
			success('Profile updated!')
			modifyprofilegui.destroy()
		except:
			failed('Operation failed, please make sure you input the right data!')
	modifyprofile_btn["command"] = updateprofile

def bookappointment():
	global choosedoctorgui
	choosedoctorgui = Toplevel()
	choosedoctorgui.title("Choose doctor")
	width=400
	height=400
	screenwidth = choosedoctorgui.winfo_screenwidth()
	screenheight = choosedoctorgui.winfo_screenheight()
	alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
	choosedoctorgui.geometry(alignstr)
	choosedoctorgui.resizable(width=False, height=False)

	doctornamelabel=tk.Label(choosedoctorgui)
	ft = tkFont.Font(family='Times',size=0)
	doctornamelabel["font"] = ft
	doctornamelabel["fg"] = "#ff0b0b"
	doctornamelabel["justify"] = "center"
	doctornamelabel["text"] = ""
	doctornamelabel.place(x=0,y=0,width=0,height=0)

	doctorslist=tk.Listbox(choosedoctorgui)
	doctorslist["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	doctorslist["font"] = ft
	doctorslist["fg"] = "#333333"
	doctorslist["justify"] = "center"
	doctorslist.place(x=20,y=10,width=178,height=371)

	myCur.execute("select * from DOCTOR")
	results = myCur.fetchall()
	for result in results:
		result = list(result)
		name = result[3]
		doctorslist.insert(END,name)

	date_text=tk.Entry(choosedoctorgui)
	date_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	date_text["font"] = ft
	date_text["fg"] = "#333333"
	date_text["justify"] = "center"
	date_text["text"] = "Entry"
	date_text.place(x=220,y=300,width=160,height=30)

	enterdate_label=tk.Label(choosedoctorgui)
	ft = tkFont.Font(family='Times',size=10)
	enterdate_label["font"] = ft
	enterdate_label["fg"] = "#333333"
	enterdate_label["justify"] = "center"
	enterdate_label["text"] = "Enter date (YYYY-MM-DD)"
	enterdate_label.place(x=200,y=270,width=204,height=30)

	choosedoctor_btn=tk.Button(choosedoctorgui)
	choosedoctor_btn["bg"] = "#5fb878"
	ft = tkFont.Font(family='Times',size=10)
	choosedoctor_btn["font"] = ft
	choosedoctor_btn["fg"] = "#000000"
	choosedoctor_btn["justify"] = "center"
	choosedoctor_btn["text"] = "Choose doctor"
	choosedoctor_btn.place(x=270,y=350,width=123,height=30)

	def onSelectDoctor(evt, *args):
		try:
			w = evt.widget
			index = int(w.curselection()[0])
			name = w.get(index).lower()
		except:
			return
		doctornamelabel["text"] = name

	def choosetime(*args):
		global choosetimegui
		choosetimegui = Toplevel()
		choosetimegui.title("Choose time")
		width=400
		height=400
		screenwidth = choosetimegui.winfo_screenwidth()
		screenheight = choosetimegui.winfo_screenheight()
		alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		choosetimegui.geometry(alignstr)
		choosetimegui.resizable(width=False, height=False)

		timenamelabel=tk.Label(choosetimegui)
		ft = tkFont.Font(family='Times',size=0)
		timenamelabel["font"] = ft
		timenamelabel["fg"] = "#ff0b0b"
		timenamelabel["justify"] = "center"
		timenamelabel["text"] = ""
		timenamelabel.place(x=0,y=0,width=0,height=0)

		timeslist=tk.Listbox(choosetimegui)
		timeslist["borderwidth"] = "1px"
		ft = tkFont.Font(family='Times',size=10)
		timeslist["font"] = ft
		timeslist["fg"] = "#333333"
		timeslist["justify"] = "center"
		timeslist.place(x=20,y=10,width=178,height=371)

		choosetime_btn=tk.Button(choosetimegui)
		choosetime_btn["bg"] = "#5fb878"
		ft = tkFont.Font(family='Times',size=10)
		choosetime_btn["font"] = ft
		choosetime_btn["fg"] = "#000000"
		choosetime_btn["justify"] = "center"
		choosetime_btn["text"] = "Choose time"
		choosetime_btn.place(x=270,y=350,width=123,height=30)

		doctorname = doctornamelabel["text"]
		available_times = get_doctoravailabletimes(doctorname, date_text.get())
		for time in available_times:
			timeslist.insert(END,time)

		def onSelectTime(evt, *args):
			w = evt.widget
			index = int(w.curselection()[0])
			time = w.get(index)
			timenamelabel["text"] = time
		timeslist.bind('<<ListboxSelect>>', onSelectTime)

		def makeappointment(*args):
			myCur.execute("select * from APPOINTMENT")
			results = myCur.fetchall()
			appointmentid = len(results)+1
			notes = 'aaa i forgot for now'
			sql = "insert into APPOINTMENT values(%s,%s,%s,%s,%s,%s)" #LAST %S IS NOTES BS ANA MAYT RN HA3MLHA BOKRA
			t = (appointmentid, get_doctorid(doctorname), date_text.get(), get_userid(get_username()), timenamelabel['text'], notes)
			myCur.execute(sql, t)
			db.commit()
			choosetimegui.destroy()
			success('Appointment booked with doctor ' + doctorname.capitalize())
		choosetime_btn["command"] = makeappointment

	doctorslist.bind('<<ListboxSelect>>', onSelectDoctor)
	choosedoctor_btn["command"] = choosetime
