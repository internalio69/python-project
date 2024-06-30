import customtkinter as tk
from PIL import Image
from .register import RegisterForm, users
from pages.home import HomePage

class LoginForm:
    passViewHideImg = tk.CTkImage(light_image=Image.open('images/light/pass-view/hide.png'), dark_image=Image.open('images/dark/pass-view/hide.png'))
    passViewShowImg = tk.CTkImage(light_image=Image.open('images/light/pass-view/show.png'), dark_image=Image.open('images/dark/pass-view/show.png'))
    
    def __init__(self, window):
        self.window = window
        self.heading = None
        self.img = None
        self.entryUser = None
        self.entryPass = None

    def initialize(self):
        # defining window properties
        self.window.title("Login Form")
        
        if (self.heading == None):
            self.window.geometry("400x500+500+100")
            self.theme = tk.StringVar(value="dark")
            self.themeSwitch = tk.CTkSwitch(self.window, text="Dark", font=("Arial Bold", 15), variable=self.theme, onvalue="dark", offvalue="light", progress_color="black", command=self.switch_theme)
            self.themeSwitch.place(x=1, y=0)

        # load image
        if (self.img == None):
            self.img = tk.CTkImage(light_image=Image.open("images/user-light.png"), dark_image=Image.open("images/user-dark.png"), size=(100, 100))
            self.image_label = tk.CTkLabel(self.window, image=self.img, text="")
            self.image_label.pack(side="top", pady=30)
        
        # heading
        if (self.heading == None):
            self.heading = tk.CTkLabel(self.window, width=100, height=10, fg_color="transparent", text="Login to continue..", font=("Arial Bold", 20))
            self.heading.pack(side="top")
        else:
            self.heading.configure(text="Login to continue..")

        # credentials section
        if (self.entryUser == None):
            self.entryUser = tk.CTkEntry(self.window, width=250, height=30, corner_radius=5, fg_color=("#C7C7C7" , "#1D1D1D"), border_width=0, placeholder_text="Username", font=("Arial Bold", 14))
            self.entryUser.pack(side="top", pady=20)
        
        if (self.entryPass == None):
            self.entryPass = tk.CTkEntry(self.window, width=250, height=30, corner_radius=5, fg_color=("#C7C7C7" , "#1D1D1D"), border_width=0, placeholder_text="Password", show="*", font=("Arial Bold", 14))
            self.entryPass.pack(side="top", pady=2)
        else:
            self.passView.configure(command=self.toggle_pass_visibility)
        
        self.loginBtn = tk.CTkButton(self.window, text="Login", command=self.login_event, hover_color="#a632c9", fg_color="#9d12c7", font=("Arial", 13))
        self.loginBtn.pack(side="top", pady=20)

        # Password View Btn
        self.passView = tk.CTkButton(self.window, text="", image=self.passViewShowImg, command=self.toggle_pass_visibility, height=5, width=5, fg_color="transparent", hover_color=("#bfbfbf", "#1D1D1D"))
        self.passView.place(x=330, y=256)
        
        # signup prompt
        self.registerLabel1 = tk.CTkLabel(self.window, text="Don't have an account?", fg_color="transparent", font=("Arial", 13))
        self.registerLabel1.place(x=110, y=346)
        
        self.registerLabel2 = tk.CTkLabel(self.window, text="Sign Up", fg_color="transparent", text_color="#068dd1", font=("Arial Bold", 13), height=2)
        self.registerLabel2.bind("<Button-1>", self.signup_event)
        self.registerLabel2.place(x=246, y=351)
        
        # error labels
        self.errorLabel1 = tk.CTkLabel(self.window, text="", text_color="red", fg_color="transparent", height=2)
        self.errorLabel2 = tk.CTkLabel(self.window, text="", text_color="red", fg_color="transparent", height=2)
    
    def toggle_pass_visibility(self):
        if (self.entryPass.cget("show") == "*"):
            self.entryPass.configure(show="")
            self.passView.configure(image=self.passViewHideImg)
        else:
            self.entryPass.configure(show="*")
            self.passView.configure(image=self.passViewShowImg)

    def switch_theme(self):
        self.themeSwitch.configure(text=f"{self.themeSwitch.get().capitalize()}")
        tk.set_appearance_mode(self.themeSwitch.get())

    def login_event(self):
        self.errorLabel1.configure(text="")
        self.errorLabel2.configure(text="")
        
        if (self.entryUser.get() == "" or self.entryPass.get() == ""):
            self.errorLabel1.configure(text="Please enter credentials")
        elif (users.get(self.entryUser.get()) == None):
            self.errorLabel1.configure(text="User does not exist")
        elif (users.get(self.entryUser.get()) != self.entryPass.get()):
            self.errorLabel2.configure(text="Invalid Password")
        else:
            username = self.entryUser.get()
            self.heading.destroy()
            self.image_label.destroy()
            self.entryUser.destroy()
            self.entryPass.destroy()
            self.passView.destroy()
            self.loginBtn.destroy()
            self.errorLabel1.destroy()
            self.errorLabel2.destroy()
            self.registerLabel1.destroy()
            self.registerLabel2.destroy()
            HomePage(self.window, username).initialize()

            return
            
        self.errorLabel1.place(x=78, y=185)
        self.errorLabel2.place(x=78, y=239)

    def load_home_page(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        

        
    def signup_event(self, event):
        self.errorLabel1.destroy()
        self.errorLabel2.destroy()
        self.loginBtn.destroy()
        self.registerLabel1.destroy()
        self.registerLabel2.destroy()
        RegisterForm(self.window, self.heading, self.entryUser, self.entryPass, self.passView, self).initialize()