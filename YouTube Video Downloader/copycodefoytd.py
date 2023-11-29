import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def download_video():
    url = entry_url.get()
    print(url)
    resulotion = resulotion_var.get()

    progress_label.pack(pady=(10,5))
    progress_bar.pack(pady=(10,5))
    status_label.pack(pady=(10,5))



    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=resulotion).first()
        

        #download the video into a specific path
        os.path.join("downlaods", f"{yt.title}.mp4")
        stream.download(output_path="dowmloads")

        status_label.configure(text= "Downloaded!", text_color = "white", fg_color = "green")

        stream.download()
    except Exception as e:
        status_label.configure(text= f"Error {str(e)}", text_color = "white", fg_color = "red")
    

#create a root window

root = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Title of the window

root.title("YouTube Downloader")


#set min and max width and height

root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)


#create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill = ctk.BOTH, expand = True, padx = 10, pady = 10)


#create a label and the entry widget for the video url

url_label = ctk.CTkLabel(content_frame, text="Enter the URL here: ")
entry_url = ctk.CTkEntry(content_frame, width = 400, height = 40)
url_label.pack(pady=(10, 5))
entry_url.pack(pady=(10, 5))



#create a download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=(10, 5))


#create a resulotion combo box
resulotions = ["4k","1080p","720p","360p","240p"]
resulotion_var = ctk.StringVar()
resulotion_combobox = ttk.Combobox(content_frame, width = 40, height= 10, values=resulotions, textvariable=resulotion_var)
resulotion_combobox.pack(pady=(40,10))
resulotion_combobox.set("4k")

#progress label and progress bar
progress_label = ctk.CTkLabel(content_frame, text="0%")


progress_bar = ctk.CTkProgressBar(content_frame, width = 400)
progress_bar.set(0.6)


#create status label
status_label = ctk.CTkLabel(content_frame, text="Download")

#to start the app
root.mainloop()