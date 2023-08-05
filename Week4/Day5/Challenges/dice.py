import random
import tkinter as tk
from tkinter import ttk
import time


class DiceRollSimulation:
    def __init__(self, window):
        self.window = window
        self.window.title("Dice Rolling Simulation")
        self.window.geometry("400x350")

        self.result_label = ttk.Label(self.window, text="6:6 Occurrences: 0\nTotal Rolls: 0\n")
        self.result_label.pack(pady=10)

        self.result_label2 = ttk.Label(self.window, text="Avg 6:6:\n0.0000", font=("Helvetica", 18))
        self.result_label2.pack(pady=0)

        self.stats_label = ttk.Label(self.window, text="")
        self.stats_label.pack()

        self.paused = tk.BooleanVar()
        self.paused.set(False)

        self.started = tk.BooleanVar()
        self.started.set(False)

        self.start_button = ttk.Button(self.window, text="Start", command=self.start)
        self.start_button.pack()

        self.pause_button = ttk.Button(self.window, text="Pause/Resume", command=self.pause_resume)
        self.pause_button.pack()

        self.restart_button = ttk.Button(self.window, text="Restart", command=self.restart)
        self.restart_button.pack()

        self.timer_label = ttk.Label(self.window, text="Elapsed Time: 00:00:00")
        self.timer_label.pack(pady=10)

        self.count_66 = 0
        self.count_per_roll = []
        self.total_rolls = 0
        self.start_time = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def update_labels(self):
        if not self.paused.get() and self.started.get():
            dice1, dice2 = self.roll_dice(), self.roll_dice()
            self.count_66 += int(dice1 == 6 and dice2 == 6)
            self.count_per_roll.append((dice1, dice2))
            self.total_rolls = len(self.count_per_roll)
            avg_66 = self.total_rolls / self.count_66 if self.count_66 > 0 else 0

            self.result_label.config(text=f"6:6 Occurrences: {self.count_66}\nTotal Rolls: {self.total_rolls}\n")
            self.result_label2.config(text=f"Avg 6:6:\n{avg_66:.4f}")

            if round(avg_66) == 36:
                self.result_label2.config(foreground="red", font=("Helvetica", 22))
                self.stats_label.config(text="Just enough.", foreground="red", font=("Helvetica", 22))
            else:
                self.result_label2.config(foreground="black")
            if avg_66 >= 37:
                self.stats_label.config(text="Need MORE doubles", foreground="black", font=("Helvetica", 18))
            elif avg_66 <= 35:
                self.stats_label.config(text="Need LESS doubles", foreground="black", font=("Helvetica", 18))

        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Elapsed Time: {self.format_time(elapsed_time)}")

        self.window.update_idletasks()
        self.window.after(10, self.update_labels)

    def pause_resume(self):
        self.paused.set(not self.paused.get())

    def restart(self):
        self.count_66 = 0
        self.count_per_roll = []
        self.total_rolls = 0
        self.start_time = time.time()

        self.result_label.config(text="6:6 Occurrences: 0\nTotal Rolls: 0\n")
        self.result_label2.config(text="Avg 6:6:\n0.0000", foreground="black", font=("Helvetica", 18))
        self.timer_label.config(text="Elapsed Time: 00:00:00")

    def start(self):
        if not self.started.get():
            self.started.set(True)
            self.start_time = time.time()
            self.update_labels()


if __name__ == "__main__":
    window = tk.Tk()
    dice_simulation = DiceRollSimulation(window)
    window.mainloop()
