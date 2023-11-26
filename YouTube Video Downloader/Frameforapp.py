import tkinter
from tkinter import filedialog
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        YouTube_Link = link.get()
        YouTube_Object =  YouTube(YouTube_Link, on_progress_callback=on_progress)
        video = YouTube_Object.streams.get_highest_resolution()

        # Ask the user to select the download directory
        download_directory = filedialog.askdirectory()
        video.download(download_directory)

        finishLabel.configure(text="Downloaded to:\n" + download_directory)
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


#Finish Downloading
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
download.pack(padx=10, pady=20)

# Run App
app.mainloop()