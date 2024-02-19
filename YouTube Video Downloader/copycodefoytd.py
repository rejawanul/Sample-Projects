import tkinter as tk
from tkinter import filedialog
import threading
import customtkinter
from pytube import YouTube
import os
import time
import subprocess

def startDownload():
    try:
        global download_thread, start_time

        # Record start time before starting download
        start_time = time.time()

        # Create thread for download
        download_thread = threading.Thread(target=download_video)
        download_thread.start()

    except Exception as e:
        finishLabel.configure(text=f"Download Error: {e}", text_color="red")

def download_video():
    try:
        # Get YouTube link and create YouTube object
        YouTube_Link = link.get()
        YouTube_Object = YouTube(YouTube_Link, on_progress_callback=on_progress)

        # Get available streams
        video_streams = YouTube_Object.streams

        # Get user-selected resolution
        selected_resolution = resolution_var.get()

        # Filter streams based on resolution (remove progressive=True)
        video = video_streams.filter(file_extension='mp4', res=selected_resolution).first()

        if not video:
            # Handle unsupported resolution or format
            if "1080p" in selected_resolution.lower() or "4k" in selected_resolution.lower():
                finishLabel.configure(text=f"{selected_resolution} video is not directly available. Trying to download compatible resolution...", text_color="orange")
                # Attempt to download a lower resolution
                lower_resolutions = ["720p", "480p"]
                for lower_res in lower_resolutions:
                    video = video_streams.filter(file_extension='mp4', res=lower_res).first()
                    if video:
                        finishLabel.configure(text=f"Downloaded {lower_res} video instead.", text_color="orange")
                        break
            else:
                finishLabel.configure(text=f"{selected_resolution} video not available", text_color="red")
            return

        # Ask user for download directory
        download_directory = filedialog.askdirectory()

        # If DASH stream, download audio and video separately
        if video.is_dash:
            # Download audio
            audio_stream = video_streams.filter(only_audio=True).first()
            audio_stream.download(output_path=download_directory)

            # Download video
            video.download(output_path=download_directory)

            # Merge audio and video using FFmpeg (ensure it's installed: https://ffmpeg.org/)
            subprocess.run([
                "ffmpeg", "-i", f"{download_directory}/video.mp4",
                "-i", f"{download_directory}/audio.mp4",
                "-c", "copy", f"{download_directory}/merged_{selected_resolution}.mp4"
            ])

            # Delete temporary files
            os.remove(f"{download_directory}/video.mp4")
            os.remove(f"{download_directory}/audio.mp4")

        else:
            # Otherwise, download directly
            video.download(output_path=download_directory)

        # Display success message
        finishLabel.configure(text=f"Downloaded {selected_resolution} video to:\n" + download_directory)

        # Open download folder
        os.startfile(download_directory)

        # Close app (can be removed if the app manages its own closing)
        # app.destroy()

    except Exception as e:
        finishLabel.configure(text=f"Download Error: {e}", text_color="red")

        

def on_progress(stream, chunk, bytes_remaining):
    # Calculate completion percentage and progress bar value
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progressBar.set(float(percentage_of_completion) / 100)

    # Update progress label or text field
    pPercentage.configure(text=per + '%')

    # Optionally calculate and display download speed
    # (requires start time stored globally)
    if start_time:
        now = time.time()
        elapsed_time = now - start_time
        if elapsed_time > 0:
            download_speed = bytes_downloaded / elapsed_time  # Bytes per second
            download_speed_mbps = download_speed / (1024 * 1024)  # Convert to MBps
            speed_label.configure(text=f"Download Speed: {download_speed_mbps:.2f} MBps")

def cancelDownload():
    try:
        global download_thread

        if download_thread and download_thread.is_alive():
            download_thread.join()  # Wait for thread to finish

            finishLabel.configure(text="Download canceled", text_color="red")

            # Reset progress bar and percentage
            progressBar.set(0)
            pPercentage.configure(text="0%")

            # Optionally: Delete temporary files if using DASH downloads
            download_directory = ""  # Replace with actual download directory if known
            if download_directory and video.is_dash:
                for filename in ["video.mp4", "audio.mp4"]:
                    file_path = os.path.join(download_directory, filename)
                    if os.path.exists(file_path):
                        os.remove(file_path)

            # Close app immediately (can be removed if managed elsewhere)
            # import sys
            # sys.exit(0)

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
resolution_menu.config(bg="ORANGE", width=15, height=2, font=('Montserrant', 12))
resolution_menu.pack(pady=10)

# Finish Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Speed Label
speed_label = customtkinter.CTkLabel(app, text="")
speed_label.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Cancel Button
cancel = customtkinter.CTkButton(app, text="Cancel", command=cancelDownload, fg_color="red")
cancel.pack(padx=10, pady=10)

# Run App
app.mainloop()
