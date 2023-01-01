from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
import os
import time
db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="phase1")
myCur = db.cursor()

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
	managedoctors_btn["command"] = managedoctors
	manageusers_btn=tk.Button(adminpanel)
	manageusers_btn["bg"] = "#efefef"
	ft = tkFont.Font(family='Times',size=10)
	manageusers_btn["font"] = ft
	manageusers_btn["fg"] = "#000000"
	manageusers_btn["justify"] = "center"
	manageusers_btn["text"] = "Manage users"
	manageusers_btn.place(x=240,y=320,width=110,height=30)
	#manageusers_btn["command"] = self.manageusers_btn_command

def managedoctors():
	global managedoctorsgui
	managedoctorsgui = Toplevel()
	managedoctorsgui.title("Manage Doctors")
	width=400
	height=400
	screenwidth = managedoctorsgui.winfo_screenwidth()
	screenheight = managedoctorsgui.winfo_screenheight()
	alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
	managedoctorsgui.geometry(alignstr)
	managedoctorsgui.resizable(width=False, height=False)

	Doctors_list=tk.Listbox(managedoctorsgui)
	Doctors_list["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	Doctors_list["font"] = ft
	Doctors_list["fg"] = "#333333"
	Doctors_list["justify"] = "center"
	Doctors_list.place(x=220,y=50,width=167,height=253)
	myCur.execute("select * from DOCTOR")
	results = myCur.fetchall()
	for result in results:
		result = list(result)
		name = result[3]
		Doctors_list.insert(END,name)

	doctorname_text=tk.Entry(managedoctorsgui)
	doctorname_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	doctorname_text["font"] = ft
	doctorname_text["fg"] = "#333333"
	doctorname_text["justify"] = "center"
	doctorname_text.place(x=10,y=60,width=143,height=30)
	doctorname_text.insert(0, 'Name')

	doctorposition_text=tk.Entry(managedoctorsgui)
	doctorposition_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	doctorposition_text["font"] = ft
	doctorposition_text["fg"] = "#333333"
	doctorposition_text["justify"] = "center"
	doctorposition_text.place(x=10,y=100,width=143,height=30)
	doctorposition_text.insert(0, 'Position')

	doctorphone_text=tk.Entry(managedoctorsgui)
	doctorphone_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	doctorphone_text["font"] = ft
	doctorphone_text["fg"] = "#333333"
	doctorphone_text["justify"] = "center"
	doctorphone_text.place(x=10,y=140,width=142,height=30)
	doctorphone_text.insert(0, 'Phone number')

	doctorhospitalid_text=tk.Entry(managedoctorsgui)
	doctorhospitalid_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	doctorhospitalid_text["font"] = ft
	doctorhospitalid_text["fg"] = "#333333"
	doctorhospitalid_text["justify"] = "center"
	doctorhospitalid_text.place(x=10,y=180,width=141,height=30)
	doctorhospitalid_text.insert(0, 'Hospital ID')

	doctordepid_text=tk.Entry(managedoctorsgui)
	doctordepid_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	doctordepid_text["font"] = ft
	doctordepid_text["fg"] = "#333333"
	doctordepid_text["justify"] = "center"
	doctordepid_text.place(x=10,y=220,width=141,height=30)
	doctordepid_text.insert(0, 'Department ID')

	doctorage_text=tk.Entry(managedoctorsgui)
	doctorage_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	doctorage_text["font"] = ft
	doctorage_text["fg"] = "#333333"
	doctorage_text["justify"] = "center"
	doctorage_text.place(x=10,y=260,width=141,height=30)
	doctorage_text.insert(0, 'Age')

	doctorgender_text=tk.Entry(managedoctorsgui)
	doctorgender_text["borderwidth"] = "1px"
	ft = tkFont.Font(family='Times',size=10)
	doctorgender_text["font"] = ft
	doctorgender_text["fg"] = "#333333"
	doctorgender_text["justify"] = "center"
	doctorgender_text.place(x=10,y=300,width=141,height=30)
	doctorgender_text.insert(0, 'Gender (0 female 1 male)')

	modifydoctor_btn=tk.Button(managedoctorsgui)
	modifydoctor_btn["bg"] = "#5fb878"
	ft = tkFont.Font(family='Times',size=10)
	modifydoctor_btn["font"] = ft
	modifydoctor_btn["fg"] = "#000000"
	modifydoctor_btn["justify"] = "center"
	modifydoctor_btn["text"] = "Modify doctor"
	modifydoctor_btn.place(x=10,y=340,width=131,height=30)
	#modifydoctor_btn["command"] = self.modifydoctor_btn_command

	addnewdoctor_btn=tk.Button(managedoctorsgui)
	addnewdoctor_btn["bg"] = "#5fb878"
	ft = tkFont.Font(family='Times',size=10)
	addnewdoctor_btn["font"] = ft
	addnewdoctor_btn["fg"] = "#000000"
	addnewdoctor_btn["justify"] = "center"
	addnewdoctor_btn["text"] = "Add new doctor"
	addnewdoctor_btn.place(x=260,y=340,width=131,height=30)

	deletedoctor_btn=tk.Button(managedoctorsgui)
	deletedoctor_btn["bg"] = "#5fb878"
	ft = tkFont.Font(family='Times',size=10)
	deletedoctor_btn["font"] = ft
	deletedoctor_btn["fg"] = "#000000"
	deletedoctor_btn["justify"] = "center"
	deletedoctor_btn["text"] = "Delete doctor"
	deletedoctor_btn.place(x=141,y=340,width=131,height=30)
	
	def onSelectDoctor(evt, *args):
		w = evt.widget
		index = int(w.curselection()[0])
		name = w.get(index).lower()
		sql = "select * from DOCTOR where Name = %s"
		myCur.execute(sql,[(name)])
		results = myCur.fetchall()
		results = list(results[0])
		#[1, 23, 1, 'Ameer', 'Head', '011511', 1, 1]
		doctorgender, doctorage, doctorname, doctorposition, doctorphonenumber, doctordepid, doctorhospitalid = results[1], results[2], results[3], results[4], results[5], results[6], results[7]
		doctorname_text.delete(0, END)
		doctorname_text.insert(0, doctorname)
		doctorposition_text.delete(0, END)
		doctorposition_text.insert(0, doctorposition)
		doctordepid_text.delete(0, END)
		doctordepid_text.insert(0, doctordepid)
		doctorhospitalid_text.delete(0, END)
		doctorhospitalid_text.insert(0, doctorhospitalid)
		doctorphone_text.delete(0, END)
		doctorphone_text.insert(0, doctorphonenumber)
		doctorgender_text.delete(0, END)
		doctorgender_text.insert(0, doctorgender)
		doctorage_text.delete(0, END)
		doctorage_text.insert(0, doctorage)
		#LAZM T3MLHOM F CLASS 3ASHAN KOLO YSAM3 MA3 KOLO

	def addDoctor(*args):
		doctorname = doctorname_text.get()
		doctorposition = doctorposition_text.get()
		doctordepid = doctordepid_text.get()
		doctorhospitalid = doctorhospitalid_text.get()
		doctorphonenumber = doctorphone_text.get()
		doctorgender = doctorgender_text.get()
		doctorage = doctorage_text.get()
		myCur.execute("select * from DOCTOR")
		results = myCur.fetchall()
		doctorid = len(results)+1
		if doctorgender == 0:
			doctorgender = False
		else:
			doctorgender = True
		try:
			sql = "insert into DOCTOR values(true,%s,%s,%s,%s,%s,%s,%s)" if doctorgender else "insert into DOCTOR values(false,%d,%d,%s,%s,%s,%d,%d)"
			t = (int(doctorage), doctorid, doctorname, doctorposition, doctorphonenumber, int(doctorhospitalid), int(doctordepid))
			myCur.execute(sql, t)
			db.commit()
			managedoctorsgui.destroy()
			time.sleep(0.50)
			doctor_added()
		except:
			failed()

	def deleteDoctor(*args):
		name = str(doctorname_text.get())
		try:
			sql = "delete from DOCTOR where Name=%s"
			myCur.execute(sql, [(name)])
			db.commit()
			managedoctorsgui.destroy()
			doctor_deleted()
			time.sleep(0.50)
		except:
			doctor_deleted_error()


	Doctors_list.bind('<<ListboxSelect>>', onSelectDoctor)
	addnewdoctor_btn["command"] = addDoctor
	deletedoctor_btn["command"] = deleteDoctor


def doctor_added():
	global err
	err = Toplevel()
	err.title("Success")
	err.geometry("600x100")
	Label(err,text="Doctor added",fg="green",font="bold").pack()
	Label(err,text="").pack()

def doctor_deleted():
	global err
	err = Toplevel()
	err.title("Success")
	err.geometry("600x100")
	Label(err,text="Doctor deleted",fg="green",font="bold").pack()
	Label(err,text="").pack()

def doctor_deleted_error():
	global err
	err = Toplevel()
	err.title("Error")
	err.geometry("600x100")
	Label(err,text="Doctor cannot be deleted because they have appointments!",fg="green",font="bold").pack()
	Label(err,text="").pack()

def failed():
	global fail
	fail = Toplevel()
	fail.title("Error")
	fail.geometry("200x100")
	Label(fail, text="Operation failed, please make sure you input the right data!", fg="red", font="bold").pack()
	Label(fail, text="").pack()

#def addDoctor():
	#sql = "select * from DOCTOR where Name = %s"