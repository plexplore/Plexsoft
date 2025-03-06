from views.App import App
import customtkinter as ctk
import json

with open("config/data.json") as file:
    data_config = json.load(file)
with open("config/colors.json") as file:
    color_config = json.load(file)


print("hier")
ctk.set_appearance_mode("dark")
app = App(data_config, color_config)
app.mainloop()