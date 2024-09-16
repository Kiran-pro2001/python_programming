# Download YouTube Video 

# pip install pytube


from pytube import YouTube
import tkinter as tk
from tkinter import filedialog  #tkinter is a basic 2D Graphics Library - GUI Utility Library

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(save_path)
        print("Video Downloaded Successfully!")
        
    except Exception as e:
        print("Error")
        print(e)
    
url = "https://youtu.be/zeukbj1S35M?si=2x1bRbnsa2GX1ZGU"
save_path = "C:/Users/kk984/Downloads/yt_download"    #change the path link by "/"  - forward slash

download_video(url, save_path)
    