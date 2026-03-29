from tkinter import * 
import customtkinter 
# root = Tk()

customtkinter.set_appearance_mode("dark")


root = customtkinter.CTk()
root.title("Tkinter.com - Custom")

root.geometry('600x350')

def hello():
	my_label.configure(text=my_button.cget('text'))
	# my_button.configure(state = "disabled")
	print("hello world")

my_button = customtkinter.CTkButton(root,
text="hello!",command=hello,
height = 200,
width =200,
hover_color = "green",
corner_radius=50
)

my_button.pack(pady=80)

my_label = customtkinter.CTkLabel(root,text="")
my_label.pack(pady=20)




root.mainloop()
