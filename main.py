import re
import tkinter as love
from tkinter import messagebox

#Main Window
GUI = love.Tk()
GUI.title("ISBN Validator")

# Function to check isbn

def check_isbn():
    isbn = entry.get()
    isbn = isbn.replace("-", "").replace(" ", "").upper() #Replace dash and spaces
    match = re.search(r'^(\d{9})(\d|X)', isbn)

    if not match:
        result = "Invalid ISBN"
    else:
        digits = match.group(1)
        check_digit = 10 if match.group(2) == "X" else int(match.group(2))
        result = sum((ii + 1) * int(digit) for ii, digit in enumerate(digits))

        #icorrect ang wrong isbn
        correct_check_digit = (result % 11) % 10

        # check if valid
        if correct_check_digit == check_digit:
            result = "Valid ISBN"
        else:
            corrected_isbn = isbn[:-1] + str(correct_check_digit)
            corrected_isbnFormat = "-".join([corrected_isbn[0], corrected_isbn[1:4], corrected_isbn[4:9], corrected_isbn[9]])
            result = f"Invalid ISBN\nCorrected ISBN: {corrected_isbnFormat}"

    messagebox.showinfo("Result", result)


# Frame sa widgets
frame = love.LabelFrame(GUI)
frame.pack(padx=10,pady=10)

label = love.Label(frame, text = "Enter an ISBN:")
label.grid(row=0, column=0, padx=5,pady=5)

entry = love.Entry(frame)
entry.grid(row=0, column=1, padx=5,pady=5)

check_button = love.Button(frame, text = "Check ISBN", command=check_isbn)
check_button.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

GUI.mainloop()
