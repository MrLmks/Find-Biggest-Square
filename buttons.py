
import os, tkinter as tk



class Buttons:
    def __init__(self, name, path):
        self.name = name
        self.path = path
    
    def display_map(self, path):
        try:
            with open(path, "r") as map:
                for line in map:
                    print(line)
        except FileNotFoundError:
            print(f"File not found {path}")
            print(f"Current directory: {os.getcwd()}")
            print(f"Path to map {os.path.abspath(path)}")

    def create_buttons_maps(self):
        buttons = {}
        for file in os.listdir("./maps"):
            if os.path.isfile(os.path.join("maps", file)):
                button_name = file.replace(".txt", "")
                file_path = os.path.join("maps", file)
                buttons[button_name] = file_path
        return buttons
        # map_buttons = []
        # try: 
        #     for file in os.listdir("maps"):
        #         if os.path.isfile(file):
        #             button_name = f"{file}_button"
        #             button_path = f"./maps/{file}.txt"
        #             map_button = button_name + button_path
        #             map_buttons.append(map_button)
        #     print(map_buttons)
        #     return map_buttons
        # except FileNotFoundError:
        #     print(f"File not found {file}")

    def on_click(self, path):
        self.display_map(self, path)