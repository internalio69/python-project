import customtkinter as tk
from PIL import Image,ImageFilter
import qrcode

class QRCode:
    def __init__(self, window, home):
        self.window = window
        self.home = home
        
    def initialize(self):
        self.window.title("QR Code Generator")
        self.window.grid_rowconfigure(0, weight=1, uniform='a')
        self.window.grid_columnconfigure((0,1), weight=1, uniform='a')

        self.my_frame2 = Frame2(master=self.window)
        self.my_frame1 = Frame1(master=self.window, frame2=self.my_frame2)
        self.my_frame1.grid(row=0, column=0, padx=20, pady=30, sticky="nsew")
        self.my_frame2.grid(row=0, column=1, padx=20, pady=30, sticky="nsew")

        self.backBtn = tk.CTkButton(self.window, text="⬅", fg_color="#424242", width=30, border_spacing=5, border_width=3, border_color="#424242", hover_color="#575656", corner_radius=5, font=("Arial Bold", 10), command=self.back)
        self.backBtn.place(x=225, y=42)
    
    def back(self):
        self.my_frame1.destroy()
        self.my_frame2.destroy()
        self.backBtn.destroy()
        self.home.initialize()

class Frame1(tk.CTkFrame):
    colours=("Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White")
    font_data=("Arial Bold", 15)
    font_data2=("Arial Bold", 13)
    qr_data=None
    def __init__(self, master, frame2, **kwargs):
        super().__init__(master, **kwargs)
        
        self.frame2 = frame2
        self.qr_version=tk.IntVar(master, 1)
        self.qr_ec=tk.IntVar(master, 0)
        self.qr_bac=tk.StringVar(master, "white")
        self.qr_fc=tk.StringVar(master, "black")
        self.columnconfigure((0,1), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='a')
        
        self.heading = tk.CTkLabel(self, text="• QRCode Settings", width=120, height=35, font=("Arial Bold", 20), corner_radius=5, fg_color=("#C7C7C7", "#1D1D1D"))
        self.heading.grid(row=0, column=0, padx=10, pady=10, sticky="nws")
        
        self.data_label = tk.CTkLabel(self, text="Data:", font=self.font_data)
        self.data_label.grid(row=1, column=0, padx=5, pady=1, sticky="nsw")

        self.errorlabel = tk.CTkLabel(self, text="", text_color="red", fg_color="transparent", height=2)
        self.errorlabel.grid(row=0, column=0, padx=10, pady=10, sticky="w", rowspan=2)

        self.qr_data = tk.CTkEntry(self, width=440, height=30, font=self.font_data, corner_radius=5, fg_color=("#B6B6B6", "#161616"), placeholder_text="Enter some data...")
        self.qr_data.grid(row=2, column=0, padx=10, pady=0, sticky="nsew", columnspan=2)
        
        self.divider = tk.CTkLabel(self, text="_____________________________________________________________________", text_color="#4D4D4D")
        self.divider.grid(row=3, column=0, columnspan=2)

        self.ver_label = tk.CTkLabel(self, text="Version:", font=self.font_data)
        self.ver_label.grid(row=4, column=0, padx=10, pady=1, sticky="nsw")
        self.ver_slider = tk.CTkSlider(self, from_=1, to=40, number_of_steps=40, progress_color="#A526B6", button_color="#8A0F5E", hover=False, variable=self.qr_version)
        self.ver_slider.set(1)
        self.ver_slider.grid(row=5, column=0, sticky="nw", padx=10)
        
        self.ec_label = tk.CTkLabel(self, text="Error Correction:", font=self.font_data)
        self.ec_label.grid(row=4, column=1, padx=10, pady=1, sticky="nsw")
        self.ec_slider = tk.CTkSlider(self, from_=0, to=3, number_of_steps=4, progress_color="#A526B6", button_color="#8A0F5E", hover=False, variable=self.qr_ec)
        self.ec_slider.set(0)
        self.ec_slider.grid(row=5, column=1, sticky="nw", padx=10)
        
        self.fc_label = tk.CTkLabel(self, text="Fill Colour:", font=self.font_data)
        self.fc_label.grid(row=6, column=0, padx=5, pady=1, sticky="nsw")
        self.fc_Options = tk.CTkOptionMenu(self, values=self.colours, button_color="#0F5B8A", fg_color="#0F5B8A", font=self.font_data2, variable=self.qr_fc)
        self.fc_Options.grid(row=7, column=0, padx=10, pady=0, sticky="wn", columnspan=2)
        
        self.bac_label = tk.CTkLabel(self, text="Back Colour:", font=self.font_data)
        self.bac_label.grid(row=6, column=1, padx=5, pady=1, sticky="nsw")
        self.bac_Options = tk.CTkOptionMenu(self, values=self.colours, button_color="#0F5B8A", fg_color="#0F5B8A", font=self.font_data2, variable=self.qr_bac)
        self.bac_Options.grid(row=7, column=1, padx=10, pady=0, sticky="wn", columnspan=2)

        self.divider = tk.CTkLabel(self, text="_____________________________________________________________________", text_color="#4D4D4D")
        self.divider.grid(row=8, column=0, columnspan=2)

        self.generate_btn = tk.CTkButton(self, font=self.font_data, fg_color="#01A506", text="⚙ Generate QRCode", width=30, height=30, command=self.generate_qrcode, hover_color="#14B218")
        self.generate_btn.grid(row=9, column=0, columnspan=2)

    def generate_qrcode(self):
        data = self.qr_data.get()
        if (data == ""):
            return self.errorlabel.configure(text="Please enter qrcode data!")
        else:
            self.errorlabel.configure(text="")

        ec = None

        if (self.qr_ec.get() == 0):
            ec = qrcode.constants.ERROR_CORRECT_L
        elif (self.qr_ec.get() == 1):
            ec = qrcode.constants.ERROR_CORRECT_M
        elif (self.qr_ec.get() == 2):
            ec = qrcode.constants.ERROR_CORRECT_Q
        elif (self.qr_ec.get() == 3):
            ec = qrcode.constants.ERROR_CORRECT_H

        qr = qrcode.QRCode(version=self.qr_version.get(), error_correction=ec)
        qr.add_data(data)
        self.img = qr.make_image(fill_color=self.qr_fc.get(), back_color=self.qr_bac.get())
        self.img.save('QRCode.png')
        Frame2.load_qrcode(self.frame2, data, self.qr_bac.get(), self.img)

