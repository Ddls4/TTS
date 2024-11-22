# menu.py
import tkinter as tk
import customtkinter as ctk
from views.TTSm1 import TTSm1_frame
from views.TTScv import create_frame_one
from views.TTScap3 import create_frame_three


def create_main_window():
    ctk.set_appearance_mode("light") # system dark light
    ctk.set_default_color_theme("dark-blue")
    root = tk.Tk()
    root.title("TTS_Ddls4")
    root.geometry("500x450")
    return root

def create_menu():
    root = create_main_window()
    # Crear marco contenedor
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)
    # Crear marcos individuales
    TTS_m1_frame = TTSm1_frame(container)
    TTS_cap3_frame = create_frame_three(container)
    TTS_cv_frame = create_frame_one(container)
    # Función para cambiar de marco
    def show_frame(frame,tamaño):
        frame.tkraise()
        root.geometry(tamaño)
    # Colocar botones de navegación en la ventana principal
    button_frame = tk.Frame(root ,bg="red")
    button_frame.pack(side="top", fill="x")

    tk.Button(button_frame, text="Modo 1", command=lambda: show_frame(TTS_m1_frame,"500x450")).pack(side="left", padx=5, pady=5)
    tk.Button(button_frame, text="Modo 2", command=lambda: show_frame(TTS_cap3_frame,"480x450")).pack(side="left", padx=5, pady=5)
    tk.Button(button_frame, text="Modo 3", command=lambda: show_frame(TTS_cv_frame,"850x350")).pack(side="left", padx=5, pady=5)
    # Mostrar el primer frame por defecto
    TTS_m1_frame.tkraise()
    # Iniciar la aplicación
    root.mainloop()