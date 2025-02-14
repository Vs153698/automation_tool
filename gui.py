import tkinter as tk
from tkinter import filedialog, messagebox
import recorder
import player

class AutomationToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation Tool")

        self.record_button = tk.Button(root, text="Record", command=self.start_recording)
        self.record_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)

        self.play_button = tk.Button(root, text="Play", command=self.play_recording, state=tk.DISABLED)
        self.play_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(root, text="Save", command=self.save_recording, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT)

        self.load_button = tk.Button(root, text="Load", command=self.load_recording)
        self.load_button.pack(side=tk.LEFT)

        self.speed_label = tk.Label(root, text="Playback Speed (0.1 to 3.0):")
        self.speed_label.pack(side=tk.LEFT)

        self.speed_entry = tk.Entry(root, width=10)
        self.speed_entry.insert(0, "1.0")
        self.speed_entry.pack(side=tk.LEFT)

        self.actions = []

    def start_recording(self):
        recorder.start_recording()
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_recording(self):
        recorder.stop_recording()
        self.actions = recorder.actions
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.play_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)

    def play_recording(self):
        try:
            speed = float(self.speed_entry.get())
            if 0.1 <= speed <= 3.0:
                player.play_actions(self.actions, speed)
            else:
                messagebox.showerror("Invalid Input", "Please enter a value between 0.1 and 3.0.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def save_recording(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            recorder.save_actions(filename)

    def load_recording(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            self.actions = recorder.load_actions(filename)
            self.play_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = AutomationToolApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
