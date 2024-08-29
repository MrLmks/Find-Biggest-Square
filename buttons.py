
import os
import tkinter as tk



class Buttons:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.canva = None
    
    def display_map(self, window, path):
        try: 
            if self.canva is not None:
                self.canva.destroy()
            with open(path, "r") as map:
                map_content = map.readlines()
                num_rows = len(map_content)
                num_cols = len(map_content[0].strip())
                cell_size = 30
                
                self.canva = tk.Canvas(window, bg="lightgrey", height=num_rows * cell_size, width=num_cols * cell_size)
                self.canva.place(relx=0.5, rely=0.5, anchor="center")
                
                for y, line in enumerate(map_content):
                    for x, cell in enumerate(line.strip()):
                        if cell == "x":
                            color = "red"
                        else:
                            color = "white"
                        self.canva.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill=color, outline="lightblue")
        except FileNotFoundError:
            print(f"File not found at {path}")


    def create_buttons_maps(self):
        buttons = {}
        for file in os.listdir("./maps"):
            if os.path.isfile(os.path.join("maps", file)):
                button_name = file.replace(".txt", "").capitalize()
                file_path = os.path.join("maps", file)
                buttons[button_name] = file_path
        return buttons

    def on_click(self, path):
        self.display_map(self, path)