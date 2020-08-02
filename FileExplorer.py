from tkinter import *
from tkinter import filedialog,messagebox
import sys

def browsing_files():
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))
    messagebox.showinfo("Browsing Operation is successfull")

def open_files():
    file = filedialog.askopenfile(mode ='r', filetypes =[('Python Files', '*.py'),('Text files','*.txt')])
    if file is not None:
        file_content = file.read()
        print(file_content)
    messagebox.showinfo("Opening operation is successfull")

def save_files():
    files = [('All Files', '*.*'),('Python Files', '*.py'),('Text Document', '*.txt')] 
    file = filedialog.asksaveasfile(filetypes = files, defaultextension = files) 
    messagebox.showinfo("Saving operation is successfull")

def exit_files():
    messagebox.showinfo("Exiting....")
    sys.exit(0)
    
root = Tk()
root.title("File Explorer using python")
root.config(background = "grey")
label_file_explorer = Label(root, text = "FILE EXPLORER",width=100,height=5,fg="red")

label_button_browse = Label(root, text =  "To Browse your files",width=50,height=2,fg="green")
button_browse = Button(root,text="Browse",fg="green",command=browsing_files)

label_open = Label(root,text="To open and print the content in python shell\nNote: only python and text file",width=50,height=2,fg="blue")
button_open = Button(root,text="Open",fg="blue",command = open_files)

label_save = Label(root,text="To Save your files ",width=50,height=2,fg="brown")
button_save = Button(root,text="Save",fg="brown",command = save_files)

label_exit = Label(root,text="To exit from file explorer ",width=50,height=2,fg="purple")
button_exit = Button(root,text="Exit",fg="purple",command = exit_files)

label_file_explorer.grid(column=3,row=0)
label_button_browse.grid(column=1,row=2,pady = 20, padx = 20, columnspan = 2)
button_browse.grid(column=3,row=2,pady = 20, padx = 20)

label_open.grid(column=1,row=3,pady = 20, padx = 20, columnspan = 2)
button_open.grid(column=3,row=3,pady = 20, padx = 20)

label_save.grid(column=1,row=4,pady = 20, padx = 20, columnspan = 2)
button_save.grid(column=3,row=4,pady = 20, padx = 20)

label_exit.grid(column=1,row=5,pady = 20, padx = 20, columnspan = 2)
button_exit.grid(column=3,row=5,pady = 20, padx = 20)

mainloop()
