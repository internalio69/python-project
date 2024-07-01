import customtkinter as tk
import pyttsx3

class TTS:
    def __init__(self, window, home):
        self.home = home
        self.window = window
        
    def initialize(self):
        self.window.title("Text To Speech")
        self.window.grid_rowconfigure(0, weight=1, uniform='a')
        self.window.grid_columnconfigure((0,1), weight=1, uniform='a')

        self.frame2 = Frame2(master=self.window)
        self.frame1 = Frame1(master=self.window, frame2=self.frame2)
        self.frame1.grid(row=0, column=0, padx=20, pady=30, sticky="nsew")
        self.frame2.grid(row=0, column=1, sticky="nsew", pady=30)
    
        self.backBtn = tk.CTkButton(self.window, text="⬅", fg_color="#424242", width=30, border_spacing=5, border_width=3, border_color="#424242", hover_color="#575656", corner_radius=5, font=("Arial Bold", 10), command=self.back)
        self.backBtn.place(x=225, y=42)

    def back(self):
        self.frame1.destroy()
        self.frame2.destroy()
        self.backBtn.destroy()
        self.home.initialize()

class Frame1(tk.CTkFrame):
    engine = pyttsx3.init()
    speak_rate = None
    volume = None
    voice = 0
    
    font_data=("Arial Bold", 15)
    font_data2=("Arial Bold", 13)
    qr_data=None
    def __init__(self, master, frame2, **kwargs):
        super().__init__(master, **kwargs)

        self.speak_rate = tk.IntVar(self, 1)
        self.volume = tk.IntVar(self, 1)
        self.columnconfigure((0,1), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6), weight=1, uniform='a')
        self.frame2 = frame2

        self.heading = tk.CTkLabel(self, text="• Text To Speech", width=120, height=35, font=("Arial Bold", 20), corner_radius=5, fg_color=("#C7C7C7", "#1D1D1D"))
        self.heading.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.textbox_label = tk.CTkLabel(self, text="Enter text:", height=10, font=self.font_data)
        self.textbox_label.grid(row=0, column=0, padx=15, pady=5, sticky="sw")

        self.textbox = tk.CTkTextbox(self, width=400, height=100, border_width=2)
        self.textbox.grid(row=1, column=0, columnspan=2, rowspan=2, padx=10, sticky="nswe")

        self.rate_label = tk.CTkLabel(self, text="Speaking Rate:", font=self.font_data2)
        self.rate_label.grid(row=3, column=0, sticky="sw", padx=20)
        self.rate_slider = tk.CTkSlider(self, from_=1, to=380, number_of_steps=380, hover=False, variable=self.speak_rate, button_color="#E8A701", progress_color="#C78F01")
        self.rate_slider.set(190)
        self.rate_slider.grid(row=4, column=0, sticky="nw", padx=20, pady=5)

        self.vol_label = tk.CTkLabel(self, text="Volume:", font=self.font_data2)
        self.vol_label.grid(row=3, column=1, sticky="sw", padx=20)
        self.vol_slider = tk.CTkSlider(self, from_=0, to=10, number_of_steps=11, hover=False, variable=self.volume, button_color="#F25B04", progress_color="#C74A03")
        self.vol_slider.set(10)
        self.vol_slider.grid(row=4, column=1, sticky="nw", padx=20, pady=5)

        self.voice_label = tk.CTkLabel(self, text="Voice:", font=self.font_data2)
        self.voice_label.grid(row=5, column=0, sticky="nw", padx=15)

        self.voice_btn1 = tk.CTkButton(self, text="Male", corner_radius=5, font=self.font_data, state="disabled", text_color_disabled="#B6B6B6", command=self.changeVoice, hover=False)
        self.voice_btn1.grid(row=5, column=0, sticky="swe", padx=10)
        self.voice_btn2 = tk.CTkButton(self, text="Female", corner_radius=5, font=self.font_data, text_color_disabled="#B6B6B6", command=self.changeVoice, hover=False)
        self.voice_btn2.grid(row=5, column=1, sticky="swe", padx=10)

        self.generate_btn = tk.CTkButton(self, text="⚙ Generate Voice", corner_radius=10, font=self.font_data, hover=False, fg_color="#6E01C7", command=self.generate_tts)
        self.generate_btn.grid(row=6, column=0, columnspan=2, sticky="s", pady=8)

    def changeVoice(self):
        if (self.voice == 0):
            self.voice=1
            self.voice_btn1.configure(state="enabled")
            self.voice_btn2.configure(state="disabled")
        else:
            self.voice=0
            self.voice_btn1.configure(state="disabled")
            self.voice_btn2.configure(state="enabled")

    def generate_tts(self):
        self.engine.setProperty('rate', self.speak_rate.get())
        self.frame2.lyrics.configure(text=self.textbox.get('1.0', tk.END))
        self.engine.setProperty('volume', self.volume.get()/10)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[self.voice].id)
        self.engine.say(self.textbox.get('1.0', tk.END))
        self.engine.runAndWait()
        self.frame2.animation_start()
        self.frame2.saveas_btn.configure(state="enabled")

