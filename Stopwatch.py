import tkinter as tk
import time

class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Stopwatch")
        self.geometry("400x300")

        self.time = 0.0
        self.running = False
        self.seconds = tk.StringVar()
        self.seconds.set("0.0")

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.label = tk.Label(self, textvariable=self.seconds)
        self.label.pack()

    def start(self):
        self.running = True
        self.time = time.time()
        self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.time = 0.0
        self.seconds.set("0.0")

    def update_time(self):
        if self.running:
            self.seconds.set("%.1f" % (time.time() - self.time))
            self.after(10, self.update_time)

if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.mainloop()


'''
the main loop of the Stopwatch class and mainloop function call so the app runs. The class has Start, Stop, Reset button,
a label that displays the time, and three functions for each button, start, stop and reset. The start function starts
the clock and calls the update_time() function, stop function stops the clock and reset function resets the clock to 0.0.
The update_time function uses the time module of python to get the current time, subtract it from the time the stopwatch
started and set the label text to the time elapsed.
'''