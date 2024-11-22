# frame_three.py
import tkinter as tk

def create_frame_three(container):
    frame = tk.Frame(container, bg="lightyellow")
    frame.place(relwidth=1, relheight=1)
    label = tk.Label(frame, text="Este es el Frame 3", bg="lightyellow", font=("Arial", 16))
    label.pack(pady=20)
    return frame