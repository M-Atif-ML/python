from tkinter import * 
import customtkinter 
# root = Tk()

def submit():
	my_label.configure(text=f"hello {my_entry.get()}")
	clear()
def clear():
	my_entry.delete(0,END)
customtkinter.set_appearance_mode("dark")


root = customtkinter.CTk()
root.title("Tkinter.com - Custom")

root.geometry('600x350')

my_label = customtkinter.CTkLabel(root,text="")
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root,
	placeholder_text = "Enter your name"
)
my_entry.pack(pady=20)

my_button=customtkinter.CTkButton(root,text ="Submit",
	command = submit
)

my_button.pack(pady=10)


clear_button = customtkinter.CTkButton(root,text="Clear",command=clear)
clear_button.pack(pady=50)
root.mainloop()
