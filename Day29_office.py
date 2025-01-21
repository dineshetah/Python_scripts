from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# Save Data to File 
# create a function called save ()
# write to the data inside the entries to a data.txt file when the add button is clicked.
# Each website, email, and password combination should be on a new line inside the file.

# All fields need to be cleared after Add button is pressed.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


#-----------------------Save Password ---------------------------#
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #Here, if the user specific field is nothing type then show a popup
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message=f"Please make sure you haven't left any fields emply.")
    #messagebox.showinfo(title="Title", message="Message") #this is use for popup message box

    is_ok= messagebox.askokcancel(title= website, message=f"These are the details entered: \nEmail
                           {email}" f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as data_file: # here open data file and append 
           data_file.write(f"{website} | {email} | {password}\n") # here is write all these three things and \n use for next add entry
           website_entry.delete(0, END) 
           password_entry.delete(0, END) 

website_entry.focus()
email_entry.insert(0, "dinesh.etah457@gmail.com")



# Button 
generate_password_button = Button(text = "Generate Password")
generate_password_button.grid(row = 3 , column =2)
add_button= Button(text = "Add", width=36, command=save)
add_button.grid(row= 4 , column= 1, columnspan=2)

https://tkdocs.com/tutorial/widgets.html#entry go for more knowledge 
http://effbot.org/tkinterbook/entry.htm
http://effbot.org/tkinterbook/tkinter-standard-dialogs.htm

