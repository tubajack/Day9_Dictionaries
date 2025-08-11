# In this file I will be writing another function to clear the screen
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')