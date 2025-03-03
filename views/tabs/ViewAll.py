import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ViewAll:
    def __init__(self, tab: ctk.CTkFrame, app: ctk.CTk):
        self.app = app
        self.tab = tab
        self.graph_canvases = None

        x_values = [d["name"] for d in app.data_config if d["x"]==True]

        self.cb_label = ctk.CTkLabel(self.tab, text="X-Achse", text_color="white")
        self.cb_label.pack(anchor="nw", padx=5, pady=(0,0))
        self.combo_box = ctk.CTkComboBox(self.tab, command=self.plot, values=x_values)
        self.combo_box.pack(anchor="nw", padx=5, pady=(0,0))

        self.graph_frame = ctk.CTkScrollableFrame(self.tab, fg_color="transparent")
        self.graph_frame.pack(side="left", padx=0, pady=(10,0), fill="both", expand=True)

    def update_data(self):
        self.plot()

    def plot(self, choice=None):
        x_name = self.combo_box.get()
        x_data = self.app.data[x_name]

        if self.graph_canvases:
            for canvas in self.graph_canvases:
                canvas.get_tk_widget().destroy()
        else:
            self.graph_canvases = []

        for y_name in [d["name"] for d in self.app.data_config if d["y"]==True and d["name"] != self.combo_box.get()]:
            y_data = self.app.data[y_name]
            
            fig = Figure(figsize=(5, 5))
            ax = fig.add_subplot(111)

            fig.set_facecolor(self.app.color_config["background"])
            ax.set_facecolor(self.app.color_config["background"])
            ax.tick_params(axis='both', colors='white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.title.set_color('white') 
            for spine in ax.spines.values(): spine.set_color("white")

            ax.plot(x_data, y_data, marker='o', linestyle='-', color="purple")

            dconf = [d for d in self.app.data_config if d["name"]==y_name][0]

            if dconf["min"] != None:
                ax.axhline(dconf["min"], color="red", linestyle="--")
            if dconf["max"] != None:
                ax.axhline(dconf["max"], color="red", linestyle="--")

            ax.set_xlabel(x_name)
            ax.set_ylabel(y_name)
            ax.set_title(f"{y_name} vs {x_name}")

            
            canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.config(bg=self.app.color_config["background"])
            canvas_widget.pack(fill='both', expand=True, padx=5, pady=5)
            
            canvas.draw()
            self.graph_canvases.append(canvas)
            
