from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
import mysql.connector
import os
import time
db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="phase1")
myCur = db.cursor()
#To make things easier
def failed(text):
	global fail
	fail = Toplevel()
	fail.title("Error")
	fail.geometry("600x100")
	Label(fail, text=text, fg="red", font="bold").pack()
	Label(fail, text="").pack()

def success(text):
	global succ
	succ = Toplevel()
	succ.title("Success")
	succ.geometry("600x100")
	Label(succ,text=text, fg="green",font="bold").pack()
	Label(succ,text="").pack()

def get_doctorid(name):
	sql = "select Doctor_ID from DOCTOR where Name = %s"
	myCur.execute(sql,[(name)])
	results = myCur.fetchall()
	doctorid = list(results[0])[0]
	return doctorid

def get_doctoravailabletimes(name, date):
	id = get_doctorid(name)
	alltimes = [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
	sql = "select app_time from APPOINTMENT where app_dr_id = %s and app_date = %s"
	myCur.execute(sql,(id, date))
	results = myCur.fetchall()
	results = [ele[0] for ele in results] #Converting from tuples to list
	for result in results:
		alltimes.remove(result)
	return alltimes

def get_username():
	with open('w.text', 'r') as reader:
		username = reader.readline()
	return username

def get_userid(name):
	sql = "select id from USERS where user = %s"
	myCur.execute(sql,[(name)])
	results = myCur.fetchall()
	userid = list(results[0])[0]
	return userid