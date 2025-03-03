import json
from views.App import App

with open("config/colors.json") as file:
    colors = json.load(file)

app = App(colors)
app.mainloop()