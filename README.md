# YouTube Video Downloader

This application allows you to download videos from YouTube using a user-friendly interface.

## Features

- **Video and Audio Download**: Download both the video and audio from YouTube by simply pasting the video link.
- **Select Quality**: Choose the desired quality for the video download (e.g., 720p, 1080p, etc.).
- **Save Location**: Specify the directory where you want to save the downloaded video or audio file.
- **Progress Tracking**: View the download progress to know how much of the file has been downloaded.
- **Error Handling**: The application handles errors gracefully, providing informative messages if something goes wrong.

## Requirements

- Python 3.x
- `tkinter`
- `yt-dlp`
- `ffmpeg`

Install the required libraries:

```bash
pip install tk yt-dlp
```

### Install and Set Up `ffmpeg`

1. **Download `ffmpeg`**:
   - Go to the [FFmpeg download page](https://ffmpeg.org/download.html) and download the appropriate version for your operating system.

2. **Extract `ffmpeg`**:
   - Extract the downloaded files to a directory of your choice.

3. **Add `ffmpeg` to PATH**:
   - **Windows**:
     - Open the Start Menu and search for "Environment Variables".
     - Click on "Edit the system environment variables".
     - In the System Properties window, click on the "Environment Variables" button.
     - Under "System variables", find the `Path` variable and select it.
     - Click "Edit" and add the path to the `ffmpeg` bin directory (e.g., `C:\ffmpeg\bin`).
     - Click "OK" to save the changes.
   - **MacOS**:
     - Open Terminal.
     - Add `ffmpeg` to your PATH by editing your shell profile file (e.g., `.bash_profile`, `.zshrc`).
     - Add the line: `export PATH="/path/to/ffmpeg/bin:$PATH"`
     - Save the file and run `source ~/.bash_profile` or `source ~/.zshrc` to apply the changes.
   - **Linux**:
     - Open Terminal.
     - Add `ffmpeg` to your PATH by editing your shell profile file (e.g., `.bashrc`, `.profile`).
     - Add the line: `export PATH="/path/to/ffmpeg/bin:$PATH"`
     - Save the file and run `source ~/.bashrc` or `source ~/.profile` to apply the changes.

## Files

- `main.py`: Entry point to run the YouTube video downloader application.
- `youtube_downloader.py`: Contains the code for the YouTube video downloader.
- `utils.py`: Utility functions (styles, etc.).

## How to Run

Run the main application:

```bash
python main.py
```

## How to Use

1. **Download Video**:
   - Paste the YouTube video URL.
   - Select the desired video quality.
   - Click "Download" to save the video to the specified directory.

## Contact Information

- **Email:** aneesmohamed113@gmail.com
- **LinkedIn:** [linkedin.com/in/anees-mohamed-ar](https://www.linkedin.com/in/anees-mohamed-ar)
- **GitHub:** [github.com/anees-mohamed-ar](https://github.com/anees-mohamed-ar)
- **Instagram:** [instagram.com/anees_a_r__](https://www.instagram.com/anees_a_r__)
