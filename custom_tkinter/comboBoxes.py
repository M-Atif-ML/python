from tkinter import *
import customtkinter


# functions

def color_picker(choice):
	output_label.configure(text =f"You selected: {choice}",text_color =choice)

customtkinter.set_appearance_mode("dark")

root=customtkinter.CTk()

root.title("Tkinter.com - customTkinter ComboBox")
root.geometry("700x450")

my_label = customtkinter.CTkLabel(root,text="Pick a color")
my_label.pack(pady=40)


colors= ["Red","Green","Blue"]
my_combo=customtkinter.CTkComboBox(root,values=colors,command=color_picker)
my_combo.pack(pady=0)


output_label = customtkinter.CTkLabel(root,text=f"You selected: {colors[0]}")
output_label.pack(pady=20)

root.mainloop()
