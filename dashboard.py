import customtkinter as ctk
from storage import load_moods, save_moods
from datetime import date

class Dashboard:
    def __init__(self, username):
        self.username = username
        self.window = ctk.CTk()
        self.window.title("Life in Pixels")
        self.window.geometry("700x500")
        ctk.set_appearance_mode("light")
        self.moods = load_moods()

        self.title = ctk.CTkLabel(self.window, text=f"Hello, {username} ☀", font=ctk.CTkFont("Helvetica", 32, weight="bold"))
        self.title.pack(pady=40)

        self.subtitle = ctk.CTkLabel(self.window, text="Welcome back to Life in Pixels", font=("Helvetica", 18))
        self.subtitle.pack(pady=10)

        self.mood_title = ctk.CTkLabel(self.window, text="How are you feeling today?", font=ctk.CTkFont("Helvetica", 20, weight="bold"))
        self.mood_title.pack(pady=20)

        self.mood_frame = ctk.CTkFrame(self.window)
        self.mood_frame.pack(pady=10)

        self.mood_options = {
            "😄 Amazing": "green",
            "🙂 Good": "blue",
            "😐 Neutral": "yellow",
            "😔 Bad": "red",
            "😴 Tired": "purple"
        }

        for mood in self.mood_options:
            button = ctk.CTkButton(self.mood_frame, text=mood, command=lambda m=mood: self.save_today_mood(m))
            button.pack(pady=5)

        self.window.mainloop()