from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_numbers =[choice(numbers) for _ in range(randint(2, 4))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Attention", message="Please ensure that all fields are completed")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail:{username}\nPassword:{password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as stes_file:
                stes_file.write(f"{website}|{username}|{password}\n")
            website_entry.delete(0,"end")
            password_entry.delete(0,"end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width="200", height="200")
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image =logo_img)
canvas.grid(row = 0, column = 1)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(row = 1, column = 0)

username_label = Label()
username_label.config(text="Email/Username:")
username_label.grid(row=2, column = 0)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3,column = 0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column = 1, columnspan=2,sticky="EW")
website_entry.focus()

username_entry = Entry(width = 35)
username_entry.grid(row=2, column=1, columnspan=2,sticky="EW")
username_entry.insert(0,"stephenlancaster23@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,sticky = "EW")

password_button = Button(text="Generate Password", width=14, command=generate_password)
password_button.grid(row=3,column=2,sticky = "EW")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky = "EW")





window.mainloop()