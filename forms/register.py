import customtkinter as tk
from PIL import Image

users = {"demo": "123"}

class RegisterForm():
    passViewHideImg = tk.CTkImage(light_image=Image.open('images/light/pass-view/hide.png'), dark_image=Image.open('images/dark/pass-view/hide.png'))
    passViewShowImg = tk.CTkImage(light_image=Image.open('images/light/pass-view/show.png'), dark_image=Image.open('images/dark/pass-view/show.png'))
    
    def __init__(self, window, heading, entryUser, entryPass, passView, loginForm):
        self.window = window
        self.heading = heading
        self.entryUser = entryUser
        self.entryPass = entryPass
        self.passView = passView
        self.loginForm = loginForm

    def initialize(self):
        # defining window properties
        self.window.title("Register Form")
        
        self.backBtn = tk.CTkButton(self.window, text="⬅", fg_color="#424242", width=30, border_spacing=5, border_width=3, border_color="#424242", hover_color="#575656", corner_radius=5, command=self.back, font=("Arial Bold", 10))
        self.backBtn.place(x=95, y=378)
        
        self.heading.configure(text="Register Yourself")
        self.passView.configure(command=self.toggle_pass_visibility)

        # credentials entry
        self.entryPassConf = tk.CTkEntry(self.window, width=250, height=30, corner_radius=5, fg_color=("#C7C7C7" , "#1D1D1D"), border_width=0, placeholder_text="Confirm Password", show="*", font=("Arial Bold", 14))
        self.entryPassConf.pack(side="top", pady=20)
        
        self.registerBtn = tk.CTkButton(self.window, text="Register", hover_color="#4cb569", fg_color="#32a852", font=("Arial", 13), command=self.register_event)
        self.registerBtn.pack(side="top", pady=20)
          
        # error labels
        self.errorLabel = tk.CTkLabel(self.window, text="", text_color="red", fg_color="transparent", height=2)
        self.successLabel = tk.CTkLabel(self.window, text="", text_color="green", fg_color="transparent", height=2)
        
    def register_event(self):
        self.errorLabel.configure(text="")
        self.successLabel.configure(text="")
        
        if (self.entryUser.get() == "" or self.entryPass.get() == "" or self.entryPassConf.get() == ""):
            self.errorLabel.configure(text="Please enter credentials")
        elif (users.get(self.entryUser.get()) != None):
            self.errorLabel.configure(text="User already exists")
        elif (self.entryPass.get() != self.entryPassConf.get()):
            self.errorLabel.configure(text="Passwords do not match!")
        else:
            users[self.entryUser.get()] = self.entryPassConf.get()
            self.successLabel.configure(text="Registered Successfully!")
        
        self.errorLabel.place(x=78, y=188)
        self.successLabel.place(x=78, y=188)
        
    def back(self):
        self.backBtn.destroy()
        self.entryPassConf.destroy()
        self.errorLabel.destroy()
        self.successLabel.destroy()
        self.registerBtn.destroy()
        self.loginForm.initialize()
    
    def toggle_pass_visibility(self):
        if (self.entryPass.cget("show") == "*"):
            self.entryPass.configure(show="")
            self.entryPassConf.configure(show="")
            self.passView.configure(image=self.passViewHideImg)
        else:
            self.entryPass.configure(show="*")
            self.entryPassConf.configure(show="*")
            self.passView.configure(image=self.passViewShowImg)