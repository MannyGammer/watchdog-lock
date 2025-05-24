# 🛡️ Watchdog Lock

A simple cross-platform Python script to automatically lock your screen after detecting input when monitoring is active.

## 🖥️ Platform Versions

Choose the version that matches your OS:

- 🪟 `watchdog_windows.py` — Windows
- 🐧 `watchdog_linux.py` — Linux (GNOME-based environments)
- 🍎 `watchdog_mac.py` — macOS

## 🔧 How It Works

1. Run the script for your OS.
2. Click the mouse once — it will wait 10 seconds.
3. If keyboard or mouse activity is detected after that, the system locks.

> Use this to protect your workstation when stepping away or testing input lockdown.

## 📦 Requirements

- Python 3.x
- `pynput` package  
  Install with:  
  ```bash
  pip install pynput
