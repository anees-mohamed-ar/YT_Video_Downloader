import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yt_dlp as youtube_dl
import threading
import os
from utils import apply_styles

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("600x500")
        self.root.resizable(False, False)  # Make window resizable
        self.download_history = set()
        self.save_path = ""

        # Apply styles
        apply_styles()

        # UI Elements
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Enter YouTube URL:").pack(pady=5)
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.pack(pady=5)

        ttk.Label(main_frame, text="Select Resolution:").pack(pady=5)
        self.resolution_var = tk.StringVar(value="720p")
        self.resolution_menu = ttk.Combobox(main_frame, textvariable=self.resolution_var)
        self.resolution_menu['values'] = ('1080p', '720p', '480p', '360p', '240p')
        self.resolution_menu.pack(pady=5)

        ttk.Label(main_frame, text="Download Options:").pack(pady=5)
        self.option_var = tk.StringVar(value="Video")
        self.video_radio = ttk.Radiobutton(main_frame, text="Video", variable=self.option_var, value="Video")
        self.video_radio.pack(anchor='w', pady=2)
        self.audio_radio = ttk.Radiobutton(main_frame, text="Audio (MP3)", variable=self.option_var, value="Audio")
        self.audio_radio.pack(anchor='w', pady=2)

        self.path_button = ttk.Button(main_frame, text="Choose Save Path", command=self.choose_save_path)
        self.path_button.pack(pady=5)

        self.progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.progress_label = ttk.Label(main_frame, text="")
        self.progress_label.pack(pady=5)

        # Download button
        self.download_button = ttk.Button(main_frame, text="Download", command=self.download_video)
        self.download_button.pack(pady=20)

    def choose_save_path(self):
        self.save_path = filedialog.askdirectory()
        if self.save_path:
            messagebox.showinfo("Save Path Selected", f"Files will be saved to: {self.save_path}")

    def download_video(self):
        url = self.url_entry.get()
        resolution = self.resolution_var.get()
        option = self.option_var.get()
        self.progress_bar['value'] = 0
        self.progress_label.config(text="")

        if not self.save_path:
            messagebox.showwarning("No Save Path", "Please choose a save path before downloading.")
            return

        # Check for available resolutions
        available_resolutions = self.check_resolution(url, resolution)
        if not available_resolutions:
            messagebox.showinfo("Resolution Not Available", f"The selected resolution ({resolution}) is not available.")
            return

        # Check if the video with the same resolution is already downloaded
        if (url, resolution, option) in self.download_history:
            messagebox.showinfo("Already Downloaded", "The same video with the same resolution is already downloaded.")
            return

        try:
            download_thread = threading.Thread(target=self.start_download, args=(url, resolution, option))
            download_thread.start()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def check_resolution(self, url, resolution):
        try:
            with youtube_dl.YoutubeDL({'format': 'best'}) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                formats = info_dict.get('formats', [info_dict])
                available_resolutions = [f['format_id'] for f in formats if 'height' in f and f['height'] == int(resolution[:-1])]
                return available_resolutions
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while checking resolution: {e}")
            return None

    def start_download(self, url, resolution, option):
        outtmpl = os.path.join(self.save_path, '%(title)s-%(height)sp.%(ext)s') if option == "Video" else os.path.join(self.save_path, '%(title)s.%(ext)s')
        
        ydl_opts = {
            'progress_hooks': [self.on_progress],
            'outtmpl': outtmpl
        }

        if option == "Video":
            ydl_opts.update({
                'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best',
                'merge_output_format': 'mkv'
            })
        else:
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            })

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url)
                file_path = ydl.prepare_filename(info_dict)
                messagebox.showinfo("Download Complete", f"File has been downloaded and saved as {file_path}")
                self.download_history.add((url, resolution, option))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during download: {e}")

    def on_progress(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded_bytes = d.get('downloaded_bytes', 0)
            progress = (downloaded_bytes / total_bytes) * 100 if total_bytes else 0
            self.progress_bar['value'] = progress
            self.progress_label.config(text=f"Downloaded {downloaded_bytes / (1024 * 1024):.2f} MB of {total_bytes / (1024 * 1024):.2f} MB ({progress:.2f}%)")
            self.root.update_idletasks()
        elif d['status'] == 'finished':
            self.progress_label.config(text="Download complete!")
