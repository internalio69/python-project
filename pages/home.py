import customtkinter as tk
from .qrcode import QRCode
from PIL import Image

class HomePage:
    def __init__(self, window, username):
        self.window = window
        self.username = username
        
    def initialize(self):
        self.window.title("Home Page")
        self.window.geometry("1000x600+180+50")

        # head labels
        self.heading = tk.CTkLabel(self.window, width=100, height=10, fg_color="transparent", text=f"Welcome, {self.username}!", font=("Arial Bold", 30))
        self.heading.pack(side="top", pady=40)
        self.prompt = tk.CTkLabel(self.window, width=20, height=10, fg_color=("#C7C7C7", "#1D1D1D"), text="Select a tool from below:", font=("Arial Bold", 20), corner_radius=5)
        self.prompt.pack(side="top", pady=1)

        # text to speech btn and label
        self.btn1Image = tk.CTkImage(light_image=Image.open("images/tts.png"), size=(100, 100))
        self.btn1 = tk.CTkButton(self.window, width=100, height=100, corner_radius=20, image=self.btn1Image, text="", fg_color=("#C7C7C7", "#1D1D1D"), border_spacing=20, border_color=("#B6B6B6", "#1D1D1D"), border_width=1, hover_color=("#B6B6B6", "#161616"), command=self.loadQrPage)
        self.btn1.place(x=230, y=240)
        self.ttsText = tk.CTkLabel(self.window, width=20, height=10, fg_color=("#C7C7C7", "#1D1D1D"), text="Text To\nSpeech", font=("Arial Bold", 20), corner_radius=5)
        self.ttsText.place(x=265, y=400)

        # qr code gen btn and label
        self.btn2Image = tk.CTkImage(light_image=Image.open("images/qr.png"), size=(100, 100))
        self.btn2 = tk.CTkButton(self.window, width=100, height=100, corner_radius=20, image=self.btn2Image, text="", fg_color=("#C7C7C7", "#1D1D1D"), border_spacing=20, border_color=("#B6B6B6", "#1D1D1D"), border_width=1, hover_color=("#B6B6B6", "#161616"))
        self.btn2.place(x=430, y=240)
        self.qrText = tk.CTkLabel(self.window, width=20, height=10, fg_color=("#C7C7C7", "#1D1D1D"), text="QRCode\nGenerator", font=("Arial Bold", 20), corner_radius=5)
        self.qrText.place(x=450, y=400)

        # speedtest btn and label
        self.btn3Image = tk.CTkImage(light_image=Image.open("images/st.png"), size=(100, 100))
        self.btn3 = tk.CTkButton(self.window, width=100, height=100, corner_radius=20, image=self.btn3Image, text="", fg_color=("#C7C7C7", "#1D1D1D"), border_spacing=20, border_color=("#B6B6B6", "#1D1D1D"), border_width=1, hover_color=("#B6B6B6", "#161616"))
        self.btn3.place(x=630, y=240)
        self.stText = tk.CTkLabel(self.window, width=20, height=10, fg_color=("#C7C7C7", "#1D1D1D"), text="Internet\nSpeed Test", font=("Arial Bold", 20), corner_radius=5)
        self.stText.place(x=650, y=400)

    def clearWidgets(self):
        self.heading.destroy()
        self.prompt.destroy()
        self.btn1.destroy()
        self.ttsText.destroy()
        self.btn2.destroy()
        self.qrText.destroy()
        self.btn3.destroy()
        self.stText.destroy()

    def loadQrPage(self):
        self.clearWidgets()
        QRCode(self.window).initialize()