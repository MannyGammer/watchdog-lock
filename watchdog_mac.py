from pynput import mouse, keyboard
import subprocess
import threading
import time

monitoring = False

def lock_computer():
    print("Locking computer now.")
    try:
        subprocess.run(["pmset", "displaysleepnow"])
    except Exception as e:
        print(f"Failed to lock screen: {e}")
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
    print("\a")  # Terminal bell (may or may not beep)
    print("Monitoring active.")
    monitoring = True

def on_key_press(key):
    if monitoring:
        print("Key press detected. Locking...")
        lock_computer()

def on_mouse_move(x, y):
    if monitoring:
        print("Mouse movement detected. Locking...")
        lock_computer()

def main():
    global mouse_listener, keyboard_listener
    mouse_listener = mouse.Listener(on_click=on_click, on_move=on_mouse_move)
    keyboard_listener = keyboard.Listener(on_press=on_key_press)

    mouse_listener.start()
    keyboard_listener.start()

    mouse_listener.join()
    keyboard_listener.join()

if __name__ == "__main__":
    main()