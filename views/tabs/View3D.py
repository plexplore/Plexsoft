import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

z_label = "Altitude"
x_label = "Latitude"
y_label = "Longitude"
blacklist = [z_label, x_label, y_label, "Time"]




class View3D():
    def __init__(self, tab:ctk.CTkFrame, app:ctk.CTk):
        self.app = app
        self.tab = tab
        self.graph_canvas = None

        self.combo_box = ctk.CTkComboBox(self.tab, command=self.updatePlot, values=[d["name"] for d in app.data_config if d["name"] not in blacklist])
        self.combo_box.pack(anchor="nw", padx=5, pady=(10,0))

        self.graph = ctk.CTkFrame(self.tab, fg_color="transparent")
        self.graph.pack(side="left", padx=0, pady=(30,0), fill="both", expand=True)
  

    def update_data(self):
        self.plot()

    def plot(self):
        if self.app.data is None:
            return
        

        print("hier")
        self.fig = plt.Figure(figsize=(6, 6), dpi=100, facecolor=self.app.color_config["background"])
        self.ax = self.fig.add_subplot(111, projection='3d', facecolor=self.app.color_config["background"])

        if self.graph_canvas:
            self.graph_canvas.get_tk_widget().destroy()


        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.graph_canvas.get_tk_widget().pack(fill="both", expand=True)
        self.updatePlot()

    def updatePlot(self, value=None):
        self.ax.cla()
        x,y,z = self.app.data[x_label], self.app.data[y_label], self.app.data[z_label]

        self.ax.plot(x, y, z, label="Flugbahn", color="cyan", linewidth=2)

        col_name = self.combo_box.get()
        dist = 0.1
        self.ax.scatter(x,y,z, c=self.app.data[col_name], cmap="Greens", label=col_name, marker="o", vmin=min(self.app.data[col_name]), vmax=max(self.app.data[col_name]))

        self.ax.legend()

        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.zaxis.label.set_color('white')
        self.ax.title.set_color('white')
        self.ax.tick_params(colors='white')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.graph_canvas.draw()