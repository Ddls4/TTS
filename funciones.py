from deep_translator import GoogleTranslator
import pyttsx3
import pyautogui
import pytesseract
import time
from tkinter import *

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\Tesseract'
engine = pyttsx3.init()

def traducirT(entry_x_cap, idioma_destino='es'):
        translated_text = GoogleTranslator(source='auto', target=idioma_destino)
        return translated_text.translate(entry_x_cap)

def Pronunciar(translated_text, entry_vol_cap=1):
        engine.setProperty('volume',entry_vol_cap)
        engine.say(translated_text)
        engine.runAndWait()

def insertar_texto(texto_traducido, text_area):
        text_area.delete("1.0", END)
        text_area.insert("1.5", texto_traducido)

def marca():
        time.sleep(3)
        x, y = pyautogui.position()
        return x, y

def screenshot_and_extract_text(entry_x, entry_y, entry_ancho, entry_alto):
        region = (int(entry_x.get()), int(entry_y.get()), int(entry_ancho.get()) - int(entry_x.get()), int(entry_alto.get()) - int(entry_y.get()))
        screenshot = pyautogui.screenshot(region=region)
        text = pytesseract.image_to_string(screenshot)
        return screenshot, text
