import os
import shutil
import tkinter as tk
from tkinter import messagebox

def sort_videos():
    desktop = os.path.expanduser("~/Desktop")
    target_folder = os.path.join(desktop, "Raw_Footage")
    os.makedirs(target_folder, exist_ok=True)

    video_exts = (".mp4", ".mov", ".avi", ".mkv", ".m4v")
    moved = 0

    for filename in os.listdir(desktop):
        filepath = os.path.join(desktop, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(video_exts):
            shutil.move(filepath, os.path.join(target_folder, filename))
            moved += 1

    if moved == 0:
        messagebox.showinfo("Info", "No video files found on Desktop.")
    else:
        messagebox.showinfo("Success", f"{moved} file(s) moved to Raw_Footage.")

def center_window(win, width=300, height=100):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    win.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("🎥 Raw Footage Sorter")
center_window(root)

button = tk.Button(root, text="Sort Raw Footage", command=sort_videos)
button.pack(pady=30)

root.mainloop()
