import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


font = ("Arial",12,"italic")
# ------------------------------------------------------------------------------------------------------------- #

def generate():
	
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
	           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
	
	input_password.delete(0, len(input_password.get()))
	
	password_letter = [random.choice(letters) for char in range(random.randint(10,12))]
	password_symbol = [random.choice(symbols) for char1 in range(random.randint(3, 5))]
	password_number = [random.choice(numbers) for char2 in range(random.randint(4, 6))]
	
	password_list = password_letter + password_symbol + password_number
	random.shuffle(password_list)
	password = "".join(password_list)
	
	pyperclip.copy(password)
	input_password.insert(0,password)
	
# --------------------------------------------------------------------------------------------------------------------- #

def save():
	
	if len(input_website.get()) == 0 or len(input_password.get()) == 0 :
		
		if len(input_website.get()) == 0 and len(input_password.get()) == 0:
			messagebox.showinfo(title="Missing Details", message=f"Please Fill Website and Password")
		elif len(input_password.get()) == 0:
			messagebox.showinfo(title="Missing Details", message=f"Please Fill Password")
		else:
			messagebox.showinfo(title="Missing Details", message=f"Please Fill Website")

	else:
		save_data = {
			input_website.get():{
			"Email":input_email.get(),
			"Password":input_password.get()
			}
		}
		
		output = messagebox.askokcancel(title=f"Website: {input_website.get()}",message=f"Email: {input_email.get()} \nPassword: {input_password.get()}")
		if output:
			try:
				file = open("data.json", "r")
				data = json.load(file)
			except(FileNotFoundError,json.decoder.JSONDecodeError):
				file = open("data.json", "w")
				json.dump(save_data,file,indent=4)
			else:
				data.update(save_data)
				file = open("data.json", "w")
				json.dump(data, file, indent=4)
			finally:
				input_website.delete(0,len(input_website.get()))
				input_password.delete(0,len(input_password.get()))

# ----------------------------------------------------------------------------------------------------------------------------------------------------- #

def search():
	website_search = input_website.get()
	try:
		file = open("data.json","r")
		content = json.load(file)
	except (json.decoder.JSONDecodeError,FileNotFoundError):
		messagebox.showerror(title="Error",message="No Data found")
	else:
		if len(input_website.get()) == 0:
			messagebox.showerror(message="No website given")
		else:
			if website_search in content:
					email = content[website_search]["Email"]
					password = content[website_search]["Password"]
					messagebox.showinfo(title=website_search, message=f"Email: {email} \nPassword: {password}")
					
					pyperclip.copy(password)
					input_website.delete(0, len(input_website.get()))
			else:
				messagebox.showerror(title="Error",message=f"No detail for '{input_website.get()}' exists\n")
				input_website.delete(0, len(input_website.get()))
	finally:
		pass
	
# ----------------------------------------------------------------------------------------------------------------------------------------------------- #

window = tkinter.Tk()
window.title("PASSWORD MANAGER")
window.config(padx=60, pady=60)

logo = tkinter.PhotoImage(file="img_1.png")

canvas = tkinter.Canvas(width=242, height=180)
canvas.create_image(121, 90, image=logo)
canvas.grid(row=0, column=1)

input_password = tkinter.Entry(width=18)
input_password.grid(row=3, column=1,sticky="ew")

input_website = tkinter.Entry(width=36)
input_website.grid(row=1, column=1,sticky="ew")
input_website.focus()

input_email = tkinter.Entry(width=36)
input_email.grid(row=2, column=1, columnspan=2,sticky="ew")
input_email.insert(0,"saksham22sg@gmail.com")

generate_button = tkinter.Button(text="Generate Password",width=17,command=generate)
generate_button.grid(row=3, column=2,sticky="ew",padx=1)

add_button = tkinter.Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky="ew")

search_button =  tkinter.Button(text="Search",width=17,command=search)
search_button.grid(row=1,column=2,sticky="ew",padx=1)

website_label = tkinter.Label(text="Website:  ",font=("arial",10,"italic"))
website_label.grid(row=1, column=0)
website_label.focus()

email_label = tkinter.Label(text="Email/UserName:  ",font=("arial",10,"italic"))
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:  ",font=("arial",10,"italic"))
password_label.grid(row=3, column=0)



window.mainloop()