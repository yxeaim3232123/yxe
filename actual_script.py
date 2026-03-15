import os
import ctypes
import time

# Set window title and clear screen
ctypes.windll.kernel32.SetConsoleTitleW("YXETweaks | Dev Lonware")
os.system('cls' if os.name == 'nt' else 'clear')

RED = "\033[91m"
RESET = "\033[0m"

# The Red Banner and Logo
print(RED + r"""
 __     __ __   __ ______ _______ _  _  _ _______ _______ _     _ _______
 \ \   / /  \ /  /|  ____|__   __| |  |  | |______ |_____| |____/  |______
  \ \_/ /    X    | |____   | |  |__|__|__| |______ |     | |    \_  ______|

                          DEV LONWARE EDITION
-------------------------------------------------------------------------""" + RESET)

def run_checker():
    steps = ["[+] Checking HWID...", "[+] Verifying License...", "[+] Connecting to Dev Server...", "[+] Optimizing Registry..."]
    for step in steps:
        print(step)
        time.sleep(0.6) # Creates that 'loading' feel from your video
    print(RED + "\n[!] SYSTEM OPTIMIZED & READY" + RESET)

run_checker()

# PASTE YOUR REAL MACRO LOGIC HERE
input("\nPress ENTER to close...")
