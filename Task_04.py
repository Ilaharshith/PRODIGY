import msvcrt
import time
import os
from datetime import datetime

# Color codes for styled terminal output
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

# File to save keystrokes
LOG_FILE = "keystrokes_log.txt"

# Header
os.system("cls")
print(f"{BOLD}{BLUE}======== Windows Console Keylogger ========{RESET}")
print(f"{GREEN}Logging active... (Press ESC to stop){RESET}")
print(f"Saving to: {LOG_FILE}\n")

# Start logging
with open(LOG_FILE, "a") as log:
    log.write(f"\n--- Keylogging started at {datetime.now()} ---\n")

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()

            if key == b'\x1b':  # ESC key to exit
                print(f"\n{RED}Exiting... Logging stopped.{RESET}")
                log.write(f"\n--- Keylogging stopped at {datetime.now()} ---\n")
                break

            try:
                char = key.decode("utf-8")
                print(f"{BLUE}Captured: {GREEN}{char}{RESET}", end="", flush=True)
                log.write(char)
            except:
                # Special non-character key
                print(f"{BLUE}Captured special: {RED}{key}{RESET}")
                log.write(f"[{key}]")

        time.sleep(0.01)
