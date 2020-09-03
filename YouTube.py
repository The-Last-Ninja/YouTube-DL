import os
import youtube_dl
from pytube import YouTube
import time
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox


# Function for exiting a program
def exit_prgm(app):

    exit_msg = tk.messagebox.askyesno(title="Exiting Program",
                                      message="Are you sure, you want to exit fro this program?")
    # Exits a program when "Yes" is pressed
    if exit_msg == 1:
        app.destroy()
    else:
        app.mainloop()


# Function for browsing a directory to save a video
def browse(download_path):

    download_directory = filedialog.askdirectory(initialdir="Path")

    download_path.set(download_directory)


# Function for downloading video from Youtube link
def download(vid_link, download_path):

    window = Toplevel()

    window.configure(background="Gray")

    window.geometry("500x375")

    url = vid_link.get()

    path = download_path.get()

    video = YouTube(url)

    ydl_opts = {}

    os.chdir(path)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        window.title(f'Downloading.... {video.title}')
        ydl.download([url])
        opts_txt = tk.Listbox(window, height=10, width=30, font="Helvetica 12", background="White", foreground="Black")
        opts_txt.grid(row=0, column=3)
        opts_txt.insert(1, url)
        opts_txt.insert(2, video.title)
        download_bar = Progressbar(window, orient=HORIZONTAL, length=150, mode="determinate")
        download_bar.grid(row=0, column=4)
        for x in range(5):
            download_bar['value'] += 20
            window.update_idletasks()
            time.sleep(1)
        messagebox.showinfo(title="Download Complete", message=f'Your downloaded video is in\n {path}')


# Function for clear all entry box
def clear_all(app, vid_link, download_path):

    linktxt = tk.Entry(app, width=55, textvariable=vid_link)
    linktxt.grid(row=2, column=1)
    linktxt.delete(0, END)

    destination_txt = tk.Entry(app, width=55, textvariable=download_path)
    destination_txt.grid(row=3, column=1)
    destination_txt.delete(0, END)


# Entry point of the program and displays an app
def main():

    app = tk.Tk()

    app.geometry("525x170")

    app.configure(background="Grey")

    app.title("Youtube video downloader")

    vid_link = StringVar()

    download_path = StringVar()

    # Set up a menubar for Exit a program
    menubar = Menu(app)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=lambda: exit_prgm(app))
    menubar.add_cascade(label="File", menu=filemenu)
    app.config(menu=menubar)

    # Set up a label for tile and instruction
    title_txt = Label(app, text="Youtube video downloader", background="Gray", font='Helvetica 20')
    title_txt.grid(row=0, column=1)
    instruction = Label(app, text="Paste a video link below to get started", background="Gray", font='Helvetica 14')
    instruction.grid(row=1, column=1)

    # Set up label and entry box for youtube link
    link_label = Label(app, text="YouTube link  :", background="Gray", font='Arial 12')
    link_label.grid(row=2, column=0)
    linktxt = tk.Entry(app, width=55, textvariable=vid_link)
    linktxt.grid(row=2, column=1)

    # Set up label and entry box for directory destination
    destination = Label(app, text="Destination    :", background="Gray", font='Arial 12')
    destination.grid(row=3, column=0)
    destination_txt = tk.Entry(app, width=55, textvariable=download_path)
    destination_txt.grid(row=3, column=1)

    # Set up  buttons for Browsing a file for download directory and to download youtube video
    browse_btn = tk.Button(app, text="Browse", command=lambda: browse(download_path), width=10, background="Gray")
    browse_btn.grid(row=3, column=2)
    download_btn = tk.Button(app, text="Download", command=lambda: download(vid_link, download_path),
                             width=10, background="Gray")
    download_btn.grid(row=4, column=1)
    clear_btn = tk.Button(app, text="Clear", command=lambda: clear_all(app, vid_link, download_path), width=10,
                          background="Gray")
    clear_btn.grid(row=4, column=2)

    # Display an app in a loop
    app.mainloop()


# The following if statement helps Python determine whether or not the main()
# function in this program is our entry point.
if __name__ == "__main__":
    main()
