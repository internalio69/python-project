import customtkinter as tk
from PIL import Image
import speedtest

class SpeedTest:
    def __init__(self, window, home):
        self.window = window
        self.home = home
        
    def initialize(self):
        self.window.title("Internet Speed Test")
        self.window.grid_rowconfigure(0, weight=1, uniform='a')
        self.window.grid_columnconfigure(0, weight=1, uniform='a')

        self.my_frame1 = Frame1(master=self.window, home=self.home)
        self.my_frame1.grid(row=0, column=0, columnspan=2, padx=20, pady=30, sticky="nsew")

class Frame1(tk.CTkFrame):
    green_st_img=Image.open('images/speedtest/speedtest_icon_green.png')
    yellow_st_img=Image.open('images/speedtest/speedtest_icon_yellow.png')
    red_st_img=Image.open('images/speedtest/speedtest_icon_red.png')
    go_st_img=Image.open('images/speedtest/go.png')
    go_org_st_img=Image.open('images/speedtest/go_org.png')
    font_data=("Arial Bold", 15)
    result_declared=False

    def __init__(self, master, home, **kwargs):
        super().__init__(master, **kwargs)
        self.home = home
        self.columnconfigure((0,1), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3), weight=1, uniform='a')

        self.backBtn = tk.CTkButton(self, text="⬅", fg_color="#424242", width=30, border_spacing=5, border_width=3, border_color="#424242", hover_color="#575656", corner_radius=5, font=("Arial Bold", 10), command=self.back)
        self.backBtn.place(x=225, y=13)
        self.heading = tk.CTkLabel(self, text="• Internet Speed Test", width=120, height=35, font=("Arial Bold", 20), corner_radius=5, fg_color=("#C7C7C7", "#1D1D1D"))
        self.heading.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        
        self.downloadImg = tk.CTkImage(light_image=self.yellow_st_img, size=(100, 100))
        self.downloadImgLabel = tk.CTkLabel(self, text="___", font=self.font_data, image=self.downloadImg)
        self.downloadLabel = tk.CTkLabel(self, text="Download Speed", font=self.font_data, height=3)
        self.downloadLabel.grid(row=1, column=0, sticky='n')
        self.downloadImgLabel.grid(row=1, column=0, sticky='s', ipady=20)

        self.uploadImg = tk.CTkImage(light_image=self.yellow_st_img, size=(100, 100))
        self.uploadImgLabel = tk.CTkLabel(self, text="___", font=self.font_data, image=self.uploadImg)
        self.uploadLabel = tk.CTkLabel(self, text="Upload Speed", font=self.font_data, height=3)
        self.uploadLabel.grid(row=1, column=0, columnspan=2, sticky='n')
        self.uploadImgLabel.grid(row=1, column=0, columnspan=2, sticky='s', ipady=10)

        self.pingImg = tk.CTkImage(light_image=self.yellow_st_img, size=(100, 100))
        self.pingImgLabel = tk.CTkLabel(self, text="___", font=self.font_data, image=self.pingImg)
        self.pingLabel = tk.CTkLabel(self, text="Ping", font=self.font_data, height=3)
        self.pingLabel.grid(row=1, column=1, sticky='n')
        self.pingImgLabel.grid(row=1, column=1, rowspan=1, sticky='s', ipady=10)

        self.divider = tk.CTkLabel(self, text="_____________________________________________________________________", text_color="#4D4D4D")
        self.divider.place(x=280, y=250)

        self.goBtnImg = tk.CTkImage(light_image=self.go_st_img, size=(200, 200))
        self.goLabel = tk.CTkLabel(self, image=self.goBtnImg, text="", font=("Arial Bold", 20), corner_radius=20, fg_color=("#C7C7C7", "#1D1D1D"))
        self.goLabel.grid(row=3, rowspan=2, column=0, columnspan=2, pady=5, ipady=13)
        self.goLabel.bind("<Button-1>", self.start_speedtest)
    
    def start_speedtest(self, event):
        if (self.result_declared):
            self.downloadImg.configure(light_image=self.yellow_st_img)
            self.downloadImgLabel.configure(text="___")
            self.uploadImg.configure(light_image=self.yellow_st_img)
            self.uploadImgLabel.configure(text="___")
            self.pingImg.configure(light_image=self.yellow_st_img)
            self.pingImgLabel.configure(text="___")
        self.goBtnImg.configure(light_image=self.go_org_st_img)
        self.goLabel.configure(text="Loading...")
        self.after(500, self.speed)
    
    def speed(self):
        st = speedtest.Speedtest()
        download = round(st.download() / (1024 * 1024), 2)
        upload = round(st.upload() / (1024 * 1024), 2)
        ping = round(st.results.ping, 1)

        self.downloadImgLabel.configure(text=f"{download}\nMbps")
        if (download < 15):
            self.downloadImg.configure(light_image=self.red_st_img)
        elif (download < 25):
            self.downloadImg.configure(light_image=self.yellow_st_img)
        else:
            self.downloadImg.configure(light_image=self.green_st_img)

        self.uploadImgLabel.configure(text=f"{upload}\nMbps")
        if (upload < 15):
            self.uploadImg.configure(light_image=self.red_st_img)
        elif (upload < 25):
            self.uploadImg.configure(light_image=self.yellow_st_img)
        else:
            self.uploadImg.configure(light_image=self.green_st_img)


        self.pingImgLabel.configure(text=f"{ping}\nms")
        if (ping < 10):
            self.pingImg.configure(light_image=self.green_st_img)
        elif (ping < 20):
            self.pingImg.configure(light_image=self.yellow_st_img)
        else:
            self.pingImg.configure(light_image=self.red_st_img)
        
        self.goBtnImg.configure(light_image=self.go_st_img)
        self.goLabel.configure(text="")
        self.result_declared=True

    def back(self):
        self.destroy()
        self.home.initialize()