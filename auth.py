import customtkinter as ctk
import bcrypt
from storage import load_users, save_users
from dashboard import Dashboard

class Auth:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Life in Pixels - Login")
        self.window.geometry("600x600")
        ctk.set_appearance_mode("light")

        self.users = load_users()

        self.title = ctk.CTkLabel(self.window, text="Life in Pixels", font=ctk.CTkFont("Helvetica", 32, "bold"))
        self.title.pack(pady=40)

        self.username_entry = ctk.CTkEntry(self.window, placeholder_text="Username", width=250)
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.window, placeholder_text="Password", width=250, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self.window, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.register_button = ctk.CTkButton(self.window, text="Create Account", command=self.register)
        self.register_button.pack(pady=10)
        
        self.message = ctk.CTkLabel(self.window, text="")
        self.message.pack(pady=20)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users:
            self.message.configure(text="User already exists!", text_color="red")
            return
        
        if username == "" or password == "":
            self.message.configure(text="Please fill in all fields!", text_color="red")
            return
        
        if len(password) < 6:
            self.message.configure(text="Password must be at least 6 characters!", text_color="red")
            return
        
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.users[username] = {"password": hashed_password}
        save_users(self.users)

        self.message.configure(text="Account created! Please log in.", text_color="green")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username not in self.users:
            self.message.configure(text="User not found!", text_color="red")
            return
        
        stored_password = self.users[username]["password"].encode()

        if not bcrypt.checkpw(password.encode(), stored_password):
            self.message.configure(text="Incorrect password!", text_color="red")
            return
        
        self.window.after(50, lambda: self.open_dashboard(username))

    def open_dashboard(self, username):
        self.window.destroy()
        dashboard = Dashboard(username)
        dashboard.run()

    def run(self):
        self.window.mainloop()