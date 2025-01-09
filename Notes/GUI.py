import ctypes
import ttkbootstrap as ttkb
from PIL import Image, ImageTk
import Tkinter_FileHandler
from Settings import open_settings


myappid = u'Jason.Notes.version1.2'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# --- Main GUI CONFIGS ---
root = ttkb.Window(themename="darkly")
root.geometry('500x500')
root.title('NOTES')
root.iconbitmap('../Notes/assets/imgs/299111_note_sticky_icon.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.resizable(True, True)

icon = Image.open("../Notes/assets/imgs/299111_note_sticky_icon.ico")
icon = ImageTk.PhotoImage(icon)
root.iconphoto(True, icon)

root.grid_columnconfigure(0, weight=100)
root.grid_columnconfigure(3, weight=100)

settings_button = ttkb.Button(root, text='THEMES ⛭', style="success.Outline.TButton",
                              command=lambda: open_settings(root))
settings_button.grid(column=0, row=0, pady=(30, 0), padx=(30, 0), sticky="nw")

label_title = ttkb.Label(root, text='Notes', bootstyle="success")
label_title.grid(column=0, row=0, columnspan=4, pady=(100, 0))
label_title.configure(font=("Courier New", 30))

message = ttkb.Label(root, text='Create, Delete, Edit Notes; Simplified')
message.grid(column=0, row=1, columnspan=4, pady=(0, 20))
message.configure(font=("Courier New", 16))

frame_text = ttkb.Frame(root)
frame_text.grid(row=2, column=0, columnspan=4, padx=(10, 10), pady=(10, 10), sticky="nsew")

frame_text.grid_columnconfigure(0, weight=1)
frame_text.grid_rowconfigure(0, weight=1)

message_text = ttkb.Text(frame_text, font=('Segoe UI', 13), height=20, width=80)
message_text.grid(row=0, column=0, sticky="nsew")
message_text.configure(font=("Courier New", 16), borderwidth=2)

scrollbar = ttkb.Scrollbar(frame_text, bootstyle="success", command=message_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

# Link the scrollbar to the text widget
message_text.config(yscrollcommand=scrollbar.set)

button_create = ttkb.Button(root, text="Create new File", bootstyle="success", command=Tkinter_FileHandler.create_file)
button_create.grid(row=3, column=0, padx=10, pady=10, sticky="e")

button_delete = ttkb.Button(root, text="Delete a File", bootstyle="danger",
                            command=Tkinter_FileHandler.delete_file)
button_delete.grid(row=3, column=1, padx=10, pady=10, sticky=ttkb.W)

button_edit = ttkb.Button(root, text="Edit a File", bootstyle="blue",
                          command=lambda: Tkinter_FileHandler.write_file(message_text, root))
button_edit.grid(row=3, column=2, padx=10, pady=10, sticky=ttkb.E)

button_read = ttkb.Button(root, text="Read a File", bootstyle="light",
                          command=lambda: Tkinter_FileHandler.read_file(message_text))
button_read.grid(row=3, column=3, padx=10, pady=10, sticky=ttkb.W)

root.mainloop()
