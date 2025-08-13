import tkinter as tk
from tkinter import font

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click-O-Meter")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        # Custom font
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.count_font = font.Font(family="Helvetica", size=36, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=12)

        # Main frame
        self.main_frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")

        # Header
        self.header_label = tk.Label(
            self.main_frame,
            text="Click Counter",
            font=self.title_font,
            bg="#f5f5f5",
            fg="#333"
        )
        self.header_label.pack(pady=(0, 20))

        # Counter display
        self.count = 0
        self.counter_display = tk.Label(
            self.main_frame,
            text=str(self.count),
            font=self.count_font,
            bg="#f5f5f5",
            fg="#4CAF50",
            width=5
        )
        self.counter_display.pack(pady=10)

        # Click button
        self.click_button = tk.Button(
            self.main_frame,
            text="CLICK ME!",
            font=self.button_font,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            padx=20,
            pady=10,
            command=self.increment_count
        )
        self.click_button.pack(pady=10, ipadx=10)

        # Reset button
        self.reset_button = tk.Button(
            self.main_frame,
            text="RESET",
            font=self.button_font,
            bg="#f44336",
            fg="white",
            activebackground="#d32f2f",
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            padx=20,
            pady=10,
            command=self.reset_count
        )
        self.reset_button.pack(pady=10, ipadx=10)

        # Stats label
        self.stats_label = tk.Label(
            self.main_frame,
            text="Stats will appear here",
            font=self.button_font,
            bg="#f5f5f5",
            fg="#666"
        )
        self.stats_label.pack(pady=(20, 0))

        # Hover effects
        self.click_button.bind("<Enter>", lambda e: self.click_button.config(bg="#45a049"))
        self.click_button.bind("<Leave>", lambda e: self.click_button.config(bg="#4CAF50"))
        self.reset_button.bind("<Enter>", lambda e: self.reset_button.config(bg="#d32f2f"))
        self.reset_button.bind("<Leave>", lambda e: self.reset_button.config(bg="#f44336"))

    def increment_count(self):
        self.count += 1
        self.update_display()
        self.update_stats()

    def reset_count(self):
        self.count = 0
        self.update_display()
        self.stats_label.config(text="Counter reset!")

    def update_display(self):
        self.counter_display.config(text=str(self.count))
        # Change color based on count
        if self.count == 0:
            self.counter_display.config(fg="#4CAF50")
        elif self.count % 10 == 0:
            self.counter_display.config(fg="#2196F3")
        else:
            self.counter_display.config(fg="#4CAF50")

    def update_stats(self):
        if self.count == 10:
            self.stats_label.config(text="Great! 10 clicks!")
        elif self.count == 25:
            self.stats_label.config(text="Awesome! 25 clicks!")
        elif self.count == 50:
            self.stats_label.config(text="Amazing! 50 clicks!")
        elif self.count == 100:
            self.stats_label.config(text="Legendary! 100 clicks!!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()
