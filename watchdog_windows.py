from pynput import mouse, keyboard
import os
import threading
import time
import winsound

monitoring = False

def lock_computer():
    print("Locking computer now.")
    os.system("rundll32.exe user32.dll,LockWorkStation")
    print("Script complete. You can now safely unlock your computer.")
    mouse_listener.stop()
    keyboard_listener.stop()

def on_click(x, y, button, pressed):
    global monitoring
    if pressed and not monitoring:
        print("Activation click detected. Monitoring will start in 10 seconds...")
        threading.Thread(target=start_monitoring_after_delay).start()

def start_monitoring_after_delay():
    global monitoring
    time.sleep(10)
    winsound.Beep(1000, 500)  # Frequency = 1000Hz, Duration = 500ms
    print("Monitoring started.")
    monitoring = True

def on_key_press(key):
    if monitoring:
        print("Key press detected. Locking...")
        lock_computer()

def on_mouse_move(x, y):
    if monitoring:
        print("Mouse movement detected. Locking...")
        lock_computer()

mouse_listener = mouse.Listener(on_click=on_click, on_move=on_mouse_move)
keyboard_listener = keyboard.Listener(on_press=on_key_press)

mouse_listener.start()
keyboard_listener.start()

mouse_listener.join()
keyboard_listener.join()