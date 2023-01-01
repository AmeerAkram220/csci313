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