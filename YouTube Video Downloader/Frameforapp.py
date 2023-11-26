import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

def startDownload():
    try:
        YouTube_Link = link.get()
        YouTube_Object = YouTube(YouTube_Link, on_progress_callback=on_progress)
        video = YouTube_Object.streams.get_highest_resolution()
        title.configure(text=YouTube_Object.title)
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except VideoUnavailable:
        finishLabel.configure(text="Video is unavailable or has been removed from YouTube.")
    except Exception as e:
        print(f"Error: {e}")
        finishLabel.configure(text="Download Error!")

def on_progress(stream, chunk, bytes_remaining):
    total_Size = stream.filesize  # Fix typo here
    bytes_downloaded = total_Size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_Size * 100
    print(percentage_of_completion)
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
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