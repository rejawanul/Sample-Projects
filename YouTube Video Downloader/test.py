import tkinter
from tkinter import filedialog
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        YouTube_Link = link.get()
        resolution_choice = resolution_var.get()

        YouTube_Object =  YouTube(YouTube_Link, on_progress_callback=on_progress)
        
        # Get the stream based on user's resolution choice, otherwise get the highest resolution stream
        if resolution_choice == '4k':
            video = YouTube_Object.streams.filter(res="2160p", file_extension="mp4").first() or YouTube_Object.streams.get_highest_resolution()
        elif resolution_choice == '1080p':
            video = YouTube_Object.streams.filter(res="1080p", file_extension="mp4").first() or YouTube_Object.streams.get_highest_resolution()
        elif resolution_choice == '720p':
            video = YouTube_Object.streams.filter(res="720p", file_extension="mp4").first() or YouTube_Object.streams.get_highest_resolution()
        elif resolution_choice == '480p':
            video = YouTube_Object.streams.filter(res="480p", file_extension="mp4").first() or YouTube_Object.streams.get_highest_resolution()
        else:
            video = YouTube_Object.streams.get_highest_resolution()

        # Ask the user to select the download directory
        download_directory = filedialog.askdirectory()
        video.download(download_directory)

        finishLabel.configure(text="Downloaded to:\n" + download_directory)
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

# Adding UI Elements for resolution choice
resolution_label = customtkinter.CTkLabel(app, text="Select Resolution:")
resolution_label.pack(pady=5)

resolutions = ['4k', '1080p', '720p', '480p', 'Default']
resolution_var = tkinter.StringVar(value='Default')
resolution_dropdown = customtkinter.CTkOptionMenu(app, resolution_var, *resolutions)
resolution_dropdown.pack(pady=5)


# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=20)

# Run App
app.mainloop()