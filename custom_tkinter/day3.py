from tkinter import *
import customtkinter


def checkbox_clicked():
    if check_var.get() == 'off':
        customtkinter.set_appearance_mode("light")
        my_check.configure(text="dark theme")
    else:
        customtkinter.set_appearance_mode("dark")
        my_check.configure(text="light theme")

customtkinter.set_appearance_mode("light")
def select():
	
	my_check.select()
	checkbox_clicked()
def deselect():
	my_check.deselect()
	checkbox_clicked()

root=customtkinter.CTk()

root.title("Tkinter")
root.geometry('700x450')

check_var = customtkinter.StringVar(value="off")



my_check = customtkinter.CTkCheckBox(root,text="dark theme"
			,variable=check_var,onvalue='on',offvalue='off',command=checkbox_clicked)
select_button = customtkinter.CTkButton(root,text="Select",command=select)
clear_button=customtkinter.CTkButton(root,text="Deselect",command=deselect)

my_check.pack(pady=50)
select_button.pack(pady=5)
clear_button.pack(pady=5)




root.mainloop()











