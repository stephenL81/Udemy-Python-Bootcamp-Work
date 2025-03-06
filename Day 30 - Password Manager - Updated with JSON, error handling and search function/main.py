from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- CUSTOM MESSAGEBOX ------------------------------- #

#custom messagebox as the ones provided do not dynamically adjust

def custom_messagebox(message, name):
    msg_window = Toplevel()
    msg_window.title(f"Password for {name}")

    label = Label(msg_window, text=message, padx=20, pady=20)
    label.pack()

    button_frame = Frame(msg_window)
    button_frame.pack(pady=10)

    def on_ok():
        msg_window.destroy()
        return True

    def on_cancel():
        msg_window.destroy()
        return False

    ok_button = Button(button_frame,text= "OK", command=on_ok, width=5)
    ok_button.pack(side="left", padx=20, pady=10)

    cancel_button = Button(button_frame,text="Cancel", command=on_cancel, width= 8)
    cancel_button.pack(side="left", padx=20, pady=10)

    width = max(300, len(message) *4)
    msg_window.geometry(f"{width}x250")



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
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Attention", message="Please ensure that all fields are completed")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail:{email}\nPassword:{password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)     #loading the json data
                    data.update(new_data)   #adding to the json data

            except FileNotFoundError:
                with open("data.json", mode = "w") as data_file:
                    json.dump(new_data, data_file, indent=4) #create the file if it does not exist and write data

            else:
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)    #saving the updated json data

            website_entry.delete(0,"end")
            password_entry.delete(0,"end")

# ---------------------------- PASSWORD SEARCH ------------------------------- #

def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
            site_name = website_entry.get()
            if site_name in data:
                #copy = messagebox.askokcancel(title=f"Password for {site_name}", message=f"Email: {data[site_name]['email']}\nPassword: {data[site_name]['password']}\nWould you like to copy to the clipboard?")
                copy = custom_messagebox(message=f"Website:  {site_name}\n\nEmail:  {data[site_name]['email']}\n\nPassword:  {data[site_name]['password']}\n\nWould you like to copy to the clipboard?",name=site_name)
                if copy:
                    pyperclip.copy(data[site_name]["password"])
            else:
                messagebox.showinfo(message="No details for that website exist")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

logo_img = PhotoImage(file = "logo.png")
canvas = Canvas(width="200", height="200", bg="white", highlightthickness=0)
canvas.create_image(100,100,image =logo_img)
canvas.grid(row = 0, column = 1)

website_label = Label()
website_label.config(text="Website:",bg="white")
website_label.grid(row = 1, column = 0)

email_label = Label(bg="white")
email_label.config(text="Email/Username:")
email_label.grid(row=2, column = 0)

password_label = Label(bg="white")
password_label.config(text="Password:")
password_label.grid(row=3,column = 0)

website_entry = Entry(width=21)
website_entry.grid(row=1,column = 1, columnspan=1,sticky="EW", padx=(0, 8))
website_entry.focus()

email_entry = Entry(width = 35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "stephenlancaster23@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,sticky = "EW", padx=(0, 8))

password_button = Button(text="Generate Password", width=14, bg="white", highlightthickness=1, command=generate_password)
password_button.grid(row=3,column=2,sticky = "EW")

add_button = Button(text="Add", width=35, bg="white", highlightthickness=1, command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky = "EW")

search_button = Button(text = "Search", width = 14, bg="white",highlightthickness=1,command = find_password)
search_button.grid(row=1,column=2, sticky = "EW")




window.mainloop()