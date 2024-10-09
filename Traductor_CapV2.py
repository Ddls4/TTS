import tkinter as tk
import customtkinter
from tkinter import *

import pytesseract
from deep_translator import GoogleTranslator
import pyautogui
import threading
import time
import pyttsx3

from funciones import Pronunciar, traducirT, insertar_texto, marca, screenshot_and_extract_text

pytesseract.pytesseract.tesseract_cmd = r'D:\10\Tesseract-OCR\Tesseract'
engine = pyttsx3.init()



def show(frame, show_menu):
    hide_widgets(frame)

    def start_thread():
        thread = threading.Thread(target=run_while_true)
        thread.daemon = True
        thread.start()
    def run_while_true():
        while True:
            capture_screen()
            time.sleep(10)
    # --------------------------------- Funciones ---------------------------------
    def capture_screen():
        entry_lang_cap = "es"
        screenshot, text = screenshot_and_extract_text(entry_x, entry_y, entry_ancho, entry_alto)
        texto_traducido = traducirT(text, entry_lang.get())
        insertar_texto(texto_traducido, text_area)
        return texto_traducido
    
    def tts_lol(): # No esta llamando a thread por eso se cae tkinter
        screenshot, text = screenshot_and_extract_text(entry_x, entry_y, entry_ancho, entry_alto)
        texto_traducido = traducirT(text, entry_lang.get())
        insertar_texto(texto_traducido, text_area)
        Pronunciar(texto_traducido, (int(entry_vol.get())/ 100))

    def marca1():
        entry_x.delete(0, 'end')
        entry_y.delete(0, 'end')
        x, y = marca()
        entry_x.insert(0, x)
        entry_y.insert(0, y)

    def marca2():
        entry_ancho.delete(0, 'end')
        entry_alto.delete(0, 'end')
        x, y = marca()
        entry_ancho.insert(0, x)
        entry_alto.insert(0, y)
    

    photo2 = PhotoImage(file = r"img/inf.PNG") 
    photo3 = PhotoImage(file = r"img/Sup.PNG") 
    # ---------------------------------interfaz gráfica-----------------------------
    back_button = customtkinter.CTkButton(frame, text="Volver", width=50, command=show_menu)
    back_button.grid(row=0, column=0)
    
    customtkinter.CTkLabel(frame, text="captura").grid(row=0 , column=1, columnspan=2)

    entry_x = customtkinter.CTkEntry(frame, placeholder_text="X")
    entry_x.grid(row=1, column=0, padx=5, pady=5)
    entry_y = customtkinter.CTkEntry(frame, placeholder_text="Y")
    entry_y.grid(row=2, column=0, padx=5, pady=5)
    Boton_XY = customtkinter.CTkButton(frame,image=photo3, text="", width=50, height=50 ,command=marca1).grid(row=1, column=1, rowspan=2)
    entry_ancho = customtkinter.CTkEntry(frame, placeholder_text="Ancho")
    entry_ancho.grid(row=1, column=2, padx=5, pady=5)
    entry_alto = customtkinter.CTkEntry(frame, placeholder_text="Alto")
    entry_alto.grid(row=2, column=2, padx=5, pady=5)
    Boton_AA = customtkinter.CTkButton(frame,image=photo2, text="", width=50, height=50, command=marca2).grid(row=1, column=3, rowspan=2)

    # secion 2 |   sticky="w"
    customtkinter.CTkLabel(frame, text="Volumen").grid(row=3, column=0)
    entry_vol = customtkinter.CTkEntry(frame)
    entry_vol.grid(row=4, column=0)
    entry_vol.insert(0,"100")
    # Secion traducion
    customtkinter.CTkLabel(frame, text="Lenguaje").grid(row=3, column=2)
    entry_lang = customtkinter.CTkComboBox(frame,values=['en', 'it', 'es', 'ja', 'pt'])
    entry_lang.grid(row=4, column=2)
    entry_lang.set("es")  # set initial value
    # ----------------------------------- Widget de Texto -----------------------------------
    customtkinter.CTkLabel(frame, text="Texto-Traducion").grid(row=5, column=0, columnspan=4)
    text_area = tk.Text(frame, width=55, height=10)
    text_area.grid(row=6, column=0, columnspan=4, padx=10, pady=5)
    # ----------------------------------- Botones de Captura y TTS -----------------------------------
    Boton_Captura = customtkinter.CTkButton(frame, text="Captura", width=200, command=start_thread) # command=start_thread
    Boton_Captura.grid(row=7, column=0,columnspan=2, padx=5, pady=5)
    Boton_TTS = customtkinter.CTkButton(frame, text="TTS", width=200, command=tts_lol) # command=tts_lol
    Boton_TTS.grid(row=7, column=2, columnspan=2, padx=5, pady=5)

    frame.pack(fill="both", expand=1)



def hide_widgets(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()