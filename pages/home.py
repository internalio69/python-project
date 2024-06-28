import customtkinter as tk
from PIL import Image

class HomePage:
    def __init__(self, window):
        self.window = window
        
    def initialize(self):
        self.window.title("Home Page")
        self.window.geometry("1000x600+180+50")

        self.theme = tk.StringVar(value="dark")
        self.themeSwitch = tk.CTkSwitch(self.window, text="Dark", font=("Arial Bold", 15), variable=self.theme, onvalue="dark", offvalue="light", progress_color="black", command=self.switch_theme)
        self.themeSwitch.place(x=1, y=0)

        self.btn1Image = tk.CTkImage(light_image=Image.open("images/tts.png"), size=(100, 100))
        self.btn1 = tk.CTkButton(self.window, width=100, height=100, corner_radius=20, image=self.btn1Image, text="", fg_color=("#D7D4D4", "#221F1F"), border_spacing=20)
        self.btn1.pack(side="top", pady=100)
    
    def switch_theme(self):
        self.themeSwitch.configure(text=f"{self.themeSwitch.get().capitalize()}")
        tk.set_appearance_mode(self.themeSwitch.get())