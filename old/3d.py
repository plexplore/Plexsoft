import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

z_label = "Altitude"
x_label = "Latitude"
y_label = "Longitude"
blacklist = [z_label, x_label, y_label, "Seconds"]
colormaps = ["viridis", "plasma", "cividis", "magma", "coolwarm", "cubehelix", "terrain", "twilight"]
markers = ["o", "s", "^", "D", "v", "P", "*", "X"]



class View3D():
    def __init__(self, tab:ctk.CTkFrame, app:ctk.CTk):
        self.app = app
        self.tab = tab
        self.graph_canvas = None


        self.graph = ctk.CTkFrame(self.tab, fg_color="transparent")
        self.side_bar = ctk.CTkFrame(self.tab, fg_color=app.color_config["light_background"], width=150)
        self.graph.pack(side="left", padx=0, pady=(30,0), fill="both", expand=True)
        self.side_bar.pack( side="right", fill="y", padx=(10,0), pady=(30,0))

        self.c_values = {}
        for c_name in [d["name"] for d in app.data_config if d["name"] not in blacklist]:
            self.c_values[c_name] = ctk.CTkSwitch(self.side_bar, fg_color="purple", text=c_name, variable=ctk.BooleanVar(value=True), command=self.updatePlot)
            self.c_values[c_name].pack(anchor="nw", padx=5, pady=5)

    def update_data(self):
        self.plot()

    def plot(self):
        if self.app.data is None:
            return
        self.fig = plt.Figure(figsize=(6, 6), dpi=100, facecolor=self.app.color_config["background"])
        self.ax = self.fig.add_subplot(111, projection='3d', facecolor=self.app.color_config["background"])

        if self.graph_canvas:
            self.graph_canvas.get_tk_widget().destroy()


        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.graph_canvas.get_tk_widget().pack(fill="both", expand=True)
        self.updatePlot()

    def updatePlot(self):
        self.ax.cla()
        x,y,z = self.app.data[x_label], self.app.data[y_label], self.app.data[z_label]

        self.ax.plot(x, y, z, label="Flugbahn", color="cyan", linewidth=2)

        for i, col_name in enumerate([d["name"] for d in self.app.data_config if d["name"] not in blacklist and self.c_values[d["name"]].get()]):
            dist = i*0.1+0.1
            self.ax.scatter(x+dist,y+dist,z+dist, c=self.app.data[col_name], cmap=colormaps[i%len(colormaps)], label=col_name, marker=markers[i%len(markers)], vmin=min(self.app.data[col_name]), vmax=max(self.app.data[col_name]))

        self.ax.set_zlabel("Höhe (km)")
        self.ax.legend()

        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.zaxis.label.set_color('white')
        self.ax.title.set_color('white')
        self.ax.tick_params(colors='white')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.graph_canvas.draw()