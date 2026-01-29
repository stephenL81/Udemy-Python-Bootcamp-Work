from tkinter import *

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width="150",height="120")
window.config(padx=20,pady=20)

def calculate():# function to calculate miles to km
    calculation.config(text = float(entry.get()) * 1.6)

def calculate2():#function to calculate km to miles
    calculation.config(text = float(entry.get()) / 1.6)

entry = Entry(width=10) #area where user can type number for miles or km
entry.grid(row = 0, column = 1)

miles_label = Label(text="Miles")
miles_label.grid(row = 0, column = 2)

equal_label = Label(text = "is equal to")
equal_label.grid(row = 1, column = 0)

calculation = Label() #label which will display the result of the calculation
calculation.grid(row = 1, column = 1)

km_label = Label(text = "Km")
km_label.grid(row = 1, column = 2)

button = Button(text="Calculate",command = calculate) #button to trigger whichever calculation function has been selected
button.grid(row = 2 , column = 1)

blank_label = Label() # blank label to create a rows worth of space
blank_label.grid(row = 3, column = 1)

radio_state = IntVar() #hold the current radio button state

def radio_used(): #switches the title, labels and function depending on which radio button is selected.
    if radio_state.get() == 2:
        window.title("Km to Mile Convertor")
        miles_label.config(text="Km")
        km_label.config(text="Miles")
        button.config(command= calculate2)
    else:
        window.title("Mile to Km Convertor")
        miles_label.config(text="Mile")
        km_label.config(text="Km")
        button.config(command=calculate)

radiobutton1 = Radiobutton(text="Miles to Km", value=1, variable=radio_state, command=radio_used)
radiobutton1.grid(row = 4, column = 0)

radiobutton2 = Radiobutton(text="Km to Miles", value=2, variable=radio_state, command=radio_used)
radiobutton2.grid(row = 4, column = 1)


window.mainloop()

