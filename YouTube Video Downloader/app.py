import tkinter as tk
from tkinter import filedialog
import threading
import customtkinter
from pytube import YouTube
import os


def startDownload():
    try:
        global download_thread
        download_thread = threading.Thread(target=download_video)
        download_thread.start()
    except Exception as e:
        finishLabel.configure(text=f"Download Error: {e}", text_color="red")

def download_video():
    try:
        YouTube_Link = link.get()
        YouTube_Object = YouTube(YouTube_Link, on_progress_callback=on_progress)

        # Get streams with only video
        video_streams = YouTube_Object.streams.filter(file_extension='mp4', only_video=True)

        # Get the user-selected resolution
        selected_resolution = resolution_var.get()
        video = None

        if selected_resolution == '720p':
            video = video_streams.filter(res='720p').first()
        elif selected_resolution == '1080p':
            video = video_streams.filter(res='1080p').first()
        elif selected_resolution == '4k':
            video = video_streams.filter(res='2160p').first()

        if not video:
            finishLabel.configure(text=f"{selected_resolution} video not available", text_color="red")
            return

         # Ask the user to select the download directory
        download_directory = filedialog.askdirectory()
        video.download(download_directory)

        finishLabel.configure(text=f"Downloaded {selected_resolution} video to:\n" + download_directory)

        # Open the folder in the file explorer
        os.startfile(download_directory)

        # Close the app
        app.destroy()

        finishLabel.configure(text=f"Downloaded {selected_resolution} video to:\n" + download_directory)
    except Exception as e:
        finishLabel.configure(text=f"Download Error: {e}", text_color="red")

        

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize  # Fix the typo here
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    
    # Move the update line here
    pPercentage.update()

    # Update progressbar
    progressBar.set(float(percentage_of_completion) / 100)


def cancelDownload():
    try:
        global download_thread
        if download_thread and download_thread.is_alive():
            download_thread.join()
            finishLabel.configure(text="Download canceled", text_color="red")
    except Exception as e:
        finishLabel.configure(text=f"Cancel Error: {e}", text_color="red")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)


# Link input
url_variable = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_variable)
link.pack()

# Resolution selection
resolutions = ['HD', 'FULL', '4k']
resolution_var = tk.StringVar(value=resolutions[0])

resolution_menu = tk.OptionMenu(app, resolution_var, *resolutions)
resolution_menu.config(bg="ORANGE", width=15, height=2, font=('Montserrant', 12))  # Set background color to purple, adjust width and font size
resolution_menu.pack(pady=10)


# Finish Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()



#progress percentage
pPercentage = customtkinter.CTkLabel(app, text = "0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Cancel Button
cancel = customtkinter.CTkButton(app, text="Cancel", command=cancelDownload, fg_color= "red")
cancel.pack(padx=10, pady=10)

# Run App
app.mainloop()