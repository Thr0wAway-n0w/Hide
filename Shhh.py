import tkinter as tk
from tkinter import ttk
import os
import shutil
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Create the GUI window
root = tk.Tk()
root.title("Hide/Reveal Folder")
root.configure(background='black')  # Black background

# Create the style object
style = ttk.Style(root)
style.configure('TButton', font=('Arial', 12, 'bold'), foreground='red', background='black', highlightcolor='red', highlightbackground='red', highlightthickness=0)  # Set the button style

# Function to hide the folder
def hide_folder():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    hidden_folder = os.path.join(desktop_path, 'Hidden')
    os.rename(hidden_folder, os.path.join(desktop_path, '.Hidden'))

# Function to reveal the folder
def reveal_folder():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    hidden_folder = os.path.join(desktop_path, '.Hidden')
    os.rename(hidden_folder, os.path.join(desktop_path, 'Hidden'))

# Load the image
url = "https://img.freepik.com/premium-photo/demon-woman-logo-sexy-devil-isolated-black-background-generative-ai-illustration_137321-5777.jpg"
image_data = requests.get(url).content
image = Image.open(BytesIO(image_data))

# Resize the image
image = image.resize((220, 200), Image.LANCZOS)  # Use 'antialias' instead of 'ANTIALIAS'

# Convert the PIL image to a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=photo, borderwidth=2, relief='flat', bg='black', highlightcolor='red', highlightbackground='red')
image_label.grid(row=0, column=0, columnspan=2, padx=1, pady=1)

# Create the buttons
hide_button = ttk.Button(root, text="Hide", command=hide_folder)
hide_button.grid(row=1, column=0, padx=0, pady=0)

reveal_button = ttk.Button(root, text="Reveal", command=reveal_folder)
reveal_button.grid(row=1, column=1, padx=0, pady=0)

# Run the GUI event loop
root.mainloop()
