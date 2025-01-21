

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
#from tkinter import Tk, Canvas, PhotoImage
import pyperclip
import json
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



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # new entry add for json 
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
        #                                               f"\nPassword: {password} \nIs it ok to save?")
        # if is_ok:

        try:
            with open("C:\\Users\\KIIT\Desktop\\100Days_code_programming\\data.json", "r") as data_file:
                #json.dump(new_data, data_file, indent=3)
            # Reading old data
                data =json.load(data_file)
            #data_file.write(f"{website} | {email} | {password}\n")
           #updating old data with new data
                #data.update(new_data)
            #Saving updated data
                #json.dump(data,data,indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
#------------------------------FIND PASSWORD----------------------------------#

## Challenge 2 - Search for a website in the Password Manager 
# TODO: Following task in below
# 1. Add a "Search" button next to the website entry field.

# 2. Adjust the layout and the other widgets as needed to get the desired look.

# 3. Create a function called find_password() that gets triggered when the "Search" button is pressed.

# 4. check if the user's next entry matches an item in the data.json 

# 5. if yes, show a messagebox with the website's name and password.

# 6. Catch an exception that might occur trying to access the data.json showing a messagebox with the text:"No Data File Found"

# 7. If the user's website does not exist inside the data.json, show
# a messagebox that reads "No details for the website exists".

def find_password():
    website = website.entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[password]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message="No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Create a Tkinter window
#root = Tk()

# Create a canvas widget
canvas = Canvas(window, height=150, width=150)

#canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="C:\\Users\KIIT\\Documents\\logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=25)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
search_button = Button(text = "Search", width=15, command=find_password)
search_button.grid(row=1, column=3) ## 1. Add a "Search" button next to the website entry field.
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=3)
add_button = Button(text="Add", width=26, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()