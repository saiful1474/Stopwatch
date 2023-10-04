import tkinter as tk
from time import time, strftime, gmtime, sleep
#from playsound import playsound  # Requires the 'playsound' library

# Create the main application window
app = tk.Tk()
app.title("Beautiful Stopwatch")
app.geometry("800x600")

# Create a colored background
background_color = "#3498db"
app.configure(bg=background_color)

# Create a label to display the time
time_label = tk.Label(app, font=('Helvetica', 100), bg=background_color, fg="white", text='00:00:00')
time_label.pack(pady=30)

# Create a list to store lap times
lap_times = []
lap_label = tk.Label(app, font=('Helvetica', 20), bg=background_color, fg="white", text='')
lap_label.pack()

# Stopwatch variables
start_time = None
running = False
elapsed_time = 0
lap_start_time = None

# Sound effect file (replace with your own sound file)
#sound_file = "beep.mp3"

# Keyboard shortcuts
def start(event=None):
    global start_time, running, elapsed_time, lap_start_time
    if not running:
        start_time = time() - (elapsed_time if start_time else 0)
        lap_start_time = time() - (elapsed_time if lap_start_time else 0)
        running = True
        update_time()

def stop(event=None):
    global running
    running = False

def reset(event=None):
    global start_time, running, elapsed_time, lap_start_time, lap_times
    start_time = None
    running = False
    elapsed_time = 0
    lap_start_time = None
    lap_times = []
    time_label.config(text='00:00:00')
    lap_label.config(text='')

def lap(event=None):
    global lap_start_time, lap_times
    if running:
        lap_time = time() - lap_start_time
        lap_times.append(lap_time)
        lap_start_time = time()
        lap_label.config(text=f"Lap {len(lap_times)}: {strftime('%H:%M:%S', gmtime(lap_time))}")
# Define a list to store lap times
lap_times = []

# Initialize lap_start_time as a global variable
lap_start_time = None

# Function to log lap times
def log_history():
    global lap_times, lap_start_time  # Declare lap_start_time as global
    if running:
        lap_time = time() - lap_start_time
        lap_times.append(lap_time)
        lap_start_time = time()
        lap_label.config(text=f"Lap {len(lap_times)}: {strftime('%H:%M:%S', gmtime(lap_time))}")

# Function to display lap time history
def display_log_history():
    global lap_times
    history_text.config(state=tk.NORMAL)  # Enable text widget for editing
    history_text.delete("1.0", tk.END)  # Clear existing text

    for i, lap_time in enumerate(lap_times, start=1):
        formatted_time = strftime('%H:%M:%S', gmtime(lap_time))
        history_text.insert(tk.END, f"Lap {i}: {formatted_time}\n")

    history_text.config(state=tk.DISABLED)  # Disable text widget for editing


app.bind("s", start)
app.bind("S", start)
app.bind("p", stop)
app.bind("P", stop)
app.bind("r", reset)
app.bind("R", reset)
app.bind("l", lap)
app.bind("L", lap)


# Sound effect function
#def play_sound():
#    playsound(sound_file)

# Create buttons with 3D appearance
button_color = "#e74c3c"
button_relief = "raised"  # You can use "ridge" for a different 3D effect

start_button = tk.Button(app, text="Start (S)", font=('Helvetica', 20), bg=button_color, fg="white", command=start, relief=button_relief)
stop_button = tk.Button(app, text="Stop (P)", font=('Helvetica', 20), bg=button_color, fg="white", command=stop, relief=button_relief)
reset_button = tk.Button(app, text="Reset (R)", font=('Helvetica', 20), bg=button_color, fg="white", command=reset, relief=button_relief)
lap_button = tk.Button(app, text="Lap (L)", font=('Helvetica', 20), bg=button_color, fg="white", command=lap, relief=button_relief)
#sound_button = tk.Button(app, text="Sound", font=('Helvetica', 20), bg=button_color, fg="white", command=play_sound, relief=button_relief)
log_button = tk.Button(app, text="Log Lap Times", font=('Helvetica', 20), bg=button_color, fg="white", command=log_history, relief=button_relief)
display_history_button = tk.Button(app, text="Display History", font=('Helvetica', 20), bg=button_color, fg="white", command=display_log_history, relief=button_relief)

# Pack the buttons as before
start_button.pack()
stop_button.pack()
reset_button.pack()
lap_button.pack()
#sound_button.pack()
log_button.pack()
display_history_button.pack()


# History log
history_log = []

def update_time():
    global start_time, elapsed_time
    if running:
        elapsed_time = time() - start_time
    else:
        elapsed_time = elapsed_time if start_time else 0

    # Format elapsed time as HH:MM:SS
    time_str = strftime('%H:%M:%S', gmtime(elapsed_time))
    time_label.config(text=time_str)
    time_label.after(1000, update_time)

# History log function
def log_history():
    global history_log, lap_times
    if lap_times:
        history_log.append(lap_times)
        lap_times = []

# Create a button to log lap times
#log_button = tk.Button(app, text="Log Lap Times", font=('Helvetica', 20), bg=button_color, fg="white", command=log_history)
#log_button.pack()

# Create a history log display area
history_text = tk.Text(app, font=('Helvetica', 12), height=10, width=40, bg=background_color, fg="white")
history_text.pack()

# Function to display history log
def display_history():
    global history_log
    history_text.delete("1.0", tk.END)
    for index, lap_set in enumerate(history_log, start=1):
        history_text.insert(tk.END, f"Lap Set {index}:\n")
        for i, lap_time in enumerate(lap_set, start=1):
            history_text.insert(tk.END, f"Lap {i}: {strftime('%H:%M:%S', gmtime(lap_time))}\n")
        history_text.insert(tk.END, "\n")

# Create a button to display history log
display_history_button = tk.Button(app, text="Display History", font=('Helvetica', 20), bg=button_color, fg="white", command=display_history)
display_history_button.pack()

# Start the Tkinter main loop
app.mainloop()
