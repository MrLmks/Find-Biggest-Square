# find the biggest square possible in given maps (.txt)
# Add function of colors (color the square, space it properly, display it in a window so it's more clear and esthetic)
import os
from buttons import Buttons
import tkinter as tk

def display_window():
    window = tk.Tk()
    window.title('Find Biggest Square')
    window.geometry("800x800")
    window.configure(bg="lightgrey")
    map_buttons = Buttons("map Buttons", "./maps")
    buttons_dict = Buttons.create_buttons_maps(map_buttons)
    
    for button_name, file_path in buttons_dict.items():
        btn = tk.Button(window, text=button_name, command=lambda path=file_path: buttons_dict.display_map(path))
        btn.pack(pady=20)
    
    window.mainloop()



display_window()