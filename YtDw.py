import tkinter as tk
from pytube import YouTube
import os
import time
import shutil

# Github change test

root = tk.Tk()
canvas1 = tk.Canvas(root, width=450, height=350, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Youtube Video Downloader', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(220, 60, window=label1)

sublabela = tk.Label(root, text='Video URL:')
canvas1.create_window(120, 140, window=sublabela)
sublabelb = tk.Label(root, text='Rename Video (optional):')
canvas1.create_window(82, 170, window=sublabelb)
sublabelc = tk.Label(root, text='Resolution:')
canvas1.create_window(52, 305, window=sublabelc)

entry1_url = tk.Entry(root)     # Url input area
canvas1.create_window(220, 140, window=entry1_url)
entry2_name = tk.Entry(root)    # Name input area
canvas1.create_window(220, 170, window=entry2_name)
entry3_resolution = tk.Entry(root)     # Resolution input area
canvas1.create_window(80, 330, window=entry3_resolution)


def get_vid():
    url_vid = entry1_url.get()      # Get URL
    title_vid = entry2_name.get()   # Get title
    resolution_vid = entry3_resolution.get()  # Get title

    try:
        print("Downloading . . . \n")
        # video = YouTube(url_vid).streams.first()
        # video.download()        # Downloads in 360p
        video = YouTube(url_vid).streams
        if resolution_vid:
            video = video.filter(res=resolution_vid + 'p')
        video.first().download()        # Downloads
        print("Download complete")
    except Exception as e:
        print(e)
        label2 = tk.Label(root, text='Error has occurred')  # Indication end of download
        canvas1.create_window(220, 270, window=label2)

    time.sleep(2.5)

    if title_vid:       # Change video name if user decides to
        os.rename(YouTube(url_vid).title + ".mp4", title_vid + ".mp4")
        shutil.move(title_vid + ".mp4", 'Videos')   # Move vid to 'Videos'
    else:
        shutil.move(YouTube(url_vid).title + ".mp4", 'Videos')      # Move vid to 'Videos'

    label2 = tk.Label(root, text='Your video ' + title_vid + ' has been downloaded')      # Indication end of download
    canvas1.create_window(220, 270, window=label2)


button1 = tk.Button(text='Start download', command=get_vid, bg='brown', fg='white')     # Main button
canvas1.create_window(220, 220, window=button1)

root.resizable(False, False)    # Prevents resizing
root.mainloop()     # Displays window
