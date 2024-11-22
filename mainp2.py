import tkinter as tk
import customtkinter as ctk

import views.TTSm1
import views.TTScap3
import views.TTScv

ctk.set_appearance_mode("light") # system dark light
ctk.set_default_color_theme("dark-blue")


app = ctk.CTk()
app.geometry("600x500")
app.title("Menu")
 # --------------------
TTS_cap2_frame = ctk.CTkFrame(app)
TTS_cap3_frame = ctk.CTkFrame(app)
TTS_cv_frame = ctk.CTkFrame(app)
menu_frame = ctk.CTkFrame(app ,corner_radius=10)


app.mainloop()

def show_menu(): # Show_menu es para el pack del menu principal
    hide_all_frames()
    menu_frame.pack(fill="both", expand=1)
def Show_Traductor_TTS(): # Crear una ventana para el traductor de texto con TTS
    hide_all_frames()
    views.TTSm1.show(TTS_cap2_frame, show_menu)
    app.geometry("850x350")
    
def Show_Traductor_Cap2(): # Crear una ventana para el traductor de capturas
    hide_all_frames()
    views.TTScap3.show(TTS_cap3_frame, show_menu)
    app.title("Your App")
    app.geometry("480x450")

def hide_all_frames():
    menu_frame.pack_forget()
    TTS_cap2_frame.pack_forget()
    TTS_cap3_frame.pack_forget()
    TTS_cv_frame.pack_forget()
    app.geometry("300x300")

def Show_Traductor_Cap3(): # Crear una ventana para el traductor de capturas
    hide_all_frames()
    views.TTScv.show(TTS_cv_frame, show_menu)
    app.title("Your App")
    app.geometry("480x450")