import customtkinter as ctk
from storage import load_moods, save_moods
from datetime import date

class Dashboard:
    def __init__(self, username):
        self.username = username
        self.window = ctk.CTkToplevel()
        self.window.title("Life in Pixels")
        self.window.geometry("600x600")
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

        self.status_label = ctk.CTkLabel(self.window, text="No mood logged today.", font=("Helvetica", 16))
        self.status_label.pack(pady=20)

        self.streak_label = ctk.CTkLabel(self.window, text="🔥 Streak: 0 days", font=("Helvetica", 18, "bold"))
        self.streak_label.pack(pady=10)

        self.pixel_title = ctk.CTkLabel(self.window, text="Your Mood in Pixels", font=ctk.CTkFont("Helvetica", 22, weight="bold"))
        self.pixel_title.pack(pady=20)

        self.pixel_frame = ctk.CTkFrame(self.window, fg_color="#1f1f1f")
        self.pixel_frame.pack(pady=10)

        self.update_streak()

    def update_streak(self):
        if self.username not in self.moods:
            return
        
        dates = sorted(self.moods[self.username].keys(),)
        streak = len(dates)
        self.streak_label.configure(text=f"🔥 Streak: {streak} days")

    def save_today_mood(self, mood):
        today = str(date.today())
        if self.username not in self.moods:
            self.moods[self.username] = {}

        self.moods[self.username][today] = mood
        save_moods(self.moods)

        self.status_label.configure(
            text=f"Saved today's mood: {mood}"
        )

        self.update_streak()

    def run(self):
        self.window.mainloop()