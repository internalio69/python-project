import customtkinter as tk
from forms.login import LoginForm
from pages.home import HomePage
        
app = tk.CTk()

# configuration
tk.set_appearance_mode("dark")
app.iconbitmap("images/icon.ico")
app.resizable(False, False)

# bg = ("#ebebeb", "#1D1D1D")
# primary = #("#D9D9D9" , "#1D1D1D")
# secondary = ("#CBCBCB", "#161616")

# initiate login form
#LoginForm(app).initialize()
HomePage(app, "Aaron").initialize()

# print coordinates on click
def print_click_coordinates(event):
    x, y = event.x, event.y
    print(f"Mouse clicked at: ({x}, {y})")

app.bind("<Button-1>", print_click_coordinates)


app.mainloop()