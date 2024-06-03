#Task 4
from tkinter import *
import random

root = Tk()

root.geometry("600x300")

root.title("Rock Paper Scissor Game")

computer_value = {
	"0": "Rock",
	"1": "Paper",
	"2": "Scissor"
}

def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	label1.config(text="Player			 ")
	label3.config(text="Computer")
	label4.config(text="")

def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

def isrock():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Rock":
		match_result = "Tie or Draw"
	elif c_v == "Scissor":
		match_result = "Player Win"
	else:
		match_result = "Computer Win"
	label4.config(text=match_result)
	label1.config(text="Rock		 ")
	label3.config(text=c_v)
	button_disable()

def ispaper():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Paper":
		match_result = "Tie or Draw"
	elif c_v == "Scissor":
		match_result = "Computer Win"
	else:
		match_result = "Player Win"
	label4.config(text=match_result)
	label1.config(text="Paper		 ")
	label3.config(text=c_v)
	button_disable()

def isscissor():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Rock":
		match_result = "Computer Win"
	elif c_v == "Scissor":
		match_result = "Tie or Draw"
	else:
		match_result = "Player Win"
	label4.config(text=match_result)
	label1.config(text="Scissor")
	label3.config(text=c_v)
	button_disable()

Label(root,
	text="Rock Paper Scissor",
	font="normal 20 bold",
	fg="Red").pack(pady=20)

frame = Frame(root)
frame.pack()

label1 = Label(frame,
		text="Player Input:	       ",
		font=10)

label2 = Label(frame,
		text="			 ",
		font="normal 10 bold")

label3 = Label(frame, text="Computer selection:", font=10)

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack()

label4 = Label(root,
		text="",
		font="normal 20 bold",
		bg="white",
		width=15,
		borderwidth=2,
		relief="solid")
label4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock",
			font=10, width=7,
			command=isrock)

b2 = Button(frame1, text="Paper ",
			font=10, width=7,
			command=ispaper)

b3 = Button(frame1, text="Scissor",
			font=10, width=7,
			command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Reset Game",
	font=10, fg="red",
	bg="white", command=reset_game).pack(pady=20)

root.mainloop()
