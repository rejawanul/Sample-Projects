import os
import tkinter as tk
from tkinter import filedialog

def rename_files(folder_path, custom_name):
    # Get list of files in the folder
    files = os.listdir(folder_path)
    
    # Sort the files to maintain sequence
    files.sort()
    
    # Initialize sequence count
    sequence = 1
    
    # Iterate through each file
    for file in files:
        # Extract file extension
        name, extension = os.path.splitext(file)
        
        # Construct new filename
        new_name = f"Inv_{sequence}_{custom_name}{extension}"
        
        # Build full file paths
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Increment sequence count
        sequence += 1

def browse_button():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def rename_button():
    folder_path = folder_entry.get()
    custom_name = custom_name_entry.get()
    rename_files(folder_path, custom_name)
    status_label.config(text="Files renamed successfully.")

# Create the main application window
app = tk.Tk()
app.title("File Renamer App")
app.configure(bg="#245953")  # Set background color

# Define font settings
font_settings = ("Arial", 12)  # Font family and size

# Create and place widgets
folder_label = tk.Label(app, text="Folder Path:", bg="#245953", fg="white", font=font_settings)
folder_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

folder_entry = tk.Entry(app, width=50, font=font_settings)
folder_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(app, text="Browse", command=browse_button, font=font_settings)
browse_button.grid(row=0, column=2, padx=5, pady=5)

custom_name_label = tk.Label(app, text="Custom Name:", bg="#245953", fg="white", font=font_settings)
custom_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

custom_name_entry = tk.Entry(app, width=50, font=font_settings)
custom_name_entry.grid(row=1, column=1, padx=5, pady=5)

rename_button = tk.Button(app, text="Rename Files", command=rename_button, font=font_settings)
rename_button.grid(row=2, column=1, padx=5, pady=5)

status_label = tk.Label(app, text="", bg="#245953", fg="white", font=font_settings)
status_label.grid(row=3, column=1, padx=5, pady=5)

# Run the application
app.mainloop()
