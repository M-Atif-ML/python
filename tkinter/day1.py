import tkinter as tk 

root = tk.Tk()

root.title("Simple App")

def add_to_list():	
	text = entry.get()
	if text :
		text_list.insert(tk.END,text)
		entry.delete(0,tk.END)


root.columnconfigure(0,weight =  3)
root.rowconfigure(0,weight=3)

frame = tk.Frame(root)
frame.grid(row = 0,column= 0,sticky='nsew')

entry = tk.Entry(frame)
entry.grid(row = 0,column = 0)

entry.bind('<Return>',lambda event: add_to_list())


entryButton = tk.Button(frame,text="Add",command = add_to_list)
entryButton.grid(row=0,column=1)


text_list = tk.Listbox(frame)
text_list.grid(row=1,column=0,columnspan = 2,sticky = 'ew')



root.mainloop()