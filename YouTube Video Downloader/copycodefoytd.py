import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def download_video():
    url = entry_url.get()