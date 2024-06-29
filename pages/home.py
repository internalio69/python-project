import customtkinter as tk
from PIL import Image

class HomePage:
    def __init__(self, window, username):
        self.window = window
        self.username = username
        
    def initialize(self):
        self.window.title("Home Page")
        self.window.geometry("1000x600+180+50")

        self.heading = tk.CTkLabel(self.window, width=100, height=10, fg_color="transparent", text=f"Welcome, {self.username}!", font=("Arial Bold", 30))
        self.heading.pack(side="top", pady=40)
        self.prompt = tk.CTkLabel(self.window, width=20, height=10, fg_color=("#D9D9D9", "#1D1D1D"), text="Select a tool below:", font=("Arial Bold", 20), corner_radius=5)
        self.prompt.pack(side="top", pady=1)

        self.theme = tk.StringVar(value="dark")
        self.themeSwitch = tk.CTkSwitch(self.window, text="Dark", font=("Arial Bold", 15), variable=self.theme, onvalue="dark", offvalue="light", progress_color="black", command=self.switch_theme)
        self.themeSwitch.place(x=1, y=0)

        self.btn1Image = tk.CTkImage(light_image=Image.open("images/tts.png"), size=(100, 100))
        self.btn1 = tk.CTkButton(self.window, width=100, height=100, corner_radius=20, image=self.btn1Image, text="", fg_color=("#D9D9D9", "#1D1D1D"), border_spacing=20, border_color=("#CBCBCB", "#1D1D1D"), border_width=1)
        self.btn1.place(x=230, y=240)
        self.ttsText = tk.CTkLabel(self.window, width=20, height=10, fg_color=("#D9D9D9", "#1D1D1D"), text="Text To\nSpeech", font=("Arial Bold", 20), corner_radius=5)
        self.ttsText.place(x=230, y=400)

        self.btn2Image = tk.CTkImage(light_image=Image.open("images/qr.png"), size=(100, 100))
        self.btn2 = tk.CTkButton(self.window, width=100, height=100, corner_radius=20, image=self.btn2Image, text="", fg_color=("#D9D9D9", "#1D1D1D"), border_spacing=20, border_color=("#CBCBCB", "#1D1D1D"), border_width=1)
        self.btn2.place(x=430, y=240)
        self.qrText = tk.CTkLabel(self.window, width=20, height=10, fg_color=("#D9D9D9", "#1D1D1D"), text="QRCode\nGenerator", font=("Arial Bold", 20), corner_radius=5)
        self.qrText.place(x=420, y=400)

        self.btn3Image = tk.CTkImage(light_image=Image.open("images/st.png"), size=(100, 100))
        self.btn3 = tk.CTkButton(self.window, width=100, height=100, corner_radius=20, image=self.btn3Image, text="", fg_color=("#D9D9D9", "#1D1D1D"), border_spacing=20, border_color=("#CBCBCB", "#1D1D1D"), border_width=1)
        self.btn3.place(x=630, y=240)
        self.qrText = tk.CTkLabel(self.window, width=20, height=10, fg_color=("#D9D9D9", "#1D1D1D"), text="Internet\nSpeed Test", font=("Arial Bold", 20), corner_radius=5)
        self.qrText.place(x=620, y=400)
    
    def switch_theme(self):
        self.themeSwitch.configure(text=f"{self.themeSwitch.get().capitalize()}")
        tk.set_appearance_mode(self.themeSwitch.get())