import keyboard
import time
import threading
import tkinter as tk

def simulate_key_press(key, interval, stop_event):
    while not stop_event.is_set():
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)
        time.sleep(interval)

def start_script():
    global stop_event, script_thread
    if not script_thread or not script_thread.is_alive():
        stop_event = threading.Event()
        script_thread = threading.Thread(target=simulate_key_press, args=('shift', 20, stop_event))
        script_thread.start()
        status_label.config(text="Status: Running")

def stop_script():
    global stop_event, script_thread
    if script_thread and script_thread.is_alive():
        stop_event.set()
        script_thread.join()
        status_label.config(text="Status: Stopped")

if __name__ == "__main__":
    stop_event = None
    script_thread = None

    window = tk.Tk()
    window.title("Keyboard Simulation")
    window.geometry("250x100")

    status_label = tk.Label(window, text="Status: Stopped")
    status_label.pack(pady=5)

    start_button = tk.Button(window, text="Start", command=start_script)
    start_button.pack(pady=5)

    stop_button = tk.Button(window, text="Stop", command=stop_script)
    stop_button.pack(pady=5)

    window.mainloop()
