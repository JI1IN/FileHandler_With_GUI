import tkinter as tk
from tkinter import ttk
import Tkinter_FileHandler
import ctypes
from ctypes import windll
from PIL import Image, ImageTk
myappid = u'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# ---GUI CONFIGS---
root = tk.Tk()
root.geometry('500x500')
root.title('NOTES')
root.iconbitmap('assets/imgs/299111_note_sticky_icon.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.resizable(True, True)
windll.shcore.SetProcessDpiAwareness(1)
# ---GUI CONFIGS---

icon = Image.open("assets/imgs/299111_note_sticky_icon.ico")
icon = ImageTk.PhotoImage(icon)

# Set the taskbar icon
root.iconphoto(True, icon)

# Configure grid to have all columns take equal space
root.grid_columnconfigure(0, weight=100)
root.grid_columnconfigure(3, weight=100)

label_title = tk.Label(root, text='Notes', font=('Courier New BOLD', 25))
label_title.grid(column=0, row=0, columnspan=4, pady=(100, 0))

message = ttk.Label(root, text='Create, Delete, Edit Notes; Simplified', font=('Courier New', 16))
message.grid(column=0, row=1, columnspan=4, pady=(0, 20))

message_text = tk.Text(root, font=('Courier New', 13), height=20, width=80)
message_text.grid(row=2, column=0, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="ew")

button_create = ttk.Button(root, text="Create new File", command=Tkinter_FileHandler.create_file)
button_create.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

button_delete = ttk.Button(root, text="Delete a File", command=Tkinter_FileHandler.delete_file)
button_delete.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

button_edit = ttk.Button(root, text="Edit a File", command=lambda: Tkinter_FileHandler.write_file(message_text, root))
button_edit.grid(row=3, column=2, padx=10, pady=10, sticky=tk.E)

button_read = ttk.Button(root, text="Read a File", command=lambda: Tkinter_FileHandler.read_file(message_text))
button_read.grid(row=3, column=3, padx=10, pady=10, sticky=tk.W)

root.mainloop()
