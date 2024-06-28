import customtkinter as tk
from PIL import Image

class LoginForm:
    
    users = {}
    
    def __init__(self, window):
        self.window = window
        self.img = None

    def initialize(self):
        # defining window properties
        self.window.title("Login Form")
        self.window.geometry("400x500+500+100")
        
        # load image
        if (self.img == None):
            self.img = tk.CTkImage(light_image=Image.open("images/user.png"), size=(100, 100))
            self.image_label = tk.CTkLabel(self.window, image=self.img, text="")
            self.image_label.pack(side="top", pady=30)
        
        # credentials entry
        self.entryUser = tk.CTkEntry(self.window, width=250, height=30, corner_radius=5, border_width=1, bg_color="transparent", border_color="#ffffff", text_color="white", placeholder_text="Username", font=("Arial Bold", 14))
        self.entryUser.pack(side="top", pady=20)
        
        self.entryPass = tk.CTkEntry(self.window, width=250, height=30, corner_radius=5, border_width=1, bg_color="transparent", border_color="#ffffff", text_color="white", placeholder_text="Password", show="*", font=("Arial Bold", 14))
        self.entryPass.pack(side="top", pady=2)
        
        self.passViewBtn = tk.CTkButton(self.window, command=self.toggle_pass_visibility, fg_color="transparent", text="V", width=2, height=2)
        self.passViewBtn.place(x=330, y=242)
        
        self.loginBtn = tk.CTkButton(self.window, text="Login", command=self.login_event, hover_color="#a632c9", fg_color="#9d12c7")
        self.loginBtn.pack(side="top", pady=20)
        
        # signup prompt
        self.registerLabel1 = tk.CTkLabel(self.window, text="Don't have an account?", fg_color="transparent")
        self.registerLabel1.place(x=110, y=336)
        
        self.registerLabel2 = tk.CTkLabel(self.window, text="Sign Up", fg_color="transparent", text_color="#068dd1", font=("Arial Bold", 13))
        self.registerLabel2.bind("<Button-1>", self.signup_event)
        self.registerLabel2.place(x=244, y=335)
        
        # error labels
        self.errorLabel1 = tk.CTkLabel(self.window, text="", text_color="red", fg_color="transparent", height=2)
        self.errorLabel2 = tk.CTkLabel(self.window, text="", text_color="red", fg_color="transparent", height=2)
    
    def toggle_pass_visibility(self):
        if (self.entryPass.cget("show") == "*"):
            self.entryPass.configure(show="")
        else:
            self.entryPass.configure(show="*")

    def login_event(self):
        self.errorLabel1.configure(text="")
        self.errorLabel2.configure(text="")
        
        if (self.entryUser.get() == "" or self.entryPass.get() == ""):
            self.errorLabel1.configure(text="Please enter credentials")
        elif (self.users.get(self.entryUser.get()) == None):
            self.errorLabel1.configure(text="User does not exist")
        elif (self.users.get(self.entryUser.get()) != self.entryPass.get()):
            self.errorLabel2.configure(text="Invalid Password")
            
        self.errorLabel1.place(x=78, y=160)
        self.errorLabel2.place(x=78, y=214)
        
    def signup_event(self, event):
        self.entryUser.destroy()
        self.entryPass.destroy()
        self.errorLabel1.destroy()
        self.errorLabel2.destroy()
        self.loginBtn.destroy()
        self.registerLabel1.destroy()
        self.registerLabel2.destroy()
        RegisterForm(self.window, self).initialize()

class RegisterForm(LoginForm):
    
    def __init__(self, window, loginForm):
        self.window = window
        self.loginForm = loginForm

    def initialize(self):
        # defining window properties
        self.window.title("Register Form")
        
        self.backBtn = tk.CTkButton(self.window, text="⬅", fg_color="#424242", width=30, height=30, border_spacing=5, border_width=3, border_color="#424242", hover_color="#575656", corner_radius=5, command=self.back)
        self.backBtn.place(x=3, y=3)
        
        # credentials entry
        self.entryUser = tk.CTkEntry(self.window, width=250, height=30, corner_radius=5, border_width=1, bg_color="transparent", border_color="#ffffff", text_color="white", placeholder_text="Username", font=("Arial Bold", 14))
        self.entryUser.pack(side="top", pady=5)
        
        self.entryPass = tk.CTkEntry(self.window, width=250, height=30, corner_radius=5, border_width=1, bg_color="transparent", border_color="#ffffff", text_color="white", placeholder_text="Password", font=("Arial Bold", 14))
        self.entryPass.pack(side="top", pady=5)
        self.entryPassConf = tk.CTkEntry(self.window, width=250, height=30, corner_radius=5, border_width=1, bg_color="transparent", border_color="#ffffff", text_color="white", placeholder_text="Confirm Password", font=("Arial Bold", 14))
        self.entryPassConf.pack(side="top", pady=5)
        
        self.registerBtn = tk.CTkButton(self.window, text="Register", hover_color="#4cb569", fg_color="#32a852", command=self.register_event)
        self.registerBtn.pack(side="top", pady=20)
          
        # error labels
        self.errorLabel = tk.CTkLabel(self.window, text="", text_color="red", fg_color="transparent", height=2)
        self.successLabel = tk.CTkLabel(self.window, text="", text_color="green", fg_color="transparent", height=2)
        
    def register_event(self):
        self.errorLabel.configure(text="")
        self.successLabel.configure(text="")
        
        if (self.entryUser.get() == "" or self.entryPass.get() == "" or self.entryPassConf.get() == ""):
            self.errorLabel.configure(text="Please enter credentials")
        elif (self.users.get(self.entryUser.get()) != None):
            self.errorLabel.configure(text="User already exists")
        elif (self.entryPass.get() != self.entryPassConf.get()):
            self.errorLabel.configure(text="Passwords do not match!")
        else:
            self.users[self.entryUser.get()] = self.entryPassConf.get()
            self.successLabel.configure(text="Registered Successfully!")
        
        self.errorLabel.place(x=78, y=145)
        self.successLabel.place(x=78, y=145)
        
    def back(self):
        self.backBtn.destroy()
        self.entryUser.destroy()
        self.entryPass.destroy()
        self.entryPassConf.destroy()
        self.errorLabel.destroy()
        self.successLabel.destroy()
        self.registerBtn.destroy()
        self.loginForm.initialize()
        
tk.set_appearance_mode("system")
app = tk.CTk()
LoginForm(app).initialize()

def print_click_coordinates(event):
    x, y = event.x, event.y
    print(f"Mouse clicked at: ({x}, {y})")

# app.bind("<Button-1>", print_click_coordinates)


app.mainloop()