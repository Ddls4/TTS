import pytesseract
from deep_translator import GoogleTranslator
import pyautogui
import threading
import time
import os
import tkinter as tk
import customtkinter
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\Tesseract'
engine = pyttsx3.init()

def show(frame, show_menu):
    hide_widgets(frame)
    back_button = tk.Button(frame, text="Volver al Menú", command=show_menu)
    back_button.grid(row=0, column=1)

    def matca():
        time.sleep(2)
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
    def capture_screen():
        entry_x_cap = int(entry_x.get())
        entry_y_cap = int(entry_y.get())
        entry_ancho_cap = int(entry_ancho.get())
        entry_alto_cap = int(entry_alto.get())

        screenshot = pyautogui.screenshot(region=(entry_x_cap ,entry_y_cap ,entry_ancho_cap-entry_x_cap ,entry_alto_cap-entry_y_cap))
        screenshot.save('captura2.png')
        text = pytesseract.image_to_string(screenshot)
        translated_text = GoogleTranslator(source='auto', target='es').translate(text)
        text_area.configure(text=translated_text)
        return translated_text
    def tts_lol():
        entry_x_cap = int(entry_x.get())
        entry_y_cap = int(entry_y.get())
        entry_ancho_cap = int(entry_ancho.get())
        entry_alto_cap = int(entry_alto.get())

        screenshot = pyautogui.screenshot(region=(entry_x_cap ,entry_y_cap ,entry_ancho_cap-entry_x_cap ,entry_alto_cap-entry_y_cap))
        screenshot.save('TTS.png')
        text = pytesseract.image_to_string(screenshot)
        translated_text = GoogleTranslator(source='auto', target='es').translate(text)
        text_area.configure(text=translated_text)
        
        engine.say(translated_text)
        engine.runAndWait()
    clear = lambda: os.system('cls')
    #------------------------------- hilo separado---------------------------------
    def run_while_true():
        while True:
            translated_text = capture_screen()
            clear()
            print("Texto traducido:", translated_text)
            time.sleep(10)
    # ---------------------------------interfaz gráfica-----------------------------
    def start_thread():
        thread = threading.Thread(target=run_while_true)
        thread.daemon = True
        thread.start()

    #--------------------------------------- Widgets para la sección de captura -----------------------------------
    tk.Label(frame, text="captura").grid(row=0, column=0, padx=10, pady=5, sticky="w")

    tk.Label(frame, text="x").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_x = customtkinter.CTkEntry(frame,placeholder_text="216")
    entry_x.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="y").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_y = customtkinter.CTkEntry(frame,placeholder_text="140")
    entry_y.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame, text="ancho").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_ancho = customtkinter.CTkEntry(frame,placeholder_text="1500")
    entry_ancho.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame, text="alto").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry_alto = customtkinter.CTkEntry(frame,placeholder_text="900")
    entry_alto.grid(row=4, column=1, padx=10, pady=5)

    # ----------------------------------- Widgets para la sección de volumen y lenguaje -----------------------------------
    tk.Label(frame, text="Volumen").grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_volumen = tk.Entry(frame)
    entry_volumen.grid(row=1, column=2, padx=10, pady=5)
    entry_volumen.insert(0, "1")

    tk.Label(frame, text="lenguaje del texto").grid(row=2, column=2, padx=10, pady=5, sticky="w")
    entry_lenguaje = tk.Entry(frame)
    entry_lenguaje.grid(row=3, column=2, padx=10, pady=5)
    entry_lenguaje.insert(0, "es")

    # ----------------------------------- Widget de Texto -----------------------------------
    tk.Label(frame, text="Texto").grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky="w")
    text_area = tk.Label(frame, text="Texto inicial", width=70, height=15, wraplength=300, anchor='w')
    text_area.grid(row=6, column=0, columnspan=5, padx=10, pady=5)


    # ----------------------------------- Botones de Captura y TTS -----------------------------------
    button_captura = tk.Button(frame, text="Captura", width=15, command=start_thread)
    button_captura.grid(row=7, column=0, padx=10, pady=10)

    button_tts = tk.Button(frame, text="TTS", width=15, command=tts_lol)
    button_tts.grid(row=7, column=1, padx=10, pady=10)

    button_marca = tk.Button(frame, text="marca", width=15 , command=matca)
    button_marca.grid(row=7, column=2, padx=10, pady=10)

    frame.pack(fill="both", expand=1)

def hide_widgets(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()