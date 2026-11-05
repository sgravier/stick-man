import random
import tkinter as tk

class CirclePopGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pop the Circles!")
        self.root.geometry("700x500")
        self.root.configure(bg="#f4f1ff")

        self.score = 0
        self.time_left = 30
        self.playing = False

        self.score_var = tk.StringVar(value="0")
        self.time_var = tk.StringVar(value="30")
        self.message_var = tk.StringVar(value="Press Start to play")

        top = tk.Frame(root, bg="#f4f1ff", pady=10)
        top.pack(fill="x")

        tk.Label(top, text="Score:", font=("Arial", 16, "bold"), bg="#f4f1ff").pack(side="left", padx=(20, 5))
        tk.Label(top, textvariable=self.score_var, font=("Arial", 16, "bold"), bg="#f4f1ff").pack(side="left")
        tk.Label(top, text="Time:", font=("Arial", 16, "bold"), bg="#f4f1ff").pack(side="left", padx=(30, 5))
        tk.Label(top, textvariable=self.time_var, font=("Arial", 16, "bold"), bg="#f4f1ff").pack(side="left")

        self.canvas = tk.Canvas(root, width=650, height=380, bg="white", highlightthickness=3, highlightbackground="#d9d2ff", bd=0)
        self.canvas.pack(padx=20, pady=10)

        controls = tk.Frame(root, bg="#f4f1ff", pady=10)
        controls.pack()

        self.start_button = tk.Button(controls, text="Start Game", font=("Arial", 14, "bold"), bg="#6f59ec", fg="white", padx=18, pady=8, command=self.start_game)
        self.start_button.pack(side="left", padx=10)

        self.quit_button = tk.Button(controls, text="Quit", font=("Arial", 12), bg="#e8e3ff", padx=16, pady=6, command=root.destroy)
        self.quit_button.pack(side="left", padx=10)

        tk.Label(root, textvariable=self.message_var, font=("Arial", 12), bg="#f4f1ff", fg="#4a4477").pack(pady=(0, 10))

        self.spawn_job = None
        self.tick_job = None

    def start_game(self):
        self.score = 0
        self.time_left = 30
        self.playing = True
        self.score_var.set("0")
        self.time_var.set("30")
        self.message_var.set("Pop the circles!")

        self.canvas.delete("all")
        self.start_button.config(state="disabled")

        if self.tick_job is not None:
            self.root.after_cancel(self.tick_job)
        if self.spawn_job is not None:
            self.root.after_cancel(self.spawn_job)

        self.tick_job = self.root.after(1000, self.countdown)
        self.spawn_circle()

    def countdown(self):
        if not self.playing:
            return

        self.time_left -= 1
        self.time_var.set(str(self.time_left))

        if self.time_left <= 0:
            self.end_game()
            return

        self.tick_job = self.root.after(1000, self.countdown)

    def spawn_circle(self):
        if not self.playing:
            return

        radius = random.randint(18, 42)
        x = random.randint(radius, self.canvas.winfo_width() - radius)
        y = random.randint(radius, self.canvas.winfo_height() - radius)
        color = random.choice(["#ff6b6b", "#ffa94d", "#82c91e", "#4dabf7", "#845ef7", "#f06595"])

        circle = self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=color, outline="#333333", width=2
        )

        self.canvas.tag_bind(circle, "<Button-1>", self.pop_circle)

        delay = random.randint(500, 1200)
        self.spawn_job = self.root.after(delay, self.spawn_circle)

    def pop_circle(self, event):
        if not self.playing:
            return

        item = event.widget.find_closest(event.x, event.y)
        if item:
            self.canvas.delete(item[0])
            self.score += 1
            self.score_var.set(str(self.score))
            self.message_var.set("Nice! Keep going!")

    def end_game(self):
        self.playing = False
        self.canvas.delete("all")
        self.message_var.set(f"Time's up! You popped {self.score} circles.")
        self.start_button.config(state="normal")

        if self.spawn_job is not None:
            self.root.after_cancel(self.spawn_job)
            self.spawn_job = None

        if self.tick_job is not None:
            self.root.after_cancel(self.tick_job)
            self.tick_job = None

if __name__ == "__main__":
    root = tk.Tk()
    app = CirclePopGame(root)
    root.mainloop()