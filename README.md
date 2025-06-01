# FileHandler_With_GUI - Notes

**Description:**

Notes is a graphical user interface (GUI) application built with **ttkbootstrap** for managing and handling files. The project is named **'Notes'** because the idea originated from jotting down project ideas on a sticky note.

**Current Status:**

Please note (no pun intended) that this project is currently on a break. As of now, no further improvements are planned for this project.

*UPDATE 07.08.2024:*

- Enhanced the design of the GUI using ttkbootstrap, planning on adding a combobox (I have no idea though how I should implement that).
- Created an executable of the application.
  
*UPDATE 08.08.2024:*

- Changed the theme and themes settings (for customizable themes, though currently there are only ttkb themes) of the app, added a scrollbar for the display field, enhanced design, deleted the executable from the repository because I will create one when the project is done (which of right now, it is not). 

Contributions, feedback, and suggestions are as always welcome as the project evolves.

**Features:**

- Intuitive GUI for file management
- Basic file operations such as open, save, and edit (append to file rather than edit)
- Customizable settings and options (will implement in the future, is not included yet)

**Installation:**

1. Clone the repository:
    ```bash
    git clone https://github.com/JI1IN/FileHandler_With_GUI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd FileHandler_With_GUI
    ```
3. Set up the virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

**Usage:**

Run the application using:
```bash
python Notes.py
