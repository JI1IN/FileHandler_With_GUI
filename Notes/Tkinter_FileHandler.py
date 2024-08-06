import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def read_file(text_box):
    try:
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"),
                                                                                    ("All files", "*.*")])
        with open(filename, "r") as file:
            content = file.read()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, content)
            messagebox.showinfo("Info", "File successfully read!")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except IOError as e:
        messagebox.showerror("Error", f'An error has occurred: {e}')


# Function to save the file after user confirmation
def save_file_after_confirmation(text_box):
    try:
        content = text_box.get(1.0, tk.END).strip()  # Get the user-entered text and strip leading/trailing whitespace
        if content:
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"),
                                                                                        ("All files", "*.*")])
            if filename:
                with open(filename, "a") as file:
                    file.write(content)
                    messagebox.showinfo("Info", "File successfully written!")
        else:
            messagebox.showwarning("Warning", "No text entered to save.")
    except IOError as e:
        messagebox.showerror("Error", f'An error has occurred: {e}')


def write_file(text_box, root):
    text_to_append = "Enter the text you want to append to the file: "
    # Clear the text box and insert the prompt
    text_box.delete(1.0, tk.END)
    text_box.insert('end', text_to_append)

    # Remove the prompt text and get user input when the button is clicked
    def on_confirm():
        # Remove the prompt text
        text_box.delete(1.0, "1.{}".format(len(text_to_append)))
        save_file_after_confirmation(text_box)
        confirm_button.pack_forget()  # Remove the confirm button after saving

    # Create a confirm button for the user to confirm their input
    confirm_button = ttk.Button(root, text="Confirm and Save", command=on_confirm)
    confirm_button.pack(pady=10)


def delete_file():
    try:
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"),
                                                                                    ("All files", "*.*")])
        os.remove(filename)
        messagebox.showinfo("Info", "File successfully deleted!")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except IOError as e:
        messagebox.showerror("Error", f'An error has occurred: {e}')


def create_file():
    try:
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"),
                                                                                    ("All files", "*.*")])
        with open(filename, "w"):
            messagebox.showinfo("Info", "File successfully created!")
    except IOError as e:
        messagebox.showerror("Error", f'An error has occurred: {e}')
