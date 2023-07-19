from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Ooops", message="There are some black spaces. \n "
                                                      "Please fill the fields correctly.")

    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered\n Email: {email}"
                                                                f"\n Password:{password} \n It is okay to save?")
    if is_ok:
        try:
            with open("password_manager.json", "r") as file_list:
                # file_list.write( f"{website} | {email} | {password} \n")
                # READING OLD DATA
                data = json.load(file_list)
        except FileNotFoundError:
            with open("data.json", "w") as file_list:
                json.dump(new_data, file_list, indent=4)
        else:
            # UPDATING OLD DATA WITH NEW DATA
            data.update(new_data)

            with open("password_manager.json", "w") as file_list:
                # SAVING UPDATED DATA
                json.dump(new_data, file_list, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- SEARCH ACTUAL INFO ------------------------------- #
def search():
    website_check = entry_website.get()
    with open("password_manager.json", "r") as file_list:
        # file_list.write( f"{website} | {email} | {password} \n")
        # READING OLD DATA
        data = json.load(file_list)
    try:
        messagebox.showinfo(title=f"{website_check}"
                            , message=f"These are the details entered\n "
                                                  f"Email: {data[website_check]['email']}\n"
                                      f"Password: {data[website_check]['password']}")

    except:
        messagebox.showwarning(title="Ooops", message="Seems to be that you do not have any account"
                                                      "in that website")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

# Creation of the GUI
window.title("Password Manager")
window.config(padx=80, pady=80, bg="white")

# Logo imported
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=2)

# Creation of the texts and entries.

text_website = Label(text="Website:", bg="white", font=("Courier", 10))
text_website.grid(column=0, row=3)

email_website = Label(text="Email/Username:", bg="white", font=("Courier", 10))
email_website.grid(column=0, row=4)

password_website = Label(text="Password", bg="white", font=("Courier", 10))
password_website.grid(column=0, row=5)

# Entries
entry_website = Entry(width=32)
entry_website.focus()
entry_website.grid(column=1, row=3, columnspan=1)

entry_email = Entry(width=53)
entry_email.focus()
entry_email.grid(column=1, row=4, columnspan=2)
entry_email.insert(END, "carloslbnm@gmail.com")

entry_password = Entry(width=30)
entry_password.focus()
entry_password.grid(column=1, row=5, columnspan=1)

# Buttons
generate_button = Button(text="Generate Password", width=15, bg="white", command=generate_password)
generate_button.grid(column=2, row=5)

add_button = Button(text="Add", width=50, bg="white", command=save)
add_button.grid(column=1, row=6, columnspan=2)

search_button = Button(text="Search", width=10, bg="white", command=search)
search_button.grid(column=2, row=3)

window.mainloop()
