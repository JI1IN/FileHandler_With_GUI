from tkinter import ttk

import ttkbootstrap as ttkb


def open_settings(root):
    settings_window = ttkb.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry('700x500')
    settings_window.resizable(False, False)

    def change_theme(theme_name):
        root.style.theme_use(theme_name)

    settings_title = ttk.Label(settings_window, text="Themes")
    settings_title.pack(pady=(50, 0))
    settings_title.configure(font=("Courier New", 30))
    # Label for theme options
    theme_label = ttkb.Label(settings_window, text="Select Themes; Simplified", bootstyle="primary")
    theme_label.pack(pady=10)
    theme_label.configure(font=("Courier New", 16))

    # Dropdown menu for themes
    theme_options = root.style.theme_names()
    theme_var = ttkb.StringVar(value=root.style.theme.name)
    theme_menu = ttkb.OptionMenu(
        settings_window,
        theme_var,
        root.style.theme.name,
        *theme_options,
        command=change_theme
    )
    theme_menu.pack(pady=10)

    back_button = ttkb.Button(settings_window, text="Back", command=settings_window.destroy, bootstyle="danger")
    back_button.pack(pady=20)
