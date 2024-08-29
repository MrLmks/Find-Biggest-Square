
from buttons import Buttons
import tkinter as tk

def display_window():
    window = tk.Tk()
    window.title('Find Biggest Square')
    
    window.geometry("800x800")
    window.configure(bg="lightgrey")

    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.BOTTOM, pady=50)
    button_frame.configure(bg="lightgrey")

    map_buttons = Buttons("Map Buttons", "./maps")
    buttons_dict = Buttons.create_buttons_maps(map_buttons)
    
    for button_name, file_path in buttons_dict.items():
        btn = tk.Button(button_frame, text=button_name, command=lambda path=file_path: map_buttons.display_map(window, path))
        btn.pack(side=tk.LEFT, padx=50)
    
    window.mainloop()



display_window()