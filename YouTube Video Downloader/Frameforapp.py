import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def startDownload():
    try:
        YouTube_Link = link.get()
        YouTube_Object = YouTube(YouTube_Link)
        video = YouTube_Object.streams.get_highest_resolution()

        def on_progress(stream, chunk, bytes_remaining):
            percent = (float(bytes_remaining / video.filesize) * 100)
            progress_var.set(100 - int(percent))
            app.update_idletasks()

        video.download(output_path=".", filename="video", on_progress_callback=on_progress)
        print("Download Complete")
    except VideoUnavailable:
        print("Video is unavailable or has been removed from YouTube.")
    except Exception as e:
        print(f"Error: {e}")
        print("YouTube Link is invalid")

    print("Download Complete")

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
url_variable = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_variable)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=30)

# Progress Bar
progress_var = tkinter.IntVar()
progress = customtkinter.CTkProgressBar(app, variable=progress_var)
progress.pack(pady=10)

# Run App
app.mainloop()