from tkinter import *
from tkinter import messagebox
import random
import string

password=''
def generate_password(length):
    global password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
   
def button_click():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            box.delete(1.0,'end')
            messagebox.showerror("Error", "Please enter a positive integer for password length.")
            length_entry.delete(0, END)
        else:
            box.delete(1.0,'end')
            box.config(state=NORMAL)
            box.insert(END, generate_password(int(length_entry.get())))
    except ValueError:
        box.delete(1.0,'end')
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        length_entry.delete(0, END)

window = Tk()
window.title("Password Generator")
window.geometry("500x500")
window.resizable(False, False)
window.configure(bg='#1e2020')

text = Label(window, text="Password Generator", font=("PT Serif", 25), bg='#1e2020')
text.place(relx=0.5, y=100, anchor="center")

box = Text(window, height=2, width=25, font=('Lora', 25), relief='groove', state="disabled", bg='#000000')
box.place(relx=0.5, y=190, anchor="center")

length = IntVar()
length_entry = Entry(window, width=3, relief='sunken', border=1, bg='#000000', textvariable=length)
length_entry.place(x=100, y=290)

gen_btn = Button(window, text='Generate', font=("PT Serif", 15), height=2, width=10, border=3, relief='sunken', command=button_click)
gen_btn.place(x=200, y=280)

window.mainloop()
