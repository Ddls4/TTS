import tkinter as tk
import customtkinter
import pyttsx3


import Traductor_TTS
import Traductor_Cap

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Show_menu es para el pack del menu principal
def show_menu():
    hide_all_frames()
    menu_frame.pack(fill="both", expand=1)

def Show_Traductor_TTS():
    # Crear una ventana para el traductor de texto con TTS
    hide_all_frames()
    Traductor_TTS.show(Traductor_TTS_frame, show_menu)
    root.geometry("850x350")

def Show_Traductor_Cap():
    # Crear una ventana para el traductor de capturas
    hide_all_frames()
    Traductor_Cap.show(Traductor_Cap_frame, show_menu)
    root.title("Your App")
    root.geometry("500x600")


def hide_all_frames():
    menu_frame.pack_forget()
    Traductor_Cap_frame.pack_forget()
    Traductor_TTS_frame.pack_forget()
    root.geometry("300x300")

root = customtkinter.CTk()
root.title("Menú")
root.geometry("300x300")
# crear todos los frame 
Traductor_TTS_frame = customtkinter.CTkFrame(root)
Traductor_Cap_frame = customtkinter.CTkFrame(root)
menu_frame = customtkinter.CTkFrame(root ,corner_radius=10)

menu_frame.pack(fill="both", expand=1)
# Los botones para abrir los Frames
button_TTS = customtkinter.CTkButton(menu_frame, text="Traductor_Cap", command=Show_Traductor_Cap)
button_TTS.pack(pady=10, padx=10)
button_Cap = customtkinter.CTkButton(menu_frame, text="Traductor_TTS", command=Show_Traductor_TTS)
button_Cap.pack(pady=10, padx=10)
#----------------------------- Crear el frame para la sección 2  ------------------------------------ 
frame2 = tk.Frame(root)
label2 = tk.Label(frame2, text="Estás en la Sección 2")
label2.pack(pady=10)
back_button2 = tk.Button(frame2, text="Volver al Menú", command=show_menu)
back_button2.pack(pady=10)
#-----------------------------------------------------------------
root.mainloop()