class Frame2(tk.CTkFrame):
    font_data=("Arial Bold", 15)
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.rowconfigure((0,1,2), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='a')

        self.heading = tk.CTkLabel(self, text="• Generated Result", width=120, height=35, font=("Arial Bold", 20), corner_radius=5, fg_color=("#C7C7C7", "#1D1D1D"))
        self.heading.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.qrcode_data_text = tk.CTkLabel(self, text="No Generated QRCodes", width=200, height=40, font=self.font_data, corner_radius=5, fg_color=("#C7C7C7", "#1D1D1D"))
        self.qrcode_data_text.grid(row=0, sticky="s", pady=10)

        self.saveas_btn = tk.CTkButton(self, font=self.font_data, text="⬇ Save As", width=30, height=30, command=self.saveas_qrcode, hover=False, fg_color="#9026B6")
    
    @staticmethod
    def load_qrcode(self, data, fc, img):
        self.img = img
        self.qrcode_data_text.configure(text=f"Data: {data}")
        img1 = Image.open('QRCode.png').convert('RGB')
        self.qrcode_ctkimg = tk.CTkImage(light_image=img1.filter(ImageFilter.GaussianBlur(20)), size=(200,200))
        self.qrcode_img_btn = tk.CTkButton(self, text="", image=self.qrcode_ctkimg, fg_color=fc, width=300, height=300, border_color=("#B6B6B6", "#161616"), border_width=3, hover=False)
        self.qrcode_img_btn.grid(row=1, sticky="n", rowspan=2)
        self.saveas_btn.grid(row=2, column=0, columnspan=2, sticky="s", pady=20)

        def remove_gaussian_blur():
            self.qrcode_ctkimg = tk.CTkImage(light_image=Image.open('QRCode.png'), size=(200,200))
            self.qrcode_img_btn.configure(image=self.qrcode_ctkimg)

        self.after(1000, remove_gaussian_blur)

    def saveas_qrcode(self):
        file = tk.filedialog.asksaveasfile(filetypes=[("Portable Network Graphics (PNG)", ".png")], mode='wb', defaultextension=".png", initialfile="QRCode.png")
        if file:
            self.img.save(file)
            file.close()