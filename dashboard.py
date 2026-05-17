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
            "😄 Amazing": "#57cc99",
            "🙂 Good": "#3498db",
            "😐 Neutral": "#f1c40f",
            "😔 Bad": "#e74c3c",
            "😴 Tired": "#9b59b6"
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

        self.stats_label = ctk.CTkLabel(self.window, text="", font=("Helvetica", 16))
        self.stats_label.pack(pady=20)

        self.update_streak()
        self.generate_pixel_grid()
        self.update_stats()

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

        self.generate_pixel_grid()

        self.update_streak()
        self.update_stats()

    def generate_pixel_grid(self):
        for widget in self.pixel_frame.winfo_children():
            widget.destroy()

        if self.username not in self.moods:
            return
        
        user_moods = list(self.moods[self.username].items())
        row=0
        col=0

        for day, mood in user_moods:
            color = self.mood_options.get(mood, "gray")
            pixel = ctk.CTkFrame(self.pixel_frame, width=20, height=20, fg_color=color)
            pixel.grid(row=row, column=col, padx=2, pady=2)
            pixel.bind("<Enter>", lambda e, d=day, m=mood: self.status_label.configure(text=f"{d}: {m}"))
            pixel.bind("<Leave>", lambda e: self.status_label.configure(text=f"Saved today's mood: {mood}"))

            col += 1
            if col >= 7:
                col = 0
                row += 1

    def update_stats(self):
        if self.username not in self.moods:
            self.stats_label.configure(text="No mood data available.")
            return
        
        entries = len(self.moods[self.username])
        self.stats_label.configure(text=f"You have logged your mood for {entries} days.")

    def run(self):
        self.window.mainloop()