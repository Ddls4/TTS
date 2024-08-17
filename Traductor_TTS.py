import tkinter as tk
import customtkinter as ctk
from tkinter import *
from deep_translator import GoogleTranslator
import pyttsx3

engine = pyttsx3.init()

def show(frame, show_menu):
    hide_widgets(frame)
    
    def traducir():
        #entry_x_cap = int(entry_1.get())  para entry
        entry_x_cap = entry_1.get(1.0, "end-1c") # Text
        translated_text = GoogleTranslator(source='auto', target='es').translate(entry_x_cap)
        entry_2.delete("1.0", END)
        entry_2.insert("1.5", translated_text)
    def tts2():
        entry_x_cap = entry_1.get(1.0, "end-1c") # Text
        translated_text = GoogleTranslator(source='auto', target='es').translate(entry_x_cap)
        engine.say(translated_text)
        engine.runAndWait()
    def tts():
        entry_x_cap = entry_1.get(1.0, "end-1c") # Text
        engine.say(entry_x_cap)
        engine.runAndWait()
    
    back_button = tk.Button(frame, text="Volver al Menú", command=show_menu)
    back_button.grid(row=0, column=0)

    label_1 = ctk.CTkLabel(frame, text="EN").grid(row=1, column=0)
    label_2 = ctk.CTkLabel(frame, text="ES").grid(row=1, column=1)

    entry_1 = tk.Text(frame, width=50 ,height=10)
    entry_1.grid(row=2, column=0, padx=10)
    entry_2 = tk.Text(frame, width=50 ,height=10)
    entry_2.grid(row=2, column=1, padx=10)
    
    boton_TTs1 = ctk.CTkButton(frame, text="TTS", command=tts)
    boton_TTs1.grid(row=3, column=0, pady=10)
    boton_TTs2 = ctk.CTkButton(frame, text="TTS", command=tts2)
    boton_TTs2.grid(row=3, column=1, pady=10)

    boton_3 = ctk.CTkButton(frame, text="Captura", command=traducir, width=425)
    boton_3.grid(row=4, column=0, columnspan=2, pady=10 )

    frame.pack(fill="both", expand=1)

def hide_widgets(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()
