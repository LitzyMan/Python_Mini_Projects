from tkinter import *
import string
from random import randint, choice

def generate_passsword():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# create the window
window = Tk()
window.title("Password Generator")
window.geometry("720x480")
window.config(background='#4065A4')

# create the pricipal frame
frame = Frame(window, bg='#4065A4')

# creating the image
width = 300
height = 300
image = PhotoImage(file="image/reset-password.png").zoom(19).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# create a subframe
right_frame = Frame(frame, bg='#4065A4')

# create a title
label_title = Label(right_frame, text="Password", font=("Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

# create a input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

# create a button
generate_passsword_button = Button(right_frame, text="Generate", font=("Helvetica", 20), bg='#4065A4', fg='white', command=generate_passsword)
generate_passsword_button.pack()

# on place la sous boite à droit de la frame principal
right_frame.grid(row=0, column=1, sticky=W)

# display the frame
frame.pack(expand=YES)

# create a menu
menu_bar = Menu(window)
# create a first menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=generate_passsword)
file_menu.add_command(label="Quit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# display
window.mainloop()
