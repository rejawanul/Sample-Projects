import tkinter
from tkinter import filedialog
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        YouTube_Link = link.get()
        YouTube_Object =  YouTube(YouTube_Link, on_progress_callback=on_progress)
        
        # Get the stream with 4K resolution if available, otherwise get the highest resolution stream
        video = YouTube_Object.streams.filter(res="2160p", file_extension="mp4").first() or YouTube_Object.streams.get_highest_resolution()

        # Ask the user to select the download directory
        download_directory = filedialog.askdirectory()
        video.download(download_directory)

        finishLabel.configure(text="Downloaded to:\n" + download_directory)
        
        # Close the application after download completes
        app.destroy()
    except Exception as e:
        finishLabel.configure(text=f"Download Error: {e}", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_Size = stream.filezise 
    bytes_downloaded = total_Size - bytes_remaining
    percentage_of_completation = bytes_downloaded / total_Size *100
    print(percentage_of_completation)
    per = str(int(percentage_of_completation))
    pPercentage.configure(text = per + '%')
    pPercentage.update()

    #update progressbar
    progressBar.set(float(percentage_of_completation)/100)



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