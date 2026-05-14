import customtkinter as ctk

class Dashboard:
    def __init__(self, username):
        self.window = ctk.CTk()
        self.window.title("Life in Pixels")
        self.window.geometry("700x500")
        ctk.set_appearance_mode("light")

        self.title = ctk.CTkLabel(self.window, text=f"Hello, {username} ☀", font=ctk.CTkFont("Helvetica", 32, weight="bold"))
        self.title.pack(pady=40)

        self.subtitle = ctk.CTkLabel(self.window, text="Welcome back to Life in Pixels", font=("Helvetica", 18))
        self.subtitle.pack(pady=10)

        self.window.mainloop()

Dashboard("User")