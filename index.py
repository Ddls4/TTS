import tkinter as tk
import customtkinter

import Traductor_TTS
import Traductor_CapV2
import Traductor_CapV3

customtkinter.set_appearance_mode("light") # system
customtkinter.set_default_color_theme("dark-blue")

def show_menu(): # Show_menu es para el pack del menu principal
    hide_all_frames()
    menu_frame.pack(fill="both", expand=1)
def Show_Traductor_TTS(): # Crear una ventana para el traductor de texto con TTS
    hide_all_frames()
    Traductor_TTS.show(Traductor_TTS_frame, show_menu)
    root.geometry("850x350")
    
def Show_Traductor_Cap2(): # Crear una ventana para el traductor de capturas
    hide_all_frames()
    Traductor_CapV2.show(Traductor_Cap2_frame, show_menu)
    root.title("Your App")
    root.geometry("480x450")

def hide_all_frames():
    menu_frame.pack_forget()
    Traductor_Cap2_frame.pack_forget()
    Traductor_Cap3_frame.pack_forget()
    Traductor_TTS_frame.pack_forget()
    root.geometry("300x300")

def Show_Traductor_Cap3(): # Crear una ventana para el traductor de capturas
    hide_all_frames()
    Traductor_CapV3.show(Traductor_Cap3_frame, show_menu)
    root.title("Your App")
    root.geometry("480x450")

root = customtkinter.CTk()
root.title("Menú")
root.geometry("300x300")

# crear todos los frame 
Traductor_TTS_frame = customtkinter.CTkFrame(root)
Traductor_Cap2_frame = customtkinter.CTkFrame(root)
Traductor_Cap3_frame = customtkinter.CTkFrame(root)
menu_frame = customtkinter.CTkFrame(root ,corner_radius=10)

menu_frame.pack(fill="both", expand=1)

# Los botones para abrir los Frames
button_TTs = customtkinter.CTkButton(menu_frame, text="Traductor_TTS", command=Show_Traductor_TTS)
button_TTs.pack(pady=10, padx=10)
button_Cap2 = customtkinter.CTkButton(menu_frame, text="Traductor_Cap", command=Show_Traductor_Cap2)
button_Cap2.pack(pady=10, padx=10)
button_Cap2 = customtkinter.CTkButton(menu_frame, text="Traductor_Capv3", command=Show_Traductor_Cap3)
button_Cap2.pack(pady=10, padx=10)
root.mainloop()