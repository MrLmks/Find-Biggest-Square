
import os
from tkinter import *



class Buttons:
    def __init__(self, name, path):
        self.name = name
        self.path = path
    
    def display_map(self, window, path):
        try:            
            with open(path, "r") as map:
                map_content = map.readlines()
                num_rows = len(map_content)
                num_cols = len(map_content[0].strip())
                cell_size = 20
                canva = Canvas(window, bg="black", height=num_rows * cell_size, width=num_cols * cell_size)
                canva.pack()
                for y, line in enumerate(map_content):
                    for x, cell in enumerate(line.strip()):
                        canva.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill="white", outline="lightblue")
        except FileNotFoundError:
            print(f"File not found at {path}")


    def create_buttons_maps(self):
        buttons = {}
        for file in os.listdir("./maps"):
            if os.path.isfile(os.path.join("maps", file)):
                button_name = file.replace(".txt", "")
                file_path = os.path.join("maps", file)
                buttons[button_name] = file_path
        return buttons

    def on_click(self, path):
        self.display_map(self, path)