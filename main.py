import tkinter as tk
from youtube_downloader import YouTubeDownloader

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
