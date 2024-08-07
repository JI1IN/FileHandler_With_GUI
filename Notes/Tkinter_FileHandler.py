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


def save_file_after_confirmation(text_box):
    try:
        content = text_box.get(1.0, tk.END).strip()
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

    text_box.delete(1.0, tk.END)
    text_box.insert('end', text_to_append)

    def on_confirm():
        text_box.delete(1.0, "1.{}".format(len(text_to_append)))
        save_file_after_confirmation(text_box)
        confirm_button.grid_forget()

    confirm_button = ttk.Button(root, text="Confirm & Save", command=on_confirm)
    confirm_button.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)


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