class Frame2(tk.CTkFrame):
    engine = pyttsx3.init()
    isstopped_animation = False
    font_data=("Arial Bold", 15)
    def __init__(self, master, **kwargs):
        super().__init__(master, border_width=3, **kwargs)
        self.rowconfigure((0,1,2,3), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')
        self.grid(row=0, column=1, rowspan=7, sticky="nswe", padx=10)
        self.height=20
        self.cmp1 = tk.CTkButton(self, text="", corner_radius=10, width=20, height=20, fg_color=("black", "white"), hover=False)
        self.cmp1.place(x=150, y=80)
        self.cmp2 = tk.CTkButton(self, text="", corner_radius=10, width=20, height=20, fg_color=("black", "white"), hover=False)
        self.cmp2.place(x=200, y=80)
        self.cmp3 = tk.CTkButton(self, text="", corner_radius=10, width=20, height=20, fg_color=("black", "white"), hover=False)
        self.cmp3.place(x=250, y=80)
        self.cmp4 = tk.CTkButton(self, text="", corner_radius=10, width=20, height=20, fg_color=("black", "white"), hover=False)
        self.cmp4.place(x=300, y=80)
        # ==== ANIMATION FRAME ====

        self.divider = tk.CTkLabel(self, text="________________________________________________________________", text_color="#4D4D4D")
        self.divider.grid(row=1, sticky='s')

        self.lyrics = tk.CTkLabel(self, text="", height=200, fg_color=("#C7C7C7", "#1D1D1D"))
        self.lyrics.grid(row=2, rowspan=2, sticky='nwe', padx=10, pady=20)

        self.saveas_btn = tk.CTkButton(self, font=self.font_data, hover_color=("#161616", "#B6B6B6"), text="✔ Save Audio", fg_color=("#151515" ,"#E7E7E7"), text_color=("white", "black"), state="disabled", command=lambda: self.save_audio(data=self.lyrics.cget("text")))
        self.saveas_btn.grid(row=3, sticky='s', pady=30)

    def animation_start(self):
        self.animate_btn(self.cmp1, True, x=150)
        self.after(500, lambda: self.animate_btn(self.cmp2, True, x=200))
        self.animate_btn(self.cmp3, True, x=250)
        self.after(500, lambda: self.animate_btn(self.cmp4, True, x=300))
        self.after(4000, self.animation_stop)

    def animate_btn(self, btn, up, height=20, x=50, new_y_position=None):
        if self.isstopped_animation == True: return
        if up:
            if (height == 150): up = not up
            height+=1
            new_y_position = 80 - (height - 20) / 2
            btn.configure(height=height)
            btn.place(x=x, y=new_y_position)
        else:
            if (height == 20): up = not up
            height-=1
            new_y_position = 80 - (height - 20) / 2
            btn.configure(height=height)
            btn.place(x=x, y=new_y_position)
            
        self.after(5, lambda: self.animate_btn(btn=btn, up=up, height=height, x=x, new_y_position=new_y_position))
    
    def animation_stop(self):
        self.isstopped_animation = True
        self.cmp1.configure(height=20)
        self.cmp1.place(x=150, y=80)
        self.cmp2.configure(height=20)
        self.cmp2.place(x=200, y=80)
        self.cmp3.configure(height=20)
        self.cmp3.place(x=250, y=80)
        self.cmp4.configure(height=20)
        self.cmp4.place(x=300, y=80)
        self.after(500, self.resetAnimation)

    def resetAnimation(self):
        self.isstopped_animation = False
    
    def save_audio(self, data):
        self.engine.save_to_file(data , "audio.mp3")
        self.engine.runAndWait()